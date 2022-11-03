import time

from celery.local import PromiseProxy

from celery_demo.tasks import send_msg

f: PromiseProxy = send_msg.delay("zha4324ngsan")
e: PromiseProxy = send_msg.delay("zhan324gsan")
g: PromiseProxy = send_msg.delay("zhan3423gsan")
time.sleep(6)
for res in [f, e, g]:
    print(res.result)
