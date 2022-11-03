PASSWORD = ''
BROKER_URL = 'redis://:{}@43.142.194.76:6379/0'.format(PASSWORD)
CELERY_RESULT_BACKEND = 'redis://:{}@43.142.194.76:6379/1'.format(PASSWORD)
# 设置时间参照，不设置默认使用的UTC时间
CELERY_TIMEZONE = 'Asia/Shanghai'
# 指定任务的序列化
CELERY_TASK_SERIALIZER = 'json'
# 指定执行结果的序列化
CELERY_RESULT_SERIALIZER = 'json'
