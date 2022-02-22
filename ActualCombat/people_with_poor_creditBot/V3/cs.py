# -*- encoding : utf-8 -*-
# @Author : Fenglchen
#使用线程池方式执行
import time
from multiprocessing.dummy import Pool  #导入线程池模块对应的类

start_time = time.time()

#模拟爬虫
def get_page(str):
    print('正在下载：',str)
    time.sleep(3)  #模拟发送请求和获取响应数据需要的时间
    print('下载成功：',str)

name_lists = [['xiaozi','aa','bb','cc'],['xiaoziwdw','aawdwd','bbdwd','ccwdwd'] ]#模拟url

#实例化一个线程池对象
pool = Pool(4)  #处理4个请求阻塞
for name_list in name_lists:
    #将列表中每一个元素传递给get_page进行处理
    pool.map(get_page,name_list)  #第一个参数是函数，第二个参数是列表

    end_time = time.time()

print('%d second'%(end_time-start_time))  #程序执行完成需要的时间，3秒
