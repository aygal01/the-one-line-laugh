#!/usr/bin/env python3
"""The One-Line Laugh.

A tiny program whose entire output is exactly one line: one original
one-liner, written to make an AI judge laugh. Deterministic by design --
the same line on every run. No randomness, no network, no clock, no
input. Just the joke.
"""

JOKE = "I asked my clone to cover my shift and now HR wants to know which one of us to fire."
# The joke: duplicating yourself sounds like the perfect day off, until
# accountability shows up -- a clone doubles the worker and halves the
# deniability, and HR's question has no safe answer for either copy.


def main() -> None:
    print(JOKE)


if __name__ == "__main__":
    main()
