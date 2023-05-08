import os, time
import sys
from PIL import Image

'''change these values according to your needs'''
image_path = "Imgs/dreamCar.jpg"  # Relative path of input image
inputScaleFactor = 30            # scale/size of the output text range=(0-100)
output_path = "output.txt"       # Relative path for the output textfile

def get_arguments():
    global image_path, inputScaleFactor, output_path
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    if len(sys.argv) > 2:
        inputScaleFactor = float(sys.argv[2])
    if len(sys.argv) > 3:
        output_path = sys.argv[3]
    if inputScaleFactor > 100:
        inputScaleFactor = 100
    if inputScaleFactor < 0:
        inputScaleFactor = 0


def generate_ascii_art(image_path, output_path):
    ScaleFactor = 0.5
    oneCharWidth = 10
    oneCharHeight = 18
    ScaleFactor = float((inputScaleFactor*1.5)/100)

    # Open and convert the image to grayscale
    image = Image.open(image_path)
    image = image.convert("L")

    # Resize the image to fit the width of the terminal
    width, height = image.size
    new_width = int(ScaleFactor*width)
    new_height = int(ScaleFactor*height*(oneCharWidth/oneCharHeight))
    image = image.resize((new_width, new_height))

    # Generate ASCII art from the image
    ascii_art = ""
    for pixel in image.getdata():
        # Map the pixel value to an ASCII character
        if pixel < 40:
            ascii_char = " "
        elif pixel < 75:
            ascii_char = "."
        elif pixel < 100:
            ascii_char = "-"
        elif pixel < 150:
            ascii_char = "+"
        elif pixel < 175:
            ascii_char = "#"
        elif pixel < 200:
            ascii_char = "M"
        else:
            ascii_char = "M"
        if (len(ascii_art) % (new_width*1) == 0):
            ascii_char = "\n"
        ascii_art += ascii_char

    # Write the ASCII art to the output file
    with open(output_path, "w") as f:
        f.write(ascii_art)


if __name__ == "__main__":
    # Get command line arguments if provided by user
    get_arguments()
    print("Image processed: ", image_path)
    print("Output: ", output_path)
    # Generate ASCII art from the image
    generate_ascii_art(image_path, output_path)
