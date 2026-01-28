#!/bin/bash
# Script pour pusher vers GitHub

cd ~/clawd/rdv-cpb-mathilde

# Init git si pas déjà fait
if [ ! -d .git ]; then
  git init
  git add .
  git commit -m "Initial commit - Minisite RDV CPB Mathilde"
fi

echo ""
echo "✓ Repo git initialisé"
echo ""
echo "Maintenant, ajoute ton remote GitHub :"
echo ""
echo "  git remote add origin https://github.com/TON-USERNAME/cpb-rdv.git"
echo ""
echo "Puis push :"
echo ""
echo "  git branch -M main"
echo "  git push -u origin main"
echo ""
echo "Ensuite sur Glitch.com :"
echo "  New Project → Import from GitHub → colle l'URL du repo"
echo ""
