import re
fieldname = 'student.txt'
def insert(students):
    while True:
        student = {}
        name = input("请输入学生姓名（结束添加请按Q）：")
        if name == 'Q':
            break
        student['name'] = name
        while True:
            age = input("请输入学生年龄：")
            try:
                age = int(age)
                if age < 0 or age > 150:
                    print("年龄输入不合法，请重新输入！")
                    continue
            except ValueError:
                print("年龄输入不合法，请输入一个数字！")
                continue
            else:
                student['age'] = age
                break
        while True:
            score = input("请输入学生成绩：")
            try:
                score = float(score)
                if score < 0 or score > 100:
                    print("成绩输入不合法，请重新输入！")
                    continue
            except ValueError:
                print("成绩输入不合法，请输入一个数字！")
                continue
            else:
                student['score'] = score
                break
        students.append(student)
    print("学生信息添加完成！")

def menu():
    students = []
    while True:
        print("="*50)
        print("欢迎使用学生信息管理系统v1.0".center(48))
        print("1. 添加学生信息".ljust(45))
        print("2. 查找学生信息".ljust(45))
        print("3. 修改学生信息".ljust(45))
        print("4. 删除学生信息".ljust(45))
        print("5. 排序学生信息".ljust(45))
        print("6. 统计学生总人数".ljust(45))
        print("7. 显示所有学生信息".ljust(45))
        print("0. 退出系统".ljust(45))
        print("="*50)
        option = input("请输入对应的功能选项：")
        if option == '1':
            insert(students)
        elif option == '2':
            search(students)
        elif option == '3':
            modify(students)
        elif option == '4':
            delete(students)
        elif option == '5':
            sort(students)
        elif option == '6':
            get_total_num(students)
        elif option == '7':
            show(students)
        elif option == '0':
            print("感谢使用学生信息管理系统，再见！")
            break
        else:
            print("无效选项，请重新输入。")
          
menu()  # 在程序开始调用菜单函数，显示功能菜单界面

#调用save()函数
def save(students):
    try:
        stu_txt = open(fieldname, 'a', encoding='utf-8')
    except:
        stu_txt = open(fieldname, encoding='utf-8')
    for item in students:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()

# 调用insert()函数
students = []
insert(students)
# 调用save()函数
save(students)
print('学生信息录入完毕')

def search(students):
    while True:
        option = input("请输入查找方式（1. 按姓名查找\t2. 按成绩范围查找\t3. 返回上一级菜单）：")
        if option == '1':
            name = input("请输入要查找的学生姓名：")
            result = []
            for s in students:
                if s['name'] == name:
                    result.append(s)
            if result:
                print("姓名\t\t年龄\t\t成绩")
                for r in result:
                    print("{}\t\t{}\t\t{}".format(r['name'], r['age'], r['score']))
            else:
                print("没有找到该学生信息。")
        elif option == '2':
            min_score = input("请输入成绩最低分数：")
            max_score = input("请输入成绩最高分数：")
            result = []
            for s in students:
                if s['score'] >= float(min_score) and s['score'] <= float(max_score):
                    result.append(s)
            if result:
                print("姓名\t\t年龄\t\t成绩")
                for r in result:
                    print("{}\t\t{}\t\t{}".format(r['name'], r['age'], r['score']))
            else:
                print("没有找到符合条件的学生信息。")
        elif option == '3':
            break
        else:
            print("无效选项，请重新输入。")

def delete(students):
    name = input("请输入要删除的学生姓名：")
    result = None
    for s in students:
        if s['name'] == name:
            result = s
    if result:
        students.remove(result)
        print("学生信息删除成功！")
    else:
        print("没有找到该学生信息。")

def modify(students):
    name = input("请输入要修改的学生姓名：")
    result = None
    for s in students:
        if s['name'] == name:
            result = s
    if result:
        result['age'] = input("请输入学生年龄：")
        result['score'] = input("请输入学生成绩：")
        print("学生信息修改成功！")
    else:
        print("没有找到该学生信息。")

def sort(students):
    option = input("请输入排序方式（1. 按姓名升序\t2. 按成绩降序）：")
    if option == '1':
        students.sort(key=lambda x: x['name'])
    elif option == '2':
        students.sort(key=lambda x: x['score'], reverse=True)
    else:
        print("无效选项，请重新输入。")
def get_total_num(students):
    print("当前学生总人数为：{}".format(len(students)))

def show(students):
    if len(students) == 0:
        print("学生信息列表为空。")
    else:
        print("姓名\t\t年龄\t\t成绩")
        for s in students:
            print("{}\t\t{}\t\t{}".format(s['name'], s['age'], s['score']))

def main():
    students = []
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu() # 显示菜单
        option = input("请选择：") # 选择菜单项
        option_str = re.sub("\D","",option) # 提取数字
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int = int(option_str)
            if option_int == 0: # 退出系统
                print('您已退出学生信息管理系统！')
                ctrl = False
            elif option_int == 1: # 录入学生成绩信息
                insert(students)
            elif option_int == 2: # 查找学生成绩信息
                search(students)
            elif option_int == 3: # 删除学生成绩信息
                delete(students)
            elif option_int == 4: # 修改学生成绩信息
                modify(students)
            elif option_int == 5: # 排序
                sort(students)
            elif option_int == 6: # 统计学生总数
                total(students)
            elif option_int == 7: # 显示所有学生信息
                show(students)



