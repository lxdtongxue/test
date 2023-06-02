# 导入time模块
import time

# 定义一个显示当前时间的函数
def show_time():
    # 获取当前时间
    current_time = time.localtime()
    # 格式化时间
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    # 打印时间
    print("当前时间是:", formatted_time)

# 无限循环
while True:
    # 调用显示时间的函数
    show_time()
    # 暂停一秒
    time.sleep(1)
