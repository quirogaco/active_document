from gevent import monkey; monkey.patch_all()
import gevent

from huey.contrib.mini import MiniHuey


huey = MiniHuey()

# If we want to support scheduling tasks for execution in the future, or for
# periodic execution (e.g. cron), then we need to call `huey.start()` which
# starts a scheduler thread.
print("0")
huey.start()
print("1")


@huey.task()
def add(a, b):
    print("add:", a, b)
    return a + b

res = add(1, 2)
print(res())  # Result is calculated in separate greenlet.

print('Scheduling task for execution in 12 seconds.')
res = add.schedule(args=(10, 20), delay=12)
print(res())

# Stop the scheduler. Not strictly necessary, but a good idea.
huey.stop()