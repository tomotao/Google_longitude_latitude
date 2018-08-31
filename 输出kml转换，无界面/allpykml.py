# -*- coding: utf-8 -*-
"""
@author: Andy
"""
import tkFileDialog
from lxml import etree  #用于kml节点
from pykml.factory import KML_ElementMaker as KML
import pandas as pd
import sys
from Tkinter import *
from tkMessageBox import *
reload(sys)
sys.setdefaultencoding('utf-8')

#选择需要输出的文件路径
# xlsfile=tkFileDialog.askopenfilename(title=u"请选择需要输出的文件路径")
xlsfile=r"C:\Users\Administrator\Desktop\haishu_cell_gps_GGL.xlsx"
#读取excel
k=pd.read_excel(xlsfile,sheet_name=0)
def cell():
    #搜索并限定小区名称
    result_enodeb_cell = k.drop_duplicates([u'小区名'])
    cellname=result_enodeb_cell[u'小区名']
    cellname=list(cellname)
    fold1=KML.Folder()
    for i in range(0,len(cellname)):
        result_enodeb_cell2 = k.loc[(k[u'小区名'] == cellname[i].strip().replace("\n", ""))]
        # 选择经纬度点
        lon = result_enodeb_cell2[u"wgsLon"]
        lat = result_enodeb_cell2[u"wgsLat"]
        lon = list(lon)
        lat = list(lat)
        # 简单判断文件中的经纬度个数是否一致
        if len(lon) != len(lat):
            print 'lon != lat nums'
        # 使用第一个点创建Folder
        name=cellname[i].strip().replace("\n", "").decode('utf-8','ignore')
        ford = KML.Folder(
            KML.name(name),
            KML.Placemark(
            KML.Point(KML.coordinates(str(lon[0]) + ',' + str(lat[0]) + ',0'))
        )
        )
        # 将剩余的点追加到Folder中
        for i in range(1, len(lon)):
            ford.append(KML.Placemark(
                KML.Point(KML.coordinates(str(lon[i]) + ',' + str(lat[i]) + ',0')))
            )
        fold1.append(ford)
    # 使用etree将KML节点输出为字符串数据
    content = etree.tostring(etree.ElementTree(fold1), pretty_print=True)
    filename = "E:/google.kml"
    with open(filename.decode('utf-8', 'ignore'), 'a+') as fp:
        fp.write(content)
def Enodebname():
    #搜索并限定小区名称
    result_enodeb_cell = k.drop_duplicates([u'站名'])
    cellname=result_enodeb_cell[u'站名']
    cellname=list(cellname)
    fold1=KML.Folder()
    for i in range(0,len(cellname)):
        result_enodeb_cell2 = k.loc[(k[u'站名'] == cellname[i].strip().replace("\n", ""))]
        # 选择经纬度点
        lon = result_enodeb_cell2[u"wgsLon"]
        lat = result_enodeb_cell2[u"wgsLat"]
        lon = list(lon)
        lat = list(lat)
        # 简单判断文件中的经纬度个数是否一致
        if len(lon) != len(lat):
            print 'lon != lat nums'
        # 使用第一个点创建Folder
        name=cellname[i].strip().replace("\n", "").decode('utf-8','ignore')
        ford = KML.Folder(
            KML.name(name),
            KML.Placemark(
            KML.Point(KML.coordinates(str(lon[0]) + ',' + str(lat[0]) + ',0'))
        )
        )
        # 将剩余的点追加到Folder中
        for i in range(1, len(lon)):
            ford.append(KML.Placemark(
                KML.Point(KML.coordinates(str(lon[i]) + ',' + str(lat[i]) + ',0')))
            )
        fold1.append(ford)
    # 使用etree将KML节点输出为字符串数据
    content = etree.tostring(etree.ElementTree(fold1), pretty_print=True)
    filename = "E:/google.kml"
    with open(filename.decode('utf-8', 'ignore'), 'a+') as fp:
        fp.write(content)
def CELLID():
    #搜索并限定小区名称
    result_enodeb_cell = k.drop_duplicates([u'CELL_CELLID'])
    cellname=result_enodeb_cell[u'CELL_CELLID']
    cellname=list(cellname)
    fold1=KML.Folder()
    for i in range(0,len(cellname)):
        result_enodeb_cell2 = k.loc[(k[u'CELL_CELLID'] == cellname[i])]
        # 选择经纬度点
        lon = result_enodeb_cell2[u"wgsLon"]
        lat = result_enodeb_cell2[u"wgsLat"]
        lon = list(lon)
        lat = list(lat)
        # 简单判断文件中的经纬度个数是否一致
        if len(lon) != len(lat):
            print 'lon != lat nums'
        # 使用第一个点创建Folder
        name=cellname[i]
        ford = KML.Folder(
            KML.name(name),
            KML.Placemark(
            KML.Point(KML.coordinates(str(lon[0]) + ',' + str(lat[0]) + ',0'))
        )
        )
        # 将剩余的点追加到Folder中
        for i in range(1, len(lon)):
            ford.append(KML.Placemark(
                KML.Point(KML.coordinates(str(lon[i]) + ',' + str(lat[i]) + ',0')))
            )
        fold1.append(ford)
    # 使用etree将KML节点输出为字符串数据
    content = etree.tostring(etree.ElementTree(fold1), pretty_print=True)
    filename = "E:/google.kml"
    with open(filename.decode('utf-8', 'ignore'), 'a+') as fp:
        fp.write(content)
Button(text='CELL_CELLID', command=CELLID).pack(fill=X)
Button(text='Enodebname', command=Enodebname).pack(fill=X)
Button(text='cell', command=cell).pack(fill=X)
mainloop()