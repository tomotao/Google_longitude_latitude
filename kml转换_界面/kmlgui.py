# -*- coding: utf-8 -*-
import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import xlrd
import xlwt
import math
from xlutils.copy import copy
root=Tk()
root.title("google经纬度转换 by:三年") #创建标题
root.geometry('500x360+400+200')#设置高宽和初始停留位置
root["bg"]="white" #设置背景颜色
root.attributes("-alpha", 1.0) #设置背景虚化程度
# 创建一个菜单项，类似于导航栏
menubar=Menu(root,tearoff=0)
root.config(menu=menubar)
#创建退出事件
def _quit():
    """结束主事件循环"""
    root.quit()      # 关闭窗口
    root.destroy()   # 将所有的窗口小部件进行销毁，应该有内存回收的意思
    exit()
# 创建一个名为文件的菜单项,tearoff用于去掉自带的虚线
fmenu1=Menu(root,tearoff=0)
menubar.add_cascade(label="kml文件转换",menu=fmenu1)
#添加文件菜单下的下拉选项
fmenu1.add_command(label="小区名—>KML")
fmenu1.add_command(label="CELLID—>KML")
fmenu1.add_command(label="站名—>KML")
fmenu1.add_command(label="Exit",command=_quit)
# 创建一个名为编辑的菜单项,tearoff用于去掉自带的虚线
def gaode():

fmenu2=Menu(root,tearoff=0)
menubar.add_cascade(label="经纬度转换",menu=fmenu2)
#添加编辑菜单下的下拉选项
fmenu2.add_command(label="高德—>WGS84",command=gaode)
fmenu2.add_command(label="百度—>WGS84")
# 创建一个名为视图的菜单项,tearoff用于去掉自带的虚线
fmenu3=Menu(root,tearoff=0)
menubar.add_cascade(label="其他功能",menu=fmenu3)
#添加视图菜单下的下拉选项
fmenu3.add_command(label="待添加")
fmenu3.add_command(label="待添加")
def gui_info():
    showwarning('版本', 'google.kml v1.0')
def gui_about():
    showinfo('info', '版权所有 翻版必究')
# 创建一个名为关于的菜单项,tearoff用于去掉自带的虚线
fmenu4=Menu(root,tearoff=0)
menubar.add_cascade(label="关于",menu=fmenu4)
#添加关于菜单下的下拉选项
fmenu4.add_command(label="版本信息",command=gui_info)
fmenu4.add_command(label="About",command=gui_about)
root.mainloop()