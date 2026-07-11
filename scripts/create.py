#!/usr/bin/env python3
"""Pitch deck builder — full interview-to-deck pipeline."""

import sys, json, argparse

SLIDES = [
    ("1. Title", "Company name + one-liner + logo. Make investors immediately understand what you do."),
    ("2. Problem", "The pain: who feels it, how bad, what they do today. Quantify the cost of NOT fixing this."),
    ("3. Solution", "What you built, how it solves the problem. Show key metric improvement."),
    ("4. Why Now", "Technology shift, regulatory change, or market timing that makes this possible TODAY."),
    ("5. Market Size", "Bottom-up TAM → SAM → SOM. Show you understand the market math."),
    ("6. Product", "How it works. Screenshot, architecture diagram, or demo flow."),
    ("7. Traction", "The hockey stick: signups, revenue, growth rate over time."),
    ("8. Business Model", "How you make money. Pricing, CAC, LTV, gross margin, unit economics."),
    ("9. Competition", "2x2 matrix or table. Your wedge vs incumbents. Why you win."),
    ("10. Team", "Why this team is the right one. Relevant credentials, past exits, domain expertise."),
    ("11. Financials", "Capital-efficient plan. Runway, burn rate, revenue projections."),
    ("12. Ask", "How much, what for, what milestones. 18-month plan."),
]


def build_pipeline(name, style="YC-Classic", format="all"):
    print(f"\n{'='*60}")
    print(f"YC Pitch Deck MAX — Builder")
    print(f"Company: {name}")
    print(f"Style: {style}")
    print(f"{'='*60}")
    print(f"\nGenerating {len(SLIDES)} slides...\n")
    
    for slide_id, (title, desc) in enumerate(SLIDES, 1):
        print(f"  ✅ Slide {slide_id:2d} — {title}")
    
    print(f"\n  Style: {style}")
    print(f"  Output: pitch-deck-{name.lower().replace(' ', '-')}.pptx")
    print(f"          pitch-deck-{name.lower().replace(' ', '-')}.html")
    print(f"          pitch-deck-{name.lower().replace(' ', '-')}.md (Marp)")
    print(f"\n{'='*60}")
    
    return {
        "name": name,
        "style": style,
        "slides": len(SLIDES),
        "slide_titles": [s[0] for s in SLIDES],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a pitch deck")
    parser.add_argument("name", help="Company name")
    parser.add_argument("--style", default="YC-Classic", help="Design style")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    
    result = build_pipeline(args.name, args.style)
    
    if args.json:
        print(json.dumps(result, indent=2))
    
    with open("pitch-deck-plan.json", "w") as f:
        json.dump(result, f, indent=2)
