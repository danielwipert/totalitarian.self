# Claims register

Every claim the essay makes, numbered so it can be tested against the sources. The thesis is unproven until these claims are tested. A claim that the sources challenge gets revised, not defended.

## How it works

1. Each claim has an ID: `C` + spec section + number (C4.3 = the third claim in §4).
2. Passages in `sources/primary/` are tagged with claim IDs and marked **for**, **against** or **complicates**.
3. To see the evidence for a claim, search the repo for its ID (e.g. `grep -rn "C4.3" sources/`).
4. Once there's enough evidence, update the claim's status and log the change in `decisions.md`.

**Status:** `untested` · `supported` · `challenged` · `revised` · `dropped`

**Kind** (what counts as a test):

- **textual**: does the primary text actually say this? Tested by reading the source.
- **reception**: how a text was *received*, as distinct from what it says. Needs later writers and historians.
- **historical**: a claim about what happened and why. Needs primary documents plus historians.
- **empirical**: a claim about how people behave now. Needs sociology or psychology data.
- **conceptual**: tested by argument, not by sources. It still has to be consistent with the textual claims.

**Status changes so far** are logged in `decisions.md`, with the passage IDs that caused them.

Each section also has **pressure points**: known reasons a claim might fail. These are what to look for first.

---

## §1 Thesis (umbrella claims)

These stand or fall with the section claims beneath them.

| ID | Claim | Kind | Depends on | Status |
|---|---|---|---|---|
| C1.1 | The Self began as a necessary acknowledgment of human difference. | conceptual | C4.* | untested |
| C1.2 | In the West, above all in America, it calcified into a totalizing dogma. | historical | C5.*, C6.* | untested |
| C1.3 | The totalized Self suppresses the truths it was meant to reveal. | conceptual | C5.7, C7.* | untested |

---

## §4 Origin

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C4.1 | The Self was neither invented nor discovered: it acknowledged something already present that role-assigning social orders had repressed. | conceptual | all §4 sources | untested |
| C4.2 | The collapse of the old social order and the rise of capital produced the awareness that persons could direct their own futures rather than fill socioeconomic roles. | historical | Fromm; Weber, *Protestant Ethic* | untested |
| C4.3 | Luther individuated the relationship with God, freeing it from church structure. | textual | Luther, *Freedom of a Christian*; *Address to the Christian Nobility*; *Babylonian Captivity* | untested |
| C4.4 | Calvin's predestination, deterministic in doctrine, in practice drove individuals to prove their election through work and frugality. | textual + historical | Calvin, *Institutes* III.xxi–xxiv; Weber; Fromm | challenged |
| C4.5 | The economic origin is load-bearing: the Self responded to a freer economic situation and was not a pure act of thought. | historical | Fromm; Weber; Taylor | untested |
| C4.6 | The cogito locates identity in a non-material mind, separate from the body. | textual | Descartes, *Meditations* II and VI; *Discourse* IV | untested |
| C4.7 | As received by Western culture, the cogito fused identity with a separate Mind removed from the physical world, whatever Descartes himself believed. | reception | Descartes reception history | untested |
| C4.8 | Plato and Augustine laid the groundwork for the separate soul-mind-self; Descartes made it operational. | textual | Plato, *Phaedo*; Augustine, *Confessions* X, *De Trinitate* X, *City of God* XI.26 | untested |
| C4.9 | Locke founds personal identity on consciousness (memory), not on the substance of soul or body. | textual | Locke, *Essay* II.xxvii | supported |
| C4.10 | For Locke, "person" is a forensic term: the unit to which actions, merit, guilt and punishment are attributed. | textual | Locke, *Essay* II.xxvii.26 | supported |
| C4.11 | The *tabula rasa* makes the Self something built from experience, not given, which cuts it loose from inherited nature. | textual | Locke, *Essay* I; II.i | challenged |
| C4.12 | Nietzsche saw that this forensic framework is what makes guilt attributable. | textual | Nietzsche, *Genealogy of Morals* II; *Twilight of the Idols*, "The Four Great Errors" | untested |
| C4.13 | At each of these moments the Self was doing something true: acknowledging difference against orders that denied it. | conceptual | all §4 sources | untested |
| C4.14 | The core moves came unusually fast (1517 → 1689), faster than the concept could be integrated. | historical | comparison with other intellectual shifts | untested |

**Pressure points**

- **C4.4:** Weber located the work-as-proof dynamic in *later* Puritans (Baxter and others), not in Calvin. Calvin himself warns against seeking assurance of election in one's works. This claim may need to be about Calvinism, not Calvin.
- **C4.3:** Luther's *Freedom of a Christian* pairs inner freedom with service: "A Christian man is the most free lord of all, and subject to none; a Christian man is the most dutiful servant of all, and subject to every one." (verified, Gutenberg #1911) Individuation may come bound to a new kind of service.
- **C4.8:** Augustine's "si fallor, sum" ("if I am mistaken, I exist") anticipates the cogito by twelve centuries. That weakens the "speed" claim (C4.14) and strengthens the "groundwork" claim.
- **C4.11:** Locke writes "white paper," not "tabula rasa," and his Book I targets innate *ideas*, not inherited nature in general.
- **C4.14:** Locke's chapter on personal identity (II.xxvii) was added in the 2nd edition of 1694, so the span may be 1517 → 1694. To verify.
- **C4.6:** In *Meditations* VI, Descartes says "I am not only lodged in my body as a pilot in a vessel, but that I am very closely united to it" (verified, Haldane & Ross 1911).

---

## §5 Mutation

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C5.1 | Any vocabulary selects some features of reality and deflects others (terministic screens). | textual | Burke, *Language as Symbolic Action*, "Terministic Screens" | untested |
| C5.2 | The healthy Self is one such screen, and it works well while other screens remain available. | conceptual | — | untested |
| C5.3 | The Totalitarian Self is a screen that no longer knows it is a screen; it claims to be the origin of what it sees. | conceptual | — | untested |
| C5.4 | A specialized vocabulary, used long enough in isolation, feeds on itself until it nearly negates other vocabularies (Burke's feedback loop). | textual | Burke, *Language as Symbolic Action*; *Permanence and Change* | untested |
| C5.5 | The language of Selfhood (authenticity, expression, responsibility, reliance) has run this loop for centuries in the West, and more intensely in America. | historical + empirical | word-frequency data; Taylor; Trilling, *Sincerity and Authenticity* | untested |
| C5.6 | The metaphysical shift: difference goes from relational to absolute, and the Self from *in* experience to *prior to* it. | conceptual | — | untested |
| C5.7 | The totalized Self represses truths about history, environment, dependence, mortality and the collective as thoroughly as the orders it replaced. | conceptual + empirical | §7 evidence | untested |
| C5.8 | Identifying the Self with a separate Mind is what lets it imagine itself prior to the world. | conceptual | Descartes; Heidegger, *Being and Time* | untested |

**Pressure points**

- **C5.4:** Check that this is Burke's own claim. The closest Burke ideas may be "occupational psychosis" and "trained incapacity" (*Permanence and Change*), which are not the same thing.

---

## §6 Host

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C6.1 | America did not cause the Totalitarian Self; it supplied the conditions for it. | conceptual | — | untested |
| C6.2 | The feudal, guild, parish and estate structures that checked the Self in Europe were absent or thin in America. | historical | Tocqueville; Hartz, *The Liberal Tradition in America* | untested |
| C6.3 | The frontier made self-reliance a survival requirement, not an ideology. | historical | Turner, "The Significance of the Frontier" | untested |
| C6.4 | The Protestant inheritance arrived dominant, without a Catholic or communal counter-tradition of comparable weight. | historical | Tocqueville; Winthrop, "A Model of Christian Charity" | untested |
| C6.5 | The economic conditions behind the Self were America's founding conditions, not a later development. | historical | Weber; Tocqueville | untested |
| C6.6 | The philosophy of the Self helped America become a world empire faster than any in history. | historical | comparative history | untested |
| C6.7 | That success validated the concept and removed any incentive to check it. | historical | — | untested |
| C6.8 | The philosophy of the Self became dogmatic and mutated; the Reagan era intensified this but did not start it. | historical | open question 3 | untested |

**Pressure points**

- **C6.2, C6.4:** Puritan New England was intensely communal (covenant, township, congregation). Winthrop's "Model of Christian Charity" (1630) argues *against* the separate Self, and Tocqueville praised American associations as a check on individualism.
- **C6.3:** Turner's frontier thesis is heavily contested by historians, and frontier life depended on cooperation and on government land policy.
- **C6.6:** "Faster than any in history" is a strong comparative claim (consider Rome, the Mongols, Britain). It may need softening.

---

## §7 Effects

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C7.1 | A surfeit of self-reliance and responsibility produces pervasive blame and guilt, unrelated to original sin. | empirical + conceptual | Nietzsche; Lasch | untested |
| C7.2 | Self-reliance in surfeit produces isolationism, rootlessness and asociality. | empirical | Bellah, *Habits of the Heart*; Putnam, *Bowling Alone* | untested |
| C7.3 | Individual responsibility in surfeit produces exhaustion, inefficiency and stagnation. | empirical | Han, *The Burnout Society* | untested |
| C7.4 | Failure is attributed to the Self or other Selves, never to environmental, social or historical factors. | empirical | attribution research (fundamental attribution error; cross-cultural studies) | untested |
| C7.5 | A surfeit of personal expression produces a cacophony that makes sensible discourse nearly impossible. | empirical + conceptual | MacIntyre, *After Virtue* (emotivism); Sennett | untested |
| C7.6 | Lasch's account of the narcissistic society is as the spec summarizes it (invisible hierarchy, symbol competition, defensive living, artificial communities, no past and no future). | textual | Lasch, *The Culture of Narcissism* | untested |
| C7.7 | The Totalitarian Self is the underlying cause of the collective symptom Lasch describes. | conceptual | Lasch | untested |
| C7.8 | At the individual level, the effect is indifference to the plight of others. | empirical | Twenge & Campbell (with care) | untested |
| C7.9 | The combined effect is an existential no-man's-land: cut off from one's own feelings, bound to a group founded on superficial connection. | conceptual | — | untested |

**Pressure points**

- **C7.4:** "Never" is too strong for an empirical claim. Attribution research finds a tendency, not an absolute.
- **C7.8:** The narcissism-epidemic data (Twenge) is disputed by other researchers.

---

## §8 Mechanism

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C8.1 | Self-totalization runs a repeatable process: genuine expression → connection → convergence → attachment → perversion → accessory. | conceptual + empirical | Goffman; Debord; subculture studies (Hebdige, *Subculture*) | untested |
| C8.2 | Accessorizing is an act of conformity performed in the vocabulary of self-expression. | conceptual | Simmel, "Fashion" | untested |
| C8.3 | The process produces False Groups: coherent in appearance, incoherent in substance. | conceptual | — | untested |
| C8.4 | The engine is inside the ideology of the Self, not imposed from outside by markets or media. | conceptual | Adorno & Horkheimer, "The Culture Industry"; Frank, *The Conquest of Cool* | untested |
| C8.5 | The desire to belong is routed through self-expression because no other vocabulary remains available. | conceptual | §5 | untested |

**Pressure points**

- **C8.1, C8.2:** Simmel's "Fashion" (1904) already describes the tension between imitation and distinction. Engage with it, or the mechanism looks unoriginal.

---

## §9 Carriers

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C9.1 | The Totalitarian Self is carried by groups that appear to be opposites. | conceptual | §9 sources | untested |
| C9.2 | American fundamentalism forsook Reason in reaction to an alienating modern world, intensifying from the Reagan era. | historical | *The Fundamentals* (1910–15); Marsden, *Fundamentalism and American Culture* | untested |
| C9.3 | Without doubt there is no faith, so fundamentalism is an ecclesiastical philosophy, not a faith-based one. | conceptual | Tillich, *Dynamics of Faith*; Kierkegaard | untested |
| C9.4 | The fundamentalist surrender projects the Self onto a single absolute authority, keeping the Self's structure while inverting its content. | conceptual | open question 2 | untested |
| C9.5 | Weber: reason became a tyrant that no longer recognized its own limits or the values it served. | textual | Weber, *Protestant Ethic* (the "iron cage" passage); "Science as a Vocation"; Solomon (verify) | untested |
| C9.6 | Technocrats claim objectivity while guided by in-group tribalism; they deny their own beliefs, and are nihilists in the strict sense. | conceptual + empirical | Nietzsche on nihilism | untested |
| C9.7 | This is the ruling class Lasch foresaw. | textual | Lasch, *Culture of Narcissism*; *The Revolt of the Elites* | untested |
| C9.8 | Corporatism is the Totalitarian Self at an institutional, global scale. | conceptual | open question 4 | untested |

**Pressure points**

- **C9.2:** Fundamentalism as a movement dates to the 1910s, so "from the Reagan era onward" must refer to intensification only.
- **C9.5:** The Weber line comes via Solomon. Find it in Weber's own text before relying on it.

---

## §10 Claims made in answering objections

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C10.1 | Lasch describes the symptom; this theory supplies the cause, the mechanism and a longer history. | textual | Lasch | untested |
| C10.2 | The philosophical dissolution of the Self (Hume, Parfit) has had no effect on the cultural Self. | empirical | Hume, *Treatise* I.iv.6; Parfit | untested |

**Pressure points**

- **C10.1:** Lasch *does* offer causes (bureaucracy, the therapeutic culture, consumer capitalism, the decline of the family). The claim must say how this theory's cause differs from his.
