from 后端框架tornado.项目框架.url import url  #引用url.py

import tornado.web
import os


#定义项目路径和静态资源路径
setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"template"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),
    )

application = tornado.web.Application(
    handlers=url,
    **setting
    )