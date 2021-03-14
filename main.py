from gifextract import *
from asciigenerator import *
from os import walk
import time

image_path = './images/'
ascii_path = './ascii/'
filename = "dog.gif"


def main():
    processImage(filename)

    _, _, filenames = next(walk(image_path))

    for file in filenames:
        convert_to_ascii(image_path + file)

    counter = 0

    file_prefix = filename.split(".")[0]

    while True:
        with open(ascii_path + file_prefix + '-{}.txt'.format(counter), 'r', encoding="utf8") as f:
            print(f.read(), sep='', end='', flush=True)
            time.sleep(0.01)
            if counter == (len(filenames) - 1):
                counter = 0
            else:
                counter += 1
            os.system('cls')


if __name__ == "__main__":
    main()
