# 🎨 Design du Minisite

## Concept visuel

**Thème:** "Maîtresse Geek" 🤓  
**Ambiance:** Moderne, coloré, fun mais professionnel  
**Palette:** Dégradés violets/bleus (tech-friendly)

## Éléments visuels

### Header
```
        🤓
   Rendez-vous avec Mathilde
   CPB • Février 2026 • Entretiens parents-professeur
```
- Emoji animé (bounce)
- Fond dégradé violet → violet foncé
- Typographie moderne: Space Grotesk

### Cards par jour
Chaque jour = card blanche arrondie avec ombre

```
┌─────────────────────────────────────────┐
│  📅 LUNDI 02/02/2026                    │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ 11h35   │  │ 11h50   │  │ 15h45   │ │
│  │ 📍 Box  │  │ 📍 Box  │  │ 📍 Class│ │
│  │ ✓ Dispo │  │ ✓ Dispo │  │ ✓ Dispo │ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

### Créneaux disponibles
- Fond: dégradé gris clair → gris bleu
- Hover: élévation + ombre bleue + bordure
- Animation: translateY(-5px)
- Badge vert "✓ Disponible"

### Créneaux réservés
- Fond: dégradé jaune/orange
- Badge orange "✓ Réservé"
- Nom affiché dessous
- Pas de hover

### Modal de réservation

```
┌──────────────────────────────────────────┐
│  📝 Réserver ce créneau                  │
│  ┌────────────────────────────────────┐  │
│  │ Jour:  LUNDI                       │  │
│  │ Date:  02/02/2026                  │  │
│  │ Heure: 11h35                       │  │
│  │ Lieu:  Box administration          │  │
│  └────────────────────────────────────┘  │
│                                          │
│  Nom de l'enfant *                       │
│  [                              ]        │
│                                          │
│  Nom du parent (optionnel)               │
│  [                              ]        │
│                                          │
│  [ Annuler ]  [ Confirmer ]              │
└──────────────────────────────────────────┘
```

- Fond blanc arrondi
- Backdrop blur (effet verre dépoli)
- Animation slide-in
- Bouton "Confirmer" : dégradé violet
- Bouton "Annuler" : gris

## Animations

1. **Fadedown** - Header (entrée)
2. **FadeUp** - Cards jours (entrée)
3. **Bounce** - Emoji tête (continu)
4. **Hover lift** - Cards créneaux (interaction)
5. **Slide-in** - Modal (ouverture)

## Responsive

**Desktop (>768px):**
- Créneaux en grille 3-4 colonnes

**Mobile (<768px):**
- Créneaux en colonne unique
- Espacement adapté
- Touch-friendly (boutons + grands)

## Couleurs principales

- **Background:** `#667eea` → `#764ba2` (gradient)
- **Cards:** `#ffffff`
- **Créneaux dispo:** `#f5f7fa` → `#c3cfe2`
- **Créneaux réservés:** `#ffeaa7` → `#fdcb6e`
- **Texte:** `#2d3436`
- **Accents:** `#667eea` (violet), `#55efc4` (vert), `#fab1a0` (orange)

## Police

**Space Grotesk** - Google Fonts  
Moderne, lisible, légèrement geek/tech

## Icônes

Emojis natifs pour simplicité et fun:
- 🤓 Geek/maîtresse
- 📅📘📗📙📕 Jours de la semaine (différents)
- 📍 Lieu
- ✓ Statut
- 📝 Formulaire

## Expérience utilisateur

1. **Page load** → Animations d'entrée
2. **Scroll** → Smooth
3. **Click créneau dispo** → Modal immédiate
4. **Fill form** → Validation simple
5. **Submit** → Retour instant + refresh liste
6. **Auto-refresh** → Toutes les 30s (voir maj autres parents)

## Effet "Geek"

- Typographie moderne
- Couleurs vives mais élégantes
- Animations fluides
- Design system cohérent
- Pas de stock photos
- Code propre et moderne

→ **Impression:** "Whoa, la maîtresse s'y connaît en web design !" 🚀
