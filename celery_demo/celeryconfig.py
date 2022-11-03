PASSWORD = ''
HOST = 'localhost'
BROKER_URL = 'redis://:{}@{}/6379/0'.format(PASSWORD, HOST)
CELERY_RESULT_BACKEND = 'redis://:{}@{}:6379/1'.format(PASSWORD, HOST)
# 设置时间参照，不设置默认使用的UTC时间
CELERY_TIMEZONE = 'Asia/Shanghai'
# 指定任务的序列化
CELERY_TASK_SERIALIZER = 'json'
# 指定执行结果的序列化
CELERY_RESULT_SERIALIZER = 'json'
