BRAILLE_LETTERS = {
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'm': '⠍',
    'n': '⠝',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'y': '⠽',
    'z': '⠵'
}


BRAILLE_NUMBERS = {
    '1': '⠼⠁',
    '2': '⠼⠃',
    '3': '⠼⠉',
    '4': '⠼⠙',
    '5': '⠼⠑',
    '6': '⠼⠋',
    '7': '⠼⠛',
    '8': '⠼⠓',
    '9': '⠼⠊',
    '0': '⠼⠚'
}


BRAILLE_PUNCTUATION = {
    ' ': ' ',
    ',': '⠂',
    ';': '⠆',
    ':': '⠒',
    '.': '⠲',
    '!': '⠖',
    '?': '⠦',
    "'": '⠄',
    '-': '⠤',
    '(': '⠷',
    ')': '⠾',
    '"': '⠶',
    '/': '⠌'
}


CAPITAL_SIGN = '⠠'


def text_to_braille(text):

    braille = ""

    number_mode = False

    for char in text:

        lower_char = char.lower()

        if char.isupper() and lower_char in BRAILLE_LETTERS:
            braille += CAPITAL_SIGN

        if char.isdigit():

            if not number_mode:
                braille += BRAILLE_NUMBERS[char]
                number_mode = True
            else:
                braille += BRAILLE_NUMBERS[char]

            continue

        number_mode = False

        if lower_char in BRAILLE_LETTERS:

            braille += BRAILLE_LETTERS[lower_char]

        elif char in BRAILLE_PUNCTUATION:

            braille += BRAILLE_PUNCTUATION[char]

        else:

            braille += char

    return braille
