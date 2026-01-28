# 🚀 Déploiement sur Glitch.com

## Option 1 : Import direct (recommandé)

1. Va sur **https://glitch.com**
2. Clique **"New Project"** → **"Import from GitHub"**
3. OU clique **"New Project"** → **"glitch-hello-python"** (template Python)
4. Une fois le projet créé, clique sur **"Tools"** → **"Import/Export"** → **"Import from file"**
5. Upload l'archive `rdv-cpb-mathilde.tar.gz`
6. Dans le terminal Glitch, lance : `chmod +x start-glitch.sh`
7. Édite `.glitch-assets` et ajoute :
   ```
   start: python3 server_simple.py
   ```

8. Le projet démarre automatiquement

## Option 2 : Upload manuel des fichiers

1. Va sur **https://glitch.com**
2. Clique **"New Project"** → **"glitch-hello-python"**
3. Supprime les fichiers existants
4. Upload un par un :
   - index.html
   - server_simple.py
   - slots.json
   - cancel.py
   - export.py
5. Édite le fichier `start.sh` et remplace par :
   ```bash
   #!/bin/bash
   python3 server_simple.py
   ```
6. Le projet redémarre automatiquement

## Option 3 : Via GitHub (si tu veux versionner)

1. Crée un repo GitHub : `cpb-rdv`
2. Push tous les fichiers
3. Sur Glitch : **"New Project"** → **"Import from GitHub"** → colle l'URL du repo
4. Glitch détectera Python et lancera `server_simple.py`

## Configuration du nom

Une fois le projet créé :
- Clique sur le nom du projet (en haut à gauche)
- Change en **"cpb-rdv"** ou **"rdv-cpb-mathilde"**
- URL finale : `https://cpb-rdv.glitch.me`

## Port

Glitch utilise automatiquement le port exposé par l'application.  
Modifie `server_simple.py` ligne PORT si nécessaire (Glitch set la variable `PORT`).

Si besoin, remplace :
```python
PORT = 5050
```
par :
```python
PORT = int(os.environ.get('PORT', 5050))
```

## Vérification

Une fois déployé :
- URL : https://cpb-rdv.glitch.me
- API : https://cpb-rdv.glitch.me/api/slots
- Stats : https://cpb-rdv.glitch.me/api/stats

## Limites Glitch gratuit

- Projet dort après 5 min d'inactivité (réveil automatique au premier accès)
- 1000 heures/mois gratuites (largement suffisant)

---

**Besoin d'aide ?** Ping Baptiste ou Margo 🏨
