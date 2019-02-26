# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('bar.kv')

class MainScreen(Screen):
    def switchHello(self):
        if self.ids.btnId.text != 'Hello Civen!':
            self.ids.btnId.text = 'Hello Civen!'
            self.ids.btnId.font_size = 36
        else:
            self.ids.btnId.text = 'Hello world!'
            self.ids.btnId.font_size = 18


class DemoApp(App):
    title = 'Civen App Demo 3'
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    DemoApp().run()

###############################################################################
'''
这里是代码说明:
    01. from kivy.lang import Builder
    02. from kivy.uix.screenmanager import Screen
    03. Builder.load_file('bar.kv') ## 加载 kivy 代码文件 [bar.kv] ##
    04. MainScreen(Screen) ## MainScreen 继承 Screen 窗口类 ##
    05. Kivy Button -> on_release 执行 switchHello() 切换内容
    
'''
###############################################################################
