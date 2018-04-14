'''
找人程序（4分）
题目内容：

有5名某界大佬xiaoyun、xiaohong、xiaoteng、xiaoyi和xiaoyang，其QQ号分别是88888、5555555、11111、12341234和1212121，用字典将这些数据组织起来。编程实现以下功能：用户输入某一个大佬的姓名后输出其QQ号，如果输入的姓名不在字典中则输出字符串“Not Found”。
程序框架如下：
def find_person(dict_users, strU):
     if user is in the dict:
        return user's QQ
     else:
        return 'Not Found'
if __name__ == "__main__":
     create a dict named dict_users
     strU =  input()
     print(find_person(dict_users, strU))

'''

#有了框架来根据要求填充内容   


def find_person(dict_users,strU):
    if strU in dict_users.keys():
        userQQ = dict_users[strU]
        return userQQ
    else:
        return 'Not Found'

if __name__ =='__main__':
    dict_users = {'xiaoyun':'88888','xiaohong':'5555555','xiaoteng':'11111',
        'xiaoyang':'121212','xiaoyi':'12341234'}
    strU = input()
print(find_person(dict_users,strU))
