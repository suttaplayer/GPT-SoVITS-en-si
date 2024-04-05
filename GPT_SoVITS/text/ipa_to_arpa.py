import sys

def ipa_to_arpabet(ipa_text):
    arpabet_mapping = {
        "a": "AA",
        "ɑ": "AA",
        "æ": "AE",
        "b": "B",
        "tʃ": "CH",
        "d": "D",
        "ð": "DH",
        "e": "EH",
        "ə": "AH",
        "ɛ": "EH",
        "ɪ": "IH",
        "i": "IY",
        "f": "F",
        "ɡ": "G",
        "h": "HH",
        "ʤ": "JH",
        "ʒ": "ZH",
        "k": "K",
        "l": "L",
        "m": "M",
        "n": "N",
        "ŋ": "NG",
        "oʊ": "OW",
        "ɔ": "AO",
        "ɹ": "R",
        "ɾ": "T",
        "ʃ": "SH",
        "s": "S",
        "t": "T",
        "θ": "TH",
        "u": "UW",
        "ʊ": "UH",
        "v": "V",
        "w": "W",
        "j": "Y",
        "z": "Z",
        "ʔ": "AH",
        "ˈ": "",  # Remove primary stress marker
        "ˌ": "",  # Remove secondary stress marker
        ".": ""   # Remove other non-alphabetic characters
    }

    arpabet_text = ""
    ipa_symbols = ipa_text.split()
    for symbol in ipa_symbols:
        arpabet_text += arpabet_mapping.get(symbol, "")

    return arpabet_text

# Example usage:
if __name__ == "__main__":
    ipa_text = sys.argv[1]
    arpabet_text = ipa_to_arpabet(ipa_text)
    print(arpabet_text) 
