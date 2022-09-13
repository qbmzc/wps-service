#!/usr/bin/python3

# **
# * Copyright (c) 2020 Weitian Leung
# *
# * This file is part of pywpsrpc.
# *
# * This file is distributed under the MIT License.
# * See the LICENSE file for details.
# *
# *

import os
import subprocess
import sys
import argparse

from pywpsrpc.rpcwpsapi import (createWpsRpcInstance, wpsapi)
from pywpsrpc.common import (S_OK, QtApp)

formats = {
    "doc": wpsapi.wdFormatDocument,
    "docx": wpsapi.wdFormatXMLDocument,
    "rtf": wpsapi.wdFormatRTF,
    "html": wpsapi.wdFormatHTML,
    "pdf": wpsapi.wdFormatPDF,
    "xml": wpsapi.wdFormatXML,
}


class ConvertException(Exception):

    def __init__(self, text, hr):
        self.text = text
        self.hr = hr

    def __str__(self):
        return """Convert failed:
Details: {}
ErrCode: {}
""".format(self.text, hex(self.hr & 0xFFFFFFFF))


def add_watermark():
    hr, rpc = createWpsRpcInstance()
    if hr != S_OK:
        raise ConvertException("Can't create the rpc instance", hr)

    hr, app = rpc.getWpsApplication()
    if hr != S_OK:
        raise ConvertException("Can't get the application", hr)

    # we don't need the gui
    app.Visible = False

    # 新建一个空白文件
    doc = app.Documents.Add()  # 新建一个空白文件

    actDoc = app.ActiveDocument()
    Sect = actDoc.Sections.Item.Range.Select()
    app.ActiveWindow.ActivePane.View.SeekView = 9
    # selectObj = wordApp.Selection

    app.Selection.HeaderFooter.Shapes.AddTextEffect(0, "DOt1x © QQ980469001", "等线", 1, False, False, 0,
                                                        0)
    # shpObj = vart.Select()
    app.Selection.ShapeRange.Name = 'PowerPlusWaterMarkObject27849'


    app.Selection.ShapeRange.TextEffect.NormalizedHeight = False
    app.Selection.ShapeRange.Line.Visible = False
    app.Selection.ShapeRange.Fill.Visible = True
    app.Selection.ShapeRange.Fill.Solid
    app.Selection.ShapeRange.Fill.ForeColor = 0
    app.Selection.ShapeRange.Fill.Transparency = 0.5
    # 设置颜色
    app.Selection.ShapeRange.Fill.ForeColor.ObjectThemeColor = 14
    app.Selection.ShapeRange.Fill.ForeColor.TintAndShade = 0
    app.Selection.ShapeRange.Rotation = 315
    app.Selection.ShapeRange.LockAspectRatio = True
    app.Selection.ShapeRange.Height = 120
    app.Selection.ShapeRange.Width = 460
    app.Selection.ShapeRange.WrapFormat.AllowOverlap = True
    # app.Selection.ShapeRange.WrapFormat.Side = wdWrapNone
    app.Selection.ShapeRange.WrapFormat.Type = 3
    app.Selection.ShapeRange.WrapFormat.Side = 3
    app.Selection.ShapeRange.RelativeVerticalPosition = 0
    app.Selection.ShapeRange.Left = -999995
    app.Selection.ShapeRange.Top = -999995

    # 这里出问题了，提示没有select这个方法
    # app.Selection.HeaderFooter.Shapes("0").Select
    # app.Selection.ShapeRange.Duplicate.select
    # app.Selection.ShapeRange.IncrementLeft(-426.8)
    # app.Selection.ShapeRange.IncrementTop(403.85)
    # 关闭页眉页脚
    app.ActiveWindow.ActivePane.View.SeekView = 0
    actDoc.Save()
    actDoc.Close()
    app.Close()

    app.Quit()


if __name__ == "__main__":
    add_watermark()
