"""
Batch converts image files in a source directory to PNG format.

This script accepts two command-line arguments:
1) A source directory containing image files
2) A destination directory where converted PNG images will be saved

For each file in the source directory, the script attempts to open it as an image
and convert it to PNG format. Converted images are written to the destination
directory using the original filename with a `.png` extension.

If the destination directory does not exist, it is created automatically.
Files that cannot be opened as images are skipped, and an error message is
printed to the terminal.

Usage:
    python script_name.py <source_directory> <destination_directory>
"""

from PIL import Image
import sys
import os


def convert_images(get_folder, create_folder):
    """
    Loops through a folder containing image files and converts them to PNG format.

    The function takes a source folder and a destination folder as arguments.
    If the destination folder does not exist, it is created automatically.
    Each file in the source folder is attempted to be opened as an image and
    converted to a PNG file with the same base filename.

    Converted images are saved in the destination folder.
    Files that cannot be opened as images are skipped, and an error message
    is printed to the terminal.

    Args:
        get_folder (str): Path to the folder containing the original image files.
        create_folder (str): Path to the folder where PNG images will be saved.
    """
    # check is new/ exists if not create it
    if not os.path.isdir(create_folder):
        os.mkdir(create_folder)

    # loop through Pokedex
    if os.path.isdir(get_folder):
        for filename in os.listdir(get_folder):
            path = os.path.join(get_folder, filename)
            try:
                with Image.open(path) as img:
                    # convert images to png
                    # save to the new folder
                    f, e = os.path.splitext(filename)
                    save_file = f + ".png"
                    save_path = os.path.join(create_folder, save_file)
                    img.save(save_path, "png")
            except Exception as e:
                print(f"Skipping {filename}: {e}")


def main():
    """
    Reads command-line arguments and runs the image conversion process.

    The first argument is expected to be the path to the folder containing
    the original image files. The second argument is the path to the folder
    where the converted PNG images will be saved.
    """
    # Get first and second argument
    get_folder = sys.argv[1]
    create_folder = sys.argv[2]
    convert_images(get_folder, create_folder)


if __name__ == '__main__':
    main()
