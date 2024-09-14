original_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcongr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

key = 13

#Using the given Encrytion function to create a decryption function by making necessary changes.
# Encryption function used: def encrypt(text, key):
#    encrypted_text = ""
#    for char in text:
#        if char.isalpha():
#            shifted = ord(char) + key #needs to be flipped
#           if char.islower():
#                if shifted > ord('z'): #flip
#                    shifted -= 26
#                elif shifted < ord('a'):
#                    shifted += 26
#            elif char.isupper():
#                if shifted > ord('Z'):
#                    shifted -=26
#                elif shifted < ord('A'):
#                    shifted += 26
#            encrypted_text += chr(shifted)
#        else:
#                encrypted_text += char
#    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""  # Empty string for the decrypted text
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) - key  # Shift the character backward by the key value
            if char.islower():  # If it's a lowercase letter
                if shifted < ord('a'):  # Wrap around if it goes below 'a'
                    shifted += 26
            elif char.isupper():  # If it's an uppercase letter
                if shifted < ord('A'):  # Wrap around if it goes below 'A'
                    shifted += 26
            decrypted_text += chr(shifted)  # Convert the shifted value back to a character and add it to the decrypted text
        else:
            decrypted_text += char  # Non-alphabetic characters are added unchanged
    return decrypted_text

decrypted_code = decrypt(original_code, key)
print("Encrypted Code")
print(original_code)
print("Decrypted Code")
print(decrypted_code)

Final_Code = """
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
        
#Using The provided Logic codes

    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict()

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 'key5' not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
"""

print("Running Final Code!")
exec(Final_Code)
print("Done!")
