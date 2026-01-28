# 🤓 RDV CPB Mathilde

Système de réservation de créneaux pour entretiens parents-professeur.

## 🚀 Démarrage

Ce projet tourne automatiquement sur Glitch !

**Serveur :** `python3 server_simple.py`

## 📱 Utilisation

- Page d'accueil : `/`
- API créneaux : `/api/slots`
- Réserver : POST `/api/reserve`
- Annuler : POST `/api/cancel`
- Stats : `/api/stats`

## ✨ Fonctionnalités

✓ 32 créneaux (2-6 février 2026)  
✓ Réservation en temps réel  
✓ Modification/annulation possible  
✓ Design moderne responsive  
✓ Auto-refresh 30s  

## 🔧 Fichiers importants

- `index.html` - Interface web
- `server_simple.py` - Backend API
- `slots.json` - Base de données (auto-sauvegardé)
- `cancel.py` - Admin: annuler réservations
- `export.py` - Admin: export CSV

## 👨‍💼 Admin

Dans le terminal Glitch :

```bash
# Lister réservations
python3 cancel.py list

# Annuler créneau ID 5
python3 cancel.py 5

# Export CSV
python3 export.py
```

---

Made with ❤️ by Margo 🏨
