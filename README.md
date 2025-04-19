# PRODIGY_CS_02
Hey everyone! 👋 Excited to share the second task of my Cyber Security Internship at Prodigy InfoTech!  For this task, I developed a simple image encryption tool using pixel-level manipulation in Python. The idea was to explore how even basic mathematical operations like XOR can be used to protect digital images. 🔢🖼️


PRODIGY_CS_02/
├── image_encryptor.py        ✅ Python encryption script
├── README.md                 ✅ Documentation
├── sample_input.png          ✅ Generated input image
├── encrypted_image.png       ✅ Output image after encryption


# PRODIGY_CS_02

## 🔐 Task-02: Image Encryption using Pixel Manipulation

This project is part of my Cyber Security internship at **Prodigy InfoTech**.

---

## 🧠 About the Project

This Python-based tool allows users to encrypt and decrypt images using simple pixel-level manipulation. It uses a symmetric encryption technique (XOR) to alter each pixel's RGB values.

---

## 💻 Features

- Encrypts and decrypts color images
- Uses XOR with a numeric key (0–255)
- Automatically creates a sample image if none exists
- Lightweight and beginner-friendly

---

## 📸 How It Works

Each pixel's Red, Green, and Blue values are XORed with a numeric key:
```python
(r ^ key, g ^ key, b ^ key)
```
Running the encryption process again with the same key decrypts the image back to its original form.

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x
- Pillow library (Install with `pip install pillow`)

### 🧪 Usage

```bash
python image_encryptor.py
```
The script will automatically:
- Create `sample_input.png` if it doesn’t exist
- Encrypt it using a default key (123)
- Output an encrypted image: `encrypted_image.png`

You can modify the script to change the key or switch to decryption.

---

## 📁 Included Files

- `image_encryptor.py` – Main encryption/decryption logic
- `sample_input.png` – Sample input image (auto-generated)
- `encrypted_image.png` – Output after encryption

---

## 🔗 Related Repositories

- [PRODIGY_CS_01](https://github.com/rudranarayan992/PRODIGY_CS_01) – Caesar Cipher Implementation

---

the application by running the script locally.

Ensure Dependencies:

Install the required libraries:

pip install pillow numpy

Run the Script:

Execute the Python script using python script_rudra.py and follow the on-screen instructions for encrypting and decrypting images.

## ✍️ Author

**Rudra Narayan Swain**  
Cyber Security Intern @ Prodigy InfoTech

---

## 📌 Tags

#CyberSecurity #Python #ImageEncryption #PixelManipulation #PRODIGY_CS #Task02 #GitHubProject #InternshipTasks #PIL #ImageProcessing #ProdigyInfoTech #Encryption #Decryption #Internship #RudraNarayanSwain

