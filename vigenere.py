import itertools
import argparse
import os

ASCII_A = ord('A')

def _offset(char):
        return ord(char.upper()) - ASCII_A

def _caesar_encrypt_char(char, key, decrypt=False):
    if decrypt:
        sign = -1
    else:
        sign = 1

    return chr(ASCII_A + (_offset(char) + sign * key) % 26)

def vigenere_cipher(text, key, decrypt=False):
    key_iter = itertools.cycle(map(_offset, key))

    result = ''
    for char in text:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            lower = char.islower()

            c = _caesar_encrypt_char(char.upper(), next(key_iter), decrypt=decrypt)
            if lower:
                c = c.lower()
            
            result += c
        else:
            result += char
    
    return result

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help='name of the file to be encrypted or decrypted')
    parser.add_argument('key', help='key to the vigenere cipher')
    parser.add_argument('-d', '--decrypt', help='decrypt mode', action='store_true')
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = _parse_args()

    file = args.file_name
    key = args.key
    decrypt = args.decrypt

    file = os.path.abspath(file)
    dir = os.path.dirname(file)

    if not key.isalpha():
        raise ValueError('key must be consisted only with alphabets.')

    if decrypt:
        prefix = 'decrypted_'
    else:
        prefix = 'encrypted_'
    
    with open(file) as f:
        text = f.read()
    
    result = vigenere_cipher(text, key, decrypt=decrypt)

    output_file = os.path.join(dir, prefix + os.path.basename(file))
    with open(output_file, 'w') as f:
        f.write(result)