#// /py src/main/java/org/Eclient/client/module/modules/movement/autosprint.py

import input as input;
from mine import *;
from mcpi.minecraft import *;



class AutoSprint:
    @staticmethod
    def Main():
        while True:
            if input.wasPressedSinceLast(input.KEY_W):
                input.pressKey(input.CONTROL);


if __name__ == '__main__':
    AutoSprint.Main();