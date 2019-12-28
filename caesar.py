def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for ch in plaintext:
        code = ord(ch)
        if 'a' <= ch < 'x' or 'A' <= ch < 'X':
            code += 3
        elif 'x' <= ch <= 'z' or 'X' <= ch <= 'Z':
            code -= 23
        ciphertext += chr(code)
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for ch in ciphertext:
        code = ord(ch)
        if 'd' <= ch < 'z' or 'D' <= ch < 'Z':
            code -= 3
        elif 'a' <= ch <= 'c' or 'A' <= ch <= 'C':
            code += 23
        plaintext += chr(code)
    return plaintext