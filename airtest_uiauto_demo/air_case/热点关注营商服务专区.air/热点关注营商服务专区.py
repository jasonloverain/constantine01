# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
if exists(Template(r"tpl1571281322884.png", record_pos=(-0.098, 0.618), resolution=(1080, 2340))):
    touch(Template(r"tpl1571281322884.png", record_pos=(-0.098, 0.618), resolution=(1080, 2340)))
    time.sleep(3)
    res=poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("com.alipay.mobile.nebula:id/h5_tv_title").get_text()
    if res == "营商服务专区":
        print("pass")
    else:
        print("failed")