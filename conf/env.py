# SECURITY WARNING: don't run with debug turned on in production!
import os

DEBUG = True
# Django silk
OPEN_SILK = False

# ================================================= #
# ************** mysql数据库 配置  ************** #
# ================================================= #
# 数据库类型 MYSQL/SQLITE3
DATABASE_TYPE = "MYSQL"
# 数据库地址
DATABASE_HOST = "192.168.126.153"
# 数据库端口
DATABASE_PORT = 3306
# 数据库用户名
DATABASE_USER = "myuser"
# 数据库密码
DATABASE_PASSWORD = "myuser"
# 数据库名
DATABASE_NAME = "djangoself"

EMAIL_HOST = "smtp.163.com"
# 这里要注释掉否则异常****
# EMAIL_PORT = 465
# 是否使用安全连接
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# 不是登录密码，是安全码，需要去网页版邮箱申请
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# ================================================= #
# ************** redis 数据库配置  ************** #
# ================================================= #
# 是否启用Redis缓存
# 注：不使用redis则无法使用celery
REDIS_ENABLE = True
IS_REDIS_CLUSTER = False
REDIS_DB = 1
REDIS_HOST = '192.168.126.153'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
# celery 定时任务redis 库号
CELERY_DB = 0

# ================================================= #
# ************** 默认配置  ************** #
# ================================================= #
# 只允许访问的ip地址列表
ALLOWED_HOSTS = ['*']
# 允许跨域源
CORS_ORIGIN_ALLOW_ALL = True
# 允许ajax请求携带cookie
CORS_ALLOW_CREDENTIALS = False
# 验证码状态
CAPTCHA_STATE = False
# 操作日志配置
API_LOG_ENABLE = True
API_LOG_METHODS = ['POST', 'DELETE', 'PUT'] # 'ALL' or ['POST', 'DELETE']
# 接口权限
INTERFACE_PERMISSION = True
# 是否开启登录ip转换成城市位置
ENABLE_LOGIN_LOCATION = True
