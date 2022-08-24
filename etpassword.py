#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import msoffcrypto
import os
from tkinter import messagebox as msgbox

file_suffix = ["xls", "xlsx"]
ends_with = tuple(file_suffix)


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.label = ttk.Label(text='password', style="BW.TLabel")
        self.entry = ttk.Entry(self.master)
        self.label.pack()
        self.entry.pack()

    def initWidgets(self):
        # 创建按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='Open EXCEL',
                   command=self.open_file  # 绑定open_file方法
                   ).pack(side=BOTTOM, ipadx=150, ipady=100)

    def input_password(self):
        return self.entry.get()

    def open_file(self):
        # 调用askopenfile方法获取单个打开的文件
        file_path = filedialog.askdirectory(title='Please choose a path',
                                            # 只处理的文件类型
                                            initialdir='./')  # 初始目录
        print(file_path)
        self.decrypted_excel_file(file_path)
        msgbox.showinfo(title='提示', message='处理完成')

    def decrypted_excel_file(self, file_path):
        for filepath, dirs, filenames in os.walk(file_path):
            for filename in filenames:
                print(filename)
                if os.path.isdir(filename):
                    continue
                if not os.path.join(filename).endswith(ends_with):
                    continue
                encrypted = open(os.path.join(filepath, filename), "rb")
                file = msoffcrypto.OfficeFile(encrypted)
                file.load_key(password=self.entry.get())
                out_dir = os.path.join(os.path.realpath(filepath), "decrypted")
                os.makedirs(out_dir, exist_ok=True)
                with open(out_dir + "/" + filename, "wb") as f:
                    file.decrypt(f)
                encrypted.close()


root = Tk()
root.title("decrypted-cong.zheng")
App(root)
root.mainloop()
