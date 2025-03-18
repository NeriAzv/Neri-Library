import time
import math

def hsl_to_rgb(h, s, l):
    """
    Convert HSL (Hue, Saturation, Lightness) to RGB.
    Hue is in range [0, 360], Saturation and Lightness are in range [0, 1].
    """
    h = h % 360
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x

    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return r, g, b

def rgb_text(text, r, g, b):
    """
    Return text colored with the given RGB values.
    """
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def animate_rgb_text(text, delay=0.01):
    """
    Animate text by cycling through all hues in the HSL color space.
    """
    hue = 0
    while True:
        # Convert HSL to RGB
        r, g, b = hsl_to_rgb(hue, s=1.0, l=0.5)
        
        # Print the text with the current color
        print(rgb_text(text, r, g, b), end="\r")
        
        # Increment hue for the next frame
        hue = (hue + 1) % 360
        
        # Wait for the specified delay
        time.sleep(delay)

# Start the animation
try:
    animate_rgb_text("SMOOTH RGB ANIMATION!", delay=0.01)
except KeyboardInterrupt:
    print("\nAnimation stopped.")