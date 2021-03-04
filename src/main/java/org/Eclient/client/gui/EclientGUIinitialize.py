import webbrowser
import os
import time

print (os.getenv('AppData'))
url = "file:\\\\\\"+os.getenv('AppData')+"\\.minecraft\\mcpipy/src\\main\\java\\org\\Eclient\\client\\gui\\EclientGUI.html"

webbrowser.open(url,new=2)

while True:
    time.sleep(84600)
