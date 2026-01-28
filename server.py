#!/usr/bin/env python3
"""
Minisite de réservation de rendez-vous CPB - Mathilde
Backend Flask simple avec stockage JSON
"""

from flask import Flask, jsonify, request, send_from_directory
import json
import os
from datetime import datetime
from threading import Lock

app = Flask(__name__)
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

@app.route('/')
def index():
    """Serve main page"""
    return send_from_directory('.', 'index.html')

@app.route('/api/slots', methods=['GET'])
def get_slots():
    """Get all slots"""
    slots = load_slots()
    return jsonify(slots)

@app.route('/api/reserve', methods=['POST'])
def reserve_slot():
    """Reserve a slot"""
    try:
        data = request.json
        slot_id = data.get('slotId')
        name = data.get('name', '').strip()
        
        if not slot_id or not name:
            return jsonify({'error': 'Données manquantes'}), 400
        
        # Load current slots
        slots = load_slots()
        
        # Find the slot
        slot = next((s for s in slots if s['id'] == slot_id), None)
        
        if not slot:
            return jsonify({'error': 'Créneau introuvable'}), 404
        
        if slot.get('reserved'):
            return jsonify({'error': 'Créneau déjà réservé'}), 409
        
        # Reserve the slot
        slot['nom'] = name
        slot['reserved'] = True
        slot['reserved_at'] = datetime.now().isoformat()
        
        # Save
        if not save_slots(slots):
            return jsonify({'error': 'Erreur de sauvegarde'}), 500
        
        return jsonify({'success': True, 'slot': slot})
    
    except Exception as e:
        print(f"Reservation error: {e}")
        return jsonify({'error': 'Erreur serveur'}), 500

@app.route('/api/cancel', methods=['POST'])
def cancel_reservation():
    """Cancel a reservation (optional - for admin use)"""
    try:
        data = request.json
        slot_id = data.get('slotId')
        
        if not slot_id:
            return jsonify({'error': 'ID manquant'}), 400
        
        slots = load_slots()
        slot = next((s for s in slots if s['id'] == slot_id), None)
        
        if not slot:
            return jsonify({'error': 'Créneau introuvable'}), 404
        
        # Cancel reservation
        slot['nom'] = ''
        slot['reserved'] = False
        if 'reserved_at' in slot:
            del slot['reserved_at']
        
        if not save_slots(slots):
            return jsonify({'error': 'Erreur de sauvegarde'}), 500
        
        return jsonify({'success': True})
    
    except Exception as e:
        print(f"Cancellation error: {e}")
        return jsonify({'error': 'Erreur serveur'}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get reservation statistics"""
    slots = load_slots()
    total = len(slots)
    reserved = sum(1 for s in slots if s.get('reserved'))
    available = total - reserved
    
    return jsonify({
        'total': total,
        'reserved': reserved,
        'available': available,
        'percentage': round((reserved / total * 100) if total > 0 else 0, 1)
    })

if __name__ == '__main__':
    # Check if slots file exists
    if not os.path.exists(SLOTS_FILE):
        print(f"Error: {SLOTS_FILE} not found")
        exit(1)
    
    print("=" * 60)
    print("🤓 Minisite RDV CPB - Mathilde")
    print("=" * 60)
    print(f"📂 Fichier créneaux: {SLOTS_FILE}")
    print(f"📊 Créneaux disponibles: {len(load_slots())}")
    print()
    print("🌐 Serveur démarré sur:")
    print("   • Local:   http://localhost:5000")
    print("   • Réseau:  http://0.0.0.0:5000")
    print()
    print("Appuyez sur Ctrl+C pour arrêter")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
