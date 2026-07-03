# https://www.codewars.com/kata/54b724efac3d5402db00065e
# --------------------------------- SOLUTION --------------------------------- #
MORSE_CODE = {
    # Letters
    'A': '.-',      'B': '-...',    'C': '-.-.',    'D': '-..',
    'E': '.',       'F': '..-.',    'G': '--.',     'H': '....',
    'I': '..',      'J': '.---',    'K': '-.-',     'L': '.-..',
    'M': '--',      'N': '-.',      'O': '---',     'P': '.--.',
    'Q': '--.-',    'R': '.-.',     'S': '...',     'T': '-',
    'U': '..-',     'V': '...-',    'W': '.--',     'X': '-..-',
    'Y': '-.--',    'Z': '--..',

    # Digits
    '0': '-----',   '1': '.----',   '2': '..---',   '3': '...--',
    '4': '....-',   '5': '.....',   '6': '-....',   '7': '--...',
    '8': '---..',   '9': '----.',

    # Punctuation
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',

    'SOS': '...---...',
}


# If you need to decode Morse to letters, invert the dictionary:
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def decode_morse(morse_code):
    # you can use the preloaded MORSE_CODE dictionary:
    # letter = MORSE_CODE[morse]
    # For example:
    #   MORSE_CODE['.-'] = 'A'
    #   MORSE_CODE['--...'] = '7'
    #   MORSE_CODE['...-..-'] = '$'
    out = []
    space_cnt = 0
    morse_code = morse_code.strip()
    for c in morse_code.split(' '):
        if c == '' and space_cnt == 1:
            out.append(' ')
        elif c == '':
            space_cnt += 1
        else:
            out.append(REVERSE_MORSE[c])
            space_cnt = 0

    return ''.join(out)

# 2nd way
def decode_morse(morse_code):
    # 1. Clean leading/trailing spaces
    # 2. Split by triple-space to isolate words
    words = morse_code.strip().split('   ')
    
    # 3. For each word, split by single-space to isolate characters and translate
    decoded_words = [
        "".join(MORSE_CODE[char] for char in word.split(' '))
        for word in words
    ]
    
    # 4. Join words back together with a single space
    return " ".join(decoded_words)

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(decode_morse('   ...---...'), 'SOS')
