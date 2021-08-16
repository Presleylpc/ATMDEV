import os
import sys
from core import src
#获取当前目录
BASE_PATH = os.path.dirname(__file__)

#将当前目录添加至环境变量
sys.path.append(BASE_PATH)

if __name__ == '__main__':
    src.run()