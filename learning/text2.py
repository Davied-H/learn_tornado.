import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="Please send email to me", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self):#向客户端url末尾获取数据
        self.render("www.html",title="welcome",items=1)#使用render来展示网页

class WrapHandler(tornado.web.RequestHandler):
    def post(self):#以self.argument("text")的形式得到text为标签提交的数据
        text = self.get_argument("text")
        width = self.get_argument("width", 40)
        self.write(textwrap.fill(text, width))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r"/", ReverseHandler),
            (r"/wrap", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:{}'.format(options.port))
    tornado.ioloop.IOLoop.instance().start()