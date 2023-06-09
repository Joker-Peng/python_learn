#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 10, 2018 05:22:01 PM JST  platform: Windows NT

import sys
import os

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

# 导入目录查看的方法
from tkinter.filedialog import askdirectory
from tkinter import messagebox


# 重要的方法！！！
def set_Tk_var():
    # 全局变量 目的是可以改变文本框的内容
    global lujing
    # lujing是路径输入窗口的一个字符串变量对象
    lujing = tk.StringVar()
    # 设定初始值
    lujing.set("选择要批量重命名的文件目录")
    # 想要替换掉字符串
    global old_char
    old_char = tk.StringVar()
    # 新的字符串
    global new_char
    new_char = tk.StringVar()


def cancle():
    print('正在执行【cancle()】方法')
    # 设置一个退出的变量 执行跳出message的方法 返回值是布尔类型
    byebye = messagebox.askokcancel("退出", "真的要退出么")
    # 如果返回值是true的话
    if byebye:
        # 执行关闭窗口
        destroy_window()
        sys.stdout.flush()


def do_rename():
    global lj
    try:
        # 获取目录下所有的文件名称的列表
        all_file = os.listdir(lj)
    except Exception as e:
        print("傻吊用户")
        messagebox.showinfo('提示', '选择了非法目录')
    else:
        # 获取需要替换的字符
        old = old_char.get()
        # 获取新字符
        new = new_char.get()
        # 查找列表内相同字段并惊醒替换
        for item in os.listdir(lj):
            if old in item:
                newitem = item.replace(old, new)
                os.rename(lj + "/" + item, lj + "/" + newitem)
        messagebox.showinfo('成功', '替换完成')
        print(all_file)
        print('执行完【do_rename】方法')
    finally:
        sys.stdout.flush()

    # #获取需要替换的字符
    # old = old_char.get()
    # #获取新字符
    # new = new_char.get()
    # #查找列表内相同字段并惊醒替换
    # for item in os.listdir(lj):
    #     if old in item:
    #         newitem = item.replace(old,new)
    #         os.rename(lj+"\\"+item,lj+"\\"+newitem)
    # print(all_file)


def selectPath():
    # 路径的全局变量
    global lj
    # 选择目录跳出窗口的方法
    lj = askdirectory()
    if not lj:
        lujing.set("您未选择任何目录")
    else:
        # 路径赋值给路径输入框的lujing变量
        lujing.set(lj)
        print('rename_support.selectPath')
        sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

#
# if __name__ == '__main__':
#     import rename_support.py