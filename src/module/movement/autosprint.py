# /py src/module/movement/autosprint

import input as input

def Main():
    while True:
        if input.wasPressedSinceLast(input.KEY_W):
            input.pressKey(input.CONTROL)


if __name__ == '__main__':
    Main()