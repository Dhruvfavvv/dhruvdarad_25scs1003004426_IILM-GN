import cv2
import numpy as np
import os


def preprocess_image(input_path, output_path, size=(28, 28)):
    # Read image in grayscale
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error loading image: {input_path}")
        return

    # Resize
    img_resized = cv2.resize(img, size)

    # Normalize (0–255 → 0–1)
    img_normalized = img_resized / 255.0

    # Save normalized image (convert back to 0–255 for saving)
    img_to_save = (img_normalized * 255).astype(np.uint8)
    cv2.imwrite(output_path, img_to_save)

    print(f"Processed and saved: {output_path}")


def preprocess_folder(input_folder, output_folder, size=(28, 28)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        preprocess_image(input_path, output_path, size)


# Example usage
if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "processed_images"

    preprocess_folder(input_folder, output_folder)