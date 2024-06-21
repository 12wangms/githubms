def get_user_info():
    name = input("请输入您的名字: ")
    age = int(input("请输入您的年龄: "))
    return name, age


def welcome_message(name, age):
    if age >= 0:
        if age < 18:
            status = "未成年"
        elif age >= 18 and age < 60:
            status = "成年"
        else:
            status = "老年"

        print(f"欢迎 {name}！您现在是{status}人。")
    else:
        print("年龄输入不正确，请输入一个非负整数。")

    # 主程序开始


name, age = get_user_info()
welcome_message(name, age)