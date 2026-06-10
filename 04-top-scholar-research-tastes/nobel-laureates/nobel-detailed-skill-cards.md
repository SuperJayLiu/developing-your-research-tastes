# Nobel Detailed Skill Cards

The table in the Nobel Skill Map is only an index. The actual reader-facing skills should be read here. Each card is written as a reusable research instruction rather than a short slogan. A mature skill must tell the researcher when to use it, what move to perform, how to diagnose failure, how to practice the move, and where imitation becomes bad taste.

These cards are also backed by an operational skill package under `00-start-here/_support/skills/nobel-research-taste/`. That package keeps the agent-facing trigger file, gotchas, examples, evidence anchors, reusable template, and validator separate from this chapter. The separation matters: this page should read like a short book chapter, while the support package should help maintainers and agents create, revise, and check skills consistently.

The transfer test for every card is simple: after applying the skill to a different project, the researcher should be able to say exactly what changed in the question, model, evidence, mechanism, contribution, or writing. If the card cannot improve a project outside the original Nobel topic, it remains a reading note rather than a mature skill.

---

name: causal-design-econometrics-and-measurement-discipline

description: Use when a project needs to learn from imperfect data, selective samples, dynamic systems, noisy measurement, time series, or quasi-experimental variation. This skill is especially relevant for projects inspired by Frisch, Tinbergen, Haavelmo, Heckman, McFadden, Engle, Granger, Card, Angrist, Imbens, and related Nobel traditions in econometrics and causal inference.

# Causal Design, Econometrics, and Measurement Discipline

This skill is for turning an empirical ambition into a disciplined object of learning. The central move is not to run a more advanced method. The central move is to name what the researcher wants to learn before estimating it, then make the source of learning visible enough that a skeptical reader can see both the force and the weakness of the design.

Use this skill when a project has data but the claim is still vague. The trigger is usually one of four conditions: the paper reports an effect without a clear estimand; the comparison group is convenient rather than credible; the measurement object is available but not justified; or the method is technically sophisticated but the identifying assumption is hidden. The skill asks the researcher to pause and write the learning object in plain language: what would be true in the world if this design worked?

Move 1 is to define the object of learning. For causal work, state the treatment, comparison, outcome, population, margin, and counterfactual. For econometric or time-series work, state the process, parameter, shock, persistence object, or forecasting relation. For measurement work, state the latent concept and why the observed proxy should move with it. If the object cannot be stated without method jargon, the design is not yet mature.

Move 2 is to name the source of variation or structure. The reader should know whether learning comes from timing, assignment, policy rules, instruments, panel structure, distributional restrictions, dynamic restrictions, survey design, experimental control, or model-implied moments. This move should also name the nearest threat: selection, simultaneity, anticipation, attrition, measurement error, weak instruments, omitted shocks, equilibrium feedback, or extrapolation.

Move 3 is to match the claim to the evidence. A clean estimate can support a narrow claim; it cannot automatically support a mechanism, welfare statement, or policy conclusion. If the design estimates a reduced-form effect, say so. If the paper wants a mechanism, add a design feature that tests the mechanism. If the paper wants welfare, explain what additional assumptions or model structure bridge from the estimate to welfare.

Diagnostics: Can the estimand be written in one sentence? Can a reader say where identification comes from? Is the strongest alternative explanation named before the results? Does the method clarify the question rather than replace it? Does the conclusion use the same level of language as the design supports?

Common anti-patterns include treating a method as a contribution, using "causal" language because the regression is elaborate, adding robustness checks that do not test the main threat, and presenting a coefficient as a mechanism. A project using this skill well should become more modest and more persuasive at the same time.

Practice prompt: Apply this skill to my project. State the estimand or object of learning, the source of variation or structure, the closest alternative explanation, the design feature that addresses it, the claim the evidence can support, and the claim the evidence cannot support.

---

name: formal-theory-equilibrium-and-allocation

description: Use when a project needs a model, benchmark, equilibrium argument, welfare object, or allocation logic. This skill is especially relevant for work inspired by Samuelson, Hicks, Arrow, Kantorovich, Koopmans, Debreu, Allais, and other Nobel traditions where formal structure changes how economists reason.

# Formal Theory, Equilibrium, and Allocation

This skill is for making intuition disciplined enough to travel. The purpose of a model is not to decorate a paper with mathematics. The purpose is to isolate a force, define a benchmark, derive a result, and make clear what changes when assumptions change. A good theory skill makes the research question sharper before any notation appears.

Use this skill when a project has a plausible story but no precise economic object. The trigger is a sentence like "agents respond to incentives" or "markets allocate resources inefficiently" that sounds right but does not yet specify agents, constraints, timing, information, objective functions, equilibrium, or welfare. The skill turns that loose statement into a formal environment where the key force can be inspected.

Move 1 is to build the benchmark. State what happens in the simplest world without the friction, constraint, missing market, institutional rule, or informational problem. The benchmark is not a throwaway assumption; it is what lets the reader see why the later complication matters. If the benchmark already produces the result, the proposed mechanism is not doing work.

Move 2 is to introduce one load-bearing departure. The departure might be a constraint, hidden information, dynamic adjustment, indivisibility, externality, market incompleteness, bargaining problem, participation constraint, or equilibrium refinement. Introduce it only if it changes a prediction, welfare comparison, or interpretation. A model with many realistic details but no load-bearing departure is usually weaker than a spare model with one disciplined force.

Move 3 is to translate the result back into economics. The model should tell the reader what decision, market outcome, welfare tradeoff, or empirical pattern should change. A formal result that cannot be explained outside notation is not yet a research taste skill; it is a private calculation.

Diagnostics: What is the benchmark? What assumption changes the result? Which comparative static could be wrong? What real economic object does the proposition clarify? What would an empirical reader look for if the mechanism were true?

Common anti-patterns include proving a result whose economic content is unclear, adding assumptions to force the desired conclusion, hiding intuition inside notation, and claiming generality when the result depends on a fragile parameter restriction. Strong use of this skill produces less notation than the author initially wants and more economic discipline than the reader expects.

Practice prompt: Apply this skill to my project. Define the benchmark model, name the one departure that matters, state the prediction or welfare tradeoff, explain why the result would fail without the departure, and translate the result into one empirical or institutional implication.

---

name: growth-innovation-and-historical-change

description: Use when a project studies long-run growth, technological change, innovation, development paths, institutions over time, historical persistence, or creative destruction. This skill is especially relevant for Nobel-linked work by Kuznets, Solow, Fogel, North, Nordhaus, Romer, Mokyr, Aghion, Howitt, and related scholars.

# Growth, Innovation, and Historical Change

This skill is for turning a long-run fact into a mechanism. Long-run research is attractive because the questions are large, but size alone does not create taste. The skill is to show why a historical pattern, institutional condition, technological change, or growth difference reveals a mechanism that can be stated, compared, and bounded.

Use this skill when a project begins with a broad pattern: one economy grows faster than another, a technology diffuses unevenly, an institution persists, a sector transforms, or a historical shock appears to matter decades later. The trigger is ambition without a channel. If the project says "history matters" but cannot say through what state variable, incentive, constraint, belief, technology, or organization history matters, the skill is needed.

Move 1 is to identify the moving part. The moving part might be knowledge accumulation, human capital, institutions, competition, path dependence, energy use, climate constraints, organizational routines, political incentives, or creative destruction. It must be more specific than "growth" or "technology." A reader should be able to ask whether that moving part increased, decreased, persisted, or interacted with another force.

Move 2 is to separate persistence from mechanism. A historical correlation is not yet an explanation. Ask why the effect survives: does the initial condition alter incentives, capabilities, networks, beliefs, capital stocks, policy, or selection? If the answer is only that the past predicts the present, the paper has a fact but not yet a taste move.

Move 3 is to choose the right comparison. Long-run work often cannot rely on a single clean experiment, so comparison must be cumulative and disciplined. Compare across regions, sectors, cohorts, technologies, institutions, or time periods in a way that would make the proposed channel more plausible and rival channels less plausible.

Diagnostics: What is the historical or long-run fact? What mechanism carries it forward? What comparison would make the channel credible? What rival explanation is hardest to rule out? What claim travels beyond the original setting, and what claim should stay local?

Common anti-patterns include treating history as atmosphere, treating persistence as proof, turning a broad trend into a causal claim without a channel, and claiming universal lessons from one episode. Good use of this skill makes a big question more precise rather than merely more dramatic.

Practice prompt: Apply this skill to my project. Name the long-run fact, the state variable or mechanism that carries it, the comparison that would discipline the claim, the rival channel, the evidence that would separate the channels, and the boundary of the lesson.

---

name: institutions-governance-and-political-economy

description: Use when a project studies institutions, political constraints, property rights, regulation, governance, public choice, legal rules, organizations, or the commons. This skill is especially relevant for Hayek, Myrdal, Buchanan, Coase, Stigler, Ostrom, Williamson, Acemoglu, Johnson, Robinson, and adjacent Nobel traditions.

# Institutions, Governance, and Political Economy

This skill is for treating institutions as mechanisms rather than scenery. Institutional detail is valuable only when it changes incentives, information, bargaining power, enforcement, participation, or feasible choices. The mature move is to identify exactly how a rule or governance arrangement changes economic behavior and what evidence would show that this channel matters.

Use this skill when a project has an interesting setting but the institutional content is still descriptive. The trigger is a paragraph full of legal, political, or organizational facts that does not yet explain which fact is doing the work. A reader should never have to guess whether the key institution matters through property rights, enforcement, transaction costs, information, political selection, regulatory constraints, or collective action.

Move 1 is to translate the institution into a constraint. Write the institution in the form: because rule X changes constraint Y for agent Z, behavior or outcome W should change. This sentence is the core of institutional taste. Without it, the institution is background.

Move 2 is to identify the relevant comparison. Institutional papers need a counterfactual: what would happen under a different rule, weaker enforcement, alternative governance, different political constraint, or changed property-rights regime? The comparison can be historical, cross-sectional, theoretical, or institutional, but it must make the mechanism observable.

Move 3 is to bound the claim. Institutions are bundled. A setting may differ in law, culture, wealth, geography, state capacity, markets, and selection at the same time. A good institutional claim says which bundle component the paper isolates and which components remain threats.

Diagnostics: What rule or governance arrangement matters? Whose incentives or constraints change? What behavior should change if the channel is real? What alternative institutional or historical factor could explain the same pattern? Does the conclusion claim only what the institutional comparison can support?

Common anti-patterns include using institutional color as motivation, calling every contextual difference an institution, assuming a rule is enforced because it exists, and leaping from one setting to universal institutional lessons. Strong use of this skill makes the setting less ornamental and the claim more credible.

Practice prompt: Apply this skill to my project. State the institutional rule, the agent affected, the changed constraint, the predicted behavior, the comparison that identifies the channel, the strongest bundled confound, and the narrowest honest contribution.

---

name: incentives-information-contracts-and-strategic-design

description: Use when a project involves asymmetric information, hidden action, incentives, contracts, mechanism design, auctions, game theory, strategic interaction, bargaining, or organizational design. This skill draws from Nobel traditions including Harsanyi, Nash, Selten, Mirrlees, Vickrey, Akerlof, Spence, Stiglitz, Hurwicz, Maskin, Myerson, Hart, Holmstrom, Milgrom, Wilson, and related work.

# Incentives, Information, Contracts, and Strategic Design

This skill is for finding the strategic friction that changes behavior. Many projects say "incentives matter" or "information matters." A mature skill card forces the researcher to say which incentive, which information asymmetry, which constraint, and which strategic response make the outcome different from a benchmark.

Use this skill when a project has agents whose actions depend on what they know, what others know, what contracts allow, what mechanisms ask them to reveal, or what strategic environment they face. The trigger is a story with strategic language but no explicit friction. If removing hidden information, hidden action, bargaining, or strategic interaction would not change the paper's prediction, the skill has not yet been used.

Move 1 is to name the private object. What does one party know, choose, hide, reveal, promise, or enforce that another party cannot perfectly observe or control? The private object can be type, effort, quality, risk, valuation, outside option, signal, cost, or future action. Naming it prevents the model from becoming generic incentive talk.

Move 2 is to write the constraint. The key constraint may be incentive compatibility, participation, limited liability, enforcement, budget balance, individual rationality, no-arbitrage, equilibrium beliefs, or strategic stability. The constraint should explain why the first-best outcome is unavailable.

Move 3 is to connect the design to the outcome. A contract, auction, mechanism, or equilibrium concept matters because it changes behavior under the constraint. The paper should explain what is gained, what is lost, and whose objective is being optimized.

Diagnostics: What is privately known or privately chosen? What constraint binds? What benchmark fails? What prediction changes when the friction is added? What institution or data pattern would reveal the friction?

Common anti-patterns include using game theory as vocabulary, adding incentive constraints after the empirical result, calling any heterogeneity asymmetric information, and deriving elegant equilibria with no empirical or institutional interpretation. Good use of this skill makes the friction load-bearing.

Practice prompt: Apply this skill to my project. Name the agents, the private object, the binding constraint, the benchmark without the friction, the prediction with the friction, the evidence or institution that reveals it, and the welfare or design implication.

---

name: finance-macroeconomics-and-market-signals

description: Use when a project learns from prices, returns, volatility, financial institutions, bank balance sheets, crises, monetary regimes, asset pricing models, exchange rates, or macro-financial data. This skill is especially relevant for Tobin, Friedman, Modigliani, Markowitz, Miller, Sharpe, Merton, Scholes, Lucas, Mundell, Fama, Hansen, Shiller, Bernanke, Diamond, Dybvig, and related finance and macro traditions.

# Finance, Macroeconomics, and Market Signals

This skill is for using prices and financial quantities as evidence without confusing them with explanations. Finance and macro data are powerful because they aggregate expectations, constraints, risks, policies, and institutional frictions. They are dangerous for the same reason: one pattern can usually support several stories.

Use this skill when a project observes a return pattern, price movement, volatility process, bank behavior, crisis episode, policy regime, exchange-rate fact, or macro-financial correlation. The trigger is interpretive ambiguity. If the project moves directly from a market pattern to a mechanism without considering risk, beliefs, constraints, liquidity, balance sheets, policy, and measurement, the skill is needed.

Move 1 is to define the benchmark. The benchmark might be market efficiency, no-arbitrage, representative-agent pricing, frictionless corporate finance, a monetary model, a banking model, or a simple balance-sheet identity. The benchmark tells the reader what should happen absent the proposed friction.

Move 2 is to separate interpretations. A return predictability result might reflect risk, mispricing, data mining, limits to arbitrage, changing discount rates, or cash-flow news. A bank lending contraction might reflect credit supply, loan demand, risk management, regulation, or borrower selection. The paper should not claim a mechanism until the main alternatives are named.

Move 3 is to connect evidence to the mechanism. The best finance and macro papers use additional moments, institutional details, decompositions, natural experiments, model restrictions, or cross-sectional predictions to separate channels. The mechanism should earn the right to interpret the price or quantity pattern.

Diagnostics: What is the benchmark? What pattern violates or modifies it? What are the nearest alternative interpretations? What extra evidence separates them? Does the paper claim risk, beliefs, frictions, policy, or welfare more strongly than the evidence allows?

Common anti-patterns include treating a price pattern as self-explanatory, calling an anomaly a behavioral mechanism, confusing predictability with mispricing, using crisis language without balance-sheet evidence, and making policy claims from reduced-form market facts. Good use of this skill makes interpretation slower and therefore stronger.

Practice prompt: Apply this skill to my project. State the market or macro fact, the benchmark, the candidate mechanisms, the evidence that separates them, the interpretation that survives, and the claim that remains too strong.

---

name: welfare-behavior-poverty-and-human-decision-making

description: Use when a project studies welfare, poverty, development, consumption, household behavior, labor outcomes, decision-making, behavioral economics, experiments, or human constraints. This skill is especially relevant for Schultz, Lewis, Becker, Sen, Kahneman, Deaton, Thaler, Banerjee, Duflo, Kremer, Goldin, and related traditions.

# Welfare, Behavior, Poverty, and Human Decision-Making

This skill is for making human outcomes economically precise without stripping away the constraint that makes them human. It applies when the paper studies choices, welfare, poverty, development, behavior, labor-market outcomes, or household decisions. The goal is not to moralize the outcome. The goal is to identify the decision problem, constraint, intervention, and welfare object.

Use this skill when a project has an important human outcome but the mechanism is still sentimental or descriptive. The trigger is a statement like "people make poor decisions," "poverty matters," or "women face barriers" without a precise account of constraints, information, incentives, norms, markets, institutions, or choice sets.

Move 1 is to define the decision or welfare object. What does the agent choose, experience, lack, misperceive, postpone, overvalue, undervalue, or fail to access? For welfare work, state the welfare criterion. For behavioral work, state the bias, belief error, attention constraint, or decision environment. For development work, state the binding constraint or intervention margin.

Move 2 is to connect the observed outcome to a mechanism. A treatment effect is more useful when it teaches why the intervention works. A behavioral anomaly is more useful when it changes a prediction. A welfare measure is more useful when it changes a policy ranking or research interpretation.

Move 3 is to protect the boundary. Human-centered topics invite overclaiming. The evidence may support an effect in a setting without supporting a universal behavioral law, welfare conclusion, or policy mandate. The skill requires the researcher to keep setting, population, mechanism, and welfare interpretation aligned.

Diagnostics: What is the decision problem? What constraint or behavioral force changes the outcome? What evidence distinguishes mechanism from description? What welfare criterion is being used? What policy or interpretation would be wrong if the mechanism were different?

Common anti-patterns include reporting effects without mechanism, treating poverty or inequality as self-motivating, turning behavioral language into labels, and making welfare claims without welfare objects. Good use of this skill makes empathy compatible with rigor.

Practice prompt: Apply this skill to my project. State the human outcome, the decision problem, the binding constraint or behavioral force, the evidence that identifies it, the welfare or policy implication, and the boundary of external validity.

---

name: markets-trade-allocation-and-design

description: Use when a project studies markets, trade, location, matching, auctions, search, regulation, industrial organization, allocation, market design, or resource movement across places and agents. This skill applies to Nobel traditions including Ohlin, Meade, Leontief, Stigler, Krugman, Roth, Shapley, Tirole, Diamond, Mortensen, Pissarides, and related work.

# Markets, Trade, Allocation, and Design

This skill is for seeing markets as allocation systems rather than arenas where "supply meets demand" in the abstract. A market paper becomes stronger when it identifies the allocation problem, the friction or rule that shapes the market, and the welfare or distributional consequence of that arrangement.

Use this skill when a project studies trade flows, industry structure, matching, search, auctions, regulation, market power, geography, platform rules, or institutional design. The trigger is a market description that does not yet say what problem the market solves or fails to solve. If the reader cannot say who is matched with whom, what is allocated, what constraint binds, and why the design matters, the skill is needed.

Move 1 is to state the allocation object. The object can be jobs, capital, goods, students, organs, credit, liquidity, information, firms, locations, or risk. The paper should say why the allocation is economically meaningful and what margin changes.

Move 2 is to define the friction or design feature. Search costs, increasing returns, market power, congestion, information, rules, geography, entry, matching constraints, or regulatory limits can all change allocation. The key is to show why this feature changes outcomes relative to a benchmark.

Move 3 is to state the consequence. Market design and trade papers should not stop at mechanism. They should say who gains, who loses, what efficiency changes, what distributional margin moves, or what policy counterfactual becomes clearer.

Diagnostics: What is being allocated? What benchmark allocation would occur without the friction or rule? What feature changes allocation? What evidence or model shows the change? What welfare or distributional consequence follows?

Common anti-patterns include describing a market without an allocation problem, calling a platform or auction "designed" without saying what constraint it solves, and treating trade or location patterns as interesting without explaining the economic force behind them. Good use of this skill makes the market architecture visible.

Practice prompt: Apply this skill to my project. Name the allocation object, the agents, the benchmark, the friction or design rule, the predicted allocation change, the evidence that distinguishes the mechanism, and the welfare or distributional consequence.
