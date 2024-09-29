from PIL import Image

# Function to encrypt the image using XOR
def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR operation for encryption
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image using XOR
def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR operation for decryption (same key)
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Function to swap pixels for encryption
def swap_pixels(image_path, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            if x + 1 < width and y + 1 < height:
                # Swap pixels
                pixels[x, y], pixels[x + 1, y + 1] = pixels[x + 1, y + 1], pixels[x, y]

    img.save(output_path)
    print(f"Image encrypted with pixel swapping and saved as {output_path}")

# Function to reverse swap pixels for decryption
def reverse_swap_pixels(image_path, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            if x + 1 < width and y + 1 < height:
                # Reverse pixel swap
                pixels[x, y], pixels[x + 1, y + 1] = pixels[x + 1, y + 1], pixels[x, y]

    img.save(output_path)
    print(f"Image decrypted with pixel swapping and saved as {output_path}")

# Main program to let the user choose
def main():
    print("Choose an option:")
    print("1: Encrypt an image using XOR")
    print("2: Decrypt an image using XOR")
    print("3: Encrypt an image by swapping pixels")
    print("4: Decrypt an image by reversing pixel swap")

    choice = int(input("Enter your choice (1-4): "))

    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the output path for the result image: ")
    key = 123  # You can also prompt the user to enter a key

    if choice == 1:
        encrypt_image(image_path, key, output_path)
    elif choice == 2:
        decrypt_image(image_path, key, output_path)
    elif choice == 3:
        swap_pixels(image_path, output_path)
    elif choice == 4:
        reverse_swap_pixels(image_path, output_path)
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

