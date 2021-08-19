
from db import  db_handler
def register_interface(user,pwd):

        user_dict = db_handler.select(user)

        if user_dict:
            return False,'用户已存在'

        # 业务逻辑
        user_dic = {
            'name' :user,
            'pwd' :pwd,
            'balance' :15000,
            'flow' :[],
            'shopping_car': {}
        }
        db_handler.save(user_dic)
        return True,'%s注册成功' %user