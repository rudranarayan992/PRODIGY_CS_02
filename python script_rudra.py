# This Code Written By Rudra narayan swain

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption and Decryption")
        self.root.geometry("500x650")
        self.root.configure(bg='#4b0082')  # Indigo background
        
        self.image_path = ""
        self.encrypted_image_path = ""
        self.key_entry = None
        self.original_image = None
        self.encrypted_image = None
        self.decrypted_image = None
        
        # Title Label
        self.label = tk.Label(root, text="Image Encryption and Decryption", bg='#e6e6fa', fg='#4b0082', 
                              font=("Helvetica", 18, "bold"), relief="solid", bd=1)
        self.label.pack(pady=10, fill=tk.X)
        
        # Load Image Button
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image, bg='#ff6347', fg='white', 
                                     font=("Helvetica", 12, "bold"), relief="raised")
        self.load_button.pack(pady=10)

        # Load Encrypted Image Button
        self.load_encrypted_button = tk.Button(root, text="Choose Encrypted Image", command=self.load_encrypted_image, 
                                               bg='#20b2aa', fg='white', font=("Helvetica", 12, "bold"), relief="raised")
        self.load_encrypted_button.pack(pady=10)
        # This Code Written By Rudra narayan swain
        # Key Entry
        self.key_label = tk.Label(root, text="Enter Encryption Key (Integer):", bg='#e6e6fa', fg='#4b0082', 
                                  font=("Helvetica", 14))
        self.key_label.pack(pady=10)
        
        self.key_entry = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="solid")
        self.key_entry.pack(pady=5)
        # This Code Written By Rudra narayan swain
        # Encrypt Image Button
        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image, bg='#4682b4', fg='white', 
                                        font=("Helvetica", 12, "bold"), relief="raised")
        self.encrypt_button.pack(pady=10)
        
        # Decrypt Image Button
        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image, bg='#ff8c00', fg='white', 
                                        font=("Helvetica", 12, "bold"), relief="raised")
        self.decrypt_button.pack(pady=10)
        # This Code Written By Rudra narayan swain
        # Save Encrypted Image Button
        self.save_encrypted_button = tk.Button(root, text="Save Encrypted Image", command=self.save_encrypted, 
                                               bg='#32cd32', fg='white', font=("Helvetica", 12, "bold"), relief="raised")
        self.save_encrypted_button.pack(pady=10)
        
        # Save Decrypted Image Button
        self.save_decrypted_button = tk.Button(root, text="Save Decrypted Image", command=self.save_decrypted, 
                                               bg='#8a2be2', fg='white', font=("Helvetica", 12, "bold"), relief="raised")
        self.save_decrypted_button.pack(pady=10)
        # This Code Written By Rudra narayan swain
        # Canvas for Image Display
        self.canvas = tk.Canvas(root, width=400, height=400, bg='#dcdcdc', relief="solid", bd=2)
        self.canvas.pack(pady=20)
        # This Code Written By Rudra narayan swain
        # Info Label
        self.info_label = tk.Label(root, text="", bg='#e6e6fa', fg='#4b0082', font=("Helvetica", 12))
        self.info_label.pack(pady=10)
        
    def load_image(self):
        self.image_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                                     filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                                ("All files", "*.*")))
        if self.image_path:
            self.info_label.config(text=f"Loaded image: {self.image_path}")
            self.load_and_display_image()

    def load_and_display_image(self):
        img = Image.open(self.image_path)
        img.thumbnail((400, 400))
        self.original_image = img.copy()
        self.display_image_with_message(self.original_image, "Original Image")

    def encrypt_image(self):
        if self.original_image and self.key_entry.get():
            try:
                key = int(self.key_entry.get())
                img_array = np.array(self.original_image)
                encrypted_data = np.bitwise_xor(img_array, key)
                self.encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
                self.display_image_with_message(self.encrypted_image, "Image encrypted successfully.")
            except ValueError:
                messagebox.showerror("Error", "Invalid key. Please enter an integer.")

    def decrypt_image(self):
        if self.encrypted_image and self.key_entry.get():
            try:
                key = int(self.key_entry.get())
                img_array = np.array(self.encrypted_image)
                decrypted_data = np.bitwise_xor(img_array, key)
                self.decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
                self.display_image_with_message(self.decrypted_image, "Image decrypted successfully.")
            except ValueError:
                messagebox.showerror("Error", "Invalid key. Please enter an integer.")

    def save_encrypted(self):
        if self.encrypted_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.encrypted_image.save(save_path)
                self.info_label.config(text=f"Encrypted image saved as: {save_path}")

    def save_decrypted(self):
        if self.decrypted_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.decrypted_image.save(save_path)
                self.info_label.config(text=f"Decrypted image saved as: {save_path}")

    def load_encrypted_image(self):
        self.encrypted_image_path = filedialog.askopenfilename(initialdir="/", title="Select Encrypted Image",
                                                              filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                                         ("All files", "*.*")))
        if self.encrypted_image_path:
            self.info_label.config(text=f"Loaded encrypted image: {self.encrypted_image_path}")
            self.load_and_display_encrypted_image()

    def load_and_display_encrypted_image(self):
        img = Image.open(self.encrypted_image_path)
        img.thumbnail((400, 400))
        self.encrypted_image = img.copy()
        self.display_image_with_message(self.encrypted_image, "Encrypted Image")

    def display_image_with_message(self, img, message):
        img.thumbnail((400, 400))
        self.tk_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.info_label.config(text=message)

def main():
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



# This Code Written By Rudra narayan swain
# This Code Written By Rudra narayan swain
