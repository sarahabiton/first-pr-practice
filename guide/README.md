# Guide de communication visuelle — Ville de Redon

Version interactive du *Guide de communication visuelle de la Ville de Redon* (v1.0),
conçue pour être consultée par les agents comme un mini site plutôt que lue comme un
document Word.

## Ce que contient ce dossier

| Fichier | À quoi il sert |
| --- | --- |
| `index.html` | Le site. À ouvrir directement, ou à déposer sur un serveur / GitHub Pages. Il a besoin du dossier `assets/`. |
| `assets/img/` | Le logotype, les 12 pictogrammes et les 11 visuels d'exemple, optimisés pour le web. |
| `assets/source/` | Les fichiers d'origine transmis par le service communication. Ils ne sont pas utilisés par la page : ils servent de référence pour régénérer les images de `assets/img/`. |
| `guide-communication-redon.html` | **Le même guide en un seul fichier** (2,6 Mo), images comprises. C'est celui que l'on envoie par courriel ou que l'on dépose sur l'intranet : il n'a besoin de rien d'autre. |
| `build-standalone.py` | Régénère le fichier unique à partir de `index.html`. |

## Modifier le guide

Tout le contenu est dans `index.html` — un seul fichier, sans dépendance ni outil de build.
Les parties sont repérables par leurs commentaires (`<!-- ══ 3. COULEURS ══ -->`).

Après une modification, régénérer le fichier unique :

```bash
python3 build-standalone.py
```

Le sommaire, l'index de recherche et les liens du parcours de lecture se construisent
automatiquement à partir des sections : ajouter une partie `<section class="sec" data-part="…"
data-title="…">` suffit pour qu'elle apparaisse partout.

Trois listes vivent dans le JavaScript, en fin de fichier, et sont à mettre à jour si la
charte évolue : `UNIVERS` (la palette), `PICTOS` (les pictogrammes) et `POINTS` (la checklist).

## Ce que le guide sait faire

- **Parcours de lecture** — élu·e, agent ou prestataire : le sommaire ne met en avant que les parties concernées (partie 1.3).
- **Recherche instantanée** dans tout le guide (`Ctrl`/`⌘` + `K`), insensible aux accents.
- **Palette cliquable** — un clic copie le code hexadécimal, pour ne plus le ressaisir à la main dans Canva.
- **Sélecteur de modèle** — une question, et le modèle, le composant dominant et la composition s'affichent (partie 8.1).
- **Checklist avant publication** cochable, avec barre de progression, conservée d'une visite à l'autre (partie 10.3).
- **Calcul du rétroplanning** — une date de diffusion, un type de support, et la date limite de transmission au service communication (partie 10.4).
- **Visionneuse** pour agrandir les visuels d'exemple.
- **Thème clair et sombre**, lecture sur téléphone, et une feuille de style d'impression : le guide reste imprimable en couleur.

## Points techniques

- Aucune dépendance, aucun script externe, aucun traceur.
- Poppins est la seule police utilisée, conformément à la partie 4 du guide. Elle est
  appelée sur Google Fonts ; hors connexion, la page bascule sur la Poppins du poste,
  installée chez les agents qui produisent des supports.
- Les préférences (thème, parcours, checklist) restent dans le navigateur de l'agent ;
  rien n'est envoyé nulle part.
