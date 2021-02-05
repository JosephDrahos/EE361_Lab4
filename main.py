import palindrome
import transposition
import substitution

str = "this is transposition" #sender generates plaintext
st1 = transposition.scramble2Encrypt(str) #sender generates passkey using scramble2Encrypt (odd characters before even characters)
print("Transposition Cypher encryption of : " + str)
print("Encryption: " + st1)
print("Decryption: " + transposition.scramble2Decrypt(st1)) #receiver decrypts message to recover original plaintext
print()

key = substitution.keyGen() #sender generates key which consists of random characters of the alphabet
print("Generated key for Substitution Cypher: " + key)
print("Substitution Cypher encyption of substitutioncypher: ")
str = "substitutioncypher"
st1 = substitution.substitutionEncrypt(str, key) #Sender encrypts plaintext with generated key
print("Encryption: " + st1)
print("Decryption: " + substitution.substitutionDecrypt(st1, key)) #Receiver decrypts ciphertext and recovers plaintext
print()

str = "substitutioncypher"
passkey = substitution.genKeyFromPass("hello") #Sender generates passkey from the passphrase "hello"
print("Passphrase key for Substitution Cypher:" + passkey)
print("Substitution Cypher with passphrase key encryption of substitutioncypher: ")
st1 = substitution.substitutionEncrypt(str, passkey) #Sender generates ciphertext from provided passkey and the plaintext
print("Encryption: " + st1)
print("Decryption: " + substitution.substitutionDecrypt(st1, passkey)) #Receiver decrypts ciphertext using the passkey generated by the sender - provided passphrase
print()

str = "this is transposition2"
st1 = transposition.scramble2Encrypt2(str) #Sender encrypts message using transposition cipher which separates the string into even and odd characters and generates a ciphertext by printing even characters before odd characters
print("Transposition Cyppher withe evens first of: " + str)
print("Encryption: " + st1)
print("Decryption: " + transposition.scramble2Decrypt2(st1)) #Receiver decrypts cipher text and recovers plaintext
print()

print("Palindrome Function Testing:")
print("Testing madam: ", palindrome.palindromCheck("madam"))
print("Testing nursesrum: ", palindrome.palindromCheck("nursesrun"))
print("Testing a: ", palindrome.palindromCheck("a"))
print("Testing amanaplanacanalpanama: ", palindrome.palindromCheck("amanaplanacanalpanama"))
print("Testing aabb: " , palindrome.palindromCheck("aabb"))