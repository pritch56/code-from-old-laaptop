import base64
import pyperclip
import os

def encript(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i])+ord(key_c))%256))
    encription = base64.urlsafe_b64encode("".join(enc).encode()).decode()

    return(encription)

def decript(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256+ord(message[i])-ord(key_c))%256))
        
    return(str(''.join(dec)))

key = input('enter key: ')
message = input('enter message: ')

encript_decript = input('would you like to decript or encript (e/d)? ')
if encript_decript == 'e':
    pyperclip.copy(encript(key, message))
else:
    pyperclip.copy(str(decript(key, message)))

print('Coppied to clipboard! ')