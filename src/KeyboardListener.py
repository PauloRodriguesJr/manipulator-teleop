# função do teclado
from pynput import keyboard


class KeyboardInput():

    def __init__(self):
        self.i = 0

    def on_press(self, Key):
        try:
            if Key.char == "c":
                self.i += 1
                print("On_press: ", self.i)
            elif Key.char == "v":
                self.i -= 1
                print("On_press: ", self.i)
            else:
                print(f"Pressing key: {Key.char}")
        except AttributeError:
            pass

    def on_release(self, key):
        print("On_release: ", self.i)
        if key == keyboard.Key.esc:
            # Stop listener
            return False


# Collect events until released
keyAction = KeyboardInput()
getInput = keyboard.Listener(
    on_press=keyAction.on_press, on_release=keyAction.on_release)
getInput.start()
getInput.join()
