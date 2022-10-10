import tareas_huey

#res = tareas_huey.add_numbers(1, 2)
res = tareas_huey.add_numbers.schedule((2, 3), delay=10) 

#print(res)
print("0-", res(blocking=True))
#print("1-", res())