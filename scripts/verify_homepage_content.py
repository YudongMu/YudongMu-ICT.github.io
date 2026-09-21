#!/usr/bin/env python3
"""Verify the source content for the academic profile pages."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require(text: str, fragment: str, source: str) -> None:
    assert fragment in text, f"{source} is missing {fragment!r}"


def reject(text: str, fragment: str, source: str) -> None:
    assert fragment.lower() not in text.lower(), (
        f"{source} still contains placeholder or excluded content {fragment!r}"
    )


def verify_home() -> None:
    source = "_pages/about.md"
    text = read(source)
    for fragment in (
        "Research Interests",
        "Selected Research Projects",
        "FDHA",
        "DFU-Y",
        "GenCNN",
        "NFMap",
        "Industry Experience",
    ):
        require(text, fragment, source)
    reject(text, "dLLM", source)


def verify_publications() -> None:
    page_source = "_pages/publications.html"
    page = read(page_source)
    require(page, "publication-entry.html", page_source)

    publication_dir = ROOT / "_publications"
    records = sorted(publication_dir.glob("*.md"))
    assert len(records) == 6, (
        f"_publications must contain exactly six Markdown records; found {len(records)}"
    )
    combined = "\n".join(path.read_text(encoding="utf-8") for path in records)
    for fragment in (
        "GenCNN",
        "面向 YOLO 神经网络的数据流架构优化研究",
        "FDHA",
        "NFMap",
        "A2RT",
        "A RISC-V Extended Infrastructure for CNNs",
    ):
        require(combined, fragment, "_publications/*.md")
    for placeholder in (
        "Paper Title Number 2",
        "To be added",
        "To be Added",
        "GitHub Journal of Bugs",
    ):
        reject(combined, placeholder, "_publications/*.md")
    assert (ROOT / "_includes" / "publication-entry.html").is_file(), (
        "_includes/publication-entry.html is missing"
    )


def verify_honors() -> None:
    source = "_pages/honors.html"
    text = read(source)
    for fragment in (
        'title: "Honors"',
        "permalink: /honors/",
        "Graduate Honors",
        "Undergraduate Honors",
        "Outstanding Student Model",
        "National Scholarship for Graduate Students",
        "E Fund Freshman Scholarship",
        "Outstanding Student Leader",
    ):
        require(text, fragment, source)
    reject(text, "Talks and presentations", source)
    assert not list((ROOT / "_honors").glob("*.md")), (
        "_honors still contains starter records"
    )


def verify_styles() -> None:
    source = "assets/css/main.scss"
    require(read(source), '"layout/academic-profile"', source)
    assert (ROOT / "_sass" / "layout" / "_academic-profile.scss").is_file(), (
        "_sass/layout/_academic-profile.scss is missing"
    )


def main() -> None:
    checks = (
        ("home", verify_home),
        ("publications", verify_publications),
        ("honors", verify_honors),
        ("styles", verify_styles),
    )
    failures: list[str] = []
    for name, check in checks:
        try:
            check()
        except (AssertionError, FileNotFoundError) as error:
            failures.append(f"FAIL {name}: {error}")
        else:
            print(f"PASS {name}")

    if failures:
        raise SystemExit("\n".join(failures))
    print("All academic homepage source checks passed.")


if __name__ == "__main__":
    main()
