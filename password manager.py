import os
from cryptography.fernet import Fernet

def load_or_create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    
    with open("key.key", "rb") as key_file:
        return key_file.read()

key = load_or_create_key()
fer = Fernet(key)

def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords saved yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if not data or "|" not in data:
                continue
            user, passw = data.split("|")
            try:
                decrypted_pass = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", decrypted_pass)
            except Exception:
                print("User:", user, "| Password: [Error decrypting]")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")


    with open('passwords.txt', 'a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
