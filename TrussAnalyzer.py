#!/usr/bin/env python
"""
@author: 2Fzzzzz
"""

import wx
import preprocess as pp
import analyzer as ana

class TrussAnalyzer(wx.Frame):   #主界面

        def __init__(self, parent, id):
                wx.Frame.__init__(self, parent, id, 'TrussAnalyzer',size=(500, 320))
                panel = wx.Panel(self, -1)
                panel.SetBackgroundColour("White")
                self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
                
                menuBar = wx.MenuBar()
                menu2 = wx.Menu()
                menu2.Append(wx.NewId(), " help ")
                menuBar.Append(menu2, " MENU ")
                self.SetMenuBar(menuBar)  

                
                constraint_s = wx.StaticText(panel, wx.NewId(), "constraint?",pos=(350, 20))
                constraint_s.SetBackgroundColour("White")
                
                xpos1_s = wx.StaticText(panel, wx.NewId(), "x pos 1",pos=(10, 50))
                xpos1_s.SetBackgroundColour("White")
                
                self.xpos1 = wx.TextCtrl(panel, wx.NewId(), "",size=(100, -1),pos=(60, 50))
                self.xpos1.Bind(wx.EVT_ENTER_WINDOW, self.xpos1help)
                self.xpos1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                ypos1_s = wx.StaticText(panel, wx.NewId(), "y pos 1",pos=(10, 80))
                ypos1_s.SetBackgroundColour("White")
                
                self.ypos1 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),pos=(60, 80))
                self.ypos1.Bind(wx.EVT_ENTER_WINDOW, self.ypos1help)
                self.ypos1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                 
                xpos2_s = wx.StaticText(panel, wx.NewId(), "x pos 2",pos=(10, 110))
                xpos2_s.SetBackgroundColour("White")
                
                self.xpos2 = wx.TextCtrl(panel, wx.NewId(), "",size=(100, -1),pos=(60, 110))
                self.xpos2.Bind(wx.EVT_ENTER_WINDOW, self.xpos2help)
                self.xpos2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                ypos2_s = wx.StaticText(panel, wx.NewId(), "y pos 2",pos=(10, 140))
                ypos2_s.SetBackgroundColour("White")
                
                self.ypos2 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),pos=(60, 140))
                self.ypos2.Bind(wx.EVT_ENTER_WINDOW, self.ypos2help)
                self.ypos2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                ea_s = wx.StaticText(panel, wx.NewId(), "EA",pos=(10, 170))
                ea_s.SetBackgroundColour("White")
                
                self.ea = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),pos=(60, 170))
                self.ea.Bind(wx.EVT_ENTER_WINDOW, self.eahelp)
                self.ea.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                xforce1_s = wx.StaticText(panel, wx.NewId(), "x Force 1",pos=(170, 50))
                xforce1_s.SetBackgroundColour("White")
                
                self.xforce1 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 50))
                self.xforce1.Bind(wx.EVT_ENTER_WINDOW, self.xforce1help)
                self.xforce1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                yforce1_s = wx.StaticText(panel, wx.NewId(), "y Force 1",pos=(170, 80))
                yforce1_s.SetBackgroundColour("White")
                
                self.yforce1 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 80))
                self.yforce1.Bind(wx.EVT_ENTER_WINDOW, self.yforce1help)
                self.yforce1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                xforce2_s = wx.StaticText(panel, wx.NewId(), "x Force 2",pos=(170, 110))
                xforce2_s.SetBackgroundColour("White")
                
                self.xforce2 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 110))
                self.xforce2.Bind(wx.EVT_ENTER_WINDOW, self.xforce2help)
                self.xforce2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                yforce2_s = wx.StaticText(panel, wx.NewId(), "y Force 2",pos=(170, 140))
                yforce2_s.SetBackgroundColour("White")
                
                self.yforce2 = wx.TextCtrl(panel, wx.NewId(), "0", size=(100, -1),pos=(230, 140))
                self.yforce2.Bind(wx.EVT_ENTER_WINDOW, self.yforce2help)
                self.yforce2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.xconstraint1 = wx.CheckBox(panel, wx.NewId(), "x1", pos=(340, 50), size=(100, -1))
                self.xconstraint1.Bind(wx.EVT_ENTER_WINDOW, self.xconstraint1help)
                self.xconstraint1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.yconstraint1 = wx.CheckBox(panel, wx.NewId(), "y1", pos=(340, 80), size=(100, -1))
                self.yconstraint1.Bind(wx.EVT_ENTER_WINDOW, self.yconstraint1help)
                self.yconstraint1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.xconstraint2 = wx.CheckBox(panel, wx.NewId(), "x2", pos=(340, 110), size=(100, -1))
                self.xconstraint2.Bind(wx.EVT_ENTER_WINDOW, self.xconstraint2help)
                self.xconstraint2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.yconstraint2 = wx.CheckBox(panel, wx.NewId(), "y2", pos=(340, 140), size=(100, -1))
                self.yconstraint2.Bind(wx.EVT_ENTER_WINDOW, self.yconstraint2help)
                self.yconstraint2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.saveButton = wx.Button(panel, wx.NewId(), "SAVE", pos=(170, 170))
                self.Bind(wx.EVT_BUTTON, self.OnSave, self.saveButton)
                self.saveButton.Bind(wx.EVT_ENTER_WINDOW, self.saveButtonhelp)
                self.saveButton.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.clearButton = wx.Button(panel, wx.NewId(), "CLEAR", pos=(270, 170))
                self.Bind(wx.EVT_BUTTON, self.OnClear, self.clearButton)
                self.clearButton.Bind(wx.EVT_ENTER_WINDOW, self.clearButtonhelp)
                self.clearButton.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.startButton = wx.Button(panel, wx.NewId(), "START", pos=(370, 170))
                self.Bind(wx.EVT_BUTTON, self.OnStart, self.startButton)
                self.startButton.Bind(wx.EVT_ENTER_WINDOW, self.startButtonhelp)
                self.startButton.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.statusbar = self.CreateStatusBar() 
                
                f = open('temp.txt','w')     #覆盖原文件内容
                f.close()

                
        def OnCloseWindow(self,event):    #关闭窗口
            self.Destroy()
        def OnSave(self,event):         #保存杆件
            numbers = [0,self.xpos1.GetValue(),self.ypos1.GetValue(),int(self.xconstraint1.GetValue()),
                       int(self.yconstraint1.GetValue()),self.xforce1.GetValue(),self.yforce1.GetValue(),
                       0,self.xpos2.GetValue(),self.ypos2.GetValue(),int(self.xconstraint2.GetValue()),
                       int(self.yconstraint2.GetValue()),self.xforce2.GetValue(),self.yforce2.GetValue(),
                       self.ea.GetValue()]
            f = open('temp.txt','a')
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
        def OnMove(self, event):
            pos = event.GetPosition()
            self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))
        def xpos1help(self,event):      #状态栏帮助界面
            self.statusbar.SetStatusText("请在此输入杆件其中一节点的x坐标（暂记为节点1）")
        def ypos1help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件其中一节点的y坐标（暂记为节点1）")
        def xpos2help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件另一节点的x坐标（暂记为节点2）")
        def ypos2help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件另一节点的y坐标（暂记为节点2）")
        def xforce1help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点1的x方向上的作用力（以向右为正）")
        def yforce1help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点1的y方向上的作用力（以向上为正）")
        def xforce2help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点2的x方向上的作用力（以向右为正）")
        def yforce2help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点2的y方向上的作用力（以向上为正）")
        def eahelp(self,event):
            self.statusbar.SetStatusText("请在此输入杆件EA的大小")
        def xconstraint1help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点1在x方向上约束情况，如有约束请打勾")
        def yconstraint1help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点1在y方向上约束情况，如有约束请打勾")
        def xconstraint2help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点2在x方向上约束情况，如有约束请打勾")
        def yconstraint2help(self,event):
            self.statusbar.SetStatusText("请在此输入杆件节点2在y方向上约束情况，如有约束请打勾")
        def saveButtonhelp(self,event):
            self.statusbar.SetStatusText("保存当前输入的杆件情况，将会清除您已输入的数据以便输入下一根杆件")
        def clearButtonhelp(self,event):
            self.statusbar.SetStatusText("重置输入框的状态（已保存的杆件将被保留）")
        def startButtonhelp(self,event):
            self.statusbar.SetStatusText("启动计算程序，生成杆件图并标明受力及位移状态")
        def Leave(self,event):
            self.statusbar.SetStatusText("")
        def OnStart(self,event):    #主程序启动
            pp.preprocess()
            ana.analyzer()
            frame = Result(parent=None, id=-1)
            frame.Show()
            
class Result(wx.Frame):      #结果显示界面

        def __init__(self, parent, id):    #图片显示
            image = wx.Image('ooo.PNG', wx.BITMAP_TYPE_PNG)
            temp = image.ConvertToBitmap()
            w = temp.GetWidth()
            h = temp.GetHeight()
            w = w/3
            h = h/3
            temp=temp.ConvertToImage().Scale(w,h)
            temp=temp.ConvertToBitmap()
            size = (w,h)
            print(size)
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
