# Music Mixer
A Python script that allows users to create playlists from selected folders. It includes customization options and saves preferences for future use.

[Click here for the Spanish version of this README](README-ES.md)

## Motivation and problem solved
This program was born from a real necessity I faced: solving the issue of having a long list of songs on a speaker that uses a USB drive but does not allow folder navigation.

The problem is that every time the speaker turns on, it starts playing the first song on the USB drive. This makes the music repetitive, and if there are too many songs, the last ones might never get played unless the speaker is left on long enough.

This program automatically generates a new mix of songs in a separate folder based on user preferences.

The first version was created for a physical store owned by my father, where they used a speaker with a USB drive that had no folder navigation. Over time, I improved the program until it became a flexible and automated solution.


## Main features
 - Select multiple source folders.
 - Define a destination folder.
 - Keep the folder order or shuffle the songs.
 - Choose the total number of songs for the mix or per folder.
 - Save user preferences for future executions.


## Installation and use
1. Clone the repository:  
    ```sh
    git clone https://github.com/Joaco-Femenia/music-mixer.git
    ```
2. Install dependencies:  
    ```sh
    pip install -r requirements.txt
    ```
3. Navigate to the project folder:  
    ```sh
    cd ruta/del/proyecto
    ```
4. Run the program with pyton:  
    ```sh
    python main.py
    ```
    **In Windows, use CMD or PowerShell. in macOS/Linux use the terminal**  


## Contributions and contact
**Author:** Joaquín Femenia
**GitHub:** [Joaquin-Femenia](https://github.com/Joaquin-Femenia)  
**Contributions:** pull requests and suggestions are welcome!