"""Package public static files and set metadata for a GitHub Pages URL."""

import argparse
import html
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit


def prepare(base_url, output):
    parsed = urlsplit(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError("Pass the absolute Pages base URL without a query or fragment")
    base_url = base_url.rstrip("/")
    source = Path(__file__).resolve().parent.parent / "dist"
    output = Path(output)
    if output.exists() and any(output.iterdir()):
        raise ValueError("The output directory must be empty")
    output.mkdir(parents=True, exist_ok=True)

    # Publish only visitor-facing files, excluding source and legacy hosting state.
    for name in ("index.html", "cv.html", "styles.css", "script.js"):
        shutil.copy2(source / name, output / name)
    shutil.copytree(source / "assets", output / "assets")
    (output / ".nojekyll").touch()

    home_url = html.escape(base_url + "/", quote=True)
    image_url = html.escape(base_url + "/assets/henry-oderinde.jpg", quote=True)
    index = output / "index.html"
    content = index.read_text()
    content, count = re.subn(
        r'<meta property="og:image" content="[^"]*">',
        lambda _: f'<meta property="og:image" content="{image_url}">',
        content,
    )
    if count != 1:
        raise ValueError("Expected exactly one og:image tag")
    content = content.replace(
        "</head>",
        f'  <link rel="canonical" href="{home_url}">\n'
        f'  <meta property="og:url" content="{home_url}">\n</head>',
    )
    index.write_text(content)
    print(f"Prepared {output} for {base_url}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output", default="_site")
    args = parser.parse_args()
    prepare(args.base_url, args.output)
