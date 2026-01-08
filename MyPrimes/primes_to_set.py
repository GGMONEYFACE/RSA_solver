"""primes_set.py

Auto-generated helper that exposes PRIMES as a Python set.
Loads the numbers from the adjacent `primes*.txt` file and parses integers robustly.
"""

import re
from pathlib import Path

__all__ = ["PRIMES1", "PRIMES2", "load_primes_file", "PRIMES", "PrimesCollection"]


def load_primes_file(filename: str = "primes1.txt") -> set:
    """Load integers from the neighboring file and return a set of integers >= 2.

    This is robust to formatting such as commas (e.g. "1,000") since it
    extracts continuous digit runs with a regular expression.
    """
    p = Path(__file__).with_name(filename)
    try:
        text = p.read_text()
    except Exception:
        # Fall back to empty text if file not found
        text = ""

    # Extract continuous digit runs and convert to ints; this avoids treating
    # comma-delimited numbers (like "1,000,000") as a single integer.
    nums = [int(m) for m in re.findall(r"\d+", text)]

    # Keep only values >= 2 (primes start at 2)
    return {n for n in nums if n >= 2}


# Preload the common files for convenience
PRIMES1 = load_primes_file("primes1.txt")
PRIMES2 = load_primes_file("primes2.txt")

from functools import lru_cache


@lru_cache(maxsize=None)
def _cached_load_file(filename: str) -> set:
    """Cached wrapper around :func:`load_primes_file`."""
    return load_primes_file(filename)


class PrimesCollection:
    """A lazy collection of prime sets accessible by index.

    Example:
        PRIMES[1]  -> loads and returns the set from 'primes1.txt'
        PRIMES[2]  -> loads 'primes2.txt'

    The collection caches loaded files for fast subsequent access.
    """

    def __init__(self, template: str = "primes{}.txt", max_index: int = 50):
        self.template = template
        self.max_index = int(max_index)

    def __getitem__(self, idx: int) -> set:
        if not (1 <= idx <= self.max_index):
            raise IndexError("index out of range")
        fn = self.template.format(idx)
        return _cached_load_file(fn)

    def keys(self):
        return range(1, self.max_index + 1)


# Expose a convenience collection preconfigured for up to 50 files
PRIMES = PrimesCollection(max_index=50)


if __name__ == "__main__":
    import sys

    # Allow optional filename on the command line; defaults to primes1.txt
    fn = sys.argv[1] if len(sys.argv) > 1 else "primes1.txt"
    primes = load_primes_file(fn)
    print(f"Loaded {len(primes)} primes from {Path(__file__).with_name(fn)}")
    # Show a small preview
    print(sorted(primes)[:10])
