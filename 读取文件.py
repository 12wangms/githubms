with open ("word.text","r")as f:
    content=f.readlines()
    print(content)
    count=0
    for x in content:
        print(x)
        if"itheima" in x:
            coumt+=1
            print(count)
