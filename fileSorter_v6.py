import tkinter as tk
from tkinter.filedialog import askdirectory
import shutil
import os
import glob

# Start of the GUI #
root = tk.Tk(className=' File Sorter')

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.grid(columnspan=3, rowspan=3)

#instructions
instructions = tk.Label(root, text='Select destination folder', font='Arial', bg='white')
instructions.grid(columnspan=3, column=0, row=1)

#function
def open_folder():
    browse_text.set('loading...')
    folder = askdirectory(parent=root, title='Select a folder')
    if folder:

        directory = folder
        go(directory)
        browse_text.set('Done!')
        quit()
    else: browse_text.set('Browse')
#main event
def go(directory):
    # Changes working direcotry
    os.chdir(directory)
    # glob function of glob module to detect all files inside current directory
    files_list = glob.glob("*")
    # Creating a set of extension types inside the folder to avoid duplicate entries
    extension_set = set()
    # adding each type of extension to the set
    for file in files_list:
        extension = file.split(sep=".")
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue

    # Function to create directory for each type of extension
    def createDirs():
        for dir in extension_set:
            try:
                os.makedirs(dir.upper())
            except FileExistsError:
                continue

    # Function to move files to respective folders
    def arrange():
        for file in files_list:
            fextension = file.split(sep=".")
            try:
                os.rename(file, fextension[1].upper() + "/" + file)
            except (OSError, IndexError):
                continue

    # Move new folders into sorted files_list

    def move():

        os.system('mkdir "01 - Unsorted"')

        currentPath = os.getcwd()
        newPath = currentPath + "\\01 - Unsorted"

        src = currentPath
        dst = newPath

        list = os.listdir()

        print(list)

        for e in list:
            shutil.move(os.path.join(currentPath, e), newPath)

    # Calling the functions in order
    createDirs()
    arrange()
    move()

    # Make other organizational folders
    os.system('mkdir "02 - Sorted" "03 - Edited" "04 - Exported"')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=lambda:open_folder(),
                        textvariable=browse_text, bg='#20bebe', fg='white',
                        height=2, width=15, font='Arial')
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=400, height=50, bg='white')
canvas.grid(columnspan=3)

# End of the GUI #
root.mainloop()
