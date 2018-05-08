def find():
    Int=0
    Str=0
    Space=0
    Others=0
    a=input('Please input a string:')
    for strs in a:
        if strs.isalpha():
            Str+=1
        elif strs.isdigit():
            Int+=1
        elif strs.isspace():
            Space+=1
        else:
            Others+=1
    print("中英文字符有%d个"%Str)
    print("数字有%d个"%Int)
    print("空格有%d个"%Space)
    print("其他字符有%d个"%Others)
