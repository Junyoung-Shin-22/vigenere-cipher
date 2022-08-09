import itertools
import argparse

ASCII_A = ord('A')

def _check_char_range(func):
    def inner(char, *args):
        assert isinstance(char, str) and len(char) == 1 and ord(char) in range(ASCII_A, ASCII_A + 26)

        return func(char, *args)
    
    return inner

@_check_char_range
def _caesar_encrypt_char(char, key):
    return chr(ASCII_A + (ord(char) - ASCII_A + key) % 26)

@_check_char_range
def _char_to_offset(char):
    return ord(char) - ASCII_A

def vigenere_cipher(text, key, decrypt=False):
    """
    >>> vigenere_cipher('ATTACKATDAWN', 'LEMON') == 'LXFOPVEFRNHR'
    True

    >>> vigenere_cipher('LXFOPVEFRNHR', 'LEMON', True) == 'ATTACKATDAWN'
    True
    """
    sign = -1 if decrypt else 1
    key_iter = itertools.cycle(map(_char_to_offset, key))

    result = ''
    for char in text:
        result += _caesar_encrypt_char(char, sign * next(key_iter))
    
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help='name of the file to be encrypted or decrypted')
    parser.add_argument('key', help='key to the vigenere cipher')
    parser.add_argument('-d', '--decrypt', help='decrypt mode', action='store_true')
    args = parser.parse_args()

    file = args.file_name
    key = args.key
    decrypt = args.decrypt

    if decrypt:
        prefix = 'decrypted_'
    else:
        prefix = 'encrypted_'
    
    with open(file) as f:
        text = f.read()
    
    result = vigenere_cipher(text, key, decrypt=decrypt)

    with open(prefix+file, 'w') as f:
        f.write(result)