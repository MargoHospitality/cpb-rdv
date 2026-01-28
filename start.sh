#!/bin/bash
# Script de démarrage du minisite RDV
# Compatible local + Glitch/Railway

cd "$(dirname "$0")"

echo "🤓 Minisite RDV CPB - Mathilde"
echo ""

# Check if slots.json exists
if [ ! -f "slots.json" ]; then
    echo "❌ Erreur: slots.json introuvable"
    exit 1
fi

# Use server_simple.py (no Flask required)
python3 server_simple.py
