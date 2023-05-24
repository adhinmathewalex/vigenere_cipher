from tkinter import *
from tkinter import messagebox
import base64
import os
import re


def vigenere_cipher_encrypt(plaintext, key):
    # Encryption
    plaintext = re.sub(r"[^a-zA-Z]+", "", plaintext)  # Keep only alphabetic letters
    key = re.sub(r"[^a-zA-Z]+", "", key)  # Keep only alphabetic letters
    ciphertext = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        char = char.upper()
        key_char = key[i % key_length].upper()
        if char.isalpha():
            encrypted_char = chr((ord(char) + ord(key_char) - 2 * ord("A")) % 26 + ord("A"))
            ciphertext += encrypted_char
    return ciphertext


def vigenere_cipher_decrypt(ciphertext, key):
    # Decryption
    ciphertext = re.sub(r"[^a-zA-Z]+", "", ciphertext)  # Keep only alphabetic letters
    key = re.sub(r"[^a-zA-Z]+", "", key)  # Keep only alphabetic letters
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        char = char.upper()
        key_char = key[i % key_length].upper()
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord(key_char) + 26) % 26 + ord("A"))
            plaintext += decrypted_char
    return plaintext


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        key = key_entry.get()

        encrypted_text = vigenere_cipher_encrypt(message, key)

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_text)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        key = key_entry.get()

        decrypted_text = vigenere_cipher_decrypt(message, key)

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_text)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")


def main_screen():
    global screen
    global code
    global text1
    global key_entry

    screen = Tk()
    screen.geometry("375x398")

    # icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)
        key_entry.delete(0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter the password", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Label(text="Enter  key", fg="black", font=("calibri", 13)).place(x=10, y=240)
    key_entry = Entry(width=19, bd=0, font=("arial", 12))
    key_entry.place(x=10, y=270,width=355,height=20)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=300)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=300)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=350)

    screen.mainloop()

main_screen()

   
