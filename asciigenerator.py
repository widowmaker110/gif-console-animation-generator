from PIL import Image
import os

# source: https://pythoncircle.com/post/674/python-script-13-generating-ascii-code-from-image/

def convert_to_ascii(image_path):

    # pass the image as command line argument
    img = Image.open(image_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    # write to a text file.
    with open("./ascii/" + (''.join(os.path.basename(image_path).split('.')[:-1])) + ".txt", "w") as f:
        f.write(ascii_image)