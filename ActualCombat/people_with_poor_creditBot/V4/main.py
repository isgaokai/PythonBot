# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql
import multiprocessing
import asyncio
from Bot import Bot


if __name__ == '__main__':
    pool = multiprocessing.Pool(8)
    pool.apply_async(func=Bot,args=(381, 400,100,200))
    pool.apply_async(func=Bot,args=(401, 420,100,200))
    pool.apply_async(func=Bot,args=(421,440,100,200))
    pool.apply_async(func=Bot,args=(441,460,100,200))
    pool.apply_async(func=Bot,args=(461, 480,100,200))
    pool.apply_async(func=Bot,args=(481, 500,100,200))
    pool.apply_async(func=Bot,args=(501,520,100,200))
    pool.apply_async(func=Bot,args=(521,568,100,200))
    pool.close()
    pool.join()