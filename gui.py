import tkinter as tk
import frp
import threading
import time





class myTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("easyFrp for TDR")
        self.geometry("300x200")
        self.label=tk.Label(text="本地端口")
        self.label.grid(row=1)
        self.entry1=tk.Entry()
        self.entry1.grid(row=1,column=1)
        self.label2=tk.Label(text="远程端口")
        self.label2.grid(row=2)
        self.entry2 = tk.Entry()
        self.entry2.grid(row=2, column=1)
        self.button=tk.Button(text="运行",command=self.easyRun)
        self.button.grid()

    def RunButton(self):
        myfrp = frp.MyFrp()
        time.sleep(1)
        l1=self.entry1.get()
        l2=self.entry2.get()
        myfrp.RunFrp(l1,l2,frp.ConnectionProtocol.TCP)
        # threading.Thread(target=myfrp.RunFrp,args=(l1,l2,frp.ConnectionProtocol.TCP))

    def easyRun(self):
        t1=threading.Thread(target=self.RunButton)
        t1.start()
        time.sleep(1)


def main():
    mytk=myTk()
    mytk.mainloop()


if __name__ == '__main__':
    main()
