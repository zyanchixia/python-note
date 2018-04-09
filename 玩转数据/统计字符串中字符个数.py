#统计字符串中的字符个数
'''
题目内容：
定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数
（允许输入大写字符，并且计数时不区分大小写）
'''

def countchar(str):
    num = [0] * 26
    str = str.low()#支持输入大写字符，统一转换为小写
    for i in range(len(str)):#遍历字符串
        if str[i].isalpha():#检测字符串是否只由字母组成
            temp = ord(str[i])-ord('a') #计算个数
            #ord('a')返回对应的十进制整数为97，b为98，详情查看ord()函数
            num[temp] += 1#将个数累积
    return num

if __name__ == '__main__':
    str = input()
    print(countchar(str))
        
