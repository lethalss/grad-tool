import sys
import time
from PIL import Image, ImageSequence
import numpy as np

def main():
    if len(sys.argv) != 2:
        print("Usage: python ascii_gif.py <gif_path>")
        sys.exit(1)

    gif_path = sys.argv[1]

    img = Image.open(gif_path)
    frames = get_frames(img)
    
    while True:
        for frame in frames:
            ascii_art = convert_to_ascii(frame, 80)
            print("\033[2J")  # Clear the terminal screen
            print(ascii_art)
            time.sleep(img.info['duration'] / 1000)  # Sleep for the duration of the frame

def get_frames(img):
    frames = []
    for frame in ImageSequence.Iterator(img):
        frames.append(frame.copy())
    return frames

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
