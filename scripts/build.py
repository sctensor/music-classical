#!/usr/bin/env python3
"""Renders templates/*.html.j2 + config.yaml into the site's HTML pages.

Usage:
    python3 scripts/build.py
"""

from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "index.html.j2": "index.html",
    "lineage.html.j2": "lineage.html",
}


def main() -> None:
    config = yaml.safe_load((ROOT / "config.yaml").read_text())

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )

    for template_name, out_name in PAGES.items():
        template = env.get_template(template_name)
        output = template.render(**config)
        out_path = ROOT / out_name
        out_path.write_text(output)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
