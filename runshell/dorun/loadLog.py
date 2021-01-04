from dorun.models import RunLog, Path
import time, datetime
from dorun.models import RunLog, Path


# 这个方法是异步执行的，不断的读取日志的数据，直到超时3分钟或者读取到最后一行有我们要的信息
def getLogLastLine(filename, featureId):
    startTime = time.time()
    while True:
        try:
            delyTime = time.time() - startTime
            with open(filename) as file_object:
                lines = file_object.readlines()
                last_line = lines[-1]
                if delyTime > 180000 or 'Found Web Interface' in last_line:
                    if 'Found Web Interface' in last_line:
                        result = last_line.split(" ")[::-1][:4]
                        runLog = RunLog(
                            applicationId=result[0].replace("'", "").replace(".", ""),
                            url=result[-1],
                            featureId=featureId,
                            createTime=str(time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time())))
                        )
                    runLog.save()
                    # http通知调用方我上线了
                break
        except:
            break


def getLogLastLinelocal():
    startTime = time.time()
    while True:
        delyTime = time.time() - startTime
        with open(
                'D:/codeMy/CODY_MY_AFTER__KE/pythonOnlineCourseZhaixuefeng/runshell/static/log/log.txt') as file_object:
            lines = file_object.readlines()
            last_line = lines[-1]
            if delyTime > 180000 or 'Found Web Interface' in last_line:
                if 'Found Web Interface' in last_line:
                    result = last_line.split(" ")[::-1][:4]
                    runLog = RunLog(
                        applicationId=result[0].replace("'", "").replace(".", ""),
                        url=result[-1],
                        featureId='123',
                        createTime=str(datetime.date.today())
                    )
                    runLog.save()
            break
