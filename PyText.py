# Import Modules

import tkinter
import sys
from Crypto.Cipher import AES

# Initialization
version = sys.version   # To select the module import based on python version
key = b'\xea8n\x82\n\x1b\xe8\xb7_1\xab\xad\xafr\xb74'   # Random key - It is now a constant in the first version (To replace with on the fly keys)
AES_block_size = 16
cipher = AES.new(key) # Generate Cipher

# File Dialog Import module
if '2.7' in version:
    from Tkinter import *
    import tkFileDialog
elif '3.6' in version or '3.4' in version:
    from tkinter import *
    import tkinter.tkFileDialog

# Class definition
class FileEncrypt:
    def pad(self, filecontents):
        global AES_block_size
        return (filecontents + (AES_block_size - len(filecontents))% AES_block_size *'{')
    def encrypt(self, plaintext):
        global cipher
        return cipher.encrypt(plaintext)
    def decrypt(self, ciphertext):
        global cipher
        decrypted_text = cipher.decrypt(ciphertext).decode('utf-8')
        count_pad = decrypted_text.count('{')
        return decrypted_text[:len(decrypted_text)-count_pad]
# External methods definition
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    obj = FileEncrypt()
    plaintext = obj.pad(t)
    encrypted_text = obj.encrypt(plaintext)
    savelocation = tkFileDialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(encrypted_text)
    file1.close()

def openfile():
    global text
    obj2 = FileEncrypt()
    openlocation = tkFileDialog.askopenfile()
    decrypted = obj2.decrypt(openlocation.read())
    text.insert(INSERT, decrypted)

# Main function
def main():
    root = Tk("Text Editor")
    global text
    text = Text(root)
    text.grid()
    button = Button(root, text='Save',command=saveas)
    button_open = Button(root, text='Open',command=openfile)
    button.grid()
    button_open.grid()
    root.mainloop()
    root.lift()

if __name__ == '__main__':
    main()
