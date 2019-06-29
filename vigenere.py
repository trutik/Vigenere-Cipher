import string
import codecs
import pickle

#Create the tableau 'tabula recta'
def createTables(specialChars):
    specialCharsString = ''.join(specialChars)
    alphabet=string.printable
    # alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = list(alphabet)
    #Extend alphabet with special characters
    alphabet.extend(specialChars)

    #Set alphabet for easy testing if specialChars is TEST
    if specialCharsString=='TEST':
        alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet = list(alphabet)

    #Length will be used for modulo to represent shifting alphabet
    length = len(alphabet)
    #Create Python Dictionary to represent the table {Key:Value} = {rowChar+columnChar: Character}
    tableEnc = {}
    tableDec = {}
    #Iterate the table and store the mapping
    for rowNumber, rowChar in enumerate(alphabet):
        for colNumber, colChar in enumerate(alphabet):
            char = alphabet[(rowNumber+colNumber)%(length)]
            tableEnc[rowChar+colChar]=char
            tableDec[rowChar+char]=colChar
    return [tableEnc,tableDec]

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

    messageList = list(message)
    keyList = list(key)
    keyLength = len(key)
    ciphertext=''
    counter = 0
    #Retrieve mapping of each character in message and corresponding key character (charAbove)
    for char in messageList:
        charAbove=keyList[counter]
        ciphertext = ciphertext + table[char+charAbove]
        counter = counter + 1
        if counter==keyLength:
            counter = 0
    return ciphertext

def decrypt(key,ciphertext,table,mode):
    if key=='':
        print('Key empty, using default key')
        key='defaultkey' #set default key

    ciphertextList = list(ciphertext)
    keyList = list(key)
    keyLength = len(key)
    plaintext=''
    counter =0
    #Retrieve mapping of each character in ciphertext and corresponding key character (charAbove)
    for char in ciphertextList:
        keyChar = keyList[counter]
        plaintext = plaintext + table[keyChar+char]
        counter = counter + 1
        if counter==keyLength:
            counter = 0

    #If mode is all 1 (for all objects), de-serialise object before returning
    if mode == 1:
        plaintext = pickle.loads(codecs.decode(plaintext.encode(), "base64"))

    return plaintext

#Gets all unique special characters from 'input' argument
def getSpecialChars(input):
    alphabet=string.printable
    alphabetList= list(alphabet)
    #Remove characters already in alphabet and duplicates from input
    specialCharacters = list()
    for char in input:
        if (char in alphabet) or (char in specialCharacters):
            #Dont add to specialCharacters
            pass
        else:
            specialCharacters.append(char)
    return specialCharacters

def prototype():
    userInput = input('Enter Special Chars \n')
    specialChars = getSpecialChars(userInput)
    tables = createTables(specialChars)
    tableEnc = tables[0]
    tableDec = tables[1]
    while True:
        userMsg = input('Enter message \n')
        userKey = input('Enter key \n')
        ciphertext = encrypt(userKey,userMsg,tableEnc,1)
        print('Ciphertext: '+ciphertext)
        plaintext = decrypt(userKey,ciphertext,tableDec,1)
        print('Plaintext: '+plaintext)
