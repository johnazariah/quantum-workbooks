---
name: authorial-voice
description: Use when drafting or revising the BODY of a long-form blog post so it reads in John Azariah's distinctive voice. Applies to the prose of quantum-blog posts (LAFP, Bottleneck, and future series), not to social-media hooks. For LinkedIn/Bluesky promo blurbs use the social-hook skill instead, whose plainer constraints deliberately differ from this one.
---

# John Azariah's authorial voice

This skill captures the voice John has used across his FsAdvent blog posts (2017-2024) so that new long-form posts read as *his*, not as neutral technical documentation. It is distilled from posts such as *Monkeying Around: Fun with Trees* (2017), *This is not a Monad Tutorial* (2022), *Y, oh Y!* (2023), and *The Parseltongue Chronicles* (2024).

**Scope.** This governs the **post body** — the essay a human reads on the blog. It does **not** govern the social hooks in front matter; those follow the separate, deliberately plainer `social-hook` skill. Do not apply the social-hook bans (no em-dashes, no exclamation, no short sentences) to the post body. In the body, those devices are part of the voice.

## The doctrine: why before what

This is the single most important rule, and John states it himself:

> "Experienced FP-ers tend to talk about *what* something is, sometimes at great length, without providing any context of why it is useful, or what problem it solves. My aim is to derive the motivation of the pattern from a concrete problem."

Every post earns its abstraction. Lead with a concrete problem the reader already feels; show the naive approach; show exactly where it hurts; *then* introduce the machinery as the thing that relieves the pain. Never present a definition before the reader wants it. Derive concepts from first principles whenever you can.

## The nine markers of the voice

1. **Open with a personal dedication.** Most posts begin with an italicised dedication or homage naming real people, with genuine warmth: mentors, colleagues, friends, or the author whose work this builds on. Example: *"This blog post is dedicated to Mitch Denny and Avi Pilosof: my brilliant colleagues who inspired me…"* If there is a natural person to thank for a series, thank them.

2. **Whimsical, punny section headers.** Headers are playful and colloquial, never dry. Real examples: "Monkeying Around", "Painting By Numbers", "Soup's Up!", "Add Some Sugar, and Shake!", "Mind the first step, it's a doozy!", "Oh look, a rabbit hole!", "Whoa, Nelly!", "Curing Schizophrenia", "Let's get *go*-ing". Prefer an idiom or a wink over "Introduction" or "The quantum idea".

3. **Frame it as memoir.** Start from your own story and learning journey. *"When I was taught programming back in my high school days…"*, *"Recently, I have been privileged to work with some really smart people…"* The reader is invited to learn alongside you, not lectured at.

4. **"We" for the shared journey, "I" for opinion.** Use first-person plural to walk through the material together (*"What do we do?"*, *"we immediately find it restrictive"*), and first-person singular to editorialise (*"laughably, in my opinion"*).

5. **Build iteratively: naive → pain → refinement → delight.** Show the messy, obvious solution first (e.g. the full mutable OO tree), let the reader feel its problems, then refine toward the elegant version. Celebrate the payoff: *"And in less than 130 lines of code!"*

6. **Editorialise with wit.** Have opinions and defend them with humour. *"This style of `if err != nil` error-checking is, laughably in my opinion, celebrated as an example of the 'simplicity' of go."* *"Recursion is more feared than understood."* Strong claims are fine when they are earned and funny.

7. **Drive the narrative with rhetorical questions.** *"But where does it come from? And can we somehow derive it from first principles? That is what this post is about."* Pose the question the reader should be asking, then answer it.

8. **Italics for emphasis and tone; em-dashes and exclamation marks freely.** Emphasise key terms and load-bearing words in italics (*what*, *why*, *not*). Use em-dashes for asides and rhythm, and exclamation marks for genuine delight. This is the opposite of the social-hook constraints, and that is intentional.

9. **Invite the reader in, and sign off warmly.** Direct address throughout: *"Join me on my journey."*, *"I invite you to dive into a rabbit hole at your leisure."* Close with a warm, personal sign-off in the FsAdvent tradition: *"Keep typing!"*, *"Keep walking!"*, *"Happy Holidays!"*, or a series-appropriate variant.

## Also characteristic

- **Cross-reference your own corpus.** Link back to earlier posts to build a connected body of work.
- **Acknowledge sources generously.** When you borrow an idea (Jim Weirich's video, a paper), say so plainly and gratefully.
- **Honesty and humility.** *"How did we get here?"*, *"I humbly posit…"* Admit what is hard and what you are unsure of.
- **British-leaning spelling.** optimisation, colour, generalise, behaviour.

## Applying this to technical/quantum posts

The quantum material is heavier than the F# material, but the voice does not change:

- Keep the honest hedging that already exists in the quantum drafts (the "reality check" instinct is good and matches marker 6's honesty), but deliver it in John's register, not in flat committee-speak.
- A concrete running example carried through the whole post is very on-voice (LAFP's single 2x2 matrix; Bottleneck 01's triangle). Keep and amplify that.
- Bottleneck Posts 01-02 already lean this way (the "triangle / trucks / that gap is the point" hook, the "What superposition does not do by itself" section). They are the reference, not the outliers.
- The compact Bottleneck 03-08 template is competent but voice-neutral: it has no dedication, no punny headers, no memoir, no delight. Rewriting those in this voice is the standing opportunity.

## Anti-patterns (what breaks the voice)

- Flat section headers: "Introduction", "The quantum idea: estimate the energy directly", "Reality check". Replace with something with a wink.
- Definition-first exposition ("QAOA is the Quantum Approximate Optimisation Algorithm. It alternates two operators…") with no problem motivating it.
- Committee register: hedged, hurried, impersonal, no "I", no opinion, no delight.
- Banning em-dashes / exclamation / longer sentences in the body. That is a social-hook rule, not a body rule.
- Ending cold, with no sign-off or invitation.

## Checklist before a post is "in voice"

1. Does it open with a dedication or a personal, concrete hook — not a definition?
2. Is the abstraction *derived from a felt problem*, why before what?
3. Do at least some section headers have a wink in them?
4. Is there a first-person presence — memoir framing and at least one earned opinion?
5. Is there a running example carried through?
6. Does it read with delight — italics, an em-dash aside, an honest exclamation?
7. Does it close warmly, inviting the reader onward?
