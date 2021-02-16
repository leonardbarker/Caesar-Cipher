import csv

from inputValidation import validate, yes_or_no


def cipher(mode, message, key):
    """ Encrypts and decrypts
    Mode E - Encrypts, enter plaintext and key - returns ciphertext
    Mode D - Decrypts, enter ciphertext and key - returns plaintext"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    if mode == "E":
        cipher_text = ""
        for letter in message:
            if letter == " ":
                cipher_text += letter
            else:
                cipher_text += (alphabet[alphabet.find(letter) + key])
        print(f'\nEncrypting with key: {key}\n'
              f'............................\n'
              f'Plaintext:  {message}\n'
              f'Ciphertext: {cipher_text}\n')
        return cipher_text
    else:
        plain_text = ""
        for letter in message:
            if letter == " ":
                plain_text += letter
            else:
                plain_text += (alphabet[alphabet.rfind(letter) - key])
        if mode == 'D':
            print(f'\nDecrypting with key: {key}\n'
                  f'............................\n'
                  f'Ciphertext: {message}\n'
                  f'Plaintext:  {plain_text}')
        return plain_text


def decipher(message):
    """ Iterates through a list of common english words to find a match in the plaintext
    When a match is found, user is asked if the phrase makes sense, if not - continue...
    Success in matching returns plaintext and key
    Failure to match returns a dictionary with keys and guesses at plain text
    from which you should be able to discern the key"""
    print("\nDeciphering...")
    guesses = {}
    for i in range(26):
        guess = cipher('C', message, i)
        guesses[i] = guess
        word = guess.split(' ')
        checked = []
        with open('commonwords.csv') as words:
            reader = csv.reader(words)
            for line in reader:
                formatted_line = str(line).replace("'", '').replace('[', '').replace(']', '').upper()
                if formatted_line in word:
                    if guess not in checked:
                        print(f'Match detected. \nPlaintext contains: {formatted_line}.\nKey may be {i}\n')
                        y_or_n = yes_or_no(f'Is "{guess}" a word?')
                        checked.append(guess)
                        if y_or_n == 'Y':
                            print(f'\nMessage deciphered with key {i}:\n'
                                  f'................................\n'
                                  f'Ciphertext: {message}\n'
                                  f'Plaintext:  {guess}')
                            return None
                        else:
                            print("\nDeciphering...")
    print(f"No English word matches found for ciphertext {message}.\n"
          f"Iterations of ciphertext: \n"
          f"--------------------------------------------\n"
          f"Key{'':10}Guess")
    for k, v in guesses.items():
        print(f'{str(k).ljust(13, " ")}{v}')
    yes_or_no2 = yes_or_no("Are any of the permutations above a readable message? [Y] / [N]")
    if yes_or_no2 == 'Y':
        learned_key = validate('Enter key: ', "I")
        cipher('D', message, learned_key)
    else:
        print("\nThe ciphertext could not be deciphered...\n"
              "There may be spelling errors or it does not appear to have been encrypted with the Caesar Cipher.\n"
              "If plaintext is known, check for spelling errors\n")
