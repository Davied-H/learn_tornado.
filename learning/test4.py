import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="Please send email to me", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input_word):
        self.write(input_word[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text")
        width = int(self.get_argument("width", 40))
        self.write(textwrap.fill(text, width))
class ErroHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("404044")
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap", WrapHandler),
            (r".*",ErroHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("http://127.0.0.1:{}".format(options.port))
    tornado.ioloop.IOLoop.instance().start()