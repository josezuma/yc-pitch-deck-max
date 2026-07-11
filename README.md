<div align=center>
  <h1>🚀 YC Pitch Deck MAX</h1>
  <p><em>The super-skill for startup pitch decks. Combines YC content frameworks, 30+ design styles, PPTX/HTML/Marp output, investor intelligence, and deck analysis. Based on Kevin Hale + Geoff Ralston partner frameworks.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=License></a></p>
  <p><strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma</a></p>
</div>

---

## Quick Start

```bash
git clone https://github.com/josezuma/yc-pitch-deck-max.git
cd yc-pitch-deck-max

# Create a complete pitch deck from a founder interview
python3 scripts/create.py "BrandVirality" \
  --problem "Businesses invisible in AI search" \
  --solution "GEO audit platform" \
  --traction "19 OSS repos, 85/100 avg" \
  --ask "500K seed"
```

## The 3 Vertebrae Framework

Based on Geoff Ralston's YC partner framework:

| # | Vertebra | Purpose | Investor Reaction |
|---|----------|---------|------------------|
| 1 | The Insight | Show you understand something others don't | "I see the pattern" |
| 2 | The Solution | Show you're the right team to act on it | "They have the right approach" |
| 3 | The Proof | Show traction that de-risks the bet | "This is real" |

## Demo Output

```bash
$ python3 scripts/create.py BrandVirality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PITCH STORY — BrandVirality
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Vertebra #1: The Insight
"Businesses are invisible in AI search.
85% of LLM responses cite only top 3 brands.
The $850M GEO market grew 527% in 2024."

Vertebra #2: The Solution
"BrandVirality built the first comprehensive GEO platform.
19 open-source tools, 85/100 audit score."

Vertebra #3: The Proof
"Founded by an AI visibility expert.
Capital-efficient, product-led growth.
Seeking $500K to reach 1000 paid accounts."
```

## Sub-Skills

| Skill | Description |
|-------|-------------|
| create | Full interview-to-deck pipeline |
| content | 12 YC standard slide formulas |
| design | 30+ styles (YC-Classic, Linear, Stripe, Dark) |
| pptx | PptxGenJS code generation |
| html | React slide deck output |
| marp | Marp markdown themes |
| audit | Deck analyzer against YC guidelines |
| investor | 200+ YC partner questions |
| charts | Growth/traction chart templates |
| story | Narrative structure builder |

## Install Paths

```bash
# Claude Code
/plugin install yc-pitch-deck-max

# Direct
git clone https://github.com/josezuma/yc-pitch-deck-max.git

# NPM (coming soon)
npx yc-pitch-deck-max create "My Startup"
```

## Related

- [yc-content-framework](https://github.com/josezuma/yc-content-framework)
- [slide-styles](https://github.com/josezuma/slide-styles)
- [deck-analyzer](https://github.com/josezuma/deck-analyzer)
- [investor-question-bank](https://github.com/josezuma/investor-question-bank)

## License

MIT © 2026 Jose Zuma
