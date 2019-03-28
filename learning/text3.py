
#简单表单提交网站

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("www.html")

class UserHandler(tornado.web.RequestHandler):
    def post(self):
        user_name = self.get_argument("username") #获取html表单中用户输入的变量值
        user_email = self.get_argument("email")
        user_website = self.get_argument("website")
        user_language = self.get_argument("language")
        self.render("user.html",username=user_name,email=user_email,website=user_website,language=user_language) #设置参数，user.html可通过{{username}}方式接收参数


handlers = [
    (r"/", IndexHandler),
    (r"/user", UserHandler)
]

template_path = os.path.join(os.path.dirname(__file__),"learning")

if __name__ == "__main__":
    tornado.options.parse_command_line() #解析命令行
    app = tornado.web.Application(handlers, template_path) #
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()