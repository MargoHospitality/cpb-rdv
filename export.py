#!/usr/bin/env python3
"""
Export des réservations en CSV
Usage: python3 export.py [output.csv]
"""

import json
import csv
import sys
from datetime import datetime

SLOTS_FILE = 'slots.json'

def export_reservations(output_file='reservations.csv'):
    """Export all reservations to CSV"""
    with open(SLOTS_FILE, 'r', encoding='utf-8') as f:
        slots = json.load(f)
    
    reserved = [s for s in slots if s.get('reserved')]
    
    if not reserved:
        print("❌ Aucune réservation à exporter")
        return False
    
    # Sort by date and time
    reserved.sort(key=lambda s: (s['date'], s['heure']))
    
    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        
        # Header
        writer.writerow(['ID', 'Jour', 'Date', 'Heure', 'Lieu', 'Nom enfant/parent', 'Réservé le'])
        
        # Data
        for slot in reserved:
            reserved_at = slot.get('reserved_at', '')
            if reserved_at:
                try:
                    dt = datetime.fromisoformat(reserved_at)
                    reserved_at = dt.strftime('%d/%m/%Y %H:%M')
                except:
                    pass
            
            writer.writerow([
                slot['id'],
                slot['day'],
                slot['date'],
                slot['heure'],
                slot['lieu'],
                slot['nom'],
                reserved_at
            ])
    
    print(f"✓ Export réussi: {output_file}")
    print(f"  • {len(reserved)} réservations exportées")
    
    return True

def export_all(output_file='all_slots.csv'):
    """Export all slots (reserved + available) to CSV"""
    with open(SLOTS_FILE, 'r', encoding='utf-8') as f:
        slots = json.load(f)
    
    slots.sort(key=lambda s: (s['date'], s['heure']))
    
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        
        writer.writerow(['ID', 'Jour', 'Date', 'Heure', 'Lieu', 'Statut', 'Nom', 'Réservé le'])
        
        for slot in slots:
            status = 'Réservé' if slot.get('reserved') else 'Disponible'
            reserved_at = slot.get('reserved_at', '')
            if reserved_at:
                try:
                    dt = datetime.fromisoformat(reserved_at)
                    reserved_at = dt.strftime('%d/%m/%Y %H:%M')
                except:
                    pass
            
            writer.writerow([
                slot['id'],
                slot['day'],
                slot['date'],
                slot['heure'],
                slot['lieu'],
                status,
                slot.get('nom', ''),
                reserved_at
            ])
    
    print(f"✓ Export complet réussi: {output_file}")
    print(f"  • {len(slots)} créneaux exportés")
    
    return True

if __name__ == '__main__':
    output = sys.argv[1] if len(sys.argv) > 1 else 'reservations.csv'
    
    if output.lower() == 'all':
        export_all('all_slots.csv')
    else:
        export_reservations(output)
