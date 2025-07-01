alphabet = "abcdefghijklmnopqrstuvwxyz"
def encrypt(plain, shift):
    plain = plain.lower()
    out = ""
    for let in plain:
        if (let in alphabet):
            out = out + alphabet[(alphabet.index(let) + shift) % 26]

    return out

def decrypt(cipher, shift):
    out = ""
    for char in cipher:
        if (char in alphabet):
            out = out + alphabet[(alphabet.index(char) - shift) % 26]
    return out

def bruteForce(cipher):
    for i in range(26):
        print(f"Shift: {i} | Decrypted message: {decrypt(cipher, i)}");
    print("Done\n")

plain = "Hello, this is a test to see if the caesar cipher works."
inp = 0
while (inp != -1):
    print("Enter 1 to encryp, 0 to decrypt, 2 to brute force a message or -1 to exit")
    inp = int(input("> "))
    print(inp)
    if (inp == 1):
        print("Enter your message: ")
        plain = input("> ")
        print("Enter shift value: ")
        shift = eval(input("> "))
        cipher = encrypt(plain, shift)
        print(cipher)
    elif (inp == 0):
        print("Enter ciphertext: ")
        cipher = input("> ")
        print("Enter shift value: ")
        shift = eval(input("> "))
        out = decrypt(cipher, shift)
        print(f"Decrypted message: {out}")
    elif (inp == 2):
        print("Enter ciphertext: ")
        cipher = input("> ")
        bruteForce(cipher)
    elif (inp == -1):
        break;
    else:
        print("Please enter a valid input!")

# bruteForce(cipher)
