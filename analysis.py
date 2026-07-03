import re
from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def count_characters_no_spaces(text):
    return len(text.replace(" ", ""))

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def count_paragraphs(text):
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])

def count_syllables(text):
    words = text.split()
    syllable_count = 0
    for word in words:
        word = word.lower()
        vowel_pattern = re.compile(r'[aeiou]+')
        syllable_count += len(vowel_pattern.findall(word))
    return syllable_count

def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))

def find_repeated_words(text):
    words = text.lower().split()
    word_count = Counter(words)
    return {word: count for word, count in word_count.items() if count > 1}

def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)

def average_words_per_sentence(text):
    words = count_words(text)
    sentences = count_sentences(text)
    if sentences == 0:
        return 0
    return round(words / sentences, 2)

def find_longest_words(text, count=5):
    words = text.split()
    if not words:
        return []
    sorted_words = sorted(set(words), key=len, reverse=True)
    return sorted_words[:count]

def find_shortest_words(text, count=5):
    words = text.split()
    if not words:
        return []
    sorted_words = sorted(set(words), key=len)
    return sorted_words[:count]

def count_special_characters(text):
    special_chars = re.findall(r'[^a-zA-Z0-9\s]', text)
    return len(special_chars)

def count_numbers(text):
    numbers = re.findall(r'\d+', text)
    return len(numbers)

def word_frequency(text):
    words = text.lower().split()
    return Counter(words)

def extract_nouns(text):
    words = text.split()
    nouns = [word for word in words if word[0].isupper() and word not in ['I', 'You', 'He', 'She', 'We', 'They']]
    return nouns if nouns else ["No nouns detected"]

def extract_verbs(text):
    words = text.split()
    verbs = [word for word in words if word.lower().endswith(('ing', 'ed', 'es', 'en'))]
    return verbs if verbs else ["No verbs detected"]

def extract_adjectives(text):
    words = text.split()
    adjectives = [word for word in words if word.lower().endswith(('ous', 'ful', 'able', 'ible', 'al', 'y'))]
    return adjectives if adjectives else ["No adjectives detected"]

def extract_adverbs(text):
    words = text.split()
    adverbs = [word for word in words if word.lower().endswith('ly')]
    return adverbs if adverbs else ["No adverbs detected"]

def readability_score(text):
    words = text.split()
    sentences = count_sentences(text)
    syllables = count_syllables(text)
    
    if not words or sentences == 0:
        return 0
    
    score = 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words))
    return round(score, 2)

def full_analysis(text):
    analysis = {
        "Word Count": count_words(text),
        "Character Count": count_characters(text),
        "Characters (no spaces)": count_characters_no_spaces(text),
        "Sentence Count": count_sentences(text),
        "Paragraph Count": count_paragraphs(text),
        "Syllable Count": count_syllables(text),
        "Unique Words": count_unique_words(text),
        "Average Word Length": average_word_length(text),
        "Average Words per Sentence": average_words_per_sentence(text),
        "Special Characters": count_special_characters(text),
        "Numbers Found": count_numbers(text),
        "Repeated Words": find_repeated_words(text),
        "Longest Words": find_longest_words(text, 5),
        "Shortest Words": find_shortest_words(text, 5),
        "Nouns": extract_nouns(text),
        "Verbs": extract_verbs(text),
        "Adjectives": extract_adjectives(text),
        "Adverbs": extract_adverbs(text),
        "Readability Score": readability_score(text),
        "Word Frequency": word_frequency(text)
    }
    return analysis
