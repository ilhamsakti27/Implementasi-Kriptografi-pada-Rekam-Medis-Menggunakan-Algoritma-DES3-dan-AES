# for FP Kriptogafi

#Import the required Libraries
from tkinter import *
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from hashlib import md5
# import des3_aes_forGUI

#Create an instance of Tkinter frame
root= Tk()

#Set the geometry of Tkinter frame
root.geometry("850x350")

#Initialize a Label to display the User Input
labelTitle=Label(root, text="Implementasi Kriptografi Untuk Rekam Medis \n Dengan Algoritma DES3 dan AES", font=("Courier 22 bold"))
labelTitle.pack(pady=10)

#Create an label widget to for file path
labelFilePath = Label(root, text="File Path : ")
labelFilePath.pack()

#Create an Entry widget to accept User Input for file path
entryFilePath= Entry(root, width= 50)
entryFilePath.focus_set()
entryFilePath.pack()

#Create an label widget to for file path
labelKey = Label(root, text="Key : ")
labelKey.pack()

#Create an Entry widget to accept User Input for file path
entryKey= Entry(root, width= 50)
entryKey.focus_set()
entryKey.pack()


# file_path = entryFilePath.get()
# key = entryKey.get()

# key_hash = md5(key.encode('ascii')).digest() #16-byte key 

# # chiper for DES3
# tdes_key = DES3.adjust_key_parity(key_hash)
# cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')  

# # chiper for AES
# chiperAES = AES.new(tdes_key, AES.MODE_EAX, nonce=b'0')

# def panggil():
#     print("File path " + file_path)
#     print("Key hash " + key)


def encrypt():
    file_path = entryFilePath.get()
    key = entryKey.get()

    key_hash = md5(key.encode('ascii')).digest() #16-byte key 

    # chiper for DES3
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')  

    # chiper for AES
    chiperAES = AES.new(tdes_key, AES.MODE_EAX, nonce=b'0')

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = cipher.encrypt(file_bytes)
        new_file_bytes = chiperAES.encrypt(new_file_bytes)

    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)

def decrypt():
    file_path = entryFilePath.get()
    key = entryKey.get()

    key_hash = md5(key.encode('ascii')).digest() #16-byte key 

    # chiper for DES3
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')  

    # chiper for AES
    chiperAES = AES.new(tdes_key, AES.MODE_EAX, nonce=b'0')

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = cipher.decrypt(file_bytes)
        new_file_bytes = chiperAES.decrypt(new_file_bytes)

    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)


#Create a Button to validate Entry Widget
# ttk.Button(root, text= "Okay",width= 20, command= display_text).pack(pady=20)
encryptButton = Button(root, text= "Encrypt", width=20, command=encrypt)
encryptButton.pack(pady=20)

decryptButton = Button(root, text= "Decrypt", width=20, command=decrypt)
decryptButton.pack(pady=0)


root.mainloop()

