# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
poco("com.hanweb.android.zhejiang.activity:id/tv_content").click()

assert_exists(Template(r"tpl1571198067669.png", record_pos=(0.013, -0.931), resolution=(1080, 2340)), "请填写测试点")
