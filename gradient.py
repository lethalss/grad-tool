import sys

# RGB presets
PRESETS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "yellow": (255, 255, 0),
}

def main():
    if len(sys.argv) < 4:
        print("Usage: python color_text.py <input_txt_file> <output_txt_file> <preset_name1> [<preset_name2> ...]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    preset_names = sys.argv[3:]

    for name in preset_names:
        if name not in PRESETS:
            print(f"Invalid preset name: {name}. Available presets: {', '.join(PRESETS.keys())}")
            sys.exit(1)

    colors = [PRESETS[name] for name in preset_names]

    with open(input_file, "r") as f:
        content = f.read()

    colored_text = apply_colors(content, colors)

    with open(output_file, "w") as f:
        f.write(colored_text)

def lerp_color(color1, color2, t):
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    r = r1 + t * (r2 - r1)
    g = g1 + t * (g2 - g1)
    b = b1 + t * (b2 - b1)

    return int(r), int(g), int(b)

def apply_colors(text, colors):
    result = ""
    n = len(colors)

    for i, c in enumerate(text):
        if c == "\n":
            result += c
            continue

        t = (i / len(text)) * (n - 1)
        index = int(t)
        color1 = colors[index]
        color2 = colors[min(index + 1, n - 1)]

        t -= index

        color = lerp_color(color1, color2, t)
        r, g, b = color
        result += f"\033[38;2;{r};{g};{b}m{c}"

    result += "\033[0m"
    return result

if __name__ == "__main__":
    main()
