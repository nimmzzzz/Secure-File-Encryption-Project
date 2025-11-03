# 🔒 Secure File Encryption & Decryption using Python (AES)

## Overview
This project securely encrypts and decrypts files using the AES (Advanced Encryption Standard) algorithm.  
It provides a simple graphical interface (Tkinter) to select files for encryption or decryption.
## Features
- AES encryption & decryption
- Secure key management (`secret.key`)
- Easy-to-use GUI with Tkinter
## Requirements
Install the dependencies using:
pip install pycryptodome tk
## How to Run
1. Clone the repository  
2. Run the script:
python secure_file_encryption.py
3. Use the GUI to:
   - Encrypt any file → creates a `.enc` encrypted version  
   - Decrypt the `.enc` file → restores the original  
## Output Example
- `message.txt` → original file  
- `message.txt.enc` → encrypted file  
- `message_decrypted.txt` → decrypted output  
- `secret.key` → AES key used for encryption/decryption
## Applications
- Protect personal documents  
- Secure business data  
- Safe file sharing between trusted users

