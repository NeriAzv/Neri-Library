
import argparse
import time
import re
import os

def main():

    def hsl_to_rgb(h, s, l):
        h = h % 360
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2

        if 0 <= h < 60: r, g, b = c, x, 0
        elif 60 <= h < 120: r, g, b = x, c, 0
        elif 120 <= h < 180: r, g, b = 0, c, x
        elif 180 <= h < 240: r, g, b = 0, x, c
        elif 240 <= h < 300: r, g, b = x, 0, c
        elif 300 <= h < 360: r, g, b = c, 0, x

        r = int((r + m) * 255) ; g = int((g + m) * 255) ; b = int((b + m) * 255)
        return r, g, b

    def rgb_text(text, r, g, b): return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    def animate_rgb_text(text, delay=0.01):
        hue = 0
        while True:
            r, g, b = hsl_to_rgb(hue, s=1.0, l=0.5)
            print(f" ---> \033[1m{rgb_text(text, r, g, b)}\033[0m", end="\r")
            hue = (hue + 1) % 360
            time.sleep(delay)

    current_dir = os.getcwd()

    parser = argparse.ArgumentParser(description="A CLI tool to find imports.")
    parser.add_argument("file", type=str, help="The target .py file to process")

    args = parser.parse_args()
    target_file = os.path.join(current_dir, args.file)

    if not os.path.exists(target_file):
        print(f"Error: File '{target_file}' does not exist.")
        return

    try:
        with open(target_file, "r") as file: file_content = file.read()
    except Exception as e: print(f"Error reading file: {e}")

    libraries = [
        'setuptools',
        'requests',
        'undetected-chromedriver',
        'webdriver-manager',
        'opencv-python',
        'pygetwindow',
        'pyscreeze',
        'pyautogui',
        'selenium',
        'pymupdf',
        'Pillow',
        'psutil'
    ]

    imports = []
    for lib in libraries:
        if len(re.findall(rf"\b{lib.lower()}\b", file_content)) >= 1:
            imports.append(lib)

        if len(re.findall(rf"\.bextract_pdf(\b", file_content)) >= 1:
            imports.append("pymupdf")

        if len(re.findall(rf"\.invoke_api_(\b", file_content)) >= 1:
            imports.append("requests")

        if len(re.findall(rf"\.initialize_driver(\b", file_content)) >= 1:
            imports.append("webdriver-manager", "undetected-chromedriver", "pyautogui psutil")

        if len(re.findall(rf"\.move_mouse_smoothly(\b", file_content)) >= 1:
            imports.append("webdriver-manager", "undetected-chromedriver", "pyautogui psutil")
    from bcpkgfox import ORANGE, RESET
    if imports:
        print()
        try: animate_rgb_text(f"pip install {", ".join(imports)}", delay=0.005)
        except KeyboardInterrupt: print(f"\n -> pip install {", ".join(imports)}\n {ORANGE}>{RESET} Só copiar e colar no terminal. (obs: só identifica as libs que são pertencentes da lib bcfox)", end="\r")

if __name__ == "__main__":
    main()