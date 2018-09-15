# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/jZ4ZSiGohzFTeg4yb
def willYou(young, beautiful, loved):
    # Mary believes a person is only loved iff they are young and beautiful.
    young_and_beautiful = young and beautiful
    # Check if there's any case that contradicts Mary's belief.
    return (not loved and young_and_beautiful) or (loved and not young_and_beautiful)
