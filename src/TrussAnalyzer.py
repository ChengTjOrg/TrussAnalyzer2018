#!/usr/bin/env python
"""
@author: 2Fzzzzz
"""

import wx
import pre_process as pp

class TrussAnalyzer(wx.Frame):   #主界面

        def __init__(self, parent, id):
                wx.Frame.__init__(self, parent, id, 'TrussAnalyzer',size=(500, 300))
                panel = wx.Panel(self, -1)
                panel.SetBackgroundColour("White")
                self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
                
                constraint_s = wx.StaticText(panel, wx.NewId(), "constraint?",pos=(350, 20))
                constraint_s.SetBackgroundColour("White")
                
                xpos1_s = wx.StaticText(panel, wx.NewId(), "x pos 1",pos=(10, 50))
                xpos1_s.SetBackgroundColour("White")
                
                self.xpos1 = wx.TextCtrl(panel, wx.NewId(), "",size=(100, -1),pos=(60, 50))
                
                ypos1_s = wx.StaticText(panel, wx.NewId(), "y pos 1",pos=(10, 80))
                ypos1_s.SetBackgroundColour("White")
                
                self.ypos1 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),pos=(60, 80))
                 
                xpos2_s = wx.StaticText(panel, wx.NewId(), "x pos 2",pos=(10, 110))
                xpos2_s.SetBackgroundColour("White")
                
                self.xpos2 = wx.TextCtrl(panel, wx.NewId(), "",size=(100, -1),pos=(60, 110))
                
                ypos2_s = wx.StaticText(panel, wx.NewId(), "y pos 2",pos=(10, 140))
                ypos2_s.SetBackgroundColour("White")
                
                self.ypos2 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),pos=(60, 140))
                
                ea_s = wx.StaticText(panel, wx.NewId(), "EA",pos=(10, 170))
                ea_s.SetBackgroundColour("White")
                
                self.ea = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),pos=(60, 170))
                
                xforce1_s = wx.StaticText(panel, wx.NewId(), "x Force 1",pos=(170, 50))
                xforce1_s.SetBackgroundColour("White")
                
                self.xforce1 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 50))
                
                yforce1_s = wx.StaticText(panel, wx.NewId(), "y Force 1",pos=(170, 80))
                yforce1_s.SetBackgroundColour("White")
                
                self.yforce1 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 80))
                
                xforce2_s = wx.StaticText(panel, wx.NewId(), "x Force 2",pos=(170, 110))
                xforce2_s.SetBackgroundColour("White")
                
                self.xforce2 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 110))
                
                yforce2_s = wx.StaticText(panel, wx.NewId(), "y Force 2",pos=(170, 140))
                yforce2_s.SetBackgroundColour("White")
                
                self.yforce2 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 140))
                
                xsize_s = wx.StaticText(panel, wx.NewId(), "x size",pos=(10, 220))
                xsize_s.SetBackgroundColour("White")
                
                self.xsize = wx.TextCtrl(panel, wx.NewId(), "100", size=(100, -1),pos=(60, 220))
                
                ysize_s = wx.StaticText(panel, wx.NewId(), "y size",pos=(170, 220))
                ysize_s.SetBackgroundColour("White")
                
                self.xsize = wx.TextCtrl(panel, wx.NewId(), "100", size=(100, -1),pos=(230, 220))
                
                self.xconstraint1 = wx.CheckBox(panel, wx.NewId(), "x1", pos=(340, 50), size=(100, -1))
                self.yconstraint1 = wx.CheckBox(panel, wx.NewId(), "y1", pos=(340, 80), size=(100, -1))
                self.xconstraint2 = wx.CheckBox(panel, wx.NewId(), "x2", pos=(340, 110), size=(100, -1))
                self.yconstraint2 = wx.CheckBox(panel, wx.NewId(), "y2", pos=(340, 140), size=(100, -1))
                
                saveButton = wx.Button(panel, wx.NewId(), "SAVE", pos=(200, 170))
                self.Bind(wx.EVT_BUTTON, self.OnSave, saveButton)
                
                clearButton = wx.Button(panel, wx.NewId(), "CLEAR", pos=(300, 170))
                self.Bind(wx.EVT_BUTTON, self.OnClear, clearButton)
                
                startButton = wx.Button(panel, wx.NewId(), "START", pos=(350, 220))
                self.Bind(wx.EVT_BUTTON, self.OnStart, startButton)
                
                f = open('number.txt','w')     #覆盖原文件内容
                f.close()

                
        def OnCloseWindow(self,event):    #关闭窗口
            self.Destroy()
        def OnSave(self,event):         #保存杆件
            numbers = [0,int(self.xpos1.GetValue()),int(self.ypos1.GetValue()),int(self.xconstraint1.GetValue()),
                       int(self.yconstraint1.GetValue()),int(self.xforce1.GetValue()),int(self.yforce1.GetValue()),
                       0,int(self.xpos2.GetValue()),int(self.ypos2.GetValue()),int(self.xconstraint2.GetValue()),
                       int(self.yconstraint2.GetValue()),int(self.xforce2.GetValue()),int(self.yforce2.GetValue()),
                       int(self.ea.GetValue())]
            f = open('number.txt','a')
            for e in numbers:
                f.write(str(e))
                f.write(' ')
            f.write('\n')
            f.close()
            self.OnReset()
            self.OnSuccess()
        def OnClear(self,event):     #清除输入内容
            self.xpos1.SetValue("")
            self.ypos1.SetValue("")
            self.xpos2.SetValue("")
            self.ypos2.SetValue("")
            self.ea.SetValue("")
            self.xforce1.SetValue("0")
            self.yforce1.SetValue("0")
            self.xforce2.SetValue("0")
            self.yforce2.SetValue("0")
            self.xconstraint1.SetValue(0)
            self.yconstraint1.SetValue(0)
            self.xconstraint2.SetValue(0)
            self.yconstraint2.SetValue(0)
        def OnReset(self):         #清除输入内容
            self.xpos1.SetValue("")
            self.ypos1.SetValue("")
            self.xpos2.SetValue("")
            self.ypos2.SetValue("")
            self.ea.SetValue("")
            self.xforce1.SetValue("0")
            self.yforce1.SetValue("0")
            self.xforce2.SetValue("0")
            self.yforce2.SetValue("0")
            self.xconstraint1.SetValue(0)
            self.yconstraint1.SetValue(0)
            self.xconstraint2.SetValue(0)
            self.yconstraint2.SetValue(0)
        def OnSuccess(self):      #弹出成功窗口
            dlg = wx.MessageDialog(None, "Success!",'Success',wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        def OnStart(self,event):    #主程序启动
            pp.preprocess()
            frame = Result(parent=None, id=-1)
            frame.Show()
            
class Result(wx.Frame):      #结果显示界面

        def __init__(self, parent, id):    #图片显示
            image = wx.Image('out.PNG', wx.BITMAP_TYPE_PNG)
            temp = image.ConvertToBitmap()
            size = temp.GetWidth(), temp.GetHeight()
            wx.Frame.__init__(self, parent, id, 'Result',size=size)
            panel = wx.Panel(self, -1)
            panel.SetBackgroundColour("White")
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
            self.bmp = wx.StaticBitmap(panel,-1,temp,pos=(0, 0),size=size)  
        
        def OnCloseWindow(self,event):    #关闭窗口
            self.Destroy()

if __name__ == '__main__':
        app = wx.PySimpleApp()
        frame = TrussAnalyzer(parent=None, id=-1)
        frame.Show()
        app.MainLoop()
