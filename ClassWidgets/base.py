from PyQt5.QtWidgets import QWidget
import json
import os
import time
class PluginBase:  # 插件类
    def __init__(self, cw_contexts, method):  # 初始化
        # 保存上下文和方法
        self.cw_contexts = cw_contexts
        self.method = method

        self.PATH = self.cw_contexts['PLUGIN_PATH']  # 插件路径

    def execute(self):  # 自启动执行部分
        pass

    def update(self, cw_contexts):  # 自动更新部分
        self.cw_contexts = cw_contexts
        pass


class SettingsBase(QWidget):
    def __init__(self, plugin_path, parent=None):
        super().__init__(parent)
        self.PATH = plugin_path

    def __getitem__(self, key):
        return self.config.get(key)

    def __setitem__(self, key, value):
        self.config[key] = value
        self.save_config()

    def __repr__(self):
        return json.dumps(self.config, ensure_ascii=False, indent=4)
