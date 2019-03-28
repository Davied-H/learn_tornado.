import tornado.web
import json
from 后端框架tornado.项目框架.optsql.connect_sql_server import *
from tornado.escape import json_decode, json_encode, utf8



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("shell.html")
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")
class UserHandler(tornado.web.RequestHandler):
    def post(self):
        user_name = self.get_argument("username") #获取html表单中用户输入的变量值
        user_pass = self.get_argument("password")
        print(user_pass,user_name)
        if db_search("passwd","users","name='{}'".format(user_name)):
            print("用户存在")
            if user_pass == db_search("passwd","users","name='{}'".format(user_name)) :
                self.render("index.html",username=user_name,password=user_pass) #设置参数，user.html可通过{{username}}方式接收参数
class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        a = {
            "a":1,
            "b":2
        }
        self.write(json_encode(a))
# class ShellShow(tornado.web.RequestHandler):
#     def post(self):
#         shell_show = self.get_argument("shell")
#         self.render("shell_show.html",shell=ssh_client(shell_show))
# class Search_db(tornado.web.RequestHandler):
#     def post(self):
#         search_field = self.get_argument("field")
#         search_sql = self.get_argument("sql")
#         self.render("shell_show.html",shell=search_db(search_field,search_sql))

# a = db_search("passwd","users","name='{}'".format("hedongdong"))
# print(a)
