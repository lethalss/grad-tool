import sys
from PIL import Image
import numpy as np

def main():
    if len(sys.argv) != 3:
        print("Usage: python ascii_image.py <image_path> <output_txt_file> (ps. thank your lord and savior kane)")
        sys.exit(1)

    image_path = sys.argv[1]
    output_file = sys.argv[2]

    img = Image.open(image_path)
    ascii_art = convert_to_ascii(img, 80)

    with open(output_file, "w") as f:
        f.write(ascii_art)

def convert_to_ascii(img, width):
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio)
    img_resized = img.resize((width, height))

    result = ""
    for y in range(height):
        for x in range(width):
            r, g, b, *_ = img_resized.getpixel((x, y))
            result += f"\033[48;2;{r};{g};{b}m "
        result += "\033[0m\n"

    return result


if __name__ == "__main__":
    main()
