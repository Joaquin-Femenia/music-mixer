import os
import sys

# Import platform-specific modules for getting a single key press
if sys.platform == "win32":
    import msvcrt

    def get_single_key():
        """ Waits for a single key press on Windows
        and returns it as a lowercase string. """
        return msvcrt.getch().decode("utf-8").lower()
else:
    import termios

    def get_single_key():
        """ Waits for a single key press on Unix-like systems
        and returns it as a lowercase string. """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def clear_console():
    """ Clears the console screen. """
    os.system('cls' if os.name == 'nt' else 'clear')
