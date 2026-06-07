from greeting import greet, farewell

def main():
    ""主函数 - 集成问候功能""
    print("Hello, Git!")
    print("项目初始化完成")
    
    name = input("请输入您的名字: ")
    print(greet(name))
    print(farewell(name))

if __name__ == "__main__":
    main()

