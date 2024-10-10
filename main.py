"""
Module Docstring: main.py
=============================

This is the main module of the read/write to file project.
"""

___author___ = "Thomas Ross"
___email___ = "Who's_Asking?@gmail.com"
___version___ = "0.1"
___license___ = "None"
___date___ = "10/7/2024"


def append_file(file_name, data) -> None:
    """
    Reads a text file and prints it to console.
    """
    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "a") as f:
        f.write("\n")
        f.write(data)


def read_file(file_name) -> None:
    """
    Reads a text file and prints it to console.
    """
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")

def new_file(file_name) -> None:
    """
    Creates a new file and writes data to it, or overwrites it if it already exists.
    """
    with open(file_name, "w") as f:
        f.write("Scottish Fold")


def main():
    """
    Main entry point of the program
    """
    new_file("cats.txt")
    car_name = input("Enter a cat breed: ")
    append_file("cats.txt", car_name)


if __name__ == "__main__":
    """
    Starts the program.
    """
    main()