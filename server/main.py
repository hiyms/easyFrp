import sk
import threading

while(True):
    td=threading.Thread(target=sk.MyServerSocket,name="SeverMainThread")
    td.start()
    td.join()

