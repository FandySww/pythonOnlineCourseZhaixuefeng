import json
import os
import time, datetime
from threading import Thread

import dorun.loadLog as loadLog
from django.http import HttpResponse
from dorun.models import RunLog, Path


# 上线
def indexOnline(request):
    shellPath = Path.objects.get(action='online').shellPath
    logPath = Path.objects.get(action='online').logPath
    datasourceId = request.GET.get('datasourceId')
    # 探活 如果发送的为探活的请求 返回所有的已经活跃的特征id
    if datasourceId=='exploring':
        return HttpResponse("pong")
    featureId = request.GET.get('featureId')
    sh = 'sh ' + shellPath + " > " + logPath + featureId
    try:
        # 判断数据库是不是有这个特征id
        runLogAll = RunLog.objects.all()
        for item in runLogAll:
            if item.featureId == featureId:
                result = getJsonForResponse('0', '此特征库已经启动')
                return HttpResponse(json.dumps(result), content_type="application/json")
        os.system(sh + ' ' + datasourceId + ' ' + featureId)
        # 这部操作要异步执行的
        try:
            runLocal = Thread(loadLog.getLogLastLine(logPath + featureId, featureId))
            runLocal.start()
        except Exception as e:
            result = getJsonForResponse('0', '无法启动线程',str(e))
            return HttpResponse(json.dumps(result), content_type="application/json")
    except Exception as e:
        return HttpResponse(str(e))
    else:
        result = getJsonForResponse('2', '操作成功，请耐心等待任务上线')
        return HttpResponse(json.dumps(result), content_type="application/json")


# 下线
def indexOffline(request):
    featureId = request.GET.get('featureId')
    shellPath = Path.objects.get(action='offline').shellPath
    try:
        # 没有或者返回多条会报错
        runLog = RunLog.objects.get(featureId=featureId)
    except Exception as e:
        result = getJsonForResponse('0', '此application已经下线',str(e))
        return HttpResponse(json.dumps(result), content_type="application/json")
    sh = 'sh ' + shellPath
    try:
        # 根据featureId找到applicationId
        applicationId = RunLog.objects.get(featureId=featureId).applicationId
        # 判断数据库有没有这个applicationId
        os.system(sh + ' ' + applicationId)
        # 删除数据
        runLog.delete()
    except Exception as e:
        result = getJsonForResponse('0', '下线失败请联系数据同学',str(e))
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        result = getJsonForResponse('1', '下线成功','applicationId_'+applicationId)
        return HttpResponse(json.dumps(result), content_type="application/json")

# 本地测试用
def indexOfflinelocal(request):
    applicationId = request.GET.get('applicationId')
    shellPath = Path.objects.get(action='offline').shellPath
    try:
        # 没有或者返回多条会报错
        runLog = RunLog.objects.get(applicationId=applicationId)
    except Exception as e:
        return HttpResponse(str(ResultEntity('0', "此application已经下线,或重复上线多条")))
    sh = 'sh ' + shellPath
    try:
        # 判断数据库有没有这个applicationId
        os.system(sh + ' ' + applicationId)
        # 删除数据
        runLog.delete()
    except Exception as e:
        return HttpResponse(str(e))
    else:
        return HttpResponse(str(ResultEntity('1', "操作成功，运行信息请咨询数据同学")))


# 本地测试用
def indexOnlinelocal(request):
    try:
        runLocal = Thread(target=loadLog.getLogLastLinelocal())
        runLocal.start()
    except:
        return HttpResponse("无法启动线程")
    else:
        return HttpResponse("操作成功，运行信息请咨询数据同学")

class ResultEntity:
    def __init__(self, status, result):
        self.name = status
        self.result = result
    def __str__(self):
        return self.name+":"+self.result

def getJsonForResponse(status, message, data=''):
    result = {"status": status, "message": message, "data": data}
    return result
