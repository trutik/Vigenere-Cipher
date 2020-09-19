import string
import codecs
import pickle
import re

#Create the tableau 'tabula recta'
def create_tables(special_chars=[], alphabet = string.printable):
    alphabet = list(alphabet)
    #Extend alphabet with special characters
    alphabet.extend(special_chars)

    #Length will be used for modulo to represent shifting alphabet
    length = len(alphabet)
    #Create Python Dictionary to represent the table {Key:Value} = {row_char+columnChar: Character}
    encryption_table = {}
    decryption_table = {}
    #Iterate the table and store the mapping
    for row_number, row_char in enumerate(alphabet):
        for col_number, col_char in enumerate(alphabet):
            char = alphabet[(row_number+col_number)%(length)]
            encryption_table[row_char+col_char]=char
            decryption_table[row_char+char]=col_char
    return [encryption_table,decryption_table]

#Encrypt message into ciphertext using key
def encrypt(key,message,table,mode):
    #checks for empty strings
    if message=='':
        print('Message empty, can not encrypt an empty message')
        message = 'empty message'
    if key=='':
        print('Key empty, using default key')
        key='defaultkey' #set default key

    #Serialise the object and then encode to a string for encryption (if mode is 1)
    if mode == 1:
        message = codecs.encode(pickle.dumps(message), "base64").decode()

    message_list = list(message)
    key_list = list(key)
    key_length = len(key)
    ciphertext=''
    counter = 0
    #Retrieve mapping of each character in message and corresponding key character (charAbove)
    for char in message_list:
        charAbove=key_list[counter]
        ciphertext = ciphertext + table[char+charAbove]
        counter = counter + 1
        if counter==key_length:
            counter = 0
    return ciphertext

def decrypt(key,ciphertext,table,mode):
    if key=='':
        print('Key empty, using default key')
        key='defaultkey' #set default key

    ciphertext_list = list(ciphertext)
    key_list = list(key)
    key_length = len(key)
    plaintext=''
    counter =0
    #Retrieve mapping of each character in ciphertext and corresponding key character (charAbove)
    for char in ciphertext_list:
        key_char = key_list[counter]
        plaintext = plaintext + table[key_char+char]
        counter = counter + 1
        if counter==key_length:
            counter = 0

    #If mode is all 1 (for all objects), de-serialise object before returning
    if mode == 1:
        plaintext = pickle.loads(codecs.decode(plaintext.encode(), "base64"))

    return plaintext

#Gets all unique special characters from 'input' argument
def get_special_chars(input):
    alphabet=string.printable
    alphabetList= list(alphabet)
    #Remove characters already in alphabet and duplicates from input
    special_characters = list()
    for char in input:
        if (char in alphabet) or (char in special_characters):
            #Dont add to special_characters
            pass
        else:
            special_characters.append(char)
    return special_characters

def run_vigenere():
    user_input = input('Enter Special Chars \n')
    special_chars = get_special_chars(user_input)
    tables = create_tables(special_chars)
    table_enc = tables[0]
    table_dec = tables[1]
    while True:
        user_msg = input('Enter message \n')
        user_key = input('Enter key \n')
        ciphertext = encrypt(user_key,user_msg,table_enc,1)
        print('Ciphertext: '+ciphertext)
        plaintext = decrypt(user_key,ciphertext,table_dec,1)
        print('Plaintext: '+plaintext)
