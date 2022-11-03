from celery_demo.tasks import send_msg

result = send_msg.AsyncResult('c5420731-0fc5-46a5-bdde-f8ccab27834b')
print(result.get())
