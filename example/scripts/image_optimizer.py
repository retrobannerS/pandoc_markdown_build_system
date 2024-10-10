import os
import shutil
from PIL import Image

def optimize_images(input_dir, output_dir, quality, max_size):
    print(f"Optimizing images from {input_dir} to {output_dir} with quality {quality}")

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                file_path = os.path.join(root, file)
                optimize_image(input_dir, file_path, output_dir, quality, max_size)

def optimize_image(input_dir, file_path, output_dir, quality, max_size):
    try:
        img = Image.open(file_path)
        original_format = img.format

        if img.mode in ("RGBA", "LA"):
            img = fill_transparent(img)

        img.thumbnail((max_size, max_size))

        img = img.convert("RGB")
        
        new_file_path = file_path.replace(input_dir, output_dir)
        if original_format == "PNG":
            new_file_path = os.path.splitext(new_file_path)[0] + "_png" + ".jpg"
        else:
            new_file_path = os.path.splitext(new_file_path)[0] + ".jpg"

        new_file_dir = os.path.dirname(new_file_path)
        os.makedirs(new_file_dir, exist_ok=True)

        img.save(new_file_path, "JPEG", optimize=True, quality=quality)
    except Exception as e:
        print(f"Error optimizing {file_path}: {e}")
    
def fill_transparent(img):
    non_transparent = Image.new("RGB", img.size, (255, 255, 255))
    non_transparent.paste(img, (0, 0), img)
    return non_transparent

