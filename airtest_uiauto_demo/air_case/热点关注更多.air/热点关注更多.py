# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco 
import time
from airtest.core.api import *
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
if exists(Template(r"tpl1571197411334.png", record_pos=(-0.011, -0.543), resolution=(1080, 2340))):   
    poco("com.hanweb.android.zhejiang.activity:id/tv_more").click()
assert_exists(Template(r"tpl1571197671677.png", record_pos=(0.003, -0.703), resolution=(1080, 2340)), "请填写测试点")

