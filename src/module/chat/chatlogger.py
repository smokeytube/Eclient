#// /py src/main/java/org/Eclient/client/module/modules/chat/chatlogger.py

from io import TextIOWrapper
import os;
import time;
from datetime import datetime, date;
import time;
import ctypes;
import json
from typing import TextIO;
from discord_webhook import DiscordWebhook;
from multiprocessing import Process;



class ChatLogger:
    @staticmethod
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

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
    def opencurrenttxt() -> TextIOWrapper:
        logpath = (os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\chat\\logs\\');
        txtfile = logpath+'/'+str(datetime.today().year)+'/'+str(datetime.today().month)+'/'+str(datetime.today().day)+'/'+str(datetime.now().strftime("%H-00"))+'.txt';
        try:
            filelog = open(txtfile, 'a+');
        except FileNotFoundError:
            os.makedirs(logpath+'/'+str(datetime.today().year)+'/'+str(datetime.today().month)+'/'+str(datetime.today().day)+'/');
            filelog = open(txtfile, 'a+');
        except:
            ctypes.windll.user32.MessageBoxW(0, u"An unexpected error occured. Reporting problem to microsoft", u"Error", 0);
            exit();
        return filelog;

    @staticmethod
    def Main():
        logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r");
        modulenm = str(__class__.__name__);
        configs = ChatLogger.loadconfig()['modules'][modulenm];
        webhookurl = configs['webhook'];
        loglines = ChatLogger.readlog(logfile);
        filelog = ChatLogger.opencurrenttxt();

        x = 1;
        for line in loglines:
            print (line);

            if '[main/INFO]: [CHAT] ' in line:
                content = line.split('[main/INFO]: [CHAT] ')[1];
                filelog.write(content);
                DiscordWebhook(url=webhookurl, content=content).execute();

            elif '[Client thread/INFO] [net.minecraft.client.gui.GuiNewChat]: [CHAT] ' in line:
                content = line.split('[Client thread/INFO] [net.minecraft.client.gui.GuiNewChat]: [CHAT] ')[1];
                filelog.write(content);
                DiscordWebhook(url=webhookurl, content=content).execute();
                

            if x > 1:
                filelog.close();
                filelog = ChatLogger.opencurrenttxt();
                x = 1;
            else:
                x += 1;


if __name__ == '__main__':
    ChatLogger.Main();