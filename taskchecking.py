from pywinauto import Desktop
import time
from Eclient import Eclient as Eclient
from multiprocessing import Process

while True:
    windows = Desktop(backend="uia").windows()
    tasks = ([w.window_text() for w in windows])
    if 'Minecraft 1.12.2' in tasks:
        Process(target=Eclient.Main).start();
        break
    else:
        time.sleep(5)
    