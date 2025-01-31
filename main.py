"""
    示例插件
"""
from PyQt5 import uic
from datetime import datetime
from .ClassWidgets.base  import PluginBase

from PyQt5.QtWidgets import QHBoxLayout
# 自定义小组件
WIDGET_CODE = 'widget_test.ui'
WIDGET_NAME = '当前时间'
WIDGET_WIDTH = 200


class Plugin(PluginBase):
    def __init__(self, cw_contexts, method):
        super().__init__(cw_contexts, method)

        self.method.register_widget(WIDGET_CODE,  WIDGET_NAME, WIDGET_WIDTH)


    def execute(self):
        self.test_widget  = self.method.get_widget(WIDGET_CODE)

        if self.test_widget:
            contentLayout = self.test_widget.findChild(QHBoxLayout,  'contentLayout')
            contentLayout.setSpacing(1)
        self.method.change_widget_content(WIDGET_CODE,  '当前时间', WIDGET_WIDTH)

    def update(self, cw_contexts):
        super().update(cw_contexts)
        if hasattr(self, 'test_widget'):
            current_time = datetime.now().strftime("%H:%M:%S")
            widget_content = f'{current_time}'
            self.method.change_widget_content(WIDGET_CODE,  '当前时间', widget_content)