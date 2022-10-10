from huey import RedisHuey, crontab
from huey import SqliteHuey
from huey import MemoryHuey

#huey = RedisHuey('my-app', host='127.0.0.1', port='7777')
#huey = SqliteHuey(filename='d:/tmp/demo.db')

huey = MemoryHuey()

@huey.task()
def add_numbers(a, b):
    print("suma:", a, b)
    return a + b

@huey.task(retries=2, retry_delay=60)
def flaky_task(url):
    # This task might fail, in which case it will be retried up to 2 times
    # with a delay of 60s between retries.
    return this_might_fail(url)

@huey.periodic_task(crontab(minute='0', hour='3'))
def nightly_backup():
    sync_all_data()