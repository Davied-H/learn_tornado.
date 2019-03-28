
from 后端框架tornado.项目框架.handler.index import *

url=[
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/index',UserHandler),
    (r'/json',JsonHandler)
    ]