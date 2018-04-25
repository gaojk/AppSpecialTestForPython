import os
import time
import csv

"""
获取数据
adb shell dumpsys cpuinfo | grep packagename
"""


# 控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.allData = [('timestamp', 'cpustatus')]

    # 单次测试过程
    def testprocess(self):
        """
            命令执行后返回的结果:
            0.3% 15622/com.github.android_app_bootstrap: 0.3% user + 0% kernel / faults: 3 minor
        :return:
        """
        result = os.popen('adb shell dumpsys cpuinfo | grep com.github.android_app_bootstrap')
        cpuvalue = ''
        for line in result.readlines():
            cpuvalue = line.split("%")[0]
            print(cpuvalue)

        currenttime = self.getCurrentTime()
        self.allData.append((currenttime, cpuvalue))

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(5)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return currentTime

    # 数据的存储
    def SaveDataToCSV(self):
        with open('startTime.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(self.allData)


if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()
