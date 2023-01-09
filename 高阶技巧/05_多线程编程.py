"""
演示多线程的使用
"""
import threading
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing,args=("我在唱歌",))
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance,args=("我要跳舞",))

    # 启动线程
    sing_thread.start()
    dance_thread.start()