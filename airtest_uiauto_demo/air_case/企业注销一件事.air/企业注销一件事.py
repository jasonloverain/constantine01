# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco 
import time
from airtest.core.api import *
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
swipe(Template(r"tpl1571281799916.png", record_pos=(-0.199, 0.377), resolution=(1080, 2340)), vector=[-0.1517, -0.4001])
time.sleep(2)
swipe(Template(r"tpl1571282872240.png", record_pos=(0.363, -0.046), resolution=(1080, 2340)), vector=[-0.8322, -0.0013])
touch(Template(r"tpl1571282892517.png", record_pos=(-0.232, -0.064), resolution=(1080, 2340)))
time.sleep(3)



