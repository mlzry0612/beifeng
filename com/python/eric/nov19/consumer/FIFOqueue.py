import queue

q = queue.Queue()  # 先入先出  也会阻塞
print(q.empty())  # 判断是否为空，空返回True
q.put("d1")
q.put("d2")
q.put("d3")
print(q.full())  # 判断是否满，满返回True
print(q.get())  # d1
print(q.get())  # d2
print(q.get())  # d3
print(q.get(timeout=1))

# 设置具有长度限制的队列
q = queue.Queue(maxsize=3)  # 长度为3
q.put(1)
q.put(2)
q.put(3)
# q.put(4, block=False)  # 这里程序又阻塞了,所以可以使用block,timeout参数解决阻塞问题,异常queue.Full

q = queue.PriorityQueue()  # 设置优先级队列，数字小的优先级高
q.put((1, "King"))
q.put((-1, "Jeson"))
q.put((10, "Tim"))
q.put((5, "Mike"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())

q = queue.LifoQueue() #设置后入先出队列
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())