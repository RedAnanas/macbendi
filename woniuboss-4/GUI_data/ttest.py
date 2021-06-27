#! /usr/bin/env python
# coding = utf-8
# editor:wang
import os
with open('../GUI_data/leave_note.jpg','rb+') as f:
    print(f)

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = dir_path+'\\GUI_data\\leave_npte.jpg'
print(path)

