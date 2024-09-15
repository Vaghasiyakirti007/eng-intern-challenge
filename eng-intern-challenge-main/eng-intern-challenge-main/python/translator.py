
import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O.OO..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O.OOO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO..', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O.OOOO', ' ': '......', '0': '.O....', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O.OO..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...'
}

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O.OO..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O.OOO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO..': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O.OOOO': 'z', '......': ' ', '.O....': '0', 'O.....': '1', 'O.O...': '2',
    'OO....': '3', 'OO.O..': '4', 'O.OO..': '5', 'OOO...': '6', 'OOOO..': '7',
    'O.OO..': '8', '.OO...': '9'
}

def braille_to_english(braille):
    return ''.join(braille_to_english.get(b, '?') for b in braille.split())

def english_to_braille(text):
    return ' '.join(braille_alphabet.get(c, '?') for c in text.lower())

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    is_braille = all(c in 'O. ' for c in input_text)

    if is_braille:
        result = braille_to_english(input_text)
    else:
        result = english_to_braille(input_text)

    print(result)
