
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
from airtest.core.api import *
stop_app("com.hanweb.android.zhejiang.activity")
start_app("com.hanweb.android.zhejiang.activity")
time.sleep(10)
poco("com.hanweb.android.zhejiang.activity:id/tv_city").click()
poco(text="杭州市").click()
poco(text="江干区").click()
assert_exists(Template(r"tpl1570694695222.png", record_pos=(-0.331, -0.92), resolution=(1080, 2340)), "test001")



