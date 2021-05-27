#// /py src/main/java/org/Eclient/client/module/modules/misc/privateserverfinder.py

#// I reccommend starting this file outside of minecraft right now 

from src.main.java.org.Eclient.client.module.modules.misc.mcstatus import MinecraftServer;
import threading;
from queue import Queue;
import os;
import shutil;
import os;
import json;
from mine import *;



class PrivateServerFinder:
    @staticmethod
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    @staticmethod
    def scan_ip_and_port(ip, iptxtfle, ekis) -> list:
        try:
            server = MinecraftServer.lookup("{0}:{1}".format(ip, ekis));
            status = server.status();
            latency = server.ping();
            with open(iptxtfle, "a+") as ips:
                ips.write("{0}:{1}\n".format(ip, ekis));
            ips.close();
            return [status.players.online, status.latency, latency];
        except:
            return [];

    @staticmethod
    def fill_queue(port_list: range, queue):
        for port in port_list:
            queue.put(port);

    @staticmethod
    def worker(queue, open_ports):
        while not queue.empty():
            port = queue.get();
            if PrivateServerFinder.scan_ip_and_port(port):
                open_ports.append(port);

    @staticmethod
    def Main():
        modulenm = str(__class__.__name__);
        configs: dict = PrivateServerFinder.loadconfig()['modules'][modulenm];
        halfip = configs['halfip'];

        iptxtflepth = (os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\misc\\ips');
        
        for exxx in range(0, 256):
            ip = "{0}{1}".format(halfip, exxx);
            print(ip);
            
            queue = Queue();
            open_ports = [];



            port_list: range = range(25500, 25600)
            PrivateServerFinder.fill_queue(port_list, queue)

            thread_list = []

            for t in range(100):
                thread = threading.Thread(target=PrivateServerFinder.worker, args=(queue, open_ports,))
                thread_list.append(thread)

            for thread in thread_list:
                thread.start()

            for thread in thread_list:
                thread.join()


        ipint = halfip.split('.')[0]
        if not os.path.exists("{0}\\{1}\\".format(iptxtflepth, ipint)):
            os.makedirs("{0}\\{1}".format(iptxtflepth, ipint))

        shutil.move(iptxtfle, iptxtflepth+"\\"+ipint)


if __name__ == '__main__':
    PrivateServerFinder.Main();