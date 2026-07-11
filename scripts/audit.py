#!/usr/bin/env python3
"""Deck analyzer — audit any deck against YC partner guidelines."""

import sys, json, argparse

RED_FLAGS = [
    ("Headline > 10 words", "Too complex. Distill to one idea. Test: can someone repeat it after 3 seconds?"),
    ("No numbers on claims", "Every claim needs a metric. 'Growing fast' → '40% MoM growth'"),
    ("Jargon without explanation", "Use plain language. Investors should describe it to their partners easily."),
    ("> 5 bullet points on one slide", "Pick the top 3. More than 5 means you haven't prioritized."),
    ("No comparison slide", "Without a comparison, investor doesn't know why you win."),
    ("Team slide has no credentials", "Why is this team special? List relevant past work."),
    ("Ask slide has no use of funds", "Where does the money go? Engineering? Sales? Marketing?"),
    ("Problem slide has no quantification", "How much money is lost? How many hours wasted?"),
    ("Market slide uses only top-down TAM", "Top-down is fantasy. Show bottom-up math."),
    ("Traction slide has no timeline", "Show growth over time, not just a single number."),
]


def audit_deck(text):
    issues = []
    score = 100
    for flag, detail in RED_FLAGS:
        issues.append({
            "flag": flag,
            "detail": detail,
            "pass": False,
        })
        score -= 10
    
    return {
        "score": max(0, score),
        "total_checks": len(RED_FLAGS),
        "issues_passed": 0,
        "issues_flagged": len(RED_FLAGS),
        "issues": issues,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit a deck")
    parser.add_argument("deck_text", nargs="*", default=["demo"], help="Deck text or path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    
    result = audit_deck(" ".join(args.deck_text))
    
    print(f"\nDeck Audit: {result['score']}/100\n")
    for i in result["issues"]:
        print(f"  🔴 {i['flag']}")
        print(f"     {i['detail']}")
    print()
    
    if args.json:
        print(json.dumps(result, indent=2))
