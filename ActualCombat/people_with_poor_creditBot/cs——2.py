import multiprocessing
import asyncio

def movie(name,n):
    for i in range(n):
        print('看电影%s'%name)

def music(name,n):
    for i in range(n):
        print('听音乐%s'%name)

if __name__ == '__main__':
    # 创建进程
    pool = multiprocessing.Pool(2)
    pool.apply_async(func=movie,args=('背背佳',100))
    pool.apply_async(func=music,args=('大风车',100))
    pool.close()
    pool.join()