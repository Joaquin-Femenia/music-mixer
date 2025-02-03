import time
import tkinter as tk
from tkinter import filedialog
from common import clear_console
from mix import start_mix
from common import get_single_key


def ask_confirmation():
    """Asks the user for confirmation to start the mix."""
    while True:
        print("Do you want to start the mix? (Y/N)")
        while True:
            event = get_single_key()
            if event == 'y':
                start_mix()
                exit()
                break
            elif event == 'n':
                time.sleep(1)
                clear_console()
                exit()
                break
            else:
                print("Invalid input. Try again.")


def choose_folder():
    """Opens a dialog for the user to choose a folder and
    returns the selected folder path."""
    root = tk.Tk()
    root.withdraw()  # hide the root window
    selected_folder = filedialog.askdirectory(title="Choose a folder")
    if selected_folder:
        print(f"Chosen folder: {selected_folder}")
    else:
        print("No folder selected.")

    print(selected_folder)
    return selected_folder


def ask_destination_folder():
    """ Asks the user to choose a destination folder for the mix. """
    print("Choose a destination folder, where the mix will be saved")
    while True:
        destinationFolder = choose_folder()
        if not destinationFolder:
            print("Please choose a destination folder.")
            continue
        else:
            return destinationFolder


def ask_songs_amount(available_songs):
    """ Asks the user to input the number of songs and returns it.
    Returns 'inf' if 'all' is input."""
    try:
        print(f"The folder has {available_songs} songs.")
        print("How many songs do you want to mix from this folder? "
              "(Enter 'all' for all songs)")

        while True:
            amount = input()
            if amount == 'all':
                return float('inf')

            amount = int(amount)
            if available_songs < amount:
                print(f"Error: The folder only has {available_songs} "
                      "songs. Please enter a valid amount. \n")
                continue
            else:
                break

    except ValueError:
        print("Invalid input. Try again.")
        return ask_songs_amount()
    return amount


def ask_equal_amounts():
    """ Asks the user if they want to specify the amount of songs
    per folder or use equal amounts."""
    print("Do you want to specify the amount of songs per folder "
          "or use equal amounts? (S/E) ")
    while True:
        event = get_single_key()
        if event == 'e':
            return True
        elif event == 's':
            return False
        else:
            print("Invalid input. Try again.")


def ask_shuffle():
    """Asks the user if they want to create a completely random mix or keep
    the songs sorted by folder."""
    print("Do you want to create a completely random mix (all songs shuffled) "
          "or keep the songs sorted into partitions by folder? (R/P)")
    while True:
        event = get_single_key()
        if event == 'r':
            return True
        elif event == 'p':
            return False
        else:
            print("Invalid input. Try again.")
