# check_resolution.py
from PIL import Image
import os

def check_image_resolution(path, min_dpi=300):
    with Image.open(path) as img:
        dpi = img.info.get('dpi', (0, 0))[0]
        return dpi >= min_dpi

if __name__ == "__main__":
    folder = "../resources/example_images"
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".png")):
            full_path = os.path.join(folder, filename)
            if check_image_resolution(full_path):
                print(f"{filename}: OK")
            else:
                print(f"{filename}: Resolució insuficient")
