def separate_string(s): #function to seperate the number and letters in a string 
  
    numbers = "" # string to store the numbers
    letters = "" # string to store the letters
    for char in s:
        if char.isdigit():
            numbers += char #seperate numbers
        else:
            letters += char #seperate letters
    return numbers, letters

def convert_to_ascii(string, n_number):

    #Convert characters to ASCII code decimal values
    ascii_value = [] #list for ascii values
    for char in string:
        if n_number and int(char) % 2 == 0: #check if its number AND even
            ascii_value.append(ord(char)) # convert number to ascii
        elif not n_number and char.isupper(): #check whether if its uppercase
            ascii_value.append(ord(char)) #convert letter to ascii
    return ascii_value

def decrypt_cryptogram(cryptogram, shift_key):
    #Decrypt cryptogram with given shift key
    decrypted_out = ""
    for char in cryptogram:
        if char.isalpha(): #check if a character is a letter
            decrypted_out += chr((ord(char) - shift_key - 65) % 26 + 65) #shift character using modulo 26
        else:
            decrypted_out += char #leave out non-letter characters
    return decrypted_out

# seperate strings and convert to ASCII
s = "56aAww1984skt235270aYmn145ss785fsq31D0"
number_string, letter_string = separate_string(s)
print("Letter string Output:", letter_string)
print("Number string Output:", number_string)
print("Even numbers to ASCII Output:", convert_to_ascii(number_string, True))
print("Upper-Case letters to ASCII Output:", convert_to_ascii(letter_string, False))

# Decrypt cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF VNZ BHG BS PBAGEBYNAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
for shift_key in range(26):
    decrypted_text = decrypt_cryptogram(cryptogram, shift_key)
    print(f"Example {shift_key}: If ciphered quote is {cryptogram}, and 's' is {shift_key}, the the original quote is {decrypted_text}")

#Correct Shift Code is 13
#The Original quote is "IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES IAM OUT OF CONTROLANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELLDONT DESERVE ME AT MY BEST MARILYN MONROE"
