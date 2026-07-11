<div align=center>
  <h1>🚀 YC Pitch Deck MAX</h1>
  <p><em>The super-skill for startup pitch decks. Combines YC content frameworks, 30+ design styles, PPTX/HTML/Marp output, investor intelligence, and deck analysis — all in one CLI. From founder interview to investor-ready deck.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=License></a>
  <a href=https://github.com/josezuma/yc-pitch-deck-max/actions/workflows/ci.yml><img src="https://img.shields.io/badge/CI-passing-green.svg"></a>
  <img src="https://img.shields.io/badge/styles-30-blue" alt="30 Styles">
  <img src="https://img.shields.io/badge/slides-12_YC__standard-blue" alt="12 YC Standard Slides"></p>
  <p><strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma</a></p>
</div>

---

## 🚀 One-Click Install

```bash
# Via npm (recommended)
npx yc-pitch-deck-max create "My Startup"

# Via Claude Code (plugin)
claude /plugin install josezuma/yc-pitch-deck-max

# Via git
git clone https://github.com/josezuma/yc-pitch-deck-max.git
cd yc-pitch-deck-max && python3 cli/yc-pitch-deck-max create "My Startup"
```

---

## 🔥 What YC Pitch Deck MAX Can Do

### Content Generation (6 commands)
| Command | What it does |
|---------|-------------|
| `yc-pitch-deck-max create <name>` | Full interview → complete deck pipeline |
| `yc-pitch-deck-max interview` | Run the 10-question founder interview |
| `yc-pitch-deck-max content <slide>` | Generate content for one slide (problem, solution, market, etc.) |
| `yc-pitch-deck-max story` | Generate the 3-vertebrae narrative |
| `yc-pitch-deck-max script` | Generate demo day pitch script from deck |
| `yc-pitch-deck-max bio` | Generate team credentials slide |

### Design & Output (5 commands)
| Command | What it does |
|---------|-------------|
| `yc-pitch-deck-max build <format>` | Build deck as PPTX, HTML, or Marp markdown |
| `yc-pitch-deck-max style <name>` | Apply a design style (Linear, Stripe, YC, Soft, Bold, etc.) |
| `yc-pitch-deck-max chart <type>` | Generate a chart slide (revenue, market, competitive) |
| `yc-pitch-deck-max theme` | Generate a color theme from brand color |
| `yc-pitch-deck-max preview` | Start local preview server (HTML decks) |

### Analysis (4 commands)
| Command | What it does |
|---------|-------------|
| `yc-pitch-deck-max audit <deck>` | Audit a deck against YC partner guidelines |
| `yc-pitch-deck-max review <slide-text>` | Review a single slide's content & design |
| `yc-pitch-deck-max questions` | Browse the 200+ YC partner question bank |
| `yc-pitch-deck-max compare <deck1> <deck2>` | Compare two decks |

### Calculators (3 commands)
| Command | What it does |
|---------|-------------|
| `yc-pitch-deck-max market <tam> <sam> <som>` | Generate market sizing slide |
| `yc-pitch-deck-max traction <data>` | Generate traction chart from data |
| `yc-pitch-deck-max cap-table <data>` | Generate cap table / use of funds slide |

---

## 📚 Sub-Skills (Claude Code / Cursor / Codex)

| Skill | What it masters |
|-------|----------------|
| `yc-pitch-deck-max/create` | Full pitch deck creation pipeline |
| `yc-pitch-deck-max/content` | Slide-by-slide content guidance per YC framework |
| `yc-pitch-deck-max/design` | Design system, style application, layout rules |
| `yc-pitch-deck-max/pptx` | PPTX generation with PptxGenJS |
| `yc-pitch-deck-max/html` | HTML slide deck generation (React + Vite) |
| `yc-pitch-deck-max/marp` | Marp markdown slide generation |
| `yc-pitch-deck-max/audit` | Deck audit against Kevin Hale + Geoff Ralston frameworks |
| `yc-pitch-deck-max/investor` | Investor intelligence (question bank, customization) |
| `yc-pitch-deck-max/charts` | Chart and data visualization slides |
| `yc-pitch-deck-max/story` | Narrative structure and storytelling |

---

## 🧠 How It Works

```
                        ┌─────────────────┐
                        │  Founder Interview│
                        │  (10 questions)   │
                        └────────┬─────────┘
                                 │
                        ┌────────▼─────────┐
                        │  3 Vertebrae      │
                        │  (core narrative) │
                        └────────┬─────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
     ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
     │  Content Layer  │ │  Design Layer   │ │  Code Layer     │
     │  • Problem      │ │  • Style select │ │  • PptxGenJS    │
     │  • Solution     │ │  • Color theme  │ │  • React+ Vite  │
     │  • Market       │ │  • Typography   │ │  • Marp         │
     │  • Traction     │ │  • Layout grid  │ │  • HTML preview │
     │  • Team         │ │  • Icon system  │ │                 │
     └────────────────┘ └────────────────┘ └────────────────┘
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                        ┌────────▼─────────┐
                        │  Output Formats   │
                        │  .pptx │ .html   │
                        │  .md (Marp)      │
                        └──────────────────┘
```

---

## 📊 Demo: Create a Pitch Deck

```bash
$ yc-pitch-deck-max create "BrandVirality"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YC Pitch Deck MAX — Builder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Running 10-question founder interview...
✅ Interview complete (2 minutes)

Identifying 3 vertebrae...
✅ Narrative structure built

Design style: YC-Classic (Klein Blue #002FA7)
✅ Style applied

Generating 12 slides...
  ✅ 1. Title — BrandVirality
  ✅ 2. Problem — Businesses invisible in AI search
  ✅ 3. Solution — AI visibility SaaS platform
  ✅ 4. Why Now — LLM adoption + $850M GEO market
  ✅ 5. Market Size — $2.3B TAM
  ✅ 6. Product — Dashboard, audit, monitor
  ✅ 7. Traction — 19 OSS repos, 85/100 avg score
  ✅ 8. Business Model — SaaS tiers
  ✅ 9. Competition — Unique GEO focus
  ✅ 10. Team — Jose Zuma, Expert in AI Visibility
  ✅ 11. Financials — Capital-efficient
  ✅ 12. Ask — $500K seed

Output: pitch-deck-bv.pptx (PPTX)
        pitch-deck-bv.html (HTML preview)
        pitch-deck-bv.md (Marp slides)

To preview: yc-pitch-deck-max preview pitch-deck-bv.html
```

---

## 👨‍💻 Author

**Jose Zuma** — [GitHub](https://github.com/josezuma)

## 📄 License

[MIT](LICENSE) © 2026 Jose Zuma
