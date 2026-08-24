#!/usr/bin/env python3
"""Génère la version « fichier unique » du guide.

    python3 build-standalone.py

Lit index.html et assets/img/, écrit guide-communication-redon.html : un seul
fichier HTML avec toutes les images embarquées en base64, à envoyer par courriel
ou à déposer sur l'intranet sans se soucier des chemins.

Option « --fragment CHEMIN » : écrit en plus une version sans <html>/<head>/<body>,
pour les plateformes qui enveloppent elles-mêmes le contenu.
"""
import base64, json, mimetypes, pathlib, re, sys

ICI = pathlib.Path(__file__).parent
IMG = ICI / "assets" / "img"
SRC = ICI / "index.html"


def data_uri(chemin: pathlib.Path) -> str:
    mime = mimetypes.guess_type(chemin.name)[0] or "application/octet-stream"
    return "data:%s;base64,%s" % (mime, base64.b64encode(chemin.read_bytes()).decode("ascii"))


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    uris = {f.name: data_uri(f) for f in sorted(IMG.iterdir()) if f.is_file()}
    # Seuls les pictogrammes sont construits en JavaScript : inutile d'embarquer
    # deux fois les photos, déjà présentes dans les attributs src.
    js_uris = {n: u for n, u in uris.items() if n.startswith("picto-")}

    # 1. les <img src="assets/img/…"> écrits dans le HTML
    html = re.sub(
        r'src="assets/img/([^"]+)"',
        lambda m: 'src="%s"' % uris[m.group(1)],
        html,
    )
    # 2. les images construites en JavaScript, via window.__ASSETS
    html = html.replace(
        "<script>\n(function(){",
        "<script>\nwindow.__ASSETS = %s;\n(function(){" % json.dumps(js_uris),
        1,
    )
    assert "assets/img/" not in html.replace('"assets/img/" + n', ""), "chemin d'image oublié"

    sortie = ICI / "guide-communication-redon.html"
    sortie.write_text(html, encoding="utf-8")
    print("%s — %.1f Mo" % (sortie.name, sortie.stat().st_size / 1e6))

    if "--fragment" in sys.argv:
        dest = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
        corps = html.split("<body>", 1)[1].rsplit("</body>", 1)[0]
        tete = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
        tete = re.sub(r'<meta[^>]*>|<link rel="preconnect"[^>]*>', "", tete)
        dest.write_text(tete.strip() + "\n" + corps, encoding="utf-8")
        print("%s — %.1f Mo" % (dest, dest.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
