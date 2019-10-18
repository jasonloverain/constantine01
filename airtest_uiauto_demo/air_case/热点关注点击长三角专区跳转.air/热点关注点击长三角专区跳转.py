# -*- encoding=utf8 -*-
__author__ = "wb-wgz629946"
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
resin="长三角无感漫游"
print(type(resin))
while True:
    wait(Template(r"tpl1571208672732.png", record_pos=(0.004, 0.089), resolution=(1080, 2340)))
    touch(Template(r"tpl1571207083351.png", record_pos=(0.017, 0.075), resolution=(1080, 2340)))
    time.sleep(6)
    if exists(Template(r"tpl1571208794248.png", record_pos=(0.018, -0.931), resolution=(1080, 2340))):
        res = poco("com.hanweb.android.zhejiang.activity:id/tv_title").get_text()
        print(res)
        print(resin)
        if res == resin:
            print("用例通过")
        else:
            print("用例失败")
        break;
# finally:
#     wait(Template(r"tpl1571208794248.png", record_pos=(0.018, -0.931), resolution=(1080, 2340)))
#     res = poco("com.hanweb.android.zhejiang.activity:id/tv_title").get_text()
#     print(res)
#     if assert_equal("res","长三角无感漫游"):
#         print("用例通过")
    
    
    