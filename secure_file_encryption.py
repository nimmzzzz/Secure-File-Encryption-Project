import os
from tkinter import *
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to generate and save a key
def generate_key():
    key = get_random_bytes(16)  # 128-bit AES key
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load an existing key
def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        return key
    else:
        return generate_key()

# Encrypt the file
def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select file to encrypt")
    if not file_path:
        return

    key = load_key()
    cipher = AES.new(key, AES.MODE_EAX)

    with open(file_path, "rb") as file:
        file_data = file.read()

    ciphertext, tag = cipher.encrypt_and_digest(file_data)

    encrypted_file = file_path + ".enc"
    with open(encrypted_file, "wb") as file_out:
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

    messagebox.showinfo("Success", f"File encrypted successfully:\n{encrypted_file}")

# Decrypt the file
def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select file to decrypt", filetypes=[("Encrypted files", "*.enc")])
    if not file_path:
        return

    key = load_key()
    with open(file_path, "rb") as file_in:
        nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        decrypted_file = file_path.replace(".enc", "_decrypted.txt")
        with open(decrypted_file, "wb") as file_out:
            file_out.write(data)
        messagebox.showinfo("Success", f"File decrypted successfully:\n{decrypted_file}")
    except ValueError:
        messagebox.showerror("Error", "Decryption failed! Invalid key or corrupted file.")

# UI Design
root = Tk()
root.title("🔒 Secure File Encryption & Decryption")
root.geometry("400x250")
root.config(bg="#1e1e2f")

Label(root, text="Secure File Encryption Tool", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white").pack(pady=20)
Button(root, text="Encrypt File", command=encrypt_file, width=20, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)
Button(root, text="Decrypt File", command=decrypt_file, width=20, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=10)
Button(root, text="Exit", command=root.quit, width=20, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()

