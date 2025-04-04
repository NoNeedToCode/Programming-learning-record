asd="{} {} {} {}"

print(asd.format(1,2,3,4))
print(asd.format("one","two","three","four"))
print(asd.format(True,False,True,False))
print(asd.format(asd,asd,asd,asd,2))#数字和特殊单词可以直接打出 其余视为字符 需要翻译 个数只取前四个
print(asd.format(
    "Try your",
    "Own test here",
    "Maybe a poem",
    "Or a song about fear"
))
