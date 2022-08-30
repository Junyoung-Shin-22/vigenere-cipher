# vigenere-cipher

## Usage

`$ python vigenere.py [-h] [-d] file_name key`

```
positional arguments:
  file_name      name of the file to be encrypted or decrypted
  key            key to the vigenere cipher

optional arguments:
  -h, --help     show this help message and exit
  -d, --decrypt  decrypt mode
```

## Example

### Plain Text
> test/plaintext.txt
```
Hello, world!
How many programmers does it take to change a light bulb? None, that's a hardware problem.
```

### Encryption
`$ python vigenere.py test/plaintext.txt lemon`

### Output
> test/encrypted_plaintext.txt
```
Sixzb, hsdzq!
Ssi anyc bfbrvmazpve rbpw uh gloq hb nlmbtp e xwtsx niym? Rabr, elmh'f l lmfqheds ccsnzrx.
```

### Decryption
`$ python vigenere.py test/encrypted_plaintext.txt lemon -d`

or

`$ python vigenere.py test/encrypted_plaintext.txt lemon --decrypt`

### Output
> test/decrypted_encrypted_plaintext.txt
```
Hello, world!
How many programmers does it take to change a light bulb? None, that's a hardware problem.
```
