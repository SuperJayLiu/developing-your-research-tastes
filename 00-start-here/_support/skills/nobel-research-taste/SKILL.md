---
name: nobel-research-taste
description: Use when turning Nobel-linked economics research, prize lectures, scientific background documents, or scholar pages into mature research taste skills for economics or finance projects; use for diagnosing whether a research idea has the causal-design, formal-theory, institutional, incentive, market-signal, welfare, growth, or allocation taste patterns associated with top scholars, and for revising short skill cards into detailed, bounded, evidence-anchored instructions.
---

# Nobel Research Taste

Use this skill to turn Nobel-linked research taste into operational research judgment. The job is not to praise laureates or summarize topics. The job is to recover a reusable move: how a scholar makes a question sharper, chooses evidence, builds a model, limits a claim, or changes what other researchers can see.

Keep the public output in prose. The final answer should usually read like a short research memo or skill card, not as a checklist. Use lists only for diagnostics, validation, or templates.

## Workflow

First, classify the user's project problem. Decide whether the live problem is mainly about causal design, formal theory, growth and history, institutions, incentives and information, finance and macro signals, welfare and human decision-making, or markets and allocation. If the project straddles several modules, choose the one that changes the next research decision most directly and mention the secondary module only if it adds a real constraint.

Second, name the research move in action language. Avoid topic labels such as "institutions" or "asset pricing." Use phrases such as "translate an institution into a changed constraint," "separate risk from mispricing before interpreting a return pattern," or "state the welfare object before claiming policy relevance."

Third, anchor the move in evidence. Use the Nobel atlas, official Nobel materials, scientific background documents, prize lectures, scholar pages, or canonical papers as anchors. Do not invent papers, mechanisms, or evidence. If the evidence is missing, mark the skill provisional.

Fourth, produce a mature skill card or diagnosis. A mature card needs a trigger, the core move, evidence anchor, diagnostic questions, common gotchas, a practice prompt, a boundary condition, and a transfer test. A diagnosis should say what is missing, why it matters, and what revision would make the project more disciplined.

Fifth, verify the output. Use `scripts/check_skill_card.py` when you create or revise a markdown skill card. The script is not a substitute for judgment; it catches missing structure so the card does not collapse back into a short slogan.

## Resource Navigation

Read `references/taste-modules.md` when you need to choose among the eight Nobel-derived taste modules or write a detailed skill card.

Read `references/gotchas.md` when a card sounds plausible but immature, overclaims from evidence, imitates a famous scholar too literally, or confuses topic with transferable taste.

Read `references/examples.md` when you need before-and-after examples of weak versus mature research-taste skills.

Read `references/evidence-anchors.md` when the user asks where a taste claim comes from, when you need to keep Nobel evidence separate from broader paper evidence, or when a card needs source discipline.

Use `assets/research-taste-skill-card-template.md` when creating a new card.

Run `scripts/check_skill_card.py <path>` after editing a card or chapter that claims to define reusable skills.

## Quality Bar

A useful Nobel-derived skill should change a research decision. It should help the researcher choose a better question, cleaner design, sharper model, more honest mechanism test, better measurement strategy, narrower contribution claim, or stronger introduction. If the card only teaches admiration, the card is not finished.

The skill should also preserve boundary conditions. Nobel taste becomes bad taste when a researcher copies scale without copying discipline: big questions with thin evidence, elegant models with no economic force, natural experiments with weak counterfactuals, institutional stories with no changed constraint, or finance anomalies interpreted before alternatives are ruled out.

## Output Forms

For a new skill card, write continuous prose with compact diagnostic and practice sections. For a project diagnosis, return the active module, the first failure point, the missing research move, the strongest gotcha, and a revised version of the move. For a chapter revision, keep the reader-facing chapter smooth and move operational details into references, templates, or scripts.

Do not bulk-download paywalled papers, fabricate source claims, or turn every scholar page into a skill. A skill should exist only when it changes how a researcher acts.
