#!/usr/bin/env python3
"""
Script pour annuler une réservation
Usage: python3 cancel.py <slot_id>
"""

import json
import sys

SLOTS_FILE = 'slots.json'

def list_reservations():
    """List all current reservations"""
    with open(SLOTS_FILE, 'r', encoding='utf-8') as f:
        slots = json.load(f)
    
    reserved = [s for s in slots if s.get('reserved')]
    
    if not reserved:
        print("❌ Aucune réservation active")
        return
    
    print(f"\n📋 Réservations actives ({len(reserved)}):\n")
    for slot in reserved:
        print(f"  ID {slot['id']:2d} | {slot['day']:9s} {slot['date']} à {slot['heure']} | {slot['nom']}")
    print()

def cancel_reservation(slot_id):
    """Cancel a specific reservation"""
    with open(SLOTS_FILE, 'r', encoding='utf-8') as f:
        slots = json.load(f)
    
    slot = next((s for s in slots if s['id'] == slot_id), None)
    
    if not slot:
        print(f"❌ Créneau ID {slot_id} introuvable")
        return False
    
    if not slot.get('reserved'):
        print(f"⚠️  Créneau ID {slot_id} n'est pas réservé")
        return False
    
    # Backup name before cancel
    old_name = slot.get('nom', 'N/A')
    
    # Cancel
    slot['nom'] = ''
    slot['reserved'] = False
    if 'reserved_at' in slot:
        del slot['reserved_at']
    
    # Save
    with open(SLOTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(slots, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Réservation annulée:")
    print(f"  • ID: {slot_id}")
    print(f"  • Créneau: {slot['day']} {slot['date']} à {slot['heure']}")
    print(f"  • Était réservé par: {old_name}")
    
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 cancel.py <slot_id>")
        print("       python3 cancel.py list")
        print()
        list_reservations()
        sys.exit(0)
    
    if sys.argv[1].lower() == 'list':
        list_reservations()
    else:
        try:
            slot_id = int(sys.argv[1])
            cancel_reservation(slot_id)
        except ValueError:
            print(f"❌ ID invalide: {sys.argv[1]}")
            sys.exit(1)
