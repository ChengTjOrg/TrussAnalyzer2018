#!/usr/bin/env python
"""
@author: 2Fzzzzz
"""

import wx
import PreProcess as pp
import Analyzer as ana
import PostProcess as post
import numpy

class TrussAnalyzer(wx.Frame):                        #主界面

        def __init__(self, parent, id):
                wx.Frame.__init__(self, parent, id, 'TrussAnalyzer',size=(500, 700))
                self.panel = wx.Panel(self, -1)
                self.panel.SetBackgroundColour("White")
                self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
                
                menu = wx.Menu()
                menu.AppendSeparator()
                exit = menu.Append(-1, "Exit")
                self.Bind(wx.EVT_MENU, self.OnExit, exit)
                helpmenu = wx.Menu()
                help = helpmenu.Append(wx.NewId(), "Help")
                self.Bind(wx.EVT_MENU, self.OnHelp, help)
                about = helpmenu.Append(wx.NewId(), "About")
                self.Bind(wx.EVT_MENU, self.OnAbout, about)
                menuBar = wx.MenuBar()
                menuBar.Append(menu, " Menu ")
                menuBar.Append(helpmenu, " Help ")
                self.SetMenuBar(menuBar)
                
                constraint_s = wx.StaticText(self.panel, wx.NewId(), "constraint?",pos=(350, 20))
                constraint_s.SetBackgroundColour("White")
                
                xpos1_s = wx.StaticText(self.panel, wx.NewId(), "x pos 1",pos=(10, 50))
                xpos1_s.SetBackgroundColour("White")
                
                self.xpos1 = wx.TextCtrl(self.panel, wx.NewId(), "",size=(100, -1),pos=(60, 50))
                self.xpos1.Bind(wx.EVT_ENTER_WINDOW, self.xpos1help)
                self.xpos1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                ypos1_s = wx.StaticText(self.panel, wx.NewId(), "y pos 1",pos=(10, 80))
                ypos1_s.SetBackgroundColour("White")
                
                self.ypos1 = wx.TextCtrl(self.panel, wx.NewId(), "", size=(100, -1),pos=(60, 80))
                self.ypos1.Bind(wx.EVT_ENTER_WINDOW, self.ypos1help)
                self.ypos1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                 
                xpos2_s = wx.StaticText(self.panel, wx.NewId(), "x pos 2",pos=(10, 110))
                xpos2_s.SetBackgroundColour("White")
                
                self.xpos2 = wx.TextCtrl(self.panel, wx.NewId(), "",size=(100, -1),pos=(60, 110))
                self.xpos2.Bind(wx.EVT_ENTER_WINDOW, self.xpos2help)
                self.xpos2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                ypos2_s = wx.StaticText(self.panel, wx.NewId(), "y pos 2",pos=(10, 140))
                ypos2_s.SetBackgroundColour("White")
                
                self.ypos2 = wx.TextCtrl(self.panel, wx.NewId(), "", size=(100, -1),pos=(60, 140))
                self.ypos2.Bind(wx.EVT_ENTER_WINDOW, self.ypos2help)
                self.ypos2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                ea_s = wx.StaticText(self.panel, wx.NewId(), "EA",pos=(10, 170))
                ea_s.SetBackgroundColour("White")
                
                self.ea = wx.TextCtrl(self.panel, wx.NewId(), "", size=(100, -1),pos=(60, 170))
                self.ea.Bind(wx.EVT_ENTER_WINDOW, self.eahelp)
                self.ea.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                xforce1_s = wx.StaticText(self.panel, wx.NewId(), "x Force 1",pos=(170, 50))
                xforce1_s.SetBackgroundColour("White")
                
                self.xforce1 = wx.TextCtrl(self.panel, wx.NewId(), "0", size=(100, -1),pos=(230, 50))
                self.xforce1.Bind(wx.EVT_ENTER_WINDOW, self.xforce1help)
                self.xforce1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave) 
                
                yforce1_s = wx.StaticText(self.panel, wx.NewId(), "y Force 1",pos=(170, 80))
                yforce1_s.SetBackgroundColour("White")
                
                self.yforce1 = wx.TextCtrl(self.panel, wx.NewId(), "0", size=(100, -1),pos=(230, 80))
                self.yforce1.Bind(wx.EVT_ENTER_WINDOW, self.yforce1help)
                self.yforce1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                xforce2_s = wx.StaticText(self.panel, wx.NewId(), "x Force 2",pos=(170, 110))
                xforce2_s.SetBackgroundColour("White")
                
                self.xforce2 = wx.TextCtrl(self.panel, wx.NewId(), "0", size=(100, -1),pos=(230, 110))
                self.xforce2.Bind(wx.EVT_ENTER_WINDOW, self.xforce2help)
                self.xforce2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                yforce2_s = wx.StaticText(self.panel, wx.NewId(), "y Force 2",pos=(170, 140))
                yforce2_s.SetBackgroundColour("White")
                
                self.yforce2 = wx.TextCtrl(self.panel, wx.NewId(), "0", size=(100, -1),pos=(230, 140))
                self.yforce2.Bind(wx.EVT_ENTER_WINDOW, self.yforce2help)
                self.yforce2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.xconstraint1 = wx.CheckBox(self.panel, wx.NewId(), "x1", pos=(340, 50), size=(100, -1))
                self.xconstraint1.Bind(wx.EVT_ENTER_WINDOW, self.xconstraint1help)
                self.xconstraint1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.yconstraint1 = wx.CheckBox(self.panel, wx.NewId(), "y1", pos=(340, 80), size=(100, -1))
                self.yconstraint1.Bind(wx.EVT_ENTER_WINDOW, self.yconstraint1help)
                self.yconstraint1.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.xconstraint2 = wx.CheckBox(self.panel, wx.NewId(), "x2", pos=(340, 110), size=(100, -1))
                self.xconstraint2.Bind(wx.EVT_ENTER_WINDOW, self.xconstraint2help)
                self.xconstraint2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.yconstraint2 = wx.CheckBox(self.panel, wx.NewId(), "y2", pos=(340, 140), size=(100, -1))
                self.yconstraint2.Bind(wx.EVT_ENTER_WINDOW, self.yconstraint2help)
                self.yconstraint2.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.saveButton = wx.Button(self.panel, wx.NewId(), "SAVE", pos=(170, 170))
                self.Bind(wx.EVT_BUTTON, self.OnSave, self.saveButton)
                self.saveButton.Bind(wx.EVT_ENTER_WINDOW, self.saveButtonhelp)
                self.saveButton.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.clearButton = wx.Button(self.panel, wx.NewId(), "CLEAR", pos=(270, 170))
                self.Bind(wx.EVT_BUTTON, self.OnClear, self.clearButton)
                self.clearButton.Bind(wx.EVT_ENTER_WINDOW, self.clearButtonhelp)
                self.clearButton.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.startButton = wx.Button(self.panel, wx.NewId(), "START", pos=(370, 170))
                self.Bind(wx.EVT_BUTTON, self.OnStart, self.startButton)
                self.startButton.Bind(wx.EVT_ENTER_WINDOW, self.startButtonhelp)
                self.startButton.Bind(wx.EVT_LEAVE_WINDOW, self.Leave)
                
                self.statusbar = self.CreateStatusBar() 
                
                f = open('temp.txt','w')              #覆盖原文件内容
                f.close()
                
        def OnCloseWindow(self,event):                #关闭窗口
            self.Destroy()
        def OnHelp(self,event):
            frame = Help(parent=None, id=-1)
            frame.Show()
        def OnAbout(self,event):
            frame = About(parent=None, id=-1)
            frame.Show()
        def OnExit(self,event):
            self.Close()
        def OnSave(self,event):                       #保存杆件
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
            '''
            number = numpy.loadtxt('temp.txt') 
            a = number.ndim
            if a==1:
                pass
            else:
                self.OnShow()
            '''
            self.OnSuccess()
        def OnClear(self,event):                      #清除输入内容
            self.OnReset()
        def OnReset(self):                            #清除输入内容
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
        def OnSuccess(self):                          #弹出成功窗口
            dlg = wx.MessageDialog(None, "Success!",'Success',wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        def xpos1help(self,event):                    #状态栏帮助界面
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
        def OnShow(self):                             #结构图片实时显示
            post.UncalculatedPostProcess()
            image = wx.Image('fig.PNG', wx.BITMAP_TYPE_PNG)
            temp = image.ConvertToBitmap()
            w = temp.GetWidth()
            h = temp.GetHeight()
            w = w/10
            h = h/10
            temp=temp.ConvertToImage().Scale(w,h)
            temp=temp.ConvertToBitmap()
            size = (w,h)
            self.bmp = wx.StaticBitmap(self.panel,-1,temp,pos=(0, 250),size=size)
            self.panel.Refresh()
        def OnStart(self,event):                      #主程序启动
            pp.preprocess()
            ana.analyzer()
            post.CalculatedPostProcess()
            frame = Result(parent=None, id=-1)
            frame.Show()
            
class Result(wx.Frame):                               #最终结果显示界面

        def __init__(self, parent, id):               #图片显示
            image = wx.Image('fig.PNG', wx.BITMAP_TYPE_PNG)
            temp = image.ConvertToBitmap()
            w = temp.GetWidth()
            h = temp.GetHeight()
            w = w/5
            h = h/5
            temp=temp.ConvertToImage().Scale(w,h)
            temp=temp.ConvertToBitmap()
            size = (w,h)
            wx.Frame.__init__(self, parent, id, 'Result',size=(w,h*1.2))
            panel = wx.Panel(self, -1)
            panel.SetBackgroundColour("White")
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
            self.bmp = wx.StaticBitmap(panel,-1,temp,pos=(0, 0),size=size)  
            
        def OnCloseWindow(self,event):                #关闭窗口
            self.Destroy()
            
class Help(wx.Frame):                                 #帮助界面

        def __init__(self, parent, id):    
            wx.Frame.__init__(self, parent, id, 'Help',size=(300,320))
            panel = wx.Panel(self, -1)
            panel.SetBackgroundColour("White")
            wx.StaticText(panel, -1, "  根据下方状态栏的提示，请在给定空格中\n"
                                     "分别输入一根杆件的两点坐标，两点的x，\n"
                                     "y方向上受力情况以及约束情况。输入完毕后\n"
                                     "按下SAVE键保存所输入的内容。系统将记录\n"
                                     "你输入的杆件情况并帮你清除已输入的数据\n"
                                     "以便你输入下一根杆件的情况。你已输入的\n"
                                     "杆件将在输入区域下方以图片的形式为你展示。\n"
                                     "当你将所有杆件的情况输入完毕后，按下START\n"
                                     "按键，将开始进行受力分析。最终将生成一张\n"
                                     "杆件的受力及位移分析图，以弹窗的形式\n"
                                     "展现，此图片也能在同一文件夹中找到。\n"
                                     "注意：在输入一根杆件时你必须把受力和\n"
                                     "约束完整地输入，即便你可能之前已经输入\n"
                                     "了一次。（下一版本将得到改进）", (20,20))
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
        def OnCloseWindow(self,event):                #关闭窗口
            self.Destroy()
            
class About(wx.Frame):                                 #帮助界面

        def __init__(self, parent, id):    
            wx.Frame.__init__(self, parent, id, 'About',size=(450,320))
            panel = wx.Panel(self, -1)
            panel.SetBackgroundColour("White")
            name = wx.StaticText(panel, -1, "TrussAnalyzer 1.0", (100, 50), (160, -1), wx.ALIGN_CENTER)
            font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            name.SetFont(font)
            wx.StaticText(panel, -1, "Author: 2Fzzzzz, Nicole and Zeyu XU", (100, 100))
            wx.StaticText(panel, -1, "Special Thanks: Chengwei", (100, 120))
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
        def OnCloseWindow(self,event):                #关闭窗口
            self.Destroy()

if __name__ == '__main__':
        app = wx.PySimpleApp()
        frame = TrussAnalyzer(parent=None, id=-1)
        frame.Show()
        app.MainLoop()
