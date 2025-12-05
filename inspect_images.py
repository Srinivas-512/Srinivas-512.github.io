from PIL import Image
import os

image_files = [
    "images/cummins/cummins-plot-1.png",
    "images/cummins/cummins-plot-2.png",
    "images/cummins/cummins-plot-3.png"
]

for img_path in image_files:
    if os.path.exists(img_path):
        try:
            img = Image.open(img_path)
            print(f"{img_path}: {img.size} (width x height)")
        except Exception as e:
            print(f"Error reading {img_path}: {e}")
    else:
        print(f"File not found: {img_path}")

