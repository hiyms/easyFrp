import socket
import json
import os
import sys
import threading

class MyServerSocket():
    def __init__(self):
        self.blacklist=json.load(r'./blacklist.json')
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bing(('',22000))
        self.s.listen(50)
        while(True):
            conn,address = self.s.accept()   # 死循环接受连接
            if(self.blacklist["state"] == True):
                if(address in self.blacklist["BlackList"]):
                    conn.sendall("Error: You are on our blacklist, please contact the administrator.".encode())
                    conn.shutdown()
            threading.Thread(target=self.ConnectionHandling,args=(conn,address)).start()

    def access(self,port):
        if port < 1024 or 65535 < port:
            # privileged port
            # out of range
            return False

        if 'win32' == sys.platform:
            cmd = 'netstat -aon|findstr ":%s "' % port
        elif 'linux' == sys.platform:
            cmd = 'netstat -aon|grep ":%s "' % port
        else:
            print('Unsupported system type %s' % sys.platform)
            return False

        with os.popen(cmd, 'r') as f:
            if '' != f.read():
                print('Port %s is occupied' % port)
                return False
            else:
                return True

    def ConnectionHandling(self,conn:socket.socket,address): #连接处理函数
        conn.settimeout(100)
        data = conn.recv(4096)
        data = json.loads(data.decode())
        replydata = self.EventHandling(data)
        conn.sendall(json.dumps(replydata).encode())
        conn.shutdown()

    def EventHandling(self,data:dict) -> dict:   # 客户端数据处理函数
        ans={}
        ans["label"] = "reply"
        if(dict["label"] == "Get_port"):
            if(self.access(dict[port])):
                ans["state"] = True
            else:
                ans["state"] = False
        return ans

