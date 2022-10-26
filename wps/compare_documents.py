#!/usr/bin/python3
# -- coding: utf-8 -
# **
# * Copyright (c) 2020 cong.zheng
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

pid = None


class ConvertException(Exception):

    def __init__(self, text, hr):
        self.text = text
        self.hr = hr

    def __str__(self):
        return """Convert failed:
Details: {}
ErrCode: {}
""".format(self.text, hex(self.hr & 0xFFFFFFFF))


def compare_documents(original_file, revised_file, abort_on_fails=False):
    hr, rpc = createWpsRpcInstance()
    if hr != S_OK:
        raise ConvertException("Can't create the rpc instance", hr)

    hr, app = rpc.getWpsApplication()
    if hr != S_OK:
        raise ConvertException("Can't get the application", hr)
    global pid
    hr, pid = rpc.getProcessPid()
    if hr != S_OK:
        raise ConvertException("Can't  get the PID", hr)
    print("PID:{}".format(pid))
    # we don't need the gui
    app.Visible = False

    docs = app.Documents

    def _handle_result(hr):
        if abort_on_fails and hr != S_OK:
            raise ConvertException("open file failed", hr)

    hr, ori_doc = docs.Open(original_file, PasswordDocument='xxx', ReadOnly=True)
    if hr != S_OK:
        return _handle_result(hr)
    hr, rev_doc = docs.Open(revised_file, PasswordDocument='xxx', ReadOnly=True)
    if hr != S_OK:
        return _handle_result(hr)

    hr, act_doc = app.CompareDocuments(ori_doc, rev_doc)

    out_dir = os.path.dirname(os.path.realpath(original_file)) + "/compare"
    os.makedirs(out_dir, exist_ok=True)
    new_file = out_dir + "/" + os.path.splitext(os.path.basename(original_file))[0] + "_compare.docx"



    ori_doc.Close()
    rev_doc.Close()
    act_doc.SaveAs(new_file)
    act_doc.Close()
    app.Quit()


if __name__ == "__main__":
    r = compare_documents('/root/Document/1.docx', '/root/Documents/2.docx')
    print(r)
