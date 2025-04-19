from PIL import Image
import os

def encrypt_decrypt_image(image_path, key, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        print(f"✅ Output saved as: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

def generate_sample_image(image_path):
    img = Image.new('RGB', (100, 100), color=(0, 102, 204))
    img.save(image_path)
    print(f"✅ Sample image created: {image_path}")

def main():
    print("=== Image Encryption Tool ===")

    choice = 'E'
    path = "sample_input.png"
    key = 123

    if not os.path.exists(path):
        generate_sample_image(path)

    if choice == 'E':
        output_path = "encrypted_image.png"
    elif choice == 'D':
        output_path = "decrypted_image.png"
    else:
        print("❌ Invalid choice!")
        return

    encrypt_decrypt_image(path, key, output_path)

if __name__ == "__main__":
    main()
