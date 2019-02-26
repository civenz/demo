# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

Builder.load_file('bar.kv')

class SwitchScreen(ScreenManager):
    pass

class DemoApp(App):
    title = 'Civen App Demo 4'
    def build(self):
        return SwitchScreen()

if __name__ == '__main__':
    DemoApp().run()



###############################################################################
'''
这里是代码说明:
    01. from kivy.lang import Builder
    02. kivy.uix.screenmanager import ScreenManager
    03. Builder.load_file('bar.kv') ## 加载 kivy 代码文件 [bar.kv] ##
    04. SwitchScreen(ScreenManager) ## SwitchScreen 继承 ScreenManager 窗口类 ##
    05. [bar.kv] on_release 以 ScreenManager.Screen.name 切换. 
    
'''
###############################################################################
