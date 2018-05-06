import string
oStr = input('请输入一串字符:')
str_num = 0
spac_num = 0
figue_num = 0
zw_num=0
qt_num=0
for strs in oStr:
    if strs in string.ascii_letters:
        str_num +=1
    elif strs.isdigit():
        figue_num +=1
    elif strs == ' ':
        spac_num +=1
    elif strs.isalpha():
        zw_num +=1   
    else:
        qt_num +=1 
print ('英文字母有：%d' %str_num)
print ('中文有：%d'%zw_num)
print ('数字有：%d'%figue_num)
print ('空格有：%d'%spac_num)
print ('其他字符有：%d'%zw_num)
