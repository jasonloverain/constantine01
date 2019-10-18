# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
swipe(Template(r"tpl1571280379731.png", record_pos=(0.245, 0.627), resolution=(1080, 2340)), vector=[-0.6864, 0.0099])


touch(Template(r"tpl1571280460353.png", record_pos=(-0.022, 0.607), resolution=(1080, 2340)))
time.sleep(3)
res = poco("com.hanweb.android.zhejiang.activity:id/tv_title").get_text()
if res == "文化旅游专区":
    print("用例通过")
else:
    print("用例失败")
RES1 =assert_equal("文化旅游专区","文化旅游专区")
print(RES1)


#wenlv=poco("android:id/content").child("android.widget.LinearLayout").offspring("com.hanweb.android.zhejiang.activity:id/fragment").child("android.widget.LinearLayout").offspring("com.hanweb.android.zhejiang.activity:id/ll_content")[1].child("android.widget.LinearLayout")[3].offspring("com.hanweb.android.zhejiang.activity:id/rv_one_thing").child("android.view.ViewGroup")[1].offspring("com.hanweb.android.zhejiang.activity:id/iv_featured_area")