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
touch(Template(r"tpl1571282450571.png", record_pos=(0.223, 0.212), resolution=(1080, 2340)))
time.sleep(5)
res= poco("com.hanweb.android.zhejiang.activity:id/activity_main").child("android.webkit.WebView").child("android.webkit.WebView").offspring("root").child("android.view.View").child("android.view.View").child("android.view.View")[0].get_text()
print(res)
if "结婚生育" in res:
    print("pass")
else:
    print("failed")

