import threading
from queue import Queue, Empty
from datetime import datetime
from collections import defaultdict
import time

#######################################

class EventEngine(object):
    """
    事件促发引擎
    """
    def __init__(self):
        """Constructor"""
        # 事件队列
        self.__queue = Queue()
        # 事件引擎开关
        self.__active = False
        # 事件处理线程
        self.__thread = threading.Thread(target=self.__run)
        # 计时器，用于触发计时器事件 (内部时钟)
        # 所有的计时器都是分部计时器，计时器都是在业务层进行完成。
        # self.__timer = QTimer()
        # self.__timer.timeout.connect(self.__onTimer)

        # 这里的__handlers是一个字典，用来保存对应的事件调用关系
        # 其中每个键对应的值是一个列表，列表中保存了对该事件进行监听的函数功能
        self.__handlers = defaultdict(list)
        # __generalHandlers是一个列表，用来保存通用回调函数（所有事件均调用）
        self.__generalHandlers = []

    def __run(self):
        """执行事件"""
        while self.__active is True:
            try:
                event = self.__queue.get(block=True, timeout=1)  # 获取事件的阻塞时间设
                print("开启事件引擎！！！")
                self.__process(event)
            except Empty:
                pass

    def __process(self,event):
        """处理事件"""
        if event.handler is not None:
            event.handler(event)
        else:
            [handler(event) for handler in self.__generalHandlers]


    # ----------------------------------------------------------------------
    # def __process(self, event):
    #     """处理事件"""
    #     # 检查是否存在对该事件进行监听的处理函数
    #     if event.type_ in self.__handlers:
    #         # 若存在，则按顺序将事件传递给处理函数执行
    #         [handler(event) for handler in self.__handlers[event.type_]]
    #         # 以上语句为Python列表解析方式的写法，对应的常规循环写法为：
    #         # for handler in self.__handlers[event.type_]:
    #         # handler(event)
    #         # 调用通用处理函数进行处理
    #     if self.__generalHandlers:
    #         [handler(event) for handler in self.__generalHandlers]

    def start(self):
        """
        开始启动引擎
        :return:
        """
        # 将引擎设为启动
        self.__active = True
        # 启动事件处理线程
        self.__thread.start()

    # ----------------------------------------------------------------------
    def stop(self):
        """停止引擎"""
        # 将引擎设为停止
        self.__active = False
        # 停止计时器
        # self.__timer.stop()
        # 等待事件处理线程退出
        self.__thread.join()

    # ----------------------------------------------------------------------
    def registerGeneralHandler(self, handler):
        """注册通用事件处理函数监听"""
        if handler not in self.__generalHandlers:
            self.__generalHandlers.append(handler)

    # ----------------------------------------------------------------------
    def unregisterGeneralHandler(self, handler):
        """注销通用事件处理函数监听"""
        if handler in self.__generalHandlers:
            self.__generalHandlers.remove(handler)

    # ----------------------------------------------------------------------
    # def registerHandler(self,handler,):
    # ----------------------------------------------------------------------
    def put(self, event):
        """向事件队列中存入事件"""
        self.__queue.put(event)

    #######################################


class Event:
    """
    实体对象
    """
    def __init__(self, handler=None, type_=None, data_handler=None):
        """Constructor"""
        self.type_ = type_       # 事件类型
        self.dict_ = {}          # 字典用于保存具体的事件数据
        self.handler = handler   # 事件回调
        self.time = time.time()  # 创建事件的时间戳
        self.data_handler = data_handler  # 用于接受数据方法的回调



def testabc(event):
    print(event.dict_)
    print("展示一次！！！")

# ----------------------------------------------------------------
def test():
    """
    单个任务的测试
    :return:
    """
    print("hello world!")
    ee = EventEngine()

    def simpletest(event):
        print(event)
        print(u'处理每秒触发的计时器事件：%s' % str(datetime.now()))
    event = Event(type_="aaa",handler=sql.testabc)
    event.dict_['data'] = "bbb"
    ee.registerGeneralHandler(simpletest)
    ee.start()
    ee.put(event)
    ee.put(event)
    ee.put(event)


# -----------------------------------------------------------------
def time_test():
    print("点击事件的促发")


# 直接运行脚本可以进行测试
if __name__ == '__main__':
    print("aaaa")
    test()
    time_test()
