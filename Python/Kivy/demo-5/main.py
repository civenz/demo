# -*- coding: utf-8 -*-


###############################################################################
## 读取配置文件 ##
from configparser import ConfigParser
mainCfg = ConfigParser()
mainCfg.read('includes/config.ini', encoding='utf-8')
#print(fontCfg.sections())

cfgFontPath = mainCfg.get('font', 'path')
cfgFontName = mainCfg.get('font', 'name')

## 设置 .ini 参数 ##
mainCfg.set('string', 'first', '首屏')

## 保存 .ini; 可以不保存 ##
#mainCfg.write(open('includes/config.ini', 'w', encoding='utf-8'))

str1 = mainCfg.get('string', 'first')
str2 = mainCfg.get('string', 'second')
###############################################################################

###############################################################################
## 中文乱码. 程序加载方式. 需要在相对应的元素设置 font_name ##
from kivy import resources
resources.resource_add_path(cfgFontPath)
font_heiti = resources.resource_find(cfgFontName)
###############################################################################

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#from kivy.core.window import Window ## 全屏


class SwitchManager(ScreenManager):
    pass
class MainScreen(Screen):
    pass
class ChildScreen(Screen):
    pass

class DemoApp(App):
    title = 'Civen App Demo 5'

    Builder.load_file('includes/kivy/bar.kv')
    ## 下面这种是查找 includes/kivy/demo.kv ##
    #kv_directory = 'includes/kivy'

    def build(self):
        return SwitchManager()

    def __init__(self, **kwargs):
        super(DemoApp, self).__init__(**kwargs)

        #Window.fullscreen = 1 ## 全屏

        self.mainText = str1     # Kivy [app.mainText]
        self.childText = str2    # Kivy [app.childText]
        self.fontSzie = 36          # Kivy [app.fontSzie]

        ## 中文乱码: 程序加载字体法. ##
        self.fontFamily = font_heiti # Kivy [app.font_heiti]


if __name__ == '__main__':
    DemoApp().run()

###############################################################################
'''
这里是代码说明:

    01. 读取 & 设置 .ini 配置文件
        from configparser import ConfigParser
        ...
        str2 = mainCfg.get('string', 'second')

    02. kivy 模板方式. bar.kv 加载 main.kv 和 child.kv
        由于 main.kv include child.kv
        bar.kv 需要 include force child.kv

    03. 中文乱码. 程序加载方式. 需要在相对应的元素设置 font_name
        from kivy import resources
        resources.resource_add_path('./')
        font_heiti = resources.resource_find('msyh.ttc')

    04. from kivy.uix.screenmanager import ScreenManager, Screen

    05. 处理中文乱码问题
        [由于 Kivy .kv 代码中不能写入中文, 需要 Python .py 传递变量]
        Kivy .kv 中 [app.xxx] 获取. 请替换 xxx 为 Python .py 中设置的变量

        def __init__(self, **kwargs):
            super(FooApp, self).__init__(**kwargs)

            self.mainText = '首屏!'     # Kivy [app.mainText]
            self.childText = '子屏!'    # Kivy [app.childText]
            self.fontSzie = 36          # Kivy [app.fontSzie]

            ## 中文乱码: 程序加载字体法. ##
            self.fontFamily = font_heiti # Kivy [app.font_heiti]
    
'''
###############################################################################
