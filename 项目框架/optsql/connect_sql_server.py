from mysql import connector


#查询功能，查询用户的对应字段
def db_search(field,table,who):  #字段，表，谁
    # try:
    session = connector.connect(
        host="192.168.239.20",
        user="root",
        passwd="123123",
        database='test'
    )
    mycursor = session.cursor()
    mycursor.execute("select {} from {} where {}".format(field,table,who))
    for i in mycursor:
        return i[0]
    session.close()
    # except :
    #     return 1
    if db_search("passwd","users","name='{}'".format("hedongdong")):
        print("aaa")


