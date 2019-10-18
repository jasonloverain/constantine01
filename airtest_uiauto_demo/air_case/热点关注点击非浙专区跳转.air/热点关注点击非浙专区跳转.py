# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
touch(Template(r"tpl1571205798196.png", record_pos=(0.023, 0.004), resolution=(1080, 2340)))

#touch(Template(r"tpl1571205798196.png", record_pos=(0.023, 0.004), resolution=(1080, 2340)))
assert_exists(Template(r"tpl1571198561457.png", record_pos=(-0.005, -0.931), resolution=(1080, 2340)), "请填写测试点")
    







