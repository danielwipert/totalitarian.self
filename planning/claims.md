# Claims register

Every claim the essay makes, numbered so it can be tested against the sources. The thesis is unproven until these claims are tested. A claim that the sources challenge gets revised, not defended.

## How it works

1. Each claim has an ID: `C` + spec section + number (C4.3 = the third claim in §4).
2. Passages in `sources/primary/` are tagged with claim IDs and marked **for**, **against** or **complicates**.
3. To see the evidence for a claim, search the repo for its ID (e.g. `grep -rn "C4.3" sources/`).
4. Once there's enough evidence, update the claim's status and log the change in `decisions.md`.

**Status:** `untested` · `supported` · `challenged` · `revised` · `dropped`

`revised` means the claim was reworded after testing. The new wording rests on the evidence that prompted it, but it should still be tested further. Earlier wordings are in `SPEC.md` and the git history.

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

**Current thesis (revised 2026-10-23):** *The Self began as a necessary acknowledgment that each person stands answerable on their own, but in the West, and above all in America, it has calcified into a totalizing dogma that suppresses the very truths it was meant to reveal.*

| ID | Claim | Kind | Depends on | Status |
|---|---|---|---|---|
| C1.1 | The Self began as a necessary acknowledgment that each person stands answerable on their own, but in the West, and above all in America, it has calcified into a totalizing dogma that suppresses the very truths it was meant to reveal. | conceptual | C4.* | revised |
| C1.2 | In the West, above all in America, it calcified into a totalizing dogma. | historical | C5.*, C6.* | untested |
| C1.3 | The totalized Self suppresses the truths it was meant to reveal. | conceptual | C5.7, C7.* | untested |

---

## §4 Origin

**The pattern (2026-10-23):** in every §4 thinker, the ancestor of the Self came with a limit attached (God, community, the body, limits on guilt). The later Self kept the structure and dropped the limit. §4 now claims this, not that the founders acknowledged individual difference.

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C4.1 | The Self was neither invented nor discovered. It grew out of a structure built for something else: each person made answerable on their own (before God, through conscience and consciousness), and bounded by God, community and the body. The Self is what that structure became as its bounds fell away. | conceptual + historical | all §4 sources; later sources for the falling-away | revised |
| C4.2 | The collapse of the old social order and the rise of capital produced the awareness that persons could direct their own futures, partly *against* the intentions of reformers like Luther and Calvin, who sanctified stations and condemned commerce. | historical | Weber, *Protestant Ethic*; Fromm; Tawney, *Religion and the Rise of Capitalism* | revised |
| C4.3 | Luther individuated each believer's standing and answerability before God ("every man stands for himself") and stripped the clergy of any spiritual estate above the laity, but moved mediation into the preached word and the congregation rather than abolishing it. | textual | Luther, the three 1520 treatises | revised |
| C4.4 | Calvin made sanctification a confirming sign of election (III.xiv.18–20) while forbidding believers to seek assurance in works or wealth. Later Calvinists turned that permitted sign into an anxious, practical proof of election through disciplined work and frugality. | textual + historical | Calvin, *Institutes* III.xiv, III.xxi–xxiv; Weber; Puritan sources (e.g. Baxter) | revised |
| C4.5 | The economic origin is load-bearing: the Self responded to a freer economic situation and was not a pure act of thought. The reformers were unintended contributors, not advocates. | historical | Weber; Fromm; Tawney | revised |
| C4.6 | The cogito locates identity in a thinking substance really distinct from the body. Descartes always pairs this with the soul's close union with the body (*Discourse* V, *Meditations* VI, *Passions* I.30), treating the union as what the person *has*, not what the I *is*. | textual | Descartes, *Discourse*, *Meditations*, *Passions* | supported |
| C4.7 | As received, the cogito was reduced to its first half (a mind distinct from the body), and the union Descartes paired with it in every major work was dropped. | reception | later readers: Hobbes's objections, Henry More, Locke, Malebranche; Ryle for the 20th-century picture | revised |
| C4.8 | Paul, Plato, Augustine and the Stoics (Cicero, Seneca) laid the groundwork for the separate soul-mind-self; Descartes made it operational. | textual | Paul, 2 Cor. 4:16, Rom. 7; Plato, *Phaedo*; Augustine, *Confessions* X, *De Trinitate* X, *City of God* XI.26; Cicero, *De Officiis* I.31; Seneca, *Letters* (via montaigne-essays.09) | revised |
| C4.9 | Locke founds personal identity on consciousness (memory), not on the substance of soul or body. | textual | Locke, *Essay* II.xxvii | supported |
| C4.10 | For Locke, "person" is a forensic term: the unit to which actions, merit, guilt and punishment are attributed. | textual | Locke, *Essay* II.xxvii.26 | supported |
| C4.11 | Locke's denial of innate principles makes the Self's beliefs and principles a product of experience and education rather than inheritance, though he keeps innate appetites and temperament. The blank page frees the mind from inborn authority but exposes it to custom. | textual | Locke, *Essay* I; II.i | revised |
| C4.12 | Nietzsche saw that this forensic framework is what makes guilt attributable. | textual | Nietzsche, *Genealogy of Morals* II; *Twilight of the Idols*, "The Four Great Errors" | untested |
| C4.13 | At each of these moments the Self's ancestors acknowledged something true against orders that denied it (each person's equal standing before God and their own answerability), which only later became an acknowledgment of individual difference. | conceptual | all §4 sources; the classical inner court (Cicero, Seneca, via Montaigne); later sources for the shift to difference | revised |
| C4.14 | The core moves came quickly (1517 → 1694, date to verify), perhaps faster than the concept could be integrated. "Unusually fast" stands only if a comparison backs it. | historical | Locke's 2nd edition; comparison with other intellectual shifts | revised |

**Pressure points**

- **C4.4:** Weber located the work-as-proof dynamic in *later* Puritans (Baxter and others), not in Calvin. Calvin himself warns against seeking assurance of election in one's works. This claim may need to be about Calvinism, not Calvin.
- **C4.3:** Luther's *Freedom of a Christian* pairs inner freedom with service: "A Christian man is the most free lord of all, and subject to none; a Christian man is the most dutiful servant of all, and subject to every one." (verified, Gutenberg #1911) Individuation may come bound to a new kind of service.
- **C4.8:** Augustine's "si fallor, sum" ("if I am mistaken, I exist") anticipates the cogito by twelve centuries. That weakens the "speed" claim (C4.14) and strengthens the "groundwork" claim.
- **C4.11:** Locke writes "white paper," not "tabula rasa," and his Book I targets innate *ideas*, not inherited nature in general.
- **C4.14:** Locke's chapter on personal identity (II.xxvii) was added in the 2nd edition of 1694, so the span may be 1517 → 1694. To verify.
- **C4.6:** In *Meditations* VI, Descartes says "I am not only lodged in my body as a pilot in a vessel, but that I am very closely united to it" (verified, Haldane & Ross 1911).

## §4b Bridge: from answerability to difference

Added 2026-10-23 (open question 8). §4 now ends with the answerable Self; these claims test where, and whether, it becomes the *different* Self. All are hypotheses until read.

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C4.15 | Difference becomes a value in the bridge from Rousseau to Emerson, but always inside a shared frame (the common heart, the universal soul, utility). Singularity, difference cut from relation, appears in none of the founding texts: it is the mutation (§5), not an inheritance. | historical + textual | all §4b sources; later authors as checks (Stirner, Whitman, Wilde, Nietzsche) | revised |
| C4.16 | Rousseau claims difference as a value and as the reason others cannot judge him, but treats the inner man he displays as typical of every man; in the *Discourse* the "fury of distinguishing ourselves" is a vice. His difference is one of make and sincerity, not of moral standard. | textual | Rousseau, *Confessions* I; *Discourse on Inequality* | revised |
| C4.17 | Rousseau keeps the answerability frame but moves its source inward, to feeling and conscience, a voice that is divine and the same in everyone, and moves its court outward: the self writes its own record and the public is the jury, with God as nominal judge. The vicar keeps the limit (God, inherited religion); Rousseau as tutor loosens it (*Emile* IV). | textual | Rousseau, *Confessions*; *Emile* IV | revised |
| C4.18 | Rousseau splits a self-sufficient Self that "lives within himself" from a social Self that "knows only how to live in the opinion of others." But his inner Self is uniform and common to all, and difference sits on the social side. The authentic/false split starts here (with a precursor in Montaigne); identifying the authentic Self with the *different* Self does not. | textual | Rousseau, *Discourse on Inequality*; *Emile*; Montaigne | revised |
| C4.19 | Emerson makes nonconformity a duty and each person's unlikeness their calling, but absorbs the §4 limits instead of dropping them: God moves inside the Self, and the community's claim is replaced by an impersonal "common nature." Difference is how a universal soul incarnates in each person; Emerson's Self is a channel, not a singular source. | textual | Emerson, "Self-Reliance," "The Over-Soul," "Spiritual Laws" | revised |
| C4.20 | Mill defends individuality first as part of well-being and second as a source of social progress, under "utility in the largest sense" and bounded by the rights and interests of others. He defends the turn to difference rather than making it (crediting Humboldt), and marks where difference is valued apart from its content ("the mere example of nonconformity [...] is itself a service"). | textual | Mill, *On Liberty* III | revised |

**Pressure points**

- **Result (2026-10-23):** Montaigne does *not* break the order. His self is a sample of the common human form, and he calls "all singular and particular fashions [...] marks of folly" (montaigne-essays.03, .10). He does give answerability a second, classical root (Cicero, Seneca).
- **C4.15:** Montaigne's *Essays* (1580) already take the self as their subject ("myself am the matter of my book"; "I study myself more than any other subject"). That is *before* Locke and outside the Reformation line. If Montaigne already has the different Self, the order "answerability first, difference later" fails, or there are two roots.
- **C4.16, C4.17:** Rousseau's uniqueness claim is followed at once by "Whenever the last trumpet shall sound, I will present..." (verified, *Confessions* I). Uniqueness and judgement arrive together.
- **C4.19:** "The Over-Soul" may make Emerson's Self a channel for something universal, not a singular Self. That would complicate the step to singularity.
- **C4.20:** Mill argues individuality serves *social* progress; it may stay bounded by utility.

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
| C5.8 | Identifying the Self with a separate Mind lets it imagine itself prior to and independent of the material world. In Descartes this priority is bounded by dependence on God; the Totalitarian Self keeps the priority and drops the dependence. | conceptual + textual | Descartes; Heidegger, *Being and Time* | revised |

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
| C6.9 | As received in America, "Self-Reliance" was cut down to its nonconformist half and the Over-Soul dropped, as the cogito lost the union (C4.7). | reception | anthologies, school readers, popular and commercial uses of Emerson | untested |

**Pressure points**

- **C6.2, C6.4:** Puritan New England was intensely communal (covenant, township, congregation). Winthrop's "Model of Christian Charity" (1630) argues *against* the separate Self, and Tocqueville praised American associations as a check on individualism.
- **C6.3:** Turner's frontier thesis is heavily contested by historians, and frontier life depended on cooperation and on government land policy.
- **C6.6:** "Faster than any in history" is a strong comparative claim (consider Rome, the Mongols, Britain). It may need softening.

---

## §7 Effects

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C7.1 | The pervasive blame and guilt of the surfeit Self do not come from Locke. The Self kept Locke's forensic accountability but lost his God and his limits on guilt ("no one shall be made to answer for what he knows nothing of"). The genealogy of the guilt itself rests on Nietzsche (C4.12). | conceptual + textual | Locke, *Essay* II.xxvii; Nietzsche, *Genealogy* II; Lasch | revised |
| C7.2 | Self-reliance in surfeit produces isolationism, rootlessness and asociality. | empirical | Bellah, *Habits of the Heart*; Putnam, *Bowling Alone* | untested |
| C7.3 | Individual responsibility in surfeit produces exhaustion, inefficiency and stagnation. | empirical | Han, *The Burnout Society* | untested |
| C7.4 | Failure is attributed to the Self or other Selves, never to environmental, social or historical factors. | empirical | attribution research (fundamental attribution error; cross-cultural studies) | untested |
| C7.5 | A surfeit of personal expression produces a cacophony that makes sensible discourse nearly impossible. | empirical + conceptual | MacIntyre, *After Virtue* (emotivism); Sennett | untested |
| C7.6 | Lasch's account of the narcissistic society is as the spec summarizes it (invisible hierarchy, symbol competition, defensive living, artificial communities, no past and no future). | textual | Lasch, *The Culture of Narcissism* | untested |
| C7.7 | The Totalitarian Self is the underlying cause of the collective symptom Lasch describes. | conceptual | Lasch | untested |
| C7.8 | At the individual level, the effect is indifference to the plight of others. | empirical | Twenge & Campbell (with care) | untested |
| C7.9 | The combined effect is an existential no-man's-land: cut off from one's own feelings, bound to a group founded on superficial connection. | conceptual | — | untested |
| C7.10 | Difference experienced as being misjudged breeds suspicion of others: the Self that others cannot judge comes to see them as hostile. Rousseau's late *Confessions* are the historical case. | textual + empirical | Rousseau, *Confessions* (rousseau-confessions.08, .13, .14); *Rousseau, Judge of Jean-Jacques* | untested |

**Pressure points**

- **C7.4:** "Never" is too strong for an empirical claim. Attribution research finds a tendency, not an absolute.
- **C7.8:** Rousseau's case shows suspicion, not indifference (see C7.10).
- **C7.8:** The narcissism-epidemic data (Twenge) is disputed by other researchers.

---

## §8 Mechanism

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C8.1 | Self-totalization runs a repeatable process: genuine expression → connection → convergence → attachment → perversion → accessory. | conceptual + empirical | Goffman; Debord; subculture studies (Hebdige, *Subculture*) | untested |
| C8.2 | Accessorizing is conformity performed in the vocabulary of self-expression. Unlike Mill's "despotism of custom," which works through the vocabulary of station ("what is suitable to my position?"), it speaks the language Mill offered as the cure. | conceptual | Mill (mill-liberty.05); Simmel, "Fashion" | revised |
| C8.3 | The process produces False Groups: coherent in appearance, incoherent in substance. | conceptual | — | untested |
| C8.4 | The engine is inside the ideology of the Self: the desire to *belong*, routed through self-expression. This differs from Mill's external engines (education, commerce, communications), from a culture industry imposed from outside, and from Rousseau's *amour-propre*, whose engine is the wish for *distinction*, not belonging. | conceptual | Mill (mill-liberty.13); Rousseau (rousseau-inequality.07, .11); Adorno & Horkheimer; Frank, *The Conquest of Cool* | revised |
| C8.5 | The desire to belong is routed through self-expression because no other vocabulary remains available. | conceptual | §5 | untested |

**Pressure points**

- **C8.1:** Rousseau's self-expression is addressed to a judging public from the start (rousseau-confessions.05, .15), so the audience may not be a later corruption. Mill values eccentricity apart from what it expresses (mill-liberty.10), which may be the opening accessorizing later used.
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
