celery 启动测试案例

### 将celeryconfig中PASSWORD修改为自己的密码,ip地址修改为自己的ip地址

### 启动服务

celery -A celery_demo worker --loglevel=INFO -P eventlet