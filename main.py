"""
    'The secret key game'
    Code by: Ferdinand Feoli
    Developer's profile: https:ferd656.wixsite.com/profile

    Description: A simple game that consists in  guessing
    a 'secret key', you win when you type it.

    Just for fun.
    You can use it as you want.
"""
# Requiered libraries - - - -
import msvcrt
# - - - - - - - - - - - - - -


class Game:
    """
    This class contains all game's functions and methods.
    Use it to initialize the game.
    """
    def __init__(self):
        """
        Starts the game
        """
        print("/" * 20 + "    T H E    S E C R E T    K E Y S    " + "/" * 20)
        print(" " * 14 + "Let's play a game. Could you guess the secret keys?\n")
        self._main_menu()

    @staticmethod
    def secondary_options():
        """
        Display secondary options.
        """
        print("+" + "-" * 48 + "+\n|    OPTIONS:" + " " * 36 + "|\n" +
              "|" + " " * 48 + "|\n" +
              "| Please select one of the following options:" + " " * 4 + "|\n" +
              "|     - 1= Return to main menu" + " " * 19 + "|\n" +
              "|     - Any other= Exit game" + " " * 21 + "|\n" +
              "+" + "-" * 48 + "+")

        kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")

        if kp == "1":
            return True
        else:
            return False

    @staticmethod
    def select_continue():
        """
        Check if user want to retry.
        """
        commands = ("y", "n")
        while True:
            print("Want to try again?(y/n)")
            command = str(msvcrt.getch()).replace("b'", "").replace("'", "").lower()

            if command not in commands:
                print("--->Invalid command, must be '%s' for yes or '%s' for no."
                      % commands)
            else:
                break

        return command

    def _main_menu(self):
        # Display main menu options.

        print("+" + "-"*48 + "+\n|    MAIN MENU:" + " "*34 + "|\n" +
              "|" + " " * 48 + "|\n" +
              "| Please select one of the following options:" + " "*4 + "|\n" +
              "|     - 1= Start game" + " "*28 + "|\n" +
              "|     - 2= Instructions" + " "*26 + "|\n" +
              "|     - Any other= Exit game" + " "*21 + "|\n" +
              "+" + "-" * 48 + "+")

        kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")

        if kp == "1":
            print("\nLet's go!")
            self._secret_key()
        elif kp == "2":
            self._instructions()

    def _instructions(self):
        # Display game _instructions.

        print("+" + "-" * 48 + "+\n|    INSTRUCTIONS:" + " " * 31 + "|\n" +
              "|" + " " * 48 + "|\n" +
              "| Use your keyboard to press any key or" + " " * 10 + "|\n" +
              "| combination of keys." + " " * 27 + "|\n" +
              "| You win when you press the secret key(s)" + " " * 7 + "|\n" +
              "|" + " " * 48 + "|\n" +
              "|    OPTIONS:" + " " * 36 + "|\n" +
              "|" + " " * 48 + "|\n" +
              "| Please select one of the following options:" + " " * 4 + "|\n" +
              "|     - 1= Start game" + " " * 28 + "|\n" +
              "|     - Any other= Exit game" + " " * 21 + "|\n" +
              "+" + "-" * 48 + "+")

        kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")

        if kp == "1":
            print("\nLet's go!")
            self._secret_key()

    def _secret_key(self):
        # Get the key pressed by the user and check if he/she wins.

        bk = chr(10) + "-"*25 + chr(10)

        while True:
            print(bk + "Press any key(s)" + bk)

            kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")
            # Store key's value.

            if r'\xe0' in kp:
                kp += str(msvcrt.getch()).replace("b'", "").replace("'", "")
                # Refactor the variable in case of multi press.

            if kp == r'\xe0\x8a':
                # If user pressed the secret key, the game ends.
                # \x8a is CTRL+F12, that's the secret key.

                print(bk + "CONGRATULATIONS YOU PRESSED THE SECRET KEYS!\a" + bk)
                print("Press any key to exit the game")
                msvcrt.getch()
                break
            else:
                print("    You pressed:'", kp + "', that's not the secret key(s)\n")
                if self.select_continue() == "n":
                    if self.secondary_options():
                        self._main_menu()
                    break


def initialize():
    """
    Calls the Game class
    Initialize the game
    """
    Game()


initialize()
