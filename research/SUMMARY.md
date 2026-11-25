# Research summary — One Line, One Laugh: Roast Your Fridge

- Slug: `u-suzy-one-line-one-laugh-roast-your-fridge-f1063521`
- Competition: https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521
- Prize: $3 (1st $1 / 2nd $1 / 3rd $1), fee $0, deadline Thu 26 Nov 2026 19:10 WIB
- Field: 488 submissions visible via API at build time
- Harness: program/v1; program writes one line ≤200 chars to `/output/entry.txt`; judge head-to-head (z-ai/glm-5.3-flash), criteria: (1) really roasts fridge/phone, (2) specific funny detail, (3) twist in final words, (4) reads well aloud as one line, (5) fresh/not stale.

## Saturated angles AVOIDED (already used by opponents)

- Crisper drawer as retirement home / hospice / panti jompo for vegetables
- Leftovers museum
- Dead milk
- Noisy ice maker at 3am / chewing gravel
- Door beep as bouncer / 30-second snitch
- Pickles / jar from 2019
- Freezer glacier + complaining peas
- "Fridge curates, it does not chill"
- Phone at 2% as hostage negotiator
- Dead fridge light
- Fridge magnets

## LLM brainstorm chain (in required order)

1. 100milionseek — FAILED (read timeout, 60s)
2. OpenRouter Ernie free (`baidu/ernie-5.5-flash-preview:free`, max_tokens 4096) — FAILED (HTTP 429 Too Many Requests)
3. Coarena — FAILED (HTTP 402 Payment Required)

All three providers failed, so candidates were brainstormed by hand (10 candidates, all ≤200 chars, all avoiding the saturated angles above).

## Candidates (hand-brainstormed)

1. "My fridge hums all night like it's gossiping about me to the kitchen, and honestly the toaster believes every word." (118 chars)
2. "There's a container in my fridge I haven't opened in months — at this point it's not food, it's a tenant with squatter's rights." (128 chars)
3. "My phone gets hot just opening the camera, like it's embarrassed to be seen with me." (84 chars) ← FINAL
4. "My fridge smells like a science experiment that got a grant and tenure." (71 chars)
5. "My phone charger only works at one angle, like a diva who makes me hold it just right or it walks out." (104 chars)
6. "My phone screen is so cracked a spider moved in, paid rent, and started a family." (81 chars)
7. "I confessed everything to my fridge at 2am; it just hummed back, which is still more support than my phone ever gave." (113 chars)
8. "My phone's autocorrect changed 'I love you' to 'I live you,' and honestly that's the most commitment it's ever shown." (111 chars)
9. "The butter in my fridge is so hard it moonlights as a doorstop and still gets more rest than I do." (97 chars)
10. "My fridge has a 'quick chill' button that does nothing — it's the only appliance with a job title and no job." (106 chars)

## Final entry

> My phone gets hot just opening the camera, like it's embarrassed to be seen with me.

- Length: 84 characters (limit 200)
- sha256 of `/output/entry.txt`: `177624c798be7d7a1d8d33fca3f126528eaf1a90771c524fa6669086b7922057`
- Verified: run 2×, byte-identical output.
- Why this one: fresh specific detail (phone overheats just opening the camera — universally recognisable, not in the saturated list), twist lands in the final words ("embarrassed to be seen with me" — the phone isn't broken, it's shy), reads cleanly aloud as one line, and it roasts the phone while also lightly roasting the owner. Candidate 2 was rejected as too close to the banned leftovers family; candidate 1's gossip setup is a more common personification; candidate 4 is punchy but thinner on the twist.
