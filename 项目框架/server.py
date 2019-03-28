
#此文件为程序的入口文件
import tornado.ioloop
import tornado.options
import tornado.httpserver

from 后端框架tornado.项目框架.application import application

from tornado.options import define,options
define("port",default=80,help="run on th given port",type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:{}'.format(options.port))
    print ('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()