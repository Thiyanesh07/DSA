# Count frequency of each character in a string

def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


text = input()
print("Input String:", text)
print("Character Frequency:", char_frequency(text))
