---
url: "https://www.threads.com/@scoutaipro/post/DYEnK-mFbUm"
author: "@scoutaipro"
clip_type: "Claude Code"
---

STOP USING CLAUDE WITHOUT THESE 3 SETTINGS
anthropic published 3 system prompt instructions that dramatically reduce claude's hallucinations
and almost nobody knows they exist
here's what they are:
1\ "allow claude to say i don't know"
> without this, claude fills knowledge gaps with plausible fiction
> it sounds confident. it sounds right. but it's completely made up

> add this instruction and claude actually says "i don't have enough information to answer that" instead of inventing an answer
> the default behavior is to always give you something even when it shouldn't
2\ "verify with citations"
> tell claude that every claim needs a source
> if it can't find one it should retract the claim
> statements that sounded authoritative before suddenly vanish from the output because they had no backing
> this alone filters out most of the hallucinated "facts"

3\ "use direct quotes for factual grounding"
> force claude to extract word-for-word quotes from documents before analyzing them
> this stops the paraphrase drift where the model subtly changes meaning while summarizing
> instead of interpreting what a document says it pulls the exact text first then builds on that
each one helps individually. all three together fundamentally change the output quality

there's a tradeoff though. citation constraints reduce creative output. so don't run these all the time
the move is to build a toggle:
> research mode: all three active. zero tolerance for made up info
> default mode: let claude think freely for brainstorming and creative work
if you use claude for anything involving research, facts, or decisions you should be using these three instructions right now
