# 🖼️ Preprocessing (Resize and Normalize)

## 📌 Overview

This project demonstrates basic image preprocessing techniques used in computer vision and machine learning pipelines.
The script resizes images to a fixed dimension and normalizes pixel values for further processing.

---

## ⚙️ Features

* Resize images to a standard size (28×28)
* Normalize pixel values (0–255 → 0–1)
* Batch processing of multiple images
* Automatic output folder creation

---

## 📂 Project Structure

```
project/
│── preprocessing.py
│── input_images/
│     ├── sample_digit_1.png
│     ├── sample_digit_2.png
│── processed_images/
│     ├── sample_digit_1.png
│     ├── sample_digit_2.png
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install opencv-python numpy
```

### 2. Add images

Place your images inside the `input_images` folder.

### 3. Run the script

```
python preprocessing.py
```

### 4. Output

Processed images will be saved in the `processed_images` folder.

---

## 🧠 What This Does

* **Resizing** ensures all images have uniform dimensions
* **Normalization** scales pixel values to improve model performance

---

## 🖼️ Sample Output

| Input Image        | Processed Image    |
| ------------------ | ------------------ |
| sample_digit_1.png | sample_digit_1.png |
| sample_digit_2.png | sample_digit_2.png |

---

## 📌 Notes

* Only sample images are included for demonstration
* You can use your own dataset by placing images in the input folder

---

## 🔮 Future Improvements

* Add visualization (before vs after)
* Support color image preprocessing
* Integrate with machine learning models

---

## 👨‍💻 Author

Your Name
