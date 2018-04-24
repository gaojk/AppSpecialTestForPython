import os


"""
获取App的package/activity命令：adb logcat | grep START

冷启动和停止
    启动App命令
    adb shell am start -W -n package/activity

    停止App命令
    adb shell am force-stop package

热启动和停止
    启动App命令
    adb shell am start -W -n package/activity

    停止App命令
    adb shell input keyevent 3 (3表示点击back键)
"""


class App(object):
    def __init__(self):
        self.content = ''
        self.startTime = 0

    # 启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.github.android_app_bootstrap/.activity.WelcomeActivity'
        self.content = os.popen(cmd)  # 执行命令了

    # 停止App
    def StopApp(self):
        cmd = 'adb shell am force-stop com.github.android_app_bootstrap'
        os.popen(cmd)

    # 获取启动时间
    def GetLaunchedTime(self):
        """
            命令执行返回的结果:
            Starting: Intent { cmp=com.github.android_app_bootstrap/.activity.WelcomeActivity }
            Status: ok
            Activity: com.github.android_app_bootstrap/.activity.WelcomeActivity
            ThisTime: 417
            TotalTime: 417
            Complete
        :return:
        """
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

if __name__ == '__main__':
    app = App()
    app.StopApp()
    app.LaunchApp()
    print(app.GetLaunchedTime())
