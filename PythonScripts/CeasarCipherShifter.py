import string

plaintext = 'abcdefghijklmnopqrstuvwxyz'
shift = -6

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
    
def freq(plaintext):
    count = dict.fromkeys(string.ascii_lowercase,0)
    for ch in plaintext:
        count[ch] += 1
    return count