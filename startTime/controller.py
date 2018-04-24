from startTime.app import App
import time
import csv


class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.counter = count    # 执行次数
        self.allData = [('timestamp', 'elapsedtime')]

    # 单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        elpasedTime = self.app.GetLaunchedTime()    # 执行的时间,耗时
        self.app.StopApp()
        currentTime = self.getCurrentTime()  # 当前时间
        self.allData.append((currentTime, elpasedTime))

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def SaveDataCSV(self):
        with open('startTime.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(self.allData)


if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataCSV()
