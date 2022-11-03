import time
from celery_demo import app


@app.task
def send_email(name):
    print("向%s发送邮箱。。。" % name)
    time.sleep(5)
    print("向%s发送邮箱完成..." % name)
    return "ok"


@app.task
def send_msg(name):
    print("向%s发送短信。。。" % name)
    time.sleep(5)
    print("向%s发送短信完成..." % name)
    return f'name {name} is send ok'
