# 🤓 Minisite RDV CPB - Mathilde

Système de réservation de créneaux pour les entretiens parents-professeur.

## 🚀 Lancement rapide

```bash
# Démarrer le serveur
python3 server.py
```

Puis ouvrir : **http://localhost:5000**

Le site est accessible sur le réseau local (http://IP-LOCAL:5000) pour que les parents puissent y accéder.

## 📁 Fichiers

- **index.html** — Interface web (design geek moderne)
- **server.py** — Backend Flask (API REST + serveur)
- **slots.json** — Données des créneaux (automatiquement mis à jour)

## 🔧 Fonctionnalités

✓ Affichage des créneaux par jour  
✓ Réservation en temps réel  
✓ Interface responsive (mobile-friendly)  
✓ Rafraîchissement automatique (30s)  
✓ Design moderne avec animations  
✓ Aucune authentification (simple et rapide)

## 📊 API Endpoints

- `GET /api/slots` — Liste des créneaux
- `POST /api/reserve` — Réserver un créneau
- `POST /api/cancel` — Annuler une réservation
- `GET /api/stats` — Statistiques

## 🛠️ Annuler une réservation (admin)

```bash
python3 cancel.py <slot_id>
```

Ou modifier directement `slots.json` :
```json
{
  "nom": "",
  "reserved": false
}
```

## 🌐 Déploiement

### Option 1: Serveur local (réseau de l'école)
Le serveur tourne sur un ordinateur, les parents se connectent en local.

### Option 2: Cloud rapide (Glitch, PythonAnywhere, Replit)
1. Upload des fichiers
2. Installer Flask : `pip install flask`
3. Lancer `server.py`

### Option 3: Hébergement web (avec Baptiste)
Peut être hébergé sur un des serveurs existants.

## 📝 Notes

- **Sécurité low** : pas d'auth, pas de validation complexe (comme demandé)
- Les réservations sont stockées dans `slots.json`
- Backup recommandé de `slots.json` avant/après les inscriptions
- Le design "geek" montre que la maîtresse est tech-savvy 🤓✨

## 💡 Améliorations possibles

- Export Excel des réservations
- Email de confirmation
- Authentification simple (code classe)
- Limite de réservations par parent
- Annulation par les parents (avec code)

---

Créé par Margo 🏨 pour Mathilde CPB
