import os
from user_inputs import choose_folder, ask_songs_amount
from common import get_single_key, clear_console
from json_realted import load_settings_json


def configure_folders(equals_amounts: bool):
    """Configures the folders to mix based on user input.

    Args:
        equals_amounts (bool): Whether to use equal amounts of songs
        from each folder.

    Returns:
        list: A list of tuples containing folder paths and the number of songs
        to mix from each folder.
    """
    folders = []
    while True:
        print("Do you want to add a folder? (Y/N)")
        event = get_single_key()
        if event == 'y':
            path = choose_folder()
            if not path or not os.path.isdir(path):
                print("No folder selected. Try again.")
                continue
            if not equals_amounts:
                available_songs = available_songs_in_folder(path)
                amount = ask_songs_amount(available_songs)
            else:
                amount = 0  # Placeholder, will be calculated later if equals_amounts is True  # noqa E501
            folders.append((path, amount))
        elif event == 'n':
            break
        else:
            print("Invalid input. Please press 'Y' to add a folder or 'N'"
                  "to finish.")

    clear_console()
    if equals_amounts:
        if len(folders) > 0:
            total = int(input("How many songs do you want to mix in total? "))
            total_available = sum(
                available_songs_in_folder(folder[0]) for folder in folders
            )

            # Check if the total requested exceeds the available songs
            if total > total_available:
                print(
                    "Warning: You requested more songs than are available "
                    "across the folders."
                )
                total = total_available

            # Initial distribution of songs equally across folders,
            # without exceeding the available number in each folder.
            amount = total // len(folders)
            folders = [
                (folder[0], min(amount, available_songs_in_folder(folder[0])))
                for folder in folders
            ]
            total -= sum(folder[1] for folder in folders)

            # Check if any folder does not have enough songs to
            # reach the requested amount
            insufficient_folders = False
            for i, folder in enumerate(folders):
                if total > 0:
                    available_songs = available_songs_in_folder(folder[0])
                    current_amount = folder[1]
                    remaining_space = available_songs - current_amount

                    if remaining_space > 0:
                        add = min(remaining_space, total)
                        folders[i] = (folder[0], current_amount + add)
                        total -= add
                    # If the current folder has fewer songs than requested,
                    # mark as insufficient
                    if current_amount < amount:
                        insufficient_folders = True

            if total != 0 or insufficient_folders:
                print(
                    "Warning: Some folders had less than the requested songs. "
                    "The distribution has been adjusted."
                )
                input("Press Enter to continue...")
        else:
            print("No folders were added, cannot distribute songs.")
            return []

    return folders


def print_saved_settings():
    """ Prints the last chosen folders to mix and the destination folder. """
    data = load_settings_json()
    if not data:
        return
    folders = data["folders"]
    if not folders:
        print("No folders were added.")
        return
    destination = data["destination"]
    equals_amounts = boolean_to_string(data["equals_amounts"])
    shuffle = boolean_to_string(data["shuffle"])

    print("Last chosen settings for the mix: ")
    for folder, amount in folders:
        if amount == float('inf'):
            amount = available_songs_in_folder(folder)
        print(f"Folder: {folder} - amount of songs from here: {amount}")
    print(f"Destination folder: {destination}")
    print(f"Equal amounts: {equals_amounts}")
    print(f"Shuffle order: {shuffle}")
    print("\n")


def boolean_to_string(boolean):
    """ Converts a boolean value to a string representation. """
    if boolean:
        return "Yes"
    else:
        return "No"


def available_songs_in_folder(folder_path):
    """ Returns the number of songs in a folder. """
    return len([file for file in os.listdir(folder_path)
                if file.endswith(".mp3")])
