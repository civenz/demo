# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Bar(GridLayout):
    pass

class FooApp(App):
    title = 'Civen App Demo 2'

    def build(self):
        return Bar()

if __name__ == '__main__':
    FooApp().run()


###############################################################################
'''
这里是代码说明:
    01. from kivy.uix.gridlayout import GridLayout
    02. class FooApp(App): 会去同目录下查找同名的 foo.kv
    02. foo.kv 的 <Bar> 与 class Bar(GridLayout) 通信. Bar 继承 GridLayout

[foo.kv] 的<Bar>继承了 GridLayout 的设置参数, 如:
    rows: 1 ## 代表 1 行
    cols: 1 ## 代表 1 列
    
'''
###############################################################################
