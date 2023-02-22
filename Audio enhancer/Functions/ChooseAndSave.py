import shutil
import os
import tkinter as tk
from tkinter import filedialog


def Choose_Save():
# Create a Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select the audio file they want to move
    audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])

    # Ask the user to select the destination folder for the audio file
    destination_folder_path = filedialog.askdirectory()

    # Use the shutil.move() function to move the audio file to the destination folder
    shutil.move(audio_file_path, destination_folder_path)

    # Print a message to confirm that the audio file has been moved
    print(f"The audio file has been moved to {destination_folder_path}")
