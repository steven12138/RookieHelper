import requests
from bs4 import BeautifulSoup
import time
import tkinter.messagebox
import tkinter as tk
import hashlib
<<<<<<< Updated upstream

#
=======
import re
>>>>>>> Stashed changes


usr_name=""
usr_pwd=""

window=tk.Tk()
window.title('rookie登陆')
window.geometry('450x190')
window.resizable(False,False,)

f=False

tk.Label(window,text='登录到rookie,请确保用户名密码正确').place(x=120,y=10)
tk.Label(window,text='用户名:').place(x=100,y=50)
tk.Label(window,text='密码:').place(x=100,y=90)
tk.Label(window,text='Made By steven12138').place(x=310,y=170)

var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=50)
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd)
entry_usr_pwd.place(x=160,y=90)
def usr_log_in():
    global usr_name
    global usr_pwd
    global f
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    usr_pwd=hashlib.new('md5',usr_pwd.encode('utf-8')).hexdigest()
    f=True
    window.destroy()

bt_login=tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=200,y=130)
window.mainloop()

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False,False,)
        self.root.wm_attributes('-topmost',1)
        self.root.title('Rookie系统填写小助手')
        self.label = tk.Label(text="")
        self.label.pack()
        self.root.geometry('300x20')
        data = {
            "_csrfToken": "",
            "loginFailCount": "0",
            "password": usr_pwd,
            "username": usr_name,
            "loginPassword": ""
        }
        loginurl = "http://rookie.pkuschool.edu.cn/user-login"
        self.x = requests.session()
        self.x.post(loginurl,data=data)
        self.f=0
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        url = "http://rookie.pkuschool.edu.cn/stup-issues"
        now = time.strftime("%H:%M:%S")
        r = self.x.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        patternNo = "\u5c1a\u672a\u88ab\u5ba1\u9605"
        patternIng = "\u6b63\u5728\u88ab\u5ba1\u9605"
        st = "".join(soup.select('div[class="pull-right"]')[0])
        if (not re.search(patternNo , st[0:17]) == None):
            pass
        else:
            if (not re.search(patternIng , st[0:17]) == None):
                pass
            else:
                if self.f==0:
                    tkinter.messagebox.showwarning('提示', '已经完成审阅')
                    print('\a')
                self.f=1
                now="已经完成审阅"
        now=time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))+" "+st[0:17]
        self.label.configure(text = now)
        sec=60
        self.root.after(sec*1000,self.update_clock)
if f:
    app = App()