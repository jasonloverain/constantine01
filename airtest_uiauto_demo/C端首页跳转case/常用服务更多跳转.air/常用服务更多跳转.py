
__author__ = "wb-wgz629946"
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
poco("android:id/content").child("android.widget.LinearLayout").offspring("com.hanweb.android.zhejiang.activity:id/fragment").child("android.widget.LinearLayout").offspring("com.hanweb.android.zhejiang.activity:id/ll_content")[1].child("android.widget.LinearLayout")[0].offspring("com.hanweb.android.zhejiang.activity:id/rv_regular_service").child("android.view.ViewGroup")[7].offspring("com.hanweb.android.zhejiang.activity:id/iv_service").click()


assert_exists(Template(r"tpl1571195118129.png", record_pos=(0.003, -0.515), resolution=(1080, 2340)), "请填写测试点")
