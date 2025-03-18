import time

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
        print(f"\033[1m{rgb_text(text, r, g, b)}\033[0m", end="\r")
        hue = (hue + 1) % 360
        time.sleep(delay)

try: animate_rgb_text("SMOOTH RGB ANIMATION!", delay=0.01)
except KeyboardInterrupt: print("\nAnimation stopped.")