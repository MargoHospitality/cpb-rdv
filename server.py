#!/usr/bin/env python3
"""
Serveur simple sans Flask - utilise http.server
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from datetime import datetime
from threading import Lock
from urllib.parse import urlparse, parse_qs
import io
import random

SLOTS_FILE = 'slots.json'
lock = Lock()

def load_slots():
    """Load slots from JSON file"""
    with lock:
        try:
            with open(SLOTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading slots: {e}")
            return []

def save_slots(slots):
    """Save slots to JSON file"""
    with lock:
        try:
            with open(SLOTS_FILE, 'w', encoding='utf-8') as f:
                json.dump(slots, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving slots: {e}")
            return False

class RDVHandler(SimpleHTTPRequestHandler):
    """Custom handler for RDV API"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/api/slots':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            slots = load_slots()
            self.wfile.write(json.dumps(slots, ensure_ascii=False).encode('utf-8'))
        
        elif parsed_path.path == '/api/stats':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            slots = load_slots()
            total = len(slots)
            reserved = sum(1 for s in slots if s.get('reserved'))
            available = total - reserved
            
            stats = {
                'total': total,
                'reserved': reserved,
                'available': available,
                'percentage': round((reserved / total * 100) if total > 0 else 0, 1)
            }
            self.wfile.write(json.dumps(stats).encode('utf-8'))
        
        else:
            # Serve static files
            super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(body) if body else {}
        except:
            self.send_error(400, 'Invalid JSON')
            return
        
        if parsed_path.path == '/api/reserve':
            slot_id = data.get('slotId')
            name = data.get('name', '').strip()
            
            if not slot_id or not name:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Données manquantes'}).encode('utf-8'))
                return
            
            slots = load_slots()
            slot = next((s for s in slots if s['id'] == slot_id), None)
            
            if not slot:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Créneau introuvable'}).encode('utf-8'))
                return
            
            # Generate or keep existing PIN
            if not slot.get('reserved'):
                pin = str(random.randint(1000, 9999))
            else:
                pin = slot.get('pin', str(random.randint(1000, 9999)))
            
            # Update slot
            slot['nom'] = name
            slot['reserved'] = True
            slot['reserved_at'] = datetime.now().isoformat()
            slot['pin'] = pin
            
            if not save_slots(slots):
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Erreur de sauvegarde'}).encode('utf-8'))
                return
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'slot': slot, 'pin': pin}, ensure_ascii=False).encode('utf-8'))
        
        elif parsed_path.path == '/api/cancel':
            slot_id = data.get('slotId')
            pin = data.get('pin', '').strip()
            
            if not slot_id:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'ID manquant'}).encode('utf-8'))
                return
            
            if not pin:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Code PIN requis'}).encode('utf-8'))
                return
            
            slots = load_slots()
            slot = next((s for s in slots if s['id'] == slot_id), None)
            
            if not slot:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Créneau introuvable'}).encode('utf-8'))
                return
            
            # Verify PIN
            if slot.get('pin') != pin:
                self.send_response(403)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Code PIN incorrect'}).encode('utf-8'))
                return
            
            # Cancel reservation
            slot['nom'] = ''
            slot['reserved'] = False
            if 'reserved_at' in slot:
                del slot['reserved_at']
            if 'pin' in slot:
                del slot['pin']
            
            if not save_slots(slots):
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Erreur de sauvegarde'}).encode('utf-8'))
                return
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
        
        else:
            self.send_error(404, 'Not Found')
    
    def log_message(self, format, *args):
        """Log requests"""
        print(f"{self.address_string()} - {format % args}")

if __name__ == '__main__':
    if not os.path.exists(SLOTS_FILE):
        print(f"Error: {SLOTS_FILE} not found")
        exit(1)
    
    # Use PORT env var if set (for Glitch, Railway, etc.)
    PORT = int(os.environ.get('PORT', 5050))
    
    print("=" * 60)
    print("🤓 Minisite RDV CPB - Mathilde")
    print("=" * 60)
    print(f"📂 Fichier créneaux: {SLOTS_FILE}")
    print(f"📊 Créneaux disponibles: {len(load_slots())}")
    print()
    print("🌐 Serveur démarré sur:")
    print(f"   • http://localhost:{PORT}")
    print(f"   • http://0.0.0.0:{PORT}")
    
    # Try to get external IP
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"   • http://{local_ip}:{PORT}")
    except:
        pass
    
    print()
    print("✏️  Créneaux modifiables même après réservation")
    print("Appuyez sur Ctrl+C pour arrêter")
    print("=" * 60)
    
    server = HTTPServer(('0.0.0.0', PORT), RDVHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Serveur arrêté")
        server.server_close()
