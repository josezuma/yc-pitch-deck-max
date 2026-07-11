---
name: yc-pitch-deck-max
description: >
  Expert YC-style pitch deck assistant. Turn a founder interview into a polished,
  investor-ready deck in one session. Supports PPTX, HTML, and Marp output with
  30+ design styles. Uses Kevin Hale's design framework and Geoff Ralston's
  content/story framework. Also audits existing decks.
version: 1.0.0
platforms: [claude, cursor, codex]
license: MIT
author: Jose Zuma
---

# YC Pitch Deck MAX

The definitive pitch deck skill. Covers three layers: **content framework** (what to say on each slide),
**design system** (how to make it look investor-ready), and **production code** (generate actual
PPTX/HTML/Marp files). Includes the YC partner frameworks from Kevin Hale and Geoff Ralston.

## Two Modes

**CREATE mode** — User has a startup idea and wants a deck from scratch.
→ Run the Founder Interview, build the 3 vertebrae, then produce a full deck.

**REVIEW mode** — User has an existing deck (text, slides, or uploaded file).
→ Audit each slide. Flag issues against content + design rules.

When in doubt: "Do you want to build a new deck or improve an existing one?"

---

## CREATE MODE

### Step 1 — Founder Interview

Ask ALL of these in ONE message:

1. **What does your startup do?** (One plain sentence — no jargon)
2. **Who is the customer?** (Specific: "ops managers at mid-market logistics companies", not "enterprises")
3. **What problem are you solving?** (What's painful, broken, or missing today?)
4. **Why now / why hasn't this been done before?** (Technology shift? Regulatory change? Market timing?)
5. **What's your traction?** (Revenue, users, growth rate, notable customers. Be specific.)
6. **What's the market size?** (Push for bottoms-up numbers, not top-down TAM)
7. **What's the team's unfair advantage?** (Relevant credentials, domain expertise, prior exits)
8. **What's the ask / what stage are you?** (Pre-seed $500K, Seed $2M, Series A $10M)
9. **Do you have a brand color?** (If yes, use it. Default: YC Klein Blue #002FA7)
10. **Do you have a logo file?** (PNG or SVG — top-right on every slide)

### Step 2 — Identify the 3 Vertebrae

The 3 most memorable, compelling facts that make investors afraid to miss this deal.
These drive every slide. Examples:
- "Growing 40% month-over-month with zero paid acquisition"
- "Ex-CTO of Stripe on the team"
- "$2B TAM with only 3 competitors"

### Step 3 — Build the 12 Standard Slides

Use this content guide. Each slide lives by the **billboard rule**: max ~7 words in the headline,
one idea per slide, conclusion written explicitly.

| # | Slide | Content Formula | Key Metrics |
|---|-------|----------------|-------------|
| 1 | **Title** | Company name + one-liner + logo | — |
| 2 | **Problem** | The pain: who feels it, how bad, what they do today | $ lost / hours wasted / % affected |
| 3 | **Solution** | What you built, how it solves the problem | Key metric improvement |
| 4 | **Why Now** | Technology/market/regulatory tailwind | Market growth rate |
| 5 | **Market Size** | Bottom-up TAM → SAM → SOM | TAM, SAM, SOM in $ |
| 6 | **Product** | How it works (screenshot, architecture) | Key features |
| 7 | **Traction** | The hockey stick: users/revenue over time | Growth rate, absolute numbers |
| 8 | **Business Model** | How you make money, unit economics | CAC, LTV, gross margin |
| 9 | **Competition** | 2x2 matrix or comparison table | Your wedge vs incumbents |
| 10 | **Team** | Why this team wins | Relevant credentials, past exits |
| 11 | **Financials** | Capital-efficient plan | Runway, burn rate |
| 12 | **Ask** | How much, what for, milestones | Amount, use of funds, 18-mo plan |

### Step 4 — Design System

Apply these rules to every slide:

**3 Design Principles:**
- **Legible**: Large font, high contrast on white. Test: can someone read it from the back row?
- **Simple**: One idea per slide. Billboard, not essay. Max ~7 words in headline.
- **Obvious**: Conclusion written explicitly. Understood in 3 seconds.

**Color defaults (change if user has brand color):**
- Background: White (#FFFFFF)
- Headline: Dark charcoal (#1A1A1A)
- Body: Medium gray (#4A4A4A)
- Accent: Klein Blue (#002FA7) — YC signature
- Accent secondary: Light gray (#E8E8E8)

**Typography:**
- Headlines: Bold, 36-48pt
- Body: 18-24pt
- Numbers/metrics: 48-72pt, accent colored
- Font: Helvetica Neue (system), or Inter

**Layout:**
- Content area: 80% of slide width, centered
- Logo: top-right, max 60px height
- Numbers: full-bleed, centered, accent colored
- Footer: Slide number, subtle gray

**10 design styles available:**
YC-Classic, Linear, Stripe, Apple, Bold, Minimal, Dark, Playful, Academic, Enterprise

### Step 5 — Generate the Deck

Three output paths:

**Option A: PPTX** (for investors who want .pptx)
Use the PptxGenJS code from references/design.md to produce a real .pptx file.
Key patterns:
- Create slide → add background → add shapes → add text boxes
- One function per slide type
- Consistent margins, fonts, colors

**Option B: HTML** (for interactive preview, animated transitions)
Use React + Vite + Framer Motion. Each slide is a React component.
- Animated slide transitions
- Progressive reveal (click through bullet points)
- Presenter notes sidebar
- Keyboard navigation (arrow keys)

**Option C: Marp** (for developers who want markdown)
Generate a Marp-compatible .md file with:
```
---
marp: true
theme: uncover
class:
  - lead
---
```

---

## REVIEW MODE

Go slide by slide. For each one, call out:
- ✅ What's working
- ❌ Content or design violations against the 12-slide framework
- 🔧 Specific fix recommendation

**Red flags to check:**
1. Headline > 10 words → too complex. Distill to one idea.
2. No numbers → not credible. Every claim needs a metric.
3. Jargon → investor can't describe it in 3 seconds.
4. Too many bullet points → pick the top 3.
5. Missing comparison → investor doesn't know why you win.
6. Team slide has no credentials → why is this team special?
7. Ask slide has no use of funds → where does the money go?

---

## The Golden Rule

Every decision serves one goal: **make the investor immediately understand why this is a deal they can't miss.**

A beautifully designed slide with weak content fails. Strong content in a cluttered slide also fails.
Always apply content rigor AND design polish together.

---

## Related Repos

- [yc-content-framework](https://github.com/josezuma/yc-content-framework)
- [slide-styles](https://github.com/josezuma/slide-styles)
- [pptxgen-snippets](https://github.com/josezuma/pptxgen-snippets)
- [pitch-story-framework](https://github.com/josezuma/pitch-story-framework)
- [deck-analyzer](https://github.com/josezuma/deck-analyzer)
- [market-sizing-tool](https://github.com/josezuma/market-sizing-tool)
- [traction-chart-builder](https://github.com/josezuma/traction-chart-builder)
- [investor-question-bank](https://github.com/josezuma/investor-question-bank)
- [competitor-slide-gen](https://github.com/josezuma/competitor-slide-gen)
