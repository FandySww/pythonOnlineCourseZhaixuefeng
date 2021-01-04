import os
import time
from threading import Thread

from django.test import TestCase

# Create your tests here.

# def testThread():
#     with open('D:/codeMy/CODY_MY_AFTER__KE/pythonOnlineCourseZhaixuefeng/runshell/static/log/log.txt') as file_object:
#         lines = file_object.readlines()
#         last_line = lines[-1]
#         result = last_line.split(" ")[::-1][:4]
#         print(result[0].replace("'", "").replace(".", ""))
#         print(result[-1])
#
# runLocal = Thread(target=testThread())
# runLocal.start()

print(str(time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time()))))
