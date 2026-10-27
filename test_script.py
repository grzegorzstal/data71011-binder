
"""
word_counter.py - a simple example Python script.
 
Counts how often each word appears in a piece of text and prints
the most common ones. Uses only the standard library.
 
Usage:
    python word_counter.py                # uses the built-in sample text
    python word_counter.py myfile.txt     # analyses a text file
    python word_counter.py myfile.txt 5   # show the top 5 words
"""
 
import re
import sys
from collections import Counter
 
SAMPLE_TEXT = """
Data science is about asking good questions of data.
Good questions lead to good analysis, and good analysis
leads to better decisions. Data is only useful when it
helps people understand something new.
"""
 
# Common words that don't tell us much on their own
STOP_WORDS = {"is", "of", "to", "and", "it", "the", "a", "when", "about", "only"}
 
 
def clean_words(text):
    """Lowercase the text and split it into a list of words."""
    return re.findall(r"[a-z']+", text.lower())
 
 
def count_words(words, ignore=STOP_WORDS):
    """Return a Counter of words, skipping any in the ignore set."""
    return Counter(word for word in words if word not in ignore)
 
 
def print_report(counts, top_n):
    """Print the most common words with a simple text bar chart."""
    total = sum(counts.values())
    print(f"Total words counted: {total}")
    print(f"Unique words:        {len(counts)}\n")
    print(f"Top {top_n} words:")
    for word, count in counts.most_common(top_n):
        bar = "#" * count
        print(f"  {word:<12} {count:>3}  {bar}")
 
 
def main():
    # Read text from a file if one was given, otherwise use the sample
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = SAMPLE_TEXT
 
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
 
    words = clean_words(text)
    counts = count_words(words)
    print_report(counts, top_n)
 
 
if __name__ == "__main__":
    main()
