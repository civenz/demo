# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder

## 使用 Builder 加载 kivy 代码 ##
say = Builder.load_string('''
Button:
    text: "01. Hello world!"
    background_color: 0, 0, 0, 1
    color: 1, 0, 0, 1
    font_size: 24
''')

## 创建 HelloApp ##
class HelloApp(App):

    title = 'Civen App Demo 1'

    def build(self):
        return say

## 运行 ##
if __name__ == '__main__':
    HelloApp().run()



###############################################################################
'''
这里是代码说明:

    屏幕输出: Hello world!

    背景颜色是黑色 [background_color: 0, 0, 0, 1]

    字体颜色是红色 [color: 1, 0, 0, 1]

    字体大小 24 pixels [font_size: 24]
'''
###############################################################################
