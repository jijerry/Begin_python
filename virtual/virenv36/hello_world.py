# 绝对坐标
import wx
# app = wx.App()
# win = wx.Frame(None, title='文本编辑器', size=(410, 335))
# win.Show()
# loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(80, 25))
# saveButton = wx.Button(win, label='Save', pos=(315, 5), size=(80, 25))
# filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
# contexts = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style= wx.TE_MULTILINE | wx.HSCROLL)
# app.MainLoop()

# 相对坐标
import wx

# def load(event):
#     file = open(filename.GetValue())
#     contexts.SetValue(file.read())
#     file.close()
#
# def save(event):
#     file = open(filename.GetValue(), 'w')
#     file.write(contexts.GetValue())
#     file.close()
#
# app = wx.App()
# win = wx.Frame(None, title = 'Simple Editor', size = (410, 335))
# bkg = wx.Panel(win)
#
# loadButton = wx.Button(bkg, label='Open')
# loadButton.Bind(wx.EVT_BUTTON, load)
# saveButton = wx.Button(bkg, label='Save')
# saveButton.Bind(wx.EVT_BUTTON, save)
# filename = wx.TextCtrl(bkg)
# contexts = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)
#
# hbox = wx.BoxSizer()
# hbox.Add(filename, proportion=1, flag=wx.EXPAND)
# hbox.Add(saveButton, proportion = 0, flag = wx.LEFT, border = 5)
# hbox.Add(loadButton, proportion = 0, flag = wx.LEFT, border = 5)
#
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
# vbox.Add(contexts, proportion=1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)
#
# bkg.SetSizer(vbox)
# win.Show()
#
# app.MainLoop()


import sqlite3
conn = sqlite3.connect('somedatabase.db')
curs = conn.cursor()        # 返回连接的游标对象
print(curs)
conn.commit()
conn.close()