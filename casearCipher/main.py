from cipher import cipher, decipher
from inputValidation import validate, yes_or_no
# This code has three functions.
# 1. Encrypting a string of alphabetic plaintext with the Caeser Cipher and a chosen int key >26
# 2. Decrypting a string of alphabetic ciphertext with the Caeser Cipher and a chosen int key >26
# 3. Deciphering a string of unknown ciphertext
# -------------Let-The-Insecure-Ciphering-Begin--------------------------------
end = "Y"
print("************************\n"
      "Welcome to Caeser Cipher\n"
      "************************")
print("\n************IMPORTANT************\n"
      "This cipher is not secure.\n"
      "Never encrypting sensitive data with this cipher.\n")

while end == "Y":
    print("Please enter your mode of choice.")
    mode = input("[E]ncrypt, [D]ecrypt or de[C]ipher: ")[0].upper()
    while mode not in ('E', 'D', 'C'):
        mode = input("\n.............\nInvalid input.\n"
                     "[E] for encrypt, [D] for Decrypt or [C]for deCipher: ").upper()
    if mode != 'C':
        pt = validate("Enter Message (Letters only): ", "A")
        key = validate("Enter key (number under 26): ", "I")
        cipher(mode, pt, key)
    else:
        ct = input("Enter ciphertext message: ").upper()
        decipher(ct)
    print("Process completed.\n")
    a = yes_or_no("To continue and perform another function enter [Y]\n"
                  "To exit enter [N]\n")
    if a == 'N':
        print("\n\nIMPORTANT!!!\n"
              "This cipher is not secure.\n"
              "Never encrypting sensitive data with this cipher.\n"
              "Exiting program...")
        break
    print("\n\nRestarting...\n.............\n\n")
    end = a
