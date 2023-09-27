"""
Class 37: External files part 1
Class 38: External files part 2
Author: Eliana Chavez
"""

import io

# Create file
# Open file
# Manipulate (read or write)
# Modes: read (r), write (w) , append (a), read and write (r+)
# Close file


def writeFile():
    # Create and open file
    # If file does not exist open will create it
    # Modes: read, write, append
    file = io.open("file.txt", "w")
    text = "Hello world from python"

    # Manipulate file
    file.write(text)

    # Close file
    file.close()


def addTextToAFile():
    # Create and open file
    # If file does not exist open will create it
    # Modes: read, write, append
    file = io.open("file.txt", "a")
    text = "\nThis should be another line INSERTED\n"

    # Manipulate file
    file.write(text)

    # Close file
    file.close()


def replaceLinesInAFile():
    # Open file
    # Modes: read, write, append
    file = io.open("file.txt", "r+")
    newText = "This is a replacing line\n"
    text = file.readlines()

    file.seek(0)
    text[1] = newText
    # Manipulate file
    file.writelines(text)

    # Close file
    file.close()


def readFile():
    # Open file
    # Modes: read, write, append
    file = io.open("file.txt", "r")

    # Manipulate file
    text = file.read()

    # Close file
    file.close()

    print("READ:\n", text)


def readMultipleLines():
    # Open file
    # Modes: read, write, append
    file = io.open("file.txt", "r")

    # Manipulate file
    # readlines returns a list with each line of the text
    lines = file.readlines()

    # Close file
    file.close()

    print(lines)


def moveCursor():
    # Open file
    # Modes: read, write, append
    file = io.open("file.txt", "r")

    # Manipulate file
    text = file.read()
    print("First read: \n", text)

    # Move cursor to the specified position (character)
    # file.seek(len(text.read()/2)) - move cursor to the middle of the text
    # file.seek(len(text.readline())) - move cursor to the end of the first line
    file.seek(5)
    print("\n")

    text = file.read()
    print("Second read: \n", text)

    # Close file
    file.close()


def readSomeCharacters():
    # Open file
    # Modes: read, write, append
    file = io.open("file.txt", "r")

    # Manipulate file
    # Get just the first n characters AND MOVE THE CURSOR
    # Next read will be since the last position
    text = file.read(11)
    print(text)

    # Close file
    file.close()


def main():
    writeFile()
    addTextToAFile()
    readFile()
    # readMultipleLines()
    # moveCursor()
    # readSomeCharacters()
    replaceLinesInAFile()
    readFile()


main()
