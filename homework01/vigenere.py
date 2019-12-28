def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    key_len = len(keyword)
    plaintext_len = len(plaintext)
    while key_len != plaintext_len:
        keyword += keyword
        key_len = len(keyword)
        if key_len > plaintext_len:
            keyword = keyword[:plaintext_len]
            key_len = len(keyword)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_len]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    key_len = len(keyword)
    ciphertext_len = len(ciphertext)
    while key_len != ciphertext_len:
        keyword += keyword
        key_len = len(keyword)
        if key_len > ciphertext_len:
            keyword = keyword[:ciphertext_len]
            key_len = len(keyword)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_len] + 26) % 26
        plaintext += chr(value + 65)
    return plaintext
