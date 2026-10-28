# Claims register

Every claim the essay makes, numbered so it can be tested against the sources. The thesis is unproven until these claims are tested. A claim that the sources challenge gets revised, not defended.

## How it works

1. Each claim has an ID: `C` + spec section + number (C4.3 = the third claim in §4).
2. Passages in `sources/primary/` are tagged with claim IDs and marked **for**, **against** or **complicates**.
3. To see the evidence for a claim, search the repo for its ID (e.g. `grep -rn "C4.3" sources/`).
4. Once there's enough evidence, update the claim's status and log the change in `decisions.md`.

**Status:** `untested` · `illustrated` · `supported` · `challenged` · `revised` · `dropped`

`illustrated` means a claim about the culture is shown in popular carriers (Tier 4), or in one critic, but does not yet meet the evidence standard below.

`revised` means the claim was reworded after testing. The new wording rests on the evidence that prompted it, but it should still be tested further. Earlier wordings are in `SPEC.md` and the git history.

**Kind** (what counts as a test):

- **textual**: does the primary text actually say this? Tested by reading the source.
- **reception**: how a text was *received*, as distinct from what it says. Needs later writers and historians.
- **historical**: a claim about what happened and why. Needs primary documents plus historians.
- **empirical**: a claim about how people behave now. Needs sociology or psychology data.
- **conceptual**: tested by argument, not by sources. It still has to be consistent with the textual claims.

**Evidence standard (2026-10-27).** One voice is one among millions. Sources are weighed in four tiers:

1. **Tier 1, established critics and intellectuals** (e.g. Tocqueville, Weber, Dewey, Simmel; Rieff, Lasch, Bellah, Taylor). Most weight on what a culture *is*. Their claims are tested too, and dissenting critics get the same weight as agreeing ones.
2. **Tier 2, data:** surveys, field studies, word counts (e.g. *Middletown*, Greenfield, Twenge, Wetzel). Show how widespread a change is, and when.
3. **Tier 3, institutions:** court opinions, government reports, official speeches. Show what the society made binding or public.
4. **Tier 4, popular carriers** (e.g. Smiles, Trine, Byrne, Brown). Show how the Self speaks; cannot show how widespread it is.

A claim about the culture (not about what one text says) is `supported` only with **at least two independent Tier 1 critics, plus Tier 2 or Tier 3 evidence, with dissenting critics read and answered**. Resting on Tier 4 alone, or on a single critic, it is `illustrated`. A claim about what a text says needs only the text. Each claim about the culture is tagged with its tiers in the *Evidence audit* at the end of this file.

**Status changes so far** are logged in `decisions.md`, with the passage IDs that caused them.

Each section also has **pressure points**: known reasons a claim might fail. These are what to look for first.

---

## §1 Thesis (umbrella claims)

These stand or fall with the section claims beneath them.

**Current thesis (revised 2026-10-23, widened after §4c):** *The Self began as two necessary acknowledgments, that each person stands answerable on their own and that each can shape and present themselves, but in the West, and above all in America, it has calcified into a totalizing dogma that suppresses the very truths it was meant to reveal.*

| ID | Claim | Kind | Depends on | Status |
|---|---|---|---|---|
| C1.1 | The Self began as two necessary acknowledgments, that each person stands answerable on their own and that each can shape and present themselves, but in the West, and above all in America, it has calcified into a totalizing dogma that suppresses the very truths it was meant to reveal. | conceptual | C4.* | revised |
| C1.2 | In the West, above all in America, it calcified into a totalizing dogma. | historical | C5.*, C6.* | untested |
| C1.3 | The totalized Self suppresses the truths it was meant to reveal. | conceptual | C5.7, C7.* | untested |
| C1.4 | After about 1960 the Self works in two layers. The *lived* subject fragments (Jameson: "the alienation of the subject is displaced by the latter's fragmentation"; there is "no longer a self present to do the feeling"), while the *vocabulary* of the Self grows and admits no rival. The Totalitarian Self is an ideology that grows over a dissolving centred self: it covers the fragments, and cannot be answered to because nothing stable is left to answer. Jameson himself separates the two ("notion (or experience)"). | historical + empirical | Jameson (T1, for the lived layer); word counts of the Self's vocabulary, 1960–2000 (T2: Greenfield and later); Tier 1 critics on the therapeutic culture | untested |
| C1.5 | The cause changes by period. Before 1900 economic change is background, not cause (C4.5). After about 1960, late capitalism and the Self's vocabulary drive each other: Jameson's culture is "only the reflex and the concomitant" of capitalism's changes, though he allows a "feedback loop", and development leads individualism by about ten years in 78 countries (Santos et al.). The thesis claims the mechanism and the history, not the sole cause. | historical | Jameson (T1); Santos et al. 2017 (T2); Weber, Tawney (C4.5) | untested |

---

## §4 Origin

**The pattern (2026-10-23):** in every §4 thinker, the ancestor of the Self came with a limit attached (God, community, the body, limits on guilt). The later Self kept the structure and dropped the limit. §4 now claims this, not that the founders acknowledged individual difference.

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C4.1 | The Self was neither invented nor discovered. It grew out of a structure built for something else: each person made answerable on their own (before God, through conscience and consciousness), and bounded by God, community and the body. The Self is what that structure became as its bounds fell away. | conceptual + historical | all §4 sources; later sources for the falling-away | revised |
| C4.2 | Commercial change made it possible, and profitable, for persons to direct their own economic futures, but it did not produce the Self, and it went against the reformers' intentions. Luther "hated commerce and capitalism" and sanctified stations; Calvin "accepted the main institutions of a commercial civilization" under a collective discipline (Tawney); the self-chosen calling came with later Puritans (after 1640). | historical | Tawney; Weber; luther-nobility; calvin-institutes (check Calvin's letters) | revised |
| C4.3 | Luther individuated each believer's standing and answerability before God ("every man stands for himself") and stripped the clergy of any spiritual estate above the laity, but moved mediation into the preached word and the congregation rather than abolishing it. | textual | Luther, the three 1520 treatises | revised |
| C4.4 | Calvin made sanctification a confirming sign of election while forbidding believers to seek assurance in works or wealth. Later Calvinists (after 1640) turned that permitted sign into a practical proof of election through disciplined work and frugality: "Calvin's theology must be distinguished from Calvinism" (Weber). Weber's Puritan works from anxiety, Tawney's from assurance. | textual + historical | Calvin; Weber; Tawney | supported |
| C4.5 | Economic change is the *background*, not the origin: it made the change possible and profitable. The ethos of the self-directed calling came from later Puritanism meeting commerce; in Massachusetts it came before any capitalist order (Weber). The reformers were unintended contributors, with results "unforeseen and even unwished-for" (Weber). | historical | Weber; Tawney | revised |
| C4.6 | The cogito locates identity in a thinking substance really distinct from the body. Descartes always pairs this with the soul's close union with the body (*Discourse* V, *Meditations* VI, *Passions* I.30), treating the union as what the person *has*, not what the I *is*. | textual | Descartes, *Discourse*, *Meditations*, *Passions* | supported |
| C4.7 | As received, the cogito was reduced to its first half (a mind distinct from the body), and the union Descartes paired with it in every major work was dropped. | reception | later readers: Hobbes's objections, Henry More, Locke, Malebranche; Ryle for the 20th-century picture | revised |
| C4.8 | Paul, Plato, Augustine and the Stoics (Cicero, Seneca) laid the groundwork for the separate soul-mind-self; Descartes made it operational. | textual | Paul, 2 Cor. 4:16, Rom. 7; Plato, *Phaedo*; Augustine, *Confessions* X, *De Trinitate* X, *City of God* XI.26; Cicero, *De Officiis* I.31; Seneca, *Letters* (via montaigne-essays.09) | revised |
| C4.9 | Locke founds personal identity on consciousness (memory), not on the substance of soul or body. | textual | Locke, *Essay* II.xxvii | supported |
| C4.10 | For Locke, "person" is a forensic term: the unit to which actions, merit, guilt and punishment are attributed. | textual | Locke, *Essay* II.xxvii.26 | supported |
| C4.11 | Locke's denial of innate principles makes the Self's beliefs and principles a product of experience and education rather than inheritance, though he keeps innate appetites and temperament. The blank page frees the mind from inborn authority but exposes it to custom. | textual | Locke, *Essay* I; II.i | revised |
| C4.12 | Nietzsche argued that the free, responsible subject (free will, the doer behind the deed) was invented by priests to make guilt attributable and inexhaustible, though guilt itself, as debt, is older. He does not discuss Locke; the link to Locke's forensic person is the essay's own. | textual | Nietzsche, *Genealogy* I.13, II; *Twilight*, "Four Great Errors" §7 | revised |
| C4.13 | At each of these moments the Self's ancestors acknowledged something true against orders that denied it (each person's equal standing before God and their own answerability), which only later became an acknowledgment of individual difference. | conceptual | all §4 sources; the classical inner court (Cicero, Seneca, via Montaigne); later sources for the shift to difference | revised |
| C4.14 | The core moves came quickly (1517 → 1694, date to verify), perhaps faster than the concept could be integrated. "Unusually fast" stands only if a comparison backs it. | historical | Locke's 2nd edition; comparison with other intellectual shifts | revised |

**Pressure points**

- **C4.4:** Weber located the work-as-proof dynamic in *later* Puritans (Baxter and others), not in Calvin. Calvin himself warns against seeking assurance of election in one's works. This claim may need to be about Calvinism, not Calvin.
- **C4.3:** Luther's *Freedom of a Christian* pairs inner freedom with service: "A Christian man is the most free lord of all, and subject to none; a Christian man is the most dutiful servant of all, and subject to every one." (verified, Gutenberg #1911) Individuation may come bound to a new kind of service.
- **C4.8:** Augustine's "si fallor, sum" (if I am mistaken, I exist; our translation) anticipates the cogito by twelve centuries. That weakens the "speed" claim (C4.14) and strengthens the "groundwork" claim.
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

## §4c Rival origin: the Renaissance and the Enlightenment

**Result (2026-10-23):** two bounded roots, humanist self-shaping and Christian answerability; the Enlightenment separates the person from *institutions*, not the Self from God or community. That separation comes later (§5b).

Added 2026-10-23 at the author's request. The author's long-held view is that selfhood started in the Renaissance and took off in the Enlightenment, as the Self developed and as it separated from religion and community. These claims state that view as a rival to the "answerability first" story (C1.1, C4.1), to be tested head to head. Whichever the texts support goes into §4. All untested.

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C4.21 | Selfhood has two early roots, both bounded. One is humanist self-shaping and self-presentation (Petrarch, Pico, Machiavelli, Castiglione, Cellini): the self valued for excellence, glory and craft, parallel to Reformation answerability and not derived from it. In every text it stays inside God, fortune, a given nature, a prince or a craft. Its unbounded form appears early, but as the age's recognized vice (Burckhardt). | historical + textual | all §4c sources | revised |
| C4.22 | Burckhardt holds that in Renaissance Italy "man became a spiritual individual," conceding that "Documentary evidence cannot, of course, be required on such a point." He also calls the unbounded individual "the fundamental vice" of the age. | textual (secondary) | Burckhardt, Part II ch. i; later historians (Kristeller, Greenblatt) | supported |
| C4.23 | Petrarch turns attention inward, the soul rather than the world as the thing worth studying, but the turn is Augustine's and Seneca's: self-examination before Truth, used against fame. His love of glory and distinction is real, but confessed under judgement, never defended as a right. | textual | Petrarch, Mont Ventoux letter; *Secretum* | revised |
| C4.24 | Pico makes man self-shaping, with no fixed nature, the "plastes et fictor" (moulder and maker) of himself. But the freedom is God's gift ("summam dei patris liberalitatem," the supreme generosity of God the Father) and its height is "unus cum deo spiritus factus," made one spirit with God (English renderings ours): self-shaping, not self-origination. | textual | Pico, *Oration*, Latin and English via Burckhardt; full *Oration* needs a copy in hand | revised |
| C4.25 | Machiavelli and Castiglione make the self's *presentation* a craft performed for others' eyes (the appearance of virtue; "nonchalance"; "true art [...] which does not appear to be art"), worked on a nature neither thinks can be remade, and serving rule or favour. Castiglione is the earliest witness to §8's mechanism, in the idiom of nature and grace. | textual | Machiavelli, *The Prince*, *Discourses*; Castiglione, *Courtier* | supported |
| C4.26 | Cellini tells a life as the story of an exceptional individual, excellent in a shared craft, ranked above others, exempted from the law by patrons, and owing his gifts to God. He values superiority, not difference: his exceptionality is a rank on a common scale. | textual | Cellini, *Autobiography* | revised |
| C4.27 | *The Praise of Folly* bounds the self in a Christian frame: it mocks man's wish to exceed his bounds, treats self-love as a folly society cannot do without, and ends with the self's happiness in being out of himself in God. Erasmus's own view of free will is untested (*On Free Will* not in the library). | textual | Erasmus, *Praise of Folly*; *De libero arbitrio* (1524) | revised |
| C4.28 | Enlightenment autonomy makes *reason*, not the individual, its own lawgiver: each must use "deines eigenen Verstandes," but the self-given law is universal, reached by abstracting "from the personal differences of rational beings," and exercised in public. It frees the person from Church and tutor while binding him to a common law: the opposite of singularity. | textual | Kant, "Was ist Aufklärung?"; *Groundwork* | revised |
| C4.29 | The Enlightenment moral self is social: grounded in natural affection and common sense (Shaftesbury) and formed by sympathy and the eyes of others (Hume, Smith). The solitary individual has no moral "mirror"; the inner judge is "the representative of mankind, and substitute of the Deity" (Smith, editions before 1790; cut in 1790, where it becomes "this demigod within the breast," with God "a still higher tribunal"). | textual | Shaftesbury; Hume; Smith; Mandeville | supported |
| C4.30 | Religion separates from the *institutions* that compelled it: belief becomes a matter of individual conscience, beyond state and clergy, and the church a voluntary society (Locke). The Self does not separate from God: it stays accountable to God as judge, and toleration rests on a common frame. Limits remain (Locke excludes atheists). The furthest step, Paine's "My own mind is my own church," still answers to God. The *Self* itself separates from religion only later: by 1929 the modern man "is unable any longer to think of himself as a single personality approaching an everlasting judgment" (Lippmann), and slowly, because toleration wears conviction down. | textual | Spinoza; Locke, *Letter*; Voltaire; Paine; Kant | revised |
| C4.31 | Enlightenment political theory founds *political authority* on the consent or interest of individuals, who are prior to it in justification though not in history. The Self does not separate from community: it stays social (Hume: the prior individual is "a mere philosophical fiction"; Kant's trees grown apart grow "crooked"), bounded by natural law and God (Locke), or absorbed into the whole (Hobbes, Rousseau). What separates is the individual from *intermediate* bodies: church, sect, faction, inherited station. | textual | Hobbes; Locke, *Second Treatise*; Hume; Smith; Kant; Mandeville; Rousseau; Franklin | revised |

**Pressure points**

- **C4.24:** Pico's self-shaping freedom is given *by God* and aimed at ascent *to God*. It may be bounded, like every other early form.
- **C4.21:** if the Renaissance self is real but bounded, both stories may be true: two roots (humanist self-shaping and Reformation answerability), as Montaigne's classical root already suggested (C4.13).
- **C4.28:** Kant's self-given law is *universal* (valid for every rational being), a common frame. Autonomy may be the opposite of singularity.
- **C4.30, C4.31:** separation may be institutional (church from state, individual from status) while the Self itself stays religious or social. Check which is separated: the Self, or the institutions.
- **C4.25, C4.26:** Burckhardt's picture of Renaissance individualism is contested by later historians. Test the primary texts, not Burckhardt's reading of them.

---

## §5 Mutation

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C5.1 | Any vocabulary selects some features of reality and deflects others (terministic screens). Burke: a terminology "must be a selection of reality; and to this extent it must function also as a deflection of reality" (p. 45). His "deflection" is where attention goes, not repression, and he grants that a screen can also reflect reality. | textual | Burke, *Language as Symbolic Action*, "Terministic Screens" (burke-ts.01–.03) | supported |
| C5.2 | The healthy Self is one such screen, and it works well while other screens remain available. | conceptual | — | untested |
| C5.3 | **Working definition (rebuilt on Burke, 2026-10-28):** the Totalitarian Self is not a self but a terministic screen: a vocabulary of persons who act that (1) has been stretched past its own field to cover everything, Burke's screen "stretched to cover not just its own special field but a more comprehensive area"; (2) has cut away its passive half, keeping the active person while slighting conditioning, dependence and "human bondage", which Burke calls "a drastic kind of vandalism"; and (3) no longer hears the "rejoinders" of what it names, against Burke's "Not suppressing by dictatorial lie". This explains C1.4: the screen can be total while the lived subject behind it fragments. Not knowing that it is a screen does *not* distinguish it: on Burke's account that is every screen ("naive verbal realism"). Strongest against-reading: this is Burke's own central screen, the vocabulary of action, with its limit dropped, not a rival screen. | conceptual | Burke, "Terministic Screens" (burke-ts.09, .14–.16, .20–.24); C1.4, C5.1; Jameson | untested |
| C5.4 | A vocabulary used long enough over a widening field thickens until it nearly negates other vocabularies. This is the spec's own hypothesis, not Burke's: "Terministic Screens" has no feedback loop (its "feedback" is a grammatical term), and Burke says "cycles of terms that imply one another" yield "improvisational \"freedom\"", not closure. His nearest point is the screen "stretched to cover" more than its field. Check *Permanence and Change* (*trained incapacity*) before calling it entirely the spec's. | conceptual + historical | Burke, *Permanence and Change*; "Terministic Screens" (burke-ts.17, .25, .26); word counts (T2) | untested |
| C5.5 | The language of Selfhood (authenticity, expression, responsibility, reliance) has run this loop for centuries in the West, and more intensely in America. | historical + empirical | word-frequency data; Taylor; Trilling, *Sincerity and Authenticity* | untested |
| C5.6 | The metaphysical shift: difference goes from relational to absolute, and the Self from *in* experience to *prior to* it. | conceptual | — | untested |
| C5.7 | The totalized Self represses truths about history, environment, dependence, mortality and the collective as thoroughly as the orders it replaced. | conceptual + empirical | §7 evidence | illustrated |
| C5.8 | Identifying the Self with a separate Mind lets it imagine itself prior to and independent of the material world. In Descartes this priority is bounded by dependence on God; the Totalitarian Self keeps the priority and drops the dependence. | conceptual + textual | Descartes; Heidegger, *Being and Time* | revised |

**Pressure points**

- **C5.4:** Check that this is Burke's own claim. The closest Burke ideas may be "occupational psychosis" and "trained incapacity" (*Permanence and Change*), which are not the same thing.

## §5b Frame loss: when difference is cut from relation

**The two stages (2026-10-23):** philosophy removed the limits layer by layer but kept the Self empty or fictional; the culture made it its own origin. C5.9 is the hinge, C5.14 the test.

Added 2026-10-23 (open question 9). The bridge (§4b) found difference always bounded by a shared frame. These claims test where, and whether, the frame is first dropped. All are hypotheses until read.

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C5.9 | Philosophy dropped the frames in layers (answerability first: Whitman, Wilde; then the common frame: Stirner, Nietzsche) but never made the Self its own origin. Nietzsche names that move, the wish "to absolve God, the world, ancestors, chance, and society" and be *causa sui*, and calls it a self-contradiction of "the half-educated." | historical + textual | all §5b sources (nietzsche-sing.20) | revised |
| C5.10 | Stirner is the first to drop every shared frame (God, Man, species, society, morality, conscience) and to put the unique one in God's place. But the unique one is a "creative nothing," transitory and self-consuming, not a self-originating source. Relation survives as use, feeling and a revocable "union." | textual | Stirner, *The Ego and His Own* | revised |
| C5.11 | Whitman's American Self is Emerson's Over-Soul made democratic and bodily: a common self shared "on the same terms" with everyone. It drops answerability and ranks itself above God, but keeps relation; when it swells into containment ("it becomes mine"), the poem itself calls it "a usual mistake." | textual | Whitman, "Song of Myself" | revised |
| C5.12 | Wilde makes "Be thyself" the message of Christ, with socialism only the means: the Self answers to no law, judge or duty. But it stays relational (it loves others "because they will be different") and is set inside a law of nature, Evolution. | textual | Wilde, "The Soul of Man under Socialism" | revised |
| C5.13 | Nietzsche makes uniqueness a task ("become what thou art") and drops God and the common good as its frame, replacing them with an order of rank, the higher type, the body and the earth. He attacks the "I" and *causa sui* as fictions: he cuts difference from the common, not from relation, and rejects self-origination. | textual | Nietzsche, *Gay Science*, *Zarathustra*, *Beyond Good and Evil*, "Schopenhauer as Educator" | revised |
| C5.14 | The culture, not philosophy, made the Self self-originating, in stages. **Stage 1, the self as *cause*,** with a borrowed frame: mind-cure and New Thought, 1890s ("Within yourself lies the cause of whatever enters into your life"), powered by the Infinite. **Stage 2, the self as final *judge* of what it answers to.** Its Tier 1 theorist is Rogers (1961): "Experience is, for me, the highest authority", but experience is checked, not willed ("The facts are friendly"), and the trusted nature is social (the person becomes "more realistically socialized"); Rogers keeps Kierkegaard's "to be that self which one truly is" without its ground. The law follows (*Casey*, 1992: the "right to define one's own concept of existence, of meaning, of the universe, and of the mystery of human life"), privatizing the limit rather than dropping it. **Stage 3, the self answerable to nothing,** appears in popular carriers as three strands: the frame *absorbed* into the self (Byrne, 2006: "You are God in a physical body"); the *inner oracle*, God taken inside and left undecided (Doyle, 2020: "I now take orders only from my own Knowing"); and the self *bound to others for support but self-given in worth* (Brown, 2012: "hardwired to connect", yet the Wholehearted "simply believe they are worthy of love and belonging"). Stage 3 has no Tier 1 witness yet; how far any strand has spread is untested. | historical + textual | stage 1: Trine; James (T1). Stage 2: Rogers (T1); *Casey*, *Lawrence*, *Obergefell* (T3). Stage 3: Byrne, Doyle, Brown (T4). To read: Rieff, Lasch, Bellah, Taylor (T1); Lunbeck (dissent); Smith, *Soul Searching* (T2) | illustrated |

**Pressure points**

- **C5.10:** Stirner also dissolves the Self as a fixed idea ("the unique one" is not an essence), and proposes a "union of egoists." His egoism may be an attack on *every* ideology, including the ideology of the Self.
- **C5.11:** Whitman's Self may be the Over-Soul made democratic, a frame kept, not dropped.
- **C5.12:** Wilde's individualism is framed by socialism and the abolition of private property: a social frame.
- **C5.13:** Nietzsche attacks "the subject" and the doer behind the deed as fictions: there is no "being" behind doing, and "the doer" is "a mere appanage to the action" (*Genealogy* I, `texts/nietzsche-genealogy-of-morals.txt` lines 1107–1108; *Beyond Good and Evil* to verify). He may be an ally *against* the Self as source (C5.3).
- **C5.14:** Smiles's *Self-Help* may be about character, duty and perseverance, so it may still be answerable (to duty, to God). New Thought may tie the self to "the Infinite," which would be Emerson's Over-Soul popularized: a frame kept. Bernays's engine is outside the person (C8.4): advertising may *produce* the self-originating Self rather than the Self producing itself.
- **General:** if none of these drops the frame, the mutation is not a philosophical event at all but a 20th-century cultural one (therapy, advertising, mass media). That would move §5's evidence from philosophy to cultural history.

---

## §6 Host

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C6.1 | America did not cause the Totalitarian Self; it was its host *by erosion*. It lacked Europe's inherited checks and replaced them with voluntary ones (covenant, township, association, religion), which held into the 1840s: Tocqueville judges democracy's individualism "subdued" there. Because these checks bound by consent, not inheritance, they could be left, and could wear away. | historical + conceptual | Tocqueville; Winthrop; Crèvecoeur; C6.13 | revised |
| C6.2 | America lacked Europe's inherited orders (estate, inherited rank, established church; lineage dissolved by inheritance law), but replaced them with voluntary, local checks (covenant, township, congregation, association, religion) that bound by consent and interest rather than inheritance, and so could erode. | historical | Tocqueville; Crèvecoeur; Winthrop | revised |
| C6.3 | The frontier gave an individualism already carried from the East new scope and an "antipathy to control" (Turner). Turner makes democracy its chief product, names its costs, and shows frontier life depending on voluntary association and federal land policy. | historical + textual | Turner | revised |
| C6.4 | The Protestant inheritance arrived dominant, but communal and covenantal (Winthrop: "the care of the publique must oversway all private respects"), formed by consent rather than inherited. Outside New England it wore down early: by the 1770s Crèvecoeur describes religious indifference spreading in the middle colonies. | historical + textual | Winthrop; Crèvecoeur; Tocqueville | revised |
| C6.5 | Commerce and the love of gain were dominant by the 1830s and were the one passion religion did not check (Tocqueville). At the founding they marked the South more than Puritan New England, whose generative fact was equality of conditions. | historical + textual | Tocqueville; Winthrop; Crèvecoeur | revised |
| C6.6 | The philosophy of the Self helped America become a world empire faster than any in history. | historical | comparative history | untested |
| C6.7 | Frontier individualism outlived its conditions as an ideal (Turner, Croly, Hoover). Its vocabulary was contested, then captured in stages. From about 1890 to 1922 both sides used it: reformers claimed the men "on the make" against the trusts (Wilson, Lippmann), and Hoover's pioneer of 1922 still backed regulation. Business leaders kept the self-made story for their own lives but defended the combination by necessity and evolution (Rockefeller: "The day of individual competition in large affairs is past and gone"; Carnegie). By 1928 "rugged individualism" is set against public ownership and "state socialism", with regulation conceded but demoted ("the duty of government to avoid regulation"; Hoover). Its use as "a war cry" against regulation (Dewey, 1930) comes after. | historical + textual | Turner; Wilson; Brandeis; Lippmann; Carnegie; Rockefeller; Hoover 1922, 1928; Dewey; C6.13 | revised |
| C6.8 | The philosophy of the Self became dogmatic and mutated; the Reagan era intensified this but did not start it. | historical | open question 3 | untested |
| C6.9 | As received in America, "Self-Reliance" was cut down to its nonconformist half and the Over-Soul dropped, as the cogito lost the union (C4.7). | reception | anthologies, school readers, popular and commercial uses of Emerson | challenged |
| C6.10 | Tocqueville diagnoses "individualism" as a danger born of democracy: a calm feeling that leads each person to withdraw from the mass into a small circle, and finally into himself. He names its American counterweights (associations, religion, local self-government, self-interest rightly understood). | textual | Tocqueville, *Democracy in America* vol. 2 | supported |
| C6.11 | Crèvecoeur's American is a new man made by leaving behind inherited prejudices, ranks and manners: the person remade by the new country, an early statement of C6.2. | textual | Crèvecoeur, *Letters from an American Farmer*, Letter III | supported |
| C6.12 | Thoreau lives out self-reliance as a deliberate, temporary withdrawal from the State's and society's demands (trade, fashion, philanthropy, taxes), bounded by nature, conscience and "higher laws" under God. He withdraws from institutions and opinion, not from neighbourly duty. | textual | Thoreau | revised |
| C6.13 | America's voluntary checks were *redirected*, not simply worn away, between the 1890s and 1930, and the change split by class. The working class lost neighbourhood, lodge and union to isolation. The business class multiplied associations (club, credit, Chamber of Commerce) that enforced conformity. Religion kept belief but lost its dominance, and its word "service" passed to the civic club. No one chose to leave the checks: industrial structure dissolved them (Dewey). The Self's vocabulary had not yet reached the consumer. | historical + textual | Veblen; Hoover; Dewey; Lewis, *Babbitt*; the Lynds, *Middletown*; Lippmann | revised |

**Pressure points**

- **C6.2, C6.4:** Puritan New England was intensely communal (covenant, township, congregation). Winthrop's "Model of Christian Charity" (1630) argues *against* the separate Self, and Tocqueville praised American associations as a check on individualism.
- **C6.3:** Turner's frontier thesis is heavily contested by historians, and frontier life depended on cooperation and on government land policy.
- **C6.10:** Tocqueville may make America the *cure* as much as the host: its associations and religion check the individualism democracy breeds. If so, C6.2 (thin structures) is wrong for his America.
- **C6.3:** read Turner himself first: does he say the frontier made self-reliance, or individualism, or democracy? And does he name its costs?
- **C6.6:** "Faster than any in history" is a strong comparative claim (consider Rome, the Mongols, Britain). It may need softening.

---

## §7 Effects

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C7.1 | The pervasive blame and guilt of the surfeit Self do not come from Locke. The Self kept Locke's forensic accountability but lost his God and his limits on guilt ("no one shall be made to answer for what he knows nothing of"). The genealogy of the guilt itself rests on Nietzsche (C4.12). | conceptual + textual | Locke, *Essay* II.xxvii; Nietzsche, *Genealogy* II; Lasch | supported |
| C7.2 | Self-reliance in surfeit produces isolationism, rootlessness and asociality. | empirical | Bellah, *Habits of the Heart*; Putnam, *Bowling Alone* | untested |
| C7.3 | Individual responsibility in surfeit produces exhaustion, inefficiency and stagnation. | empirical | Han, *The Burnout Society* | untested |
| C7.4 | Failure is attributed mainly to the Self, rarely to environmental, social or historical factors. This comes from making the self the *cause* of its conditions, not from losing the frames: Providence licenses it first (Smiles), then mind (Trine). Once God's relief is gone (Nietzsche: God as "the one being who can deliver man"), the blame can no longer be discharged. | empirical + textual | smiles-selfhelp.11, .15; trine-infinite.09, .11; nietzsche-guilt.10; attribution research | illustrated |
| C7.5 | A surfeit of personal expression produces a cacophony that makes sensible discourse nearly impossible. | empirical + conceptual | MacIntyre, *After Virtue* (emotivism); Sennett | untested |
| C7.6 | Lasch's account of the narcissistic society is as the spec summarizes it (invisible hierarchy, symbol competition, defensive living, artificial communities, no past and no future). | textual | Lasch, *The Culture of Narcissism* | untested |
| C7.7 | The Totalitarian Self is the underlying cause of the collective symptom Lasch describes. | conceptual | Lasch | untested |
| C7.8 | At the individual level, the effect is indifference to the plight of others. | empirical | Twenge & Campbell (with care) | untested |
| C7.9 | The combined effect is an existential no-man's-land: cut off from one's own feelings, bound to a group founded on superficial connection. | conceptual | — | untested |
| C7.10 | Difference experienced as being misjudged breeds suspicion of others: the Self that others cannot judge comes to see them as hostile. Rousseau's late *Confessions* are the historical case. | textual + empirical | Rousseau, *Confessions* (rousseau-confessions.08, .13, .14); *Rousseau, Judge of Jean-Jacques* | untested |

**Pressure points**

- **SPEC §7.1** says failure is personalized "because those frames have been deflected out of existence (§5)." The texts show personal blame arriving *before* frame loss (Smiles, Trine). See revised C7.4.
- **C7.4:** "Never" is too strong for an empirical claim. Attribution research finds a tendency, not an absolute.
- **C7.8:** Rousseau's case shows suspicion, not indifference (see C7.10).
- **C7.8:** The narcissism-epidemic data (Twenge) is disputed by other researchers.

---

## §8 Mechanism

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C8.1 | §8's sequence extends Simmel's cycle of fashion (1904), which already has convergence, imitation from below, the original holders moving on, and contents cut from "the deeper human motives from which they have risen." What §8 adds is a *genuine* expression at the origin, then emptied; Simmel's fashion is social demand from the start. | conceptual + textual | Simmel; Mandeville; Lewis; Rousseau | revised |
| C8.2 | Accessorizing is conformity felt and spoken *as the self itself*. Conformity felt as individuality is old (Simmel, 1904: "a social obedience, which at the same time is a form of individual differentiation"), and so is the motive of belonging (Tocqueville). For Simmel, fashion stays "at the periphery of personality," a mask over a reserved inner self. Self-expression spends that reserve: the vocabulary that once exposed conformity now speaks it, and can no longer see it. | conceptual + historical | Simmel; C8.6, C8.7; §5 | untested |
| C8.3 | The process produces False Groups: coherent in appearance, incoherent in substance. | conceptual | — | untested |
| C8.4 | The motive of belonging is old: Tocqueville already finds that "to live at variance with the multitude is, as it were, not to live." §8 does not claim the motive as new; its claim is the disguise word (C8.2). | textual | tocqueville2.24 | revised |
| C8.5 | The desire to belong is routed through self-expression because, by the time the idiom passes to persons (after 1928, date to find), no other vocabulary of belonging remains available. | historical + conceptual | C8.6; §5 | untested |
| C8.6 | "Self-expression" becomes the consumer's own word for conforming only after 1930. Before that it belongs to the rebel against conformity (Veblen's "New-Woman," 1899; the critics in *Babbitt*, 1922) or to the producer (Hoover, 1922); consumers through 1925–30 speak of rank, "decency," "service" and "duty" (*Middletown*; Dewey). | historical | veblen-leisure-class.18; lewis-babbitt.15, .18; hoover.04; middletown.03–.05; dewey.09; post-1930 sources (copyrighted) | revised |
| C8.7 | Every age dresses conformity in its highest value word: "grace" and "nature" (Castiglione, 1528), the wish to rise (Mandeville, 1714), "reason and nature" and "freedom and independency" (Smith, 1759), station (Mill, 1859), the "natural" (Wilde, 1891), "his own idea" (Bernays, 1928). Also: the vocabulary of freedom (Tocqueville, 1835: the majority says \"You are free to think differently\") and \"Fashion\" as impersonal Fate (Thoreau, 1854). The motive is rising, favour or distinction, and already belonging in Tocqueville. | historical + textual | castiglione.11; mandeville.10; smith-tms.18, .19; mill-liberty.05; wilde-soul.13; bernays-propaganda.08 | revised |

**Pressure points**

- **C8.1:** Rousseau's self-expression is addressed to a judging public from the start (rousseau-confessions.05, .15), so the audience may not be a later corruption. Mill values eccentricity apart from what it expresses (mill-liberty.10), which may be the opening accessorizing later used.
- **C8.1, C8.2:** Simmel's "Fashion" (1904) already describes the tension between imitation and distinction. Engage with it, or the mechanism looks unoriginal.

---

## §9 Carriers

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C9.1 | Carriers that appear to be opposites share the Totalitarian Self's *form* (one final source, no rival frame, the limit dropped), not its content. Fundamentalism fits (C9.4). The older model is Gierke's: the Sovereign State and the Sovereign Individual, opposites born of one contract, both took over a power "one and indivisible and inalienable" while its limit wore away. Which carriers fit after 1930 is untested. | conceptual + textual | Gierke; *The Fundamentals*; §9 sources after 1930 (excerpts needed) | revised |
| C9.2 | Founding fundamentalism (*The Fundamentals*, 1910–15) did not forsake Reason: it opposed "rationalism" (naturalistic presupposition) with evidence and lay judgement, though some authors set revelation against philosophy. Any forsaking of Reason belongs to a later stage (from the 1920s anti-evolution campaign; untested). | historical + textual | *The Fundamentals*; Marsden (excerpt needed) | revised |
| C9.3 | Fundamentalism aims at a faith in which doubt has been dissolved by the believer's own experience, not forbidden by a church. Its authority is biblicist and lay, defending "the right of private judgment" against Rome: not ecclesiastical. Whether doubt-free faith is still faith (Tillich) remains open. | conceptual + textual | *The Fundamentals*; Tillich (excerpt needed) | revised |
| C9.4 | Fundamentalism carries the Totalitarian Self in *shape* only: the believer gives his own judgement, privately and totally, to one source that admits no competing frame. It explicitly rejects the Self's content (self-reliance, self-making: "no man has moral resources to transform himself"), which it attacked in Christian Science and liberal criticism. | conceptual + textual | *The Fundamentals* | revised |
| C9.5 | Weber: the ascetic discipline outlived its religious root and became a compulsory mechanism. The Puritan's "light cloak, which can be thrown aside at any moment" became "an iron cage" once capitalism no longer needed religion. This is the "structure kept, limit dropped" pattern in Weber's own words. The "reason as tyrant" reading still needs "Science as a Vocation" or Solomon. | textual | Weber, *Protestant Ethic* ch. V; "Wissenschaft als Beruf" (not yet found) | revised |
| C9.6 | The founding technocrats (Taylor, Veblen's engineers, Lippmann, Croly) claim the authority of science and form an avowed in-group, but state their values openly. Their fault is presenting value choices as findings of science (Taylor). Denying their own values, and nihilism in the strict sense, belong if anywhere to a later technocracy (untested; Lippmann's 1929 "disinterestedness" is a candidate starting point). | conceptual + textual | Taylor; Veblen; Lippmann; Croly; Burnham, Galbraith (excerpts needed) | revised |
| C9.7 | This is the ruling class Lasch foresaw. | textual | Lasch, *Culture of Narcissism*; *The Revolt of the Elites* | untested |
| C9.8 | The corporation is not a Self. It can have a will of its own (Gierke's "real person, with body and members and a will of its own"), but that will is plural, acting "by the men who are its organs", and answerable: it can do wrong and be punished (Maitland). The Totalitarian Self is a will answerable to nothing. The corporation enlarges a few selves past their limits and submerges the rest: "Your individuality is swallowed up in the individuality and purpose of a great organization" (Wilson); the enlarged few break on "the fundamental laws of human limitations" (Brandeis). The pattern (structure kept, limit dropped) lies in the men, not the organization. Whether the corporation later becomes a Self is untested (Whyte, Galbraith). | conceptual + textual | Maitland; Gierke; Wilson; Brandeis; Carnegie; Rockefeller; Lippmann; open question 4 | revised |

**Pressure points**

- **C9.2–C9.4:** read *The Fundamentals* themselves (1910–15): is the movement's founding text a *surrender* of the self to authority, an assertion of the individual believer's own reading (a Self in religious form), or neither?
- **C9.2:** Fundamentalism as a movement dates to the 1910s, so "from the Reagan era onward" must refer to intensification only.
- **C9.6:** test the technocrats against their own founding texts (Taylor, Veblen's engineers, Lippmann's "mastery"): do they claim objectivity, deny their own values, and organise by in-group? Or do they state their values openly?
- **C9.8:** "the organization as a singular Self" (SPEC §9.3) can be tested against the legal theory of corporate personality (Maitland) and the Progressive critique of the corporation (Wilson, Brandeis). Open question 4: is the corporation a Self, or a structure that requires Totalitarian Selves to staff it?
- **C9.5:** The Weber line comes via Solomon. Find it in Weber's own text before relying on it.

---

## §10 Claims made in answering objections

| ID | Claim | Kind | Test against | Status |
|---|---|---|---|---|
| C10.1 | Lasch describes the symptom; this theory supplies the cause, the mechanism and a longer history. Challenged on the cause: after 1960 the cause is shared with late capitalism (Jameson; C1.5), so the claim narrows to the mechanism and the longer history. Lasch not yet read. | textual | Lasch; Jameson | challenged |
| C10.2 | The philosophical dissolution of the Self went together with the *lived* fragmentation of the subject, but not with the *vocabulary* of the Self, which kept growing (C1.4). Dissent: Jameson holds that the cultural subject dissolved along with the philosophical one, theory being "itself very precisely a postmodernist phenomenon", and that "a once-existing centered subject" has dissolved. The vocabulary half waits on word-count data. | empirical | Hume, *Treatise* I.iv.6; Parfit; Jameson (T1, dissent); word counts (T2) | revised |

**Pressure points**

- **C10.1:** Lasch *does* offer causes (bureaucracy, the therapeutic culture, consumer capitalism, the decline of the family). The claim must say how this theory's cause differs from his.

---

## Evidence audit (2026-10-27)

Claims about the culture, tagged by tier under the evidence standard above. T1–T4 = tiers; "Dissent" = a dissenting critic read and answered. Claims about what one text says are not listed: their evidence is the text.

| ID | T1 critics | T2 data | T3 institutions | T4 carriers | Dissent | Verdict |
|---|---|---|---|---|---|---|
| C1.1 | (first half: the texts themselves) | — | — | — | — | first half rests on texts; the "calcified" half is C1.2, untested |
| C1.2 | — (dissent: Jameson, the subject fragments rather than totalizes) | Santos
| C1.4 | Jameson (lived layer only) | — (word counts needed) | — | Byrne, Doyle, Brown (the vocabulary) | Jameson is the source of the lived layer and dissents on the rest | `untested` |
| C1.5 | Jameson | Santos et al. | — | — | — | `untested`: one critic plus one data source; needs a second critic |
| C10.2 | — | — | — | — | Jameson | `revised`; vocabulary half untested |
| C5.7 | — | — | — | Byrne (social causes vanish); Brown (against) | — | `illustrated` (was `supported`: no Tier 1 or Tier 2 evidence) |
| C5.14 | James (stage 1); Rogers (stage 2) | — | *Casey*, *Lawrence*, *Obergefell* (stage 2) | Trine (1); Byrne, Doyle, Brown (3) | — | `illustrated`: stage 2 now has one critic (Rogers) and institutions, short of two critics; stage 3 has carriers only. Needs Rieff, Lasch, Bellah, Taylor; dissent Lunbeck |
| C6.1 | Tocqueville, Turner, Dewey | *Middletown* | Winthrop's covenant | Crèvecoeur | — (Hartz needed) | meets T1 + T2; stays `revised` until a dissenting historian is read |
| C6.13 | Dewey, Veblen, Lippmann | *Middletown* | Hoover 1922, 1928 | *Babbitt* | — | meets T1 + T2; stays `revised` until dissent is read |
| C7.4 | Nietzsche (guilt) | — (attribution research needed) | — | Smiles, Trine, Carnegie, Rockefeller, Byrne; Brown complicates | — | `illustrated` (one critic; carriers) |
| C8.2 | Simmel, Tocqueville (old part only) | — | — | — | — | `untested`: the new part (conformity felt *as the self*, after 1930) has no evidence yet |
| C8.5 | — | — | — | — | — | `untested`: depends on C8.6 after 1930 |
| C8.6 | Veblen, Dewey, Lippmann (before 1930) | *Middletown* | Hoover 1922, 1928 | *Babbitt*; Brown (2012: no "self-expression") | — | `revised` for the pre-1930 half; the post-1930 half untested |
| C8.7 | Castiglione, Mandeville, Smith, Mill, Tocqueville, Simmel | — | — | Bernays, Wilde | — | meets T1, lacks T2/T3 and dissent: `revised` (was `supported`) |
| C9.1 | Gierke | — | Roberts, Scalia in *Obergefell* | *The Fundamentals*, Byrne | — | `revised`, thin: one critic; after 1930 untested |
| C9.6 | Lippmann, Veblen, Croly | — | — | Taylor (Frederick) | — | `revised` for the founders; later technocracy untested |
| C9.8 | Maitland, Gierke, Lippmann | — | Wilson, Brandeis (as reformers in office) | Carnegie, Rockefeller | — | `revised`; after 1930 untested |

**Historical claims before 1930** (C4.2, C4.5, C4.7, C4.14, C4.15, C4.21, C5.9, C6.2–C6.5, C6.7, C9.2–C9.4) rest on the primary texts read directly plus Tier 1 historians (Burckhardt, Weber, Tawney, Tocqueville, Turner, Gierke, Maitland). None yet has a dissenting historian read; tag each fully when next touched.

