import itertools
import string

def letter_combos():
    wombo_combo = itertools.product(string.ascii_lowercase, string.ascii_lowercase, string.ascii_lowercase, string.ascii_lowercase)
    return list(wombo_combo)