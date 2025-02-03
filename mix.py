import os
import random
import shutil
from common import clear_console
from json_realted import load_settings_json, validate_json
from tqdm import tqdm  # Barra de progreso
import sys
sys.stdout.reconfigure(encoding='utf-8')


def start_mix():
    """ Starts the mix process. """
    try:
        if not validate_json():
            print("Error: The file config.json is not a valid JSON.")
            input()
            return

        data = load_settings_json()
        if not data or not all(key in data for key in ("folders",
                                                       "destination",
                                                       "shuffle")):
            print("Error: Missing required data in config.json.")
            input()
            return

        folders = data["folders"]
        destination = data["destination"]
        shuffle = data["shuffle"]

        clean_last_mix(destination)
        mix = create_mix(folders, shuffle)
        copy_mix(mix, destination)

        print("\nMix created successfully.")
        print(f"Destination folder: {destination}")
        input("Press Enter to continue...")

    except Exception as e:
        print(f"Error during mix: {e}")
        return


def create_mix(folders: list, shuffle: bool):
    """Creates a mix from the given folders.

    Args:
        folders (list): A list of tuples where each tuple contains
        a folder path and the number of songs to select from that folder.
        shuffle (bool): Whether to shuffle the final mix.

    Returns:
        list: A list of file paths representing the mixed songs.
    """
    songs_from_folder = {}
    for folder in folders:
        folder_path, song_count = folder  # Unpacking tuple

        if not os.path.isdir(folder_path):
            print(f"Warning: The folder {folder_path} does not exist."
                  "Skipping...")
            continue

        songs_from_folder[folder_path] = [
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
            if file.endswith(".mp3")
        ]

    mix = []
    for folder_path, song_count in folders:
        if folder_path not in songs_from_folder:
            continue  # Skip folders that were invalid

        available_songs = songs_from_folder[folder_path]
        if song_count > len(available_songs):  # this will happend only when song_count is 'all' ~ infinity  # noqa E501
            song_count = len(available_songs)
        limit = min(song_count, len(available_songs))  # Prevent out-of-range errors  # noqa E501
        random.shuffle(available_songs)
        mix.extend(available_songs[:limit])

    if shuffle:
        random.shuffle(mix)

    return mix


def copy_mix(mix: list, destination_folder: str):
    """
    Copies the list of songs to the specified destination folder,
    displaying a progress bar.

    Args:
        mix (list): A list of file paths representing the mixed songs.
        destination_folder (str): The destination folder where the mix
        will be saved.
    """
    print("Creating mix...")
    print("Do not close the program until the process is finished.")
    total = len(mix)
    with tqdm(total=total, desc="Creating mix", unit="song") as bar:
        for i, song in enumerate(mix):
            destination_name = os.path.join(destination_folder,
                                            f"{i+1}_{os.path.basename(song)}")
            shutil.copy(song, destination_name)
            bar.update(1)


def clean_last_mix(destination_folder):
    """Removes all files from the destination folder."""
    print("Cleaning last mix...")
    for archivo in os.listdir(destination_folder):
        os.remove(os.path.join(destination_folder, archivo))
    clear_console()
