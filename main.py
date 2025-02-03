import time
import os
from common import clear_console, get_single_key
from utils import configure_folders, print_saved_settings
from user_inputs import (
    ask_equal_amounts,
    ask_shuffle,
    ask_destination_folder,
    ask_confirmation
)
from json_realted import validate_json, save_settings_json

# Change the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    # Check if the user wants to use last settings
    if validate_json():
        print_saved_settings()
        print("Do you want to use the last settings? (Y/N)")
        while True:
            event = get_single_key()
            if event == 'y':
                ask_confirmation()
                exit()
                break
            elif event == 'n':
                clear_console()
                break
            else:
                print("Invalid input. Try again.")
    else:
        print("No saved settings found.")
        time.sleep(1)
        clear_console()

    # Ask the user if they want to mix the same amount of songs from each folder  # noqa E501
    equals_amounts = ask_equal_amounts()
    clear_console()

    # Configure the folders to mix
    folders = configure_folders(equals_amounts)
    # Ask the user for the destination folder
    destination = ask_destination_folder()
    clear_console()

    # Ask the user if they want to shuffle the songs
    shuffle = ask_shuffle()
    clear_console()

    # Save the settings to a JSON file
    data = {
        'folders': folders,
        'destination': destination,
        'equals_amounts': equals_amounts,
        'shuffle': shuffle
    }
    save_settings_json(data)
    print("Settings saved successfully.")
    time.sleep(1)
    clear_console()
    print_saved_settings()
    ask_confirmation()

except KeyboardInterrupt:
    print("\nProgram interrupted by the user.")
