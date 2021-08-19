'''写用户功能层'''

from  interface import user_interface
#1.注册
def register():
    while True:
        #用户功能层
        user = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        re_pwd = input('请确认密码：').strip()
        if pwd == re_pwd:

            # 调用注册接口
            # msg == '%注册成功' % user
            #(True. %s注册成功) or (False. 用户已存在)
            flag, msg = user_interface.register_interface(user,pwd)

            #判断
            if flag:
                print(msg)
                break
            else:
                print(msg)


#2.登陆
def login():
    pass

#3.查看余额
def check_balance():
    pass

#4.提现
def withdraw():
    pass

#5.转账
def transfer():
    pass

#6.还款
def repay():
    pass

#7.查看流水
def check_flow():
    pass

#8.购物车功能
def shopping_car():
    pass

#9.查看购物车
def check_shopping_car():
    pass

#10.注销
def logout():
    pass

#选择功能的字典
func_dic={'1':register,
          '2':login,
          '3':check_balance,
          '4':withdraw,
          '5':transfer,
          '6':repay,
          '7':check_flow,
          '8':shopping_car,
          '9':check_shopping_car,
          '10':logout,
          }



def run():
    while True:
        print('''
    1、注册
    2、登录
    3、查看余额
    4、提现
    5、转账
    6、还款
    7、查看流水
    8、购物车功能
    9、查看购物车
    10、注销
        ''')
        choose = input("请输入功能编号").strip()

        if choose == 'q':
            break
        if choose not in func_dic:
            print("请选择功能的编号！")
            continue

        #调用用户选择的功能
        func_dic[choose]()