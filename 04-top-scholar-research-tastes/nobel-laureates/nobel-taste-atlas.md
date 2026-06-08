# Nobel Research Taste Atlas

This atlas summarizes Nobel-linked research taste from official Nobel evidence. It uses the Nobel API snapshot for laureate names and motivations, the local NobelPrize.org PDF manifest for evidence files, and extracted text from the local PDF cache for keyword signals. It is not a complete literature review and it does not store copyrighted journal PDFs.

The goal is practical: convert each recognized contribution into a portable research skill while preserving the boundary that prevents shallow imitation.

```mermaid
flowchart LR
    A["Nobel motivation"] --> B["Official PDF evidence"]
    B --> C["Taste diagnosis"]
    C --> D["Copyable skill"]
    D --> E["Boundary condition"]
```

## Evidence Read

The local cache currently records 91 official Nobel PDFs. The generated PDF text index is `00-start-here/_support/evidence/nobel-open-access/nobel_pdf_read_index.json`; it records page counts, extracted character counts, and extraction errors where relevant. PDF binaries remain ignored by Git.

## How To Use This Atlas

Read the laureate entry as a first-pass taste diagnosis. The entry should tell you what question the laureate made important, what method or model carried the argument, what evidence standard disciplines the contribution, and what mistake a reader should avoid when copying the move.

## 1969 - Ragnar Frisch, Jan Tinbergen

### Ragnar Frisch

Official motivation: for having developed and applied dynamic models for the analysis of economic processes.

Evidence read: 1 lecture; extracted text: 27,756 characters; status: PDF-backed; PDF signals: welfare/behavior/development, incentives/information, growth/innovation, institutions/governance.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for having developed and applied dynamic models for the analysis of economic processes.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

### Jan Tinbergen

Official motivation: for having developed and applied dynamic models for the analysis of economic processes.

Evidence read: 1 lecture; extracted text: 49,234 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, incentives/information, institutions/governance.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for having developed and applied dynamic models for the analysis of economic processes.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 1970 - Paul A. Samuelson

### Paul A. Samuelson

Official motivation: for the scientific work through which he has developed static and dynamic economic theory and actively contributed to raising the level of analysis in economic science.

Evidence read: 1 lecture; extracted text: 44,690 characters; status: PDF-backed; PDF signals: finance/macro, incentives/information, institutions/governance, welfare/behavior/development, growth/innovation.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for the scientific work through which he has developed static and dynamic economic theory and actively contributed to raising the level of analysis in economic science.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

## 1971 - Simon Kuznets

### Simon Kuznets

Official motivation: for his empirically founded interpretation of economic growth which has led to new and deepened insight into the economic and social structure and process of development.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for his empirically founded interpretation of economic growth which has led to new and deepened insight into the economic and social structure and process of development.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.

## 1972 - John R. Hicks, Kenneth J. Arrow

### John R. Hicks

Official motivation: for their pioneering contributions to general economic equilibrium theory and welfare theory.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for their pioneering contributions to general economic equilibrium theory and welfare theory.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

### Kenneth J. Arrow

Official motivation: for their pioneering contributions to general economic equilibrium theory and welfare theory.

Evidence read: 1 lecture; extracted text: 60,958 characters; status: PDF-backed; PDF signals: incentives/information, markets/allocation/design, finance/macro, welfare/behavior/development, growth/innovation.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for their pioneering contributions to general economic equilibrium theory and welfare theory.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

## 1973 - Wassily Leontief

### Wassily Leontief

Official motivation: for the development of the input-output method and for its application to important economic problems.

Evidence read: 1 lecture; extracted text: 23,047 characters; status: PDF-backed; PDF signals: markets/allocation/design, welfare/behavior/development, growth/innovation, finance/macro, incentives/information.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for the development of the input-output method and for its application to important economic problems.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 1974 - Gunnar Myrdal, Friedrich von Hayek

### Gunnar Myrdal

Official motivation: for their pioneering work in the theory of money and economic fluctuations and for their penetrating analysis of the interdependence of economic, social and institutional phenomena.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for their pioneering work in the theory of money and economic fluctuations and for their penetrating analysis of the interdependence of economic, social and institutional phenomena.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

### Friedrich von Hayek

Official motivation: for their pioneering work in the theory of money and economic fluctuations and for their penetrating analysis of the interdependence of economic, social and institutional phenomena.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for their pioneering work in the theory of money and economic fluctuations and for their penetrating analysis of the interdependence of economic, social and institutional phenomena.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 1975 - Leonid Vitaliyevich Kantorovich, Tjalling C. Koopmans

### Leonid Vitaliyevich Kantorovich

Official motivation: for their contributions to the theory of optimum allocation of resources.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for their contributions to the theory of optimum allocation of resources.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

### Tjalling C. Koopmans

Official motivation: for their contributions to the theory of optimum allocation of resources.

Evidence read: 1 lecture; extracted text: 50,154 characters; status: PDF-backed; PDF signals: growth/innovation, welfare/behavior/development, markets/allocation/design, causal/econometric design, finance/macro.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for their contributions to the theory of optimum allocation of resources.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

## 1976 - Milton Friedman

### Milton Friedman

Official motivation: for his achievements in the fields of consumption analysis, monetary history and theory and for his demonstration of the complexity of stabilization policy.

Evidence read: 1 lecture; extracted text: 66,124 characters; status: PDF-backed; PDF signals: no strong keyword signal.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for his achievements in the fields of consumption analysis, monetary history and theory and for his demonstration of the complexity of stabilization policy.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 1977 - Bertil Ohlin, James E. Meade

### Bertil Ohlin

Official motivation: for their pathbreaking contribution to the theory of international trade and international capital movements.

Evidence read: 1 lecture; extracted text: 43,270 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, growth/innovation, welfare/behavior/development, incentives/information.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for their pathbreaking contribution to the theory of international trade and international capital movements.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

### James E. Meade

Official motivation: for their pathbreaking contribution to the theory of international trade and international capital movements.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for their pathbreaking contribution to the theory of international trade and international capital movements.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

## 1978 - Herbert Simon

### Herbert Simon

Official motivation: for his pioneering research into the decision-making process within economic organizations.

Evidence read: 1 lecture; extracted text: 87,077 characters; status: PDF-backed; PDF signals: welfare/behavior/development, incentives/information, institutions/governance, growth/innovation, causal/econometric design.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for his pioneering research into the decision-making process within economic organizations.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 1979 - Theodore W. Schultz, Sir Arthur Lewis

### Theodore W. Schultz

Official motivation: for their pioneering research into economic development research with particular consideration of the problems of developing countries.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for their pioneering research into economic development research with particular consideration of the problems of developing countries.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

### Sir Arthur Lewis

Official motivation: for their pioneering research into economic development research with particular consideration of the problems of developing countries.

Evidence read: 1 lecture; extracted text: 110,140 characters; status: PDF-backed; PDF signals: no strong keyword signal.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for their pioneering research into economic development research with particular consideration of the problems of developing countries.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 1980 - Lawrence R. Klein

### Lawrence R. Klein

Official motivation: for the creation of econometric models and the application to the analysis of economic fluctuations and economic policies.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for the creation of econometric models and the application to the analysis of economic fluctuations and economic policies.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 1981 - James Tobin

### James Tobin

Official motivation: for his analysis of financial markets and their relations to expenditure decisions, employment, production and prices.

Evidence read: 1 lecture; extracted text: 97,246 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, welfare/behavior/development, incentives/information, institutions/governance.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for his analysis of financial markets and their relations to expenditure decisions, employment, production and prices.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 1982 - George J. Stigler

### George J. Stigler

Official motivation: for his seminal studies of industrial structures, functioning of markets and causes and effects of public regulation.

Evidence read: 1 lecture; extracted text: 65,551 characters; status: PDF-backed; PDF signals: institutions/governance, markets/allocation/design, growth/innovation, finance/macro, welfare/behavior/development.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for his seminal studies of industrial structures, functioning of markets and causes and effects of public regulation.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 1983 - Gerard Debreu

### Gerard Debreu

Official motivation: for having incorporated new analytical methods into economic theory and for his rigorous reformulation of the theory of general equilibrium.

Evidence read: 1 lecture; extracted text: 45,939 characters; status: PDF-backed; PDF signals: incentives/information, markets/allocation/design, formal theory/allocation, causal/econometric design, welfare/behavior/development.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for having incorporated new analytical methods into economic theory and for his rigorous reformulation of the theory of general equilibrium.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

## 1984 - Richard Stone

### Richard Stone

Official motivation: for having made fundamental contributions to the development of systems of national accounts and hence greatly improved the basis for empirical economic analysis.

Evidence read: 1 lecture; extracted text: 66,007 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, welfare/behavior/development, incentives/information, institutions/governance.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for having made fundamental contributions to the development of systems of national accounts and hence greatly improved the basis for empirical economic analysis.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 1985 - Franco Modigliani

### Franco Modigliani

Official motivation: for his pioneering analyses of saving and of financial markets.

Evidence read: 1 lecture; extracted text: 67,371 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, finance/macro, markets/allocation/design, incentives/information.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for his pioneering analyses of saving and of financial markets.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 1986 - James M. Buchanan Jr.

### James M. Buchanan Jr.

Official motivation: for his development of the contractual and constitutional bases for the theory of economic and political decision-making.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for his development of the contractual and constitutional bases for the theory of economic and political decision-making.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 1987 - Robert M. Solow

### Robert M. Solow

Official motivation: for his contributions to the theory of economic growth.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for his contributions to the theory of economic growth.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.

## 1988 - Maurice Allais

### Maurice Allais

Official motivation: for his pioneering contributions to the theory of markets and efficient utilization of resources.

Evidence read: 1 lecture; extracted text: 79,356 characters; status: PDF-backed; PDF signals: finance/macro, growth/innovation, markets/allocation/design, welfare/behavior/development, incentives/information.

Taste diagnosis: formal theory, equilibrium, and allocation.

Question taste: The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed? In this case, the motivating contribution is: for his pioneering contributions to the theory of markets and efficient utilization of resources.

Method or model taste: The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.

Evidence standard: The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.

Copyable skills:

- Build the benchmark model before adding institutional or empirical complications.
- Use assumptions to clarify what must be true for the result to matter.
- Translate the formal result back into an economic decision, constraint, or welfare tradeoff.

## 1989 - Trygve Haavelmo

### Trygve Haavelmo

Official motivation: for his clarification of the probability theory foundations of econometrics and his analyses of simultaneous economic structures.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for his clarification of the probability theory foundations of econometrics and his analyses of simultaneous economic structures.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 1990 - Harry M. Markowitz, Merton H. Miller, William F. Sharpe

### Harry M. Markowitz

Official motivation: for their pioneering work in the theory of financial economics.

Evidence read: 1 lecture; extracted text: 26,636 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, causal/econometric design, incentives/information, formal theory/allocation.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their pioneering work in the theory of financial economics.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Merton H. Miller

Official motivation: for their pioneering work in the theory of financial economics.

Evidence read: 1 lecture; extracted text: 30,864 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, institutions/governance, welfare/behavior/development, growth/innovation.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their pioneering work in the theory of financial economics.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### William F. Sharpe

Official motivation: for their pioneering work in the theory of financial economics.

Evidence read: 1 lecture; extracted text: 59,854 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, incentives/information, growth/innovation, institutions/governance.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their pioneering work in the theory of financial economics.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 1991 - Ronald H. Coase

### Ronald H. Coase

Official motivation: for his discovery and clarification of the significance of transaction costs and property rights for the institutional structure and functioning of the economy.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for his discovery and clarification of the significance of transaction costs and property rights for the institutional structure and functioning of the economy.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 1992 - Gary Becker

### Gary Becker

Official motivation: for having extended the domain of microeconomic analysis to a wide range of human behaviour and interaction, including nonmarket behaviour.

Evidence read: 1 lecture; extracted text: 60,470 characters; status: PDF-backed; PDF signals: institutions/governance, growth/innovation, welfare/behavior/development, markets/allocation/design, finance/macro.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for having extended the domain of microeconomic analysis to a wide range of human behaviour and interaction, including nonmarket behaviour.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 1993 - Robert W. Fogel, Douglass C. North

### Robert W. Fogel

Official motivation: for having renewed research in economic history by applying economic theory and quantitative methods in order to explain economic and institutional change.

Evidence read: 1 lecture; extracted text: 92,175 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, markets/allocation/design, incentives/information, finance/macro.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for having renewed research in economic history by applying economic theory and quantitative methods in order to explain economic and institutional change.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

### Douglass C. North

Official motivation: for having renewed research in economic history by applying economic theory and quantitative methods in order to explain economic and institutional change.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for having renewed research in economic history by applying economic theory and quantitative methods in order to explain economic and institutional change.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 1994 - John C. Harsanyi, John F. Nash Jr., Reinhard Selten

### John C. Harsanyi

Official motivation: for their pioneering analysis of equilibria in the theory of non-cooperative games.

Evidence read: 1 lecture; extracted text: 41,764 characters; status: PDF-backed; PDF signals: incentives/information, welfare/behavior/development, institutions/governance, causal/econometric design, markets/allocation/design.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their pioneering analysis of equilibria in the theory of non-cooperative games.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### John F. Nash Jr.

Official motivation: for their pioneering analysis of equilibria in the theory of non-cooperative games.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their pioneering analysis of equilibria in the theory of non-cooperative games.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Reinhard Selten

Official motivation: for their pioneering analysis of equilibria in the theory of non-cooperative games.

Evidence read: 1 lecture; extracted text: 65,939 characters; status: PDF-backed; PDF signals: incentives/information, markets/allocation/design, institutions/governance, welfare/behavior/development, growth/innovation.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their pioneering analysis of equilibria in the theory of non-cooperative games.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 1995 - Robert E. Lucas Jr.

### Robert E. Lucas Jr.

Official motivation: for having developed and applied the hypothesis of rational expectations, and thereby having transformed macroeconomic analysis and deepened our understanding of economic policy.

Evidence read: 1 lecture; extracted text: 56,417 characters; status: PDF-backed; PDF signals: finance/macro, incentives/information, markets/allocation/design, growth/innovation, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for having developed and applied the hypothesis of rational expectations, and thereby having transformed macroeconomic analysis and deepened our understanding of economic policy.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 1996 - James A. Mirrlees, William Vickrey

### James A. Mirrlees

Official motivation: for their fundamental contributions to the economic theory of incentives under asymmetric information.

Evidence read: 1 lecture; extracted text: 19 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their fundamental contributions to the economic theory of incentives under asymmetric information.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### William Vickrey

Official motivation: for their fundamental contributions to the economic theory of incentives under asymmetric information.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their fundamental contributions to the economic theory of incentives under asymmetric information.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 1997 - Robert C. Merton, Myron Scholes

### Robert C. Merton

Official motivation: for a new method to determine the value of derivatives.

Evidence read: 1 lecture; extracted text: 33 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for a new method to determine the value of derivatives.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Myron Scholes

Official motivation: for a new method to determine the value of derivatives.

Evidence read: 1 lecture; extracted text: 27 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for a new method to determine the value of derivatives.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 1998 - Amartya Sen

### Amartya Sen

Official motivation: for his contributions to welfare economics.

Evidence read: 1 lecture; extracted text: 37 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for his contributions to welfare economics.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 1999 - Robert Mundell

### Robert Mundell

Official motivation: for his analysis of monetary and fiscal policy under different exchange rate regimes and his analysis of optimum currency areas.

Evidence read: 1 lecture; extracted text: 18 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for his analysis of monetary and fiscal policy under different exchange rate regimes and his analysis of optimum currency areas.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 2000 - James J. Heckman, Daniel L. McFadden

### James J. Heckman

Official motivation: for his development of theory and methods for analyzing selective samples.

Evidence read: 1 lecture; extracted text: 67 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for his development of theory and methods for analyzing selective samples.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

### Daniel L. McFadden

Official motivation: for his development of theory and methods for analyzing discrete choice.

Evidence read: 1 lecture; extracted text: 35 characters; status: PDF present, text extraction weak; PDF signals: no strong keyword signal.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for his development of theory and methods for analyzing discrete choice.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 2001 - George A. Akerlof, A. Michael Spence, Joseph E. Stiglitz

### George A. Akerlof

Official motivation: for their analyses of markets with asymmetric information.

Evidence read: 1 lecture; extracted text: 124,223 characters; status: PDF-backed; PDF signals: finance/macro.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their analyses of markets with asymmetric information.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### A. Michael Spence

Official motivation: for their analyses of markets with asymmetric information.

Evidence read: 1 lecture; extracted text: 122,257 characters; status: PDF-backed; PDF signals: no strong keyword signal.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their analyses of markets with asymmetric information.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Joseph E. Stiglitz

Official motivation: for their analyses of markets with asymmetric information.

Evidence read: 1 lecture; extracted text: 122,480 characters; status: PDF-backed; PDF signals: no strong keyword signal.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their analyses of markets with asymmetric information.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 2002 - Daniel Kahneman, Vernon L. Smith

### Daniel Kahneman

Official motivation: for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

### Vernon L. Smith

Official motivation: for having established laboratory experiments as a tool in empirical economic analysis, especially in the study of alternative market mechanisms.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 49,751 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, causal/econometric design, incentives/information, institutions/governance.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for having established laboratory experiments as a tool in empirical economic analysis, especially in the study of alternative market mechanisms.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

## 2003 - Robert F. Engle III, Clive W.J. Granger

### Robert F. Engle III

Official motivation: for methods of analyzing economic time series with time-varying volatility (ARCH).

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for methods of analyzing economic time series with time-varying volatility (ARCH).

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

### Clive W.J. Granger

Official motivation: for methods of analyzing economic time series with common trends (cointegration).

Evidence read: 1 lecture; extracted text: 22,034 characters; status: PDF-backed; PDF signals: causal/econometric design, finance/macro, markets/allocation/design, welfare/behavior/development, growth/innovation.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for methods of analyzing economic time series with common trends (cointegration).

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 2004 - Finn E. Kydland, Edward C. Prescott

### Finn E. Kydland

Official motivation: for their contributions to dynamic macroeconomics: the time consistency of economic policy and the driving forces behind business cycles.

Evidence read: 1 lecture; extracted text: 39,180 characters; status: PDF-backed; PDF signals: finance/macro, growth/innovation, welfare/behavior/development, markets/allocation/design, causal/econometric design.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their contributions to dynamic macroeconomics: the time consistency of economic policy and the driving forces behind business cycles.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Edward C. Prescott

Official motivation: for their contributions to dynamic macroeconomics: the time consistency of economic policy and the driving forces behind business cycles.

Evidence read: 1 lecture; extracted text: 75,894 characters; status: PDF-backed; PDF signals: welfare/behavior/development, finance/macro, growth/innovation, incentives/information, markets/allocation/design.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their contributions to dynamic macroeconomics: the time consistency of economic policy and the driving forces behind business cycles.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 2005 - Robert J. Aumann, Thomas C. Schelling

### Robert J. Aumann

Official motivation: for having enhanced our understanding of conflict and cooperation through game-theory analysis.

Evidence read: 1 lecture; extracted text: 26,107 characters; status: PDF-backed; PDF signals: incentives/information, markets/allocation/design, causal/econometric design, finance/macro, growth/innovation.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for having enhanced our understanding of conflict and cooperation through game-theory analysis.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Thomas C. Schelling

Official motivation: for having enhanced our understanding of conflict and cooperation through game-theory analysis.

Evidence read: 1 lecture; extracted text: 35,699 characters; status: PDF-backed; PDF signals: growth/innovation, institutions/governance, finance/macro, incentives/information.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for having enhanced our understanding of conflict and cooperation through game-theory analysis.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 2006 - Edmund S. Phelps

### Edmund S. Phelps

Official motivation: for his analysis of intertemporal tradeoffs in macroeconomic policy.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for his analysis of intertemporal tradeoffs in macroeconomic policy.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 2007 - Leonid Hurwicz, Eric S. Maskin, Roger B. Myerson

### Leonid Hurwicz

Official motivation: for having laid the foundations of mechanism design theory.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for having laid the foundations of mechanism design theory.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Eric S. Maskin

Official motivation: for having laid the foundations of mechanism design theory.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for having laid the foundations of mechanism design theory.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Roger B. Myerson

Official motivation: for having laid the foundations of mechanism design theory.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for having laid the foundations of mechanism design theory.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 2008 - Paul Krugman

### Paul Krugman

Official motivation: for his analysis of trade patterns and location of economic activity.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for his analysis of trade patterns and location of economic activity.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

## 2009 - Elinor Ostrom, Oliver E. Williamson

### Elinor Ostrom

Official motivation: for her analysis of economic governance, especially the commons.

Evidence read: 1 lecture slides; extracted text: 11,890 characters; status: PDF-backed; PDF signals: institutions/governance, welfare/behavior/development, growth/innovation, incentives/information, markets/allocation/design.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for her analysis of economic governance, especially the commons.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

### Oliver E. Williamson

Official motivation: for his analysis of economic governance, especially the boundaries of the firm.

Evidence read: 1 lecture slides; extracted text: 11,842 characters; status: PDF-backed; PDF signals: institutions/governance, markets/allocation/design, incentives/information, growth/innovation, finance/macro.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for his analysis of economic governance, especially the boundaries of the firm.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 2010 - Peter A. Diamond, Dale T. Mortensen, Christopher A. Pissarides

### Peter A. Diamond

Official motivation: for their analysis of markets with search frictions.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 105,553 characters; status: PDF-backed; PDF signals: markets/allocation/design, welfare/behavior/development, incentives/information, finance/macro, growth/innovation.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for their analysis of markets with search frictions.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

### Dale T. Mortensen

Official motivation: for their analysis of markets with search frictions.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 64,890 characters; status: PDF-backed; PDF signals: markets/allocation/design, incentives/information, welfare/behavior/development, finance/macro, growth/innovation.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for their analysis of markets with search frictions.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

### Christopher A. Pissarides

Official motivation: for their analysis of markets with search frictions.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 42,984 characters; status: PDF-backed; PDF signals: markets/allocation/design, incentives/information, welfare/behavior/development, institutions/governance, growth/innovation.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for their analysis of markets with search frictions.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

## 2011 - Thomas J. Sargent, Christopher A. Sims

### Thomas J. Sargent

Official motivation: for their empirical research on cause and effect in the macroeconomy.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for their empirical research on cause and effect in the macroeconomy.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

### Christopher A. Sims

Official motivation: for their empirical research on cause and effect in the macroeconomy.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for their empirical research on cause and effect in the macroeconomy.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 2012 - Alvin E. Roth, Lloyd S. Shapley

### Alvin E. Roth

Official motivation: for the theory of stable allocations and the practice of market design.

Evidence read: 1 lecture; extracted text: 49,895 characters; status: PDF-backed; PDF signals: markets/allocation/design, incentives/information, welfare/behavior/development, institutions/governance, finance/macro.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for the theory of stable allocations and the practice of market design.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

### Lloyd S. Shapley

Official motivation: for the theory of stable allocations and the practice of market design.

Evidence read: 1 lecture; extracted text: 4,382 characters; status: PDF-backed; PDF signals: markets/allocation/design, incentives/information.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for the theory of stable allocations and the practice of market design.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

## 2013 - Eugene F. Fama, Lars Peter Hansen, Robert J. Shiller

### Eugene F. Fama

Official motivation: for their empirical analysis of asset prices.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 61,708 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, incentives/information, growth/innovation, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their empirical analysis of asset prices.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Lars Peter Hansen

Official motivation: for their empirical analysis of asset prices.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 130,486 characters; status: PDF-backed; PDF signals: finance/macro, causal/econometric design, markets/allocation/design, incentives/information, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their empirical analysis of asset prices.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Robert J. Shiller

Official motivation: for their empirical analysis of asset prices.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 119,235 characters; status: PDF-backed; PDF signals: markets/allocation/design, finance/macro, institutions/governance, growth/innovation, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for their empirical analysis of asset prices.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 2014 - Jean Tirole

### Jean Tirole

Official motivation: for his analysis of market power and regulation.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 56,896 characters; status: PDF-backed; PDF signals: markets/allocation/design, incentives/information, institutions/governance, growth/innovation, finance/macro.

Taste diagnosis: markets, trade, allocation, and design.

Question taste: The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit. In this case, the motivating contribution is: for his analysis of market power and regulation.

Method or model taste: The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.

Evidence standard: The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.

Copyable skills:

- Start from the allocation problem before proposing a market mechanism.
- Use a benchmark to identify which friction changes the outcome.
- Explain the welfare or distributional consequence of the market design choice.

## 2015 - Angus Deaton

### Angus Deaton

Official motivation: for his analysis of consumption, poverty, and welfare.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 99,856 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, finance/macro, institutions/governance, markets/allocation/design.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for his analysis of consumption, poverty, and welfare.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 2016 - Oliver Hart, Bengt Holmstrom

### Oliver Hart

Official motivation: for their contributions to contract theory.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 88,421 characters; status: PDF-backed; PDF signals: incentives/information, finance/macro, markets/allocation/design, institutions/governance, welfare/behavior/development.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their contributions to contract theory.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Bengt Holmstrom

Official motivation: for their contributions to contract theory.

Evidence read: 1 lecture, 1 lecture slides; extracted text: 86,855 characters; status: PDF-backed; PDF signals: incentives/information, markets/allocation/design, finance/macro, institutions/governance, growth/innovation.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for their contributions to contract theory.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 2017 - Richard H. Thaler

### Richard H. Thaler

Official motivation: for his contributions to behavioural economics.

Evidence read: 1 lecture slides; extracted text: 12,854 characters; status: PDF-backed; PDF signals: welfare/behavior/development, markets/allocation/design, finance/macro, formal theory/allocation, growth/innovation.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for his contributions to behavioural economics.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 2018 - William D. Nordhaus, Paul M. Romer

### William D. Nordhaus

Official motivation: for integrating climate change into long-run macroeconomic analysis.

Evidence read: 1 advanced background, 1 lecture, 1 popular background; extracted text: 213,406 characters; status: PDF-backed; PDF signals: growth/innovation, markets/allocation/design, welfare/behavior/development, finance/macro, incentives/information.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for integrating climate change into long-run macroeconomic analysis.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.

### Paul M. Romer

Official motivation: for integrating technological innovations into long-run macroeconomic analysis.

Evidence read: 1 advanced background, 1 popular background; extracted text: 145,355 characters; status: PDF-backed; PDF signals: growth/innovation, welfare/behavior/development, markets/allocation/design, finance/macro, incentives/information.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for integrating technological innovations into long-run macroeconomic analysis.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.

## 2019 - Abhijit Banerjee, Esther Duflo, Michael Kremer

### Abhijit Banerjee

Official motivation: for their experimental approach to alleviating global poverty.

Evidence read: 1 advanced background, 1 lecture, 1 popular background; extracted text: 166,752 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, incentives/information, finance/macro, institutions/governance.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for their experimental approach to alleviating global poverty.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

### Esther Duflo

Official motivation: for their experimental approach to alleviating global poverty.

Evidence read: 1 advanced background, 1 lecture, 1 lecture slides, 1 popular background; extracted text: 196,310 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, incentives/information, finance/macro, institutions/governance.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for their experimental approach to alleviating global poverty.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

### Michael Kremer

Official motivation: for their experimental approach to alleviating global poverty.

Evidence read: 1 advanced background, 1 lecture, 1 popular background; extracted text: 182,036 characters; status: PDF-backed; PDF signals: welfare/behavior/development, growth/innovation, incentives/information, institutions/governance, finance/macro.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for their experimental approach to alleviating global poverty.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 2020 - Paul R. Milgrom, Robert B. Wilson

### Paul R. Milgrom

Official motivation: for improvements to auction theory and inventions of new auction formats.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for improvements to auction theory and inventions of new auction formats.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

### Robert B. Wilson

Official motivation: for improvements to auction theory and inventions of new auction formats.

Evidence read: No direct official PDF in local cache; extracted text: 0 characters; status: API-only, PDF needed; PDF signals: none.

Taste diagnosis: incentives, information, contracts, and strategic design.

Question taste: The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict. In this case, the motivating contribution is: for improvements to auction theory and inventions of new auction formats.

Method or model taste: The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.

Evidence standard: The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.

Copyable skills:

- Isolate the information or incentive friction before adding complexity.
- Use the model to generate a prediction that could be wrong.
- Explain the real institution through the constraint that binds in the model.

## 2021 - David Card, Joshua D. Angrist, Guido W. Imbens

### David Card

Official motivation: for his empirical contributions to labour economics.

Evidence read: 1 advanced background; extracted text: 121,244 characters; status: PDF-backed; PDF signals: causal/econometric design, welfare/behavior/development, markets/allocation/design, growth/innovation, institutions/governance.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for his empirical contributions to labour economics.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

### Joshua D. Angrist

Official motivation: for their methodological contributions to the analysis of causal relationships.

Evidence read: 1 advanced background; extracted text: 121,244 characters; status: PDF-backed; PDF signals: causal/econometric design, welfare/behavior/development, markets/allocation/design, growth/innovation, institutions/governance.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for their methodological contributions to the analysis of causal relationships.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

### Guido W. Imbens

Official motivation: for their methodological contributions to the analysis of causal relationships.

Evidence read: 1 advanced background; extracted text: 121,244 characters; status: PDF-backed; PDF signals: causal/econometric design, welfare/behavior/development, markets/allocation/design, growth/innovation, institutions/governance.

Taste diagnosis: causal design, econometrics, and measurement discipline.

Question taste: The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit. In this case, the motivating contribution is: for their methodological contributions to the analysis of causal relationships.

Method or model taste: The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.

Evidence standard: The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.

Copyable skills:

- Name the object of learning before estimating it.
- Turn a data limitation into an explicit design or model assumption.
- Write the failure mode of the empirical strategy in plain language.

## 2022 - Ben Bernanke, Douglas Diamond, Philip Dybvig

### Ben Bernanke

Official motivation: for research on banks and financial crises.

Evidence read: 1 advanced background, 1 lecture slides, 1 popular background; extracted text: 154,423 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, incentives/information, institutions/governance, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for research on banks and financial crises.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Douglas Diamond

Official motivation: for research on banks and financial crises.

Evidence read: 1 advanced background, 1 lecture slides, 1 popular background; extracted text: 151,495 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, incentives/information, institutions/governance, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for research on banks and financial crises.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

### Philip Dybvig

Official motivation: for research on banks and financial crises.

Evidence read: 1 advanced background, 1 lecture slides, 1 popular background; extracted text: 149,104 characters; status: PDF-backed; PDF signals: finance/macro, markets/allocation/design, incentives/information, institutions/governance, welfare/behavior/development.

Taste diagnosis: finance, macroeconomics, and market signals.

Question taste: The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes. In this case, the motivating contribution is: for research on banks and financial crises.

Method or model taste: The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.

Evidence standard: The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.

Copyable skills:

- Use prices or balance sheets as evidence without confusing them with explanation.
- Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.
- Build a benchmark case first, then show which friction makes the observed fact informative.

## 2023 - Claudia Goldin

### Claudia Goldin

Official motivation: for having advanced our understanding of women's labour market outcomes.

Evidence read: 1 advanced background, 1 lecture slides, 1 popular background; extracted text: 132,440 characters; status: PDF-backed; PDF signals: welfare/behavior/development, markets/allocation/design, growth/innovation, institutions/governance, incentives/information.

Taste diagnosis: welfare, behavior, poverty, and human decision-making.

Question taste: The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved. In this case, the motivating contribution is: for having advanced our understanding of women's labour market outcomes.

Method or model taste: The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.

Evidence standard: The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.

Copyable skills:

- Turn a human outcome into a decision problem with constraints.
- Use experiments, surveys, or welfare formulas to distinguish mechanism from description.
- Keep policy claims tied to the behavioral or welfare evidence actually observed.

## 2024 - Daron Acemoglu, Simon Johnson, James A. Robinson

### Daron Acemoglu

Official motivation: for studies of how institutions are formed and affect prosperity.

Evidence read: 1 advanced background, 1 lecture, 1 popular background; extracted text: 155,062 characters; status: PDF-backed; PDF signals: institutions/governance, growth/innovation, incentives/information, welfare/behavior/development, causal/econometric design.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for studies of how institutions are formed and affect prosperity.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

### Simon Johnson

Official motivation: for studies of how institutions are formed and affect prosperity.

Evidence read: 1 advanced background, 1 lecture, 1 popular background; extracted text: 151,146 characters; status: PDF-backed; PDF signals: institutions/governance, growth/innovation, incentives/information, welfare/behavior/development, causal/econometric design.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for studies of how institutions are formed and affect prosperity.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

### James A. Robinson

Official motivation: for studies of how institutions are formed and affect prosperity.

Evidence read: 1 advanced background, 1 lecture, 1 popular background; extracted text: 179,754 characters; status: PDF-backed; PDF signals: institutions/governance, growth/innovation, incentives/information, causal/econometric design, welfare/behavior/development.

Taste diagnosis: institutions, governance, and political economy.

Question taste: The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context. In this case, the motivating contribution is: for studies of how institutions are formed and affect prosperity.

Method or model taste: The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.

Evidence standard: The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.

Copyable skills:

- Translate an institutional detail into a causal mechanism.
- Compare governance arrangements by the incentives and constraints they create.
- Keep the claim bounded to what the institutional evidence can actually identify.

## 2025 - Joel Mokyr, Philippe Aghion, Peter Howitt

### Joel Mokyr

Official motivation: for having identified the prerequisites for sustained growth through technological progress.

Evidence read: 1 advanced background, 1 popular background; extracted text: 143,265 characters; status: PDF-backed; PDF signals: growth/innovation, markets/allocation/design, incentives/information, welfare/behavior/development, institutions/governance.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for having identified the prerequisites for sustained growth through technological progress.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.

### Philippe Aghion

Official motivation: for the theory of sustained growth through creative destruction.

Evidence read: 1 advanced background, 1 popular background; extracted text: 143,265 characters; status: PDF-backed; PDF signals: growth/innovation, markets/allocation/design, incentives/information, welfare/behavior/development, institutions/governance.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for the theory of sustained growth through creative destruction.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.

### Peter Howitt

Official motivation: for the theory of sustained growth through creative destruction.

Evidence read: 1 advanced background, 1 popular background; extracted text: 143,265 characters; status: PDF-backed; PDF signals: growth/innovation, markets/allocation/design, incentives/information, welfare/behavior/development, institutions/governance.

Taste diagnosis: growth, innovation, and historical change.

Question taste: The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy? In this case, the motivating contribution is: for the theory of sustained growth through creative destruction.

Method or model taste: The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.

Evidence standard: The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.

Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.

Boundary: The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.

Copyable skills:

- Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.
- Use historical comparison to separate persistence, shock, and adaptation.
- State why the mechanism travels beyond the original episode without claiming universality.
