#// /py src/main/java/org/Eclient/client/module/modules/misc/ZeroWaitForYou.py

#// I reccommend starting this file outside of minecraft right now because it
#// starts outside of minecraft

import ctypes
from io import TextIOWrapper;
import os;
import time;
from datetime import datetime;
import time;
import pyautogui;
import win32api, win32con;
from discord_webhook import DiscordWebhook;
import random;
import json;
from mine import *;


#//    ___                  _ _     _  _                       
#//   / _ \                (_) |   | || |                      
#//  | | | | __      ____ _ _| |_  | || |_   _   _  ___  _   _ 
#//  | | | | \ \ /\ / / _` | | __| |__   _| | | | |/ _ \| | | |
#//  | |_| |  \ V  V / (_| | | |_     | |   | |_| | (_) | |_| |
#//   \___/    \_/\_/ \__,_|_|\__|    |_|    \__, |\___/ \__,_|
#//                                           __/ |            
#//                                          |___/             
#//                     By smokeytube



class ZeroWaitForYou:
    @staticmethod
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    @staticmethod
    def click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);

    @staticmethod
    def doubleclick():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);

    @staticmethod
    def processImage(image) -> bool:
            start = pyautogui.locateOnScreen(image, confidence=0.8);
            pyautogui.moveTo(start);
            return start;

    @staticmethod
    def click_image(image):
        start = pyautogui.locateOnScreen(image, confidence=0.8);
        pyautogui.moveTo(start);
        ZeroWaitForYou.click();

    @staticmethod
    def doubleclick_image(image):
        start = pyautogui.locateOnScreen(image, confidence=0.8);
        pyautogui.moveTo(start);
        ZeroWaitForYou.doubleclick();

    @staticmethod
    def readlog(txt):
        txt.seek(0,2);
        while True:
            line = txt.readline();
            if not line:
                time.sleep(0.1);
                continue;
            yield line;

    @staticmethod
    def Main():
        modulenm = str(__class__.__name__);
        configs = ZeroWaitForYou.loadconfig()['modules'][modulenm];
        jointime =  configs['join_time'];
        distag = configs['discord_tag'];
        diswebhook = configs['discord_webhook'];
        timeoutprompt = configs['disconnect_at_certian_position'];
        warningpos = configs['warning_position'];
        timeoutprompt = configs['reconnect'];
        soundwarning = configs['sound_warning'];
        timeoutpos = configs['disconnect_position'];
        reconnect = configs['reconnect'];
        timesleep = configs['time_between_reconnects'];

        imgpath1 = os.getenv('AppData')+"/.minecraft/mcpipy/src/main/java/org/Eclient/client/module/modules/misc/assets/disconnect/";
        imgpath2 = os.getenv('AppData')+"/.minecraft/mcpipy/src/main/java/org/Eclient/client/module/modules/misc/assets/2b2tlogo/";
        imgpath3 = os.getenv('AppData')+"/.minecraft/mcpipy/src/main/java/org/Eclient/client/module/modules/misc/assets/backtoserverlist/";
        audiopath = os.getenv('AppData')+"/.minecraft/mcpipy/src/main/java/org/Eclient/client/module/modules/misc/assets/audio/";

        repit = 1;
        while True:
            current_time = datetime.now().strftime("%H:%M");
            if current_time == jointime:
                while True:
                    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r");
                    loglines = ZeroWaitForYou.readlog(logfile);
                    print ("Started at " + current_time);
                    try:
                        DiscordWebhook(url=diswebhook, content=("Started at " + current_time)).execute();
                    except:
                        ctypes.windll.user32.MessageBoxW(0, u"Could not reach discord", u"Error", 0);
                    if ZeroWaitForYou.processImage(imgpath2+'2b2tlogoauto.png'):
                        ZeroWaitForYou.doubleclick_image(imgpath2+'2b2tlogoauto.png');
                    elif ZeroWaitForYou.processImage(imgpath2+'2b2tlogolarge.png'):
                        ZeroWaitForYou.doubleclick_image(imgpath2+'2b2tlogolarge.png');
                    elif ZeroWaitForYou.processImage(imgpath2+'2b2tlogonormal.png'):
                        ZeroWaitForYou.doubleclick_image(imgpath2+'2b2tlogonormal.png');
                    elif ZeroWaitForYou.processImage(imgpath2+'2b2tlogosmall.png'):
                        ZeroWaitForYou.doubleclick_image(imgpath2+'2b2tlogosmall.png');
                    for line in loglines:
                        if "[Client thread/INFO]: [CHAT]" in line or "[main/INFO]: [CHAT]" in line or '[Client thread/INFO] [net.minecraft.client.gui.GuiNewChat]: [CHAT]' in line:
                            linechat = line.split('[CHAT] ');
                            try:
                                queuepos = linechat[1].split(': ');
                            except:
                                queuepos = 69420360;
                            try:
                                queuepos1 = int(queuepos[-1]);
                            except:
                                queuepos1 = 69420360;
                            if queuepos1 < timeoutpos and timeoutprompt == 'y' or timeoutprompt == 'yes':
                                pyautogui.press('esc');
                                time.sleep(0.3);
                                ZeroWaitForYou.click_image(imgpath1+'disconnectautogui.png');
                                ZeroWaitForYou.click_image(imgpath1+'disconnectlargegui.png');
                                ZeroWaitForYou.click_image(imgpath1+'disconnectnormalgui.png');
                                ZeroWaitForYou.click_image(imgpath1+'disconnectsmallgui.png');
                                time.sleep(timesleep);
                                if reconnect == 'n' or reconnect == 'no':
                                    while True:
                                        time.sleep(69420);
                                else:
                                    break;
                            elif queuepos1 < warningpos:
                                try:
                                    DiscordWebhook(url=diswebhook, content=linechat[1] + ' ' + distag).execute();
                                except:
                                    ctypes.windll.user32.MessageBoxW(0, u"Could not reach discord", u"Error", 0);
                                if soundwarning == 'yes' or soundwarning == 'y' and repit == 1:
                                    randb = str(random.randint(1,5));
                                    os.startfile(audiopath+'alarm'+randb+'.mp3');
                                    repit = repit + 1
                            elif ("Position in queue") in linechat[1] or ("2b2t is full") in linechat[1]:
                                try:
                                    DiscordWebhook(url=diswebhook, content=linechat[1]).execute();
                                except:
                                    ctypes.windll.user32.MessageBoxW(0, u"Could not reach discord", u"Error", 0);  
                            else:
                                pass
                        else:
                            if ZeroWaitForYou.processImage(imgpath3+'btslauto.png'):
                                ZeroWaitForYou.click_image(imgpath3+'btslauto.png');
                                try:
                                    DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect...")).execute();
                                except:
                                    pass;
                                time.sleep(timesleep);
                                break;
                            elif ZeroWaitForYou.processImage(imgpath3+'btsllarge.png'):
                                ZeroWaitForYou.click_image(imgpath3+'btsllarge.png');
                                try:
                                    DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect...")).execute();
                                except:
                                    pass;
                                time.sleep(timesleep);
                                break;
                            elif ZeroWaitForYou.processImage(imgpath3+'btslnormal.png'):
                                ZeroWaitForYou.click_image(imgpath3+'btslnormal.png');
                                try:
                                    DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect...")).execute();
                                except:
                                    pass;
                                time.sleep(timesleep);
                                break;
                            elif ZeroWaitForYou.processImage(imgpath3+'btslsmall.png'):
                                ZeroWaitForYou.click_image(imgpath3+'btslsmall.png');
                                try:
                                    DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect...")).execute();
                                except:
                                    pass;
                                time.sleep(timesleep);
                                break;
                            else:
                                pass;
            time.sleep(10);


if __name__ == '__main__':
    ZeroWaitForYou.Main();