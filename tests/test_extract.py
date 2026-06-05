from scripts.extract_scholar_taste import (
    PaperRecord,
    analyze_paper,
    build_cards,
    load_nlp,
    recover_sections,
    render_readme,
    slugify,
)


def make_paper(index: int) -> PaperRecord:
    return PaperRecord(
        paper_id=f"paper-{index}",
        title=f"Paper {index}",
        source_pdf=f"paper_{index}.pdf",
        parser_mode="fallback",
        sections={
            "abstract": "This paper uses a difference-in-differences design. We show that the policy increased adoption.",
            "introduction": "However, little is known about the mechanism. We study how policy changes behavior.",
            "methods": "We measure adoption with an index and use panel data with fixed effects.",
            "results": "The results are robust to alternative specifications and placebo tests.",
            "discussion": "These results may not generalize where implementation quality is low. Future research should test external validity.",
        },
        references=[],
    )


def test_slugify():
    assert slugify("Jane Q. Doe") == "jane-q-doe"
    assert slugify("!!!") == "scholar"


def test_recover_sections_from_headings():
    text = """
Abstract
This paper studies a question.

1 Introduction
However, prior research leaves a gap.

Methods
We estimate the effect.

Conclusion
These results may not generalize.
"""
    sections = recover_sections(text)
    assert "abstract" in sections
    assert "introduction" in sections
    assert "methods" in sections
    assert "discussion" in sections


def test_cards_are_generated_from_repeated_signals():
    nlp = load_nlp("definitely_missing_model")
    papers = [make_paper(1), make_paper(2), make_paper(3)]
    analyses = [analyze_paper(paper, nlp) for paper in papers]
    cards = build_cards(analyses, min_support=2, total_papers=len(papers))
    titles = {card["title"] for card in cards}
    assert "Frame the contribution by locating the gap before the claim" in titles
    assert "State where the argument should and should not travel" in titles
    assert any(card["confidence"] == "methodology" for card in cards)


def test_rendered_readme_has_expected_contract():
    nlp = load_nlp("definitely_missing_model")
    papers = [make_paper(1), make_paper(2)]
    analyses = [analyze_paper(paper, nlp) for paper in papers]
    cards = build_cards(analyses, min_support=2, total_papers=len(papers))
    text = render_readme("Jane Doe", "jane-doe", papers, cards, {"paper_count": 2})
    assert "# Jane Doe" in text
    assert "## Copy/Paste Skill Cards" in text
    assert "**Critical Boundary**" in text
    assert "Evidence Anchors" in text
    assert "```json" in text
