#!/usr/bin/env python
#coding:utf-8

import tornado.httpserver #处理http协议
import tornado.ioloop #io非阻塞循环，与客户端持续连接
import tornado.options #命令行解析模块
import tornado.web #web框架和异步功能

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int) #定义服务端口


#处理程序类，一般以Handler结尾
class IndexHandler(tornado.web.RequestHandler): #继承tornado.web.RequestHandler
    def get(self, *args, **kwargs): #定义get方法
        # 调用父类方法
            # 参数一：指定greeting方法（http://127.0.0.1:8000/?greeting='hello'）
        # 参数二：默认greeting值
        greeting = self.get_argument('greeting', 'Hello')
        print(type(greeting))
        id = self.get_argument('id','1')
        self.write(greeting + ', welcome you to read: www.itdiffer.com'+ 'id{}'.format(id))
if __name__ == "__main__":
    tornado.options.parse_command_line() #执行options模块中的方法parse_command_line解析命令行
    #网站请求处理集合
    # handlers_list[0] = 请求路径
    # handlers_list[1] = 处理程序类
    # /(.*)  = /下的任意请求
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app) #创建HTTP-server实例
    http_server.listen(options.port) #设置端口
    print('Development server is running at http://127.0.0.1:{}'.format(options.port))
    tornado.ioloop.IOLoop.current().start() #接受客户端请求

