def Count(s):
    intCount = 0
    enCount = 0
    chCount = 0
    spaceCount = 0
    otherCount = 0
    for i in s:
        if i>= u'\u4e00'and i<=u'\u9fa5':
            chCount += 1
        elif i.isalpha():
            enCount += 1
        elif i.isdigit():
            intCount += 1
        elif i.isspace():
            spaceCount += 1
        else:
            otherCount += 1
    print("����=%d,Ӣ��=%d,����=%d,�ո�=%d,����=%d " % (chCount,enCount,intCount,spaceCount,otherCount))