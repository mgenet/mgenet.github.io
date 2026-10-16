#!/usr/bin/env python3
from __future__ import annotations
"""
Quarto post-render hook: applies a per-post `image-position` front-matter
field (e.g. "top", "20% 80%") as an inline `object-position` style on that
post's thumbnail <img> in the rendered listing pages (e.g. news.html).

Quarto's default listing template has no per-item hook for this, so this
patches the already-rendered HTML in `_site/` instead of touching Quarto's
internal listing templates.
"""
import glob
import re
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
FIELD_RE_TEMPLATE = r'^{field}:\s*"?([^"\n]+?)"?\s*$'
IMG_TAG_RE = re.compile(r"<img\b[^>]*>")


def read_front_matter_field(post_file: Path, field: str) -> str | None:
    text = post_file.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    field_match = re.search(
        FIELD_RE_TEMPLATE.format(field=re.escape(field)), match.group(1), re.M
    )
    return field_match.group(1).strip() if field_match else None


def patch_html_file(html_file: Path, positions: dict[str, str]) -> None:
    html = html_file.read_text(encoding="utf-8")

    def patch_img(match: re.Match) -> str:
        tag = match.group(0)
        if 'class="thumbnail-image"' not in tag or "style=" in tag:
            return tag
        for post_dir, position in positions.items():
            if f"/{post_dir}/" in tag:
                return tag.replace(
                    "<img ", f'<img style="object-position: {position};" ', 1
                )
        return tag

    patched = IMG_TAG_RE.sub(patch_img, html)
    if patched != html:
        html_file.write_text(patched, encoding="utf-8")


def main() -> None:
    positions = {}
    for post_file in glob.glob("posts/**/index.md", recursive=True) + glob.glob(
        "posts/**/index.qmd", recursive=True
    ):
        post_path = Path(post_file)
        position = read_front_matter_field(post_path, "image-position")
        if position:
            positions[post_path.parent.name] = position

    if not positions:
        return

    for html_file in glob.glob("_site/**/*.html", recursive=True):
        patch_html_file(Path(html_file), positions)


if __name__ == "__main__":
    main()
