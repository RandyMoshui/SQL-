from flask import Flask, render_template, request, redirect, session
from 数据库.sql import ODBC
import pymssql

app = Flask(__name__, template_folder='templates')
app.secret_key = 'asdasfedrfgsdgt'  # session加盐保存


def main(query_str):
    try:
        ms = ODBC(server='localhost', uid='sa', pwd='zjh5729.', db="online_course")
        sql = ms.ExecQuery(query_str)
        return sql

    except:
        print("数据库连接出错")
        return []


def change_pwd(id, oldpwd, newpwd):
    try:
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('change_pwd', (id, oldpwd, newpwd))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def add_class_task(cno, task_name, task_content, task_type):
    try:
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('add_class_task', (cno, task_name, task_content, task_type))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True

    except:
        print("数据库连接出错")
        return False


def delete_class_task(cno, task_name):
    try:
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('delete_class_task', (cno, task_name))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True

    except:
        print("数据库连接出错")
        return False


def change_class_task(cno, task_name, task_content, task_type):
    try:
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('change_class_task', (cno, task_name, task_content, task_type))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True

    except:
        print("数据库连接出错")
        return False


def sql_add_teacher(Tno, Tname, Tage, academy, Sdept):
    try:
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('add_teacher', (Tno, Tname, Tage, academy, Sdept))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def sql_add_student(Sno, Sname, sage, academy, Sdept):
    try:
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('add_student', (Sno, Sname, sage, academy, Sdept))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def sql_reset_pwd(id):
    try:
        # print(id)
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('reset_pwd', (id,))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def sql_delete_user(id):
    try:
        # print(id)
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('delete_user', (id,))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def sql_add_course(Cno,Cname,Ccredit):
    try:
        # print(id)
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('add_course', (Cno, Cname, Ccredit))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def sql_add_SC(Sno,Cno):
    try:
        # print(id)
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('add_SC', (Sno, Cno))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False


def sql_add_TC(Tno,Cno):
    try:
        # print(id)
        server = "127.0.0.1"
        user = "sa"
        password = "zjh5729."
        database = "online_course"

        db = pymssql.connect(server, user, password, database)
        cursor = db.cursor()
        cursor.callproc('add_TC', (Tno, Cno))
        db.commit()
        row = cursor.nextset()
        db.close()
        return True
    except:
        print("数据库连接出错")
        return False




@app.route('/login', methods=['GET', 'POST'])
# 表示将url和函数创建关系，当访问该url时，即执行该函数
# method为允许请求的方法
def login():
    # 视图函数无参数

    if request.method == 'GET':
        return render_template('login.html')
    # request.args # 获取get传来的值
    user = request.form.get('user')  # 获取POST传过来的值
    pwd = request.form.get('pwd')
    if len(main('SELECT * from Users where id=' + user)) != 0:
        # 将用户信息放入session,从而防止直接进入index
        if len(main("SELECT * from Users where id=" + user + "and pwd='" + pwd + "'")) != 0:
            # 读取登录类型
            session['user_info'] = user  # 将信息放入cookie
            session['type_info'] = main("SELECT * from Users where id=" + user + "and pwd='" + pwd + "'")[0][2]
            if session.get('type_info') == 'S':
                return redirect('/stu_index')
            elif session.get('type_info') == 'T':
                return redirect('/tea_index')
            else:
                return redirect('/index')
        else:
            return render_template('login.html', **{'msg': '用户名或密码错误'})
    else:
        return render_template('login.html', **{'msg': '用户名或密码错误'})
        # 页面返回报错信息 也可使用 render_template('login.html',msg='用户名或密码错误')


@app.route('/', methods=['GET', 'POST'])  # 默认转向stu_index
@app.route('/index', methods=['GET', 'POST'])  # index转向stu_index
@app.route('/stu_index', methods=['GET', 'POST'])
def stu_index():
    user_info = session.get('user_info')
    if not user_info:  # 用户鉴权
        return redirect('/login')  # 鉴权失败，转向登录界面
    if session.get('type_info') == 'T':  # 当用户为教师类型时，转向教师首页
        return redirect('/tea_index')
    elif session.get('type_info') == 'administrator':
        return redirect('/admin_index')
    elif session.get('type_info') != 'S':
        return redirect('/logout')

    # 显示已选课程
    choosen_course = dict(main("select Course.Cname,Course.Cno from Course,SC "
                               "where SC.Sno='" + user_info + "' and SC.Cno=Course.Cno"))
    # print(choosen_course)

    # 显示各科成绩
    grades = main(
        "select Course.Cname,SC.Grade from SC,Course where SC.Sno='" + user_info + "' and SC.Cno=Course.Cno")
    # print(type(grades),grades)

    # 仅接受到GET请求时
    if request.method == 'GET':
        return render_template('stu_index.html', courses=choosen_course, grades=grades,
                               **{'msg': user_info
                                  })

    # 当有POST请求时
    oldpwd = request.form.get('oldpwd')
    newpwd1 = request.form.get('newpwd1')
    newpwd2 = request.form.get('newpwd2')

    if newpwd2 != newpwd1:
        return render_template('stu_index.html', courses=choosen_course, grades=grades,
                               **{'msg': user_info,
                                  'wrongmsg': '两次新密码输入不同，请重新输入'
                                  })
    elif newpwd2 == newpwd1:
        if len(main("SELECT * from Users where id=" + user_info + "and pwd='" + oldpwd + "'")) == 0:
            return render_template('stu_index.html', courses=choosen_course, grades=grades,
                                   **{'msg': user_info,
                                      'wrongmsg': '修改密码失败，请稍后重试'
                                      })

        elif change_pwd(user_info, oldpwd, newpwd1):
            return redirect('/logout')
        else:
            return render_template('stu_index.html', courses=choosen_course, grades=grades,
                                   **{'msg': user_info,
                                      'wrongmsg': '修改密码失败，请稍后重试'
                                      })


@app.route('/tea_index', methods=['GET', 'POST'])
def tea_index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    if session.get('type_info') == 'S':
        return redirect('/stu_index')
    elif session.get('type_info') == 'administrator':
        return redirect('/admin_index')
    elif session.get('type_info') != 'T':
        return redirect('/logout')

    # 教授课程
    teaching_course = dict(main("select Course.Cname,Course.Cno from Course,TC "
                                "where TC.Tno='" + user_info + "' and TC.Cno=Course.Cno"))

    # 仅接受到GET请求时
    if request.method == 'GET':
        return render_template('tea_index.html', courses=teaching_course,
                               **{'msg': user_info,
                                  })

    # 当有POST请求时
    oldpwd = request.form.get('oldpwd')
    newpwd1 = request.form.get('newpwd1')
    newpwd2 = request.form.get('newpwd2')

    if newpwd2 != newpwd1:
        return render_template('tea_index.html', courses=teaching_course,
                               **{'msg': user_info,
                                  'wrongmsg': '两次新密码输入不同，请重新输入'
                                  })
    elif newpwd2 == newpwd1:
        if len(main("SELECT * from Users where id=" + user_info + "and pwd='" + oldpwd + "'")) == 0:
            return render_template('tea_index.html', courses=teaching_course,
                                   **{'msg': user_info,
                                      'wrongmsg': '修改密码失败，请稍后重试'
                                      })
        elif change_pwd(user_info, oldpwd, newpwd1):
            return redirect('/logout')
        else:
            return render_template('tea_index.html', courses=teaching_course,
                                   **{'msg': user_info,
                                      'wrongmsg': '修改密码失败，请稍后重试'
                                      })


@app.route('/stu_detail')
def stu_detail():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    if session.get('type_info') == 'T':
        return redirect('/tea_index')
    elif session.get('type_info') != 'S':
        return redirect('/logout')

    cno = request.args.get('cno')
    # print('当前cno为:', cno)
    # 显示课堂任务
    tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")
    # print("课堂任务为：",tasks)
    if len(main("select * from SC where Cno='" + cno + "' and Sno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
        return redirect('/stu_index')
    info = main(
        "select Course.Cname,Course.Cno,teacher.Tname from Course,TC,teacher where Course.Cno='" + cno + "' and TC.Cno=Course.Cno and teacher.Tno=TC.Tno")
    # print(info)

    print("请求类型为：", request.method)

    return render_template('stu_detail.html', Cname=info[0][0], Cno=info[0][1], Tname=info[0][2], tasks=tasks)


@app.route('/tea_detail', methods=['GET', 'POST'])
def tea_detail():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    if session.get('type_info') == 'S':
        return redirect('/stu_index')
    elif session.get('type_info') != 'T':
        return redirect('/logout')

    if request.method == 'GET':
        cno = request.args.get('cno')
        # print('当前cno为:', cno)
        if len(main("select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
            return redirect('/tea_index')
        info = main(
            "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
        # print(info)
        class_info = [info[0][0], info[0][1]]
        # print(class_info)
        student_info = {i[2]: i[3] for i in info}
        # print(student_info)

        # print("请求类型为：", request.method)

        tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

        return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                               tasks=tasks)

    cno = request.form.get('cno')
    task_name = request.form.get('task_name')
    task_content = request.form.get('task_content')
    task_type = request.form.get('task_type')
    if len(main("select * from TC where Tno='" + user_info + "' and Cno='" + cno + "'")) == 0:
        print(main("select * from TC where Tno='" + user_info + "' and Cno='" + cno + "'"))
        return redirect('/logout')  # 检测是否有异常越权post行为，若有，则强制退出账户

    if len(main("select * from class_task where Cno='" + cno + "' and task_name='" + task_name + "'")) != 0:
        info = main(
            "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
        # print(info)
        class_info = [info[0][0], info[0][1]]
        # print(class_info)
        student_info = {i[2]: i[3] for i in info}
        # print(student_info)

        # print("请求类型为：", request.method)
        tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

        return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                               tasks=tasks,
                               **{'msg': '任务名重复！请重新输入！'})

    if add_class_task(cno, task_name, task_content, task_type):
        if len(main("select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
            return redirect('/tea_index')
        info = main(
            "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
        # print(info)
        class_info = [info[0][0], info[0][1]]
        # print(class_info)
        student_info = {i[2]: i[3] for i in info}
        # print(student_info)

        # print("请求类型为：", request.method)
        tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

        return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                               tasks=tasks,
                               **{'msg': '增加任务成功'})
    else:
        if len(main("select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:
            # 判断用户是否有权限访问课程详细信息
            return redirect('/tea_index')
        info = main(
            "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
        # print(info)
        class_info = [info[0][0], info[0][1]]
        # print(class_info)
        student_info = {i[2]: i[3] for i in info}
        # print(student_info)

        # print("请求类型为：", request.method)
        tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

        return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                               tasks=tasks,
                               **{'msg': '增加任务失败，请稍后再试'})


@app.route('/change_task/', methods=['GET', 'POST'])
def change_task():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    if session.get('type_info') == 'S':
        return redirect('/stu_index')
    elif session.get('type_info') != 'T':
        return redirect('/logout')

    if request.method == 'POST':
        cno = request.form.get("cno")
        operation_type = request.form.get('operation_type')
        choose_task = request.form.get('choose_task')

        if len(main("select * from TC where Tno='" + user_info + "' and Cno='" + cno + "'")) == 0:
            print(main("select * from TC where Tno='" + user_info + "' and Cno='" + cno + "'"))
            return redirect('/logout')  # 检测是否有异常越权post行为，若有，则强制退出账户

        if operation_type == 'd':
            if delete_class_task(cno, choose_task):
                if len(main(
                        "select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
                    return redirect('/tea_index')
                info = main(
                    "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
                # print(info)
                class_info = [info[0][0], info[0][1]]
                # print(class_info)
                student_info = {i[2]: i[3] for i in info}
                # print(student_info)

                # print("请求类型为：", request.method)
                tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

                return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                                       tasks=tasks,
                                       **{'msg2': '删除任务成功'})
            else:
                if len(main(
                        "select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
                    return redirect('/tea_index')
                info = main(
                    "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
                # print(info)
                class_info = [info[0][0], info[0][1]]
                # print(class_info)
                student_info = {i[2]: i[3] for i in info}
                # print(student_info)

                # print("请求类型为：", request.method)
                tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

                return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                                       tasks=tasks,
                                       **{'msg2': '删除任务失败'})

        elif operation_type == 'c':
            change_type = request.form.get('change_type')
            change_task_content = request.form.get('change_task_content')
            if change_class_task(cno, choose_task, change_task_content, change_type):
                if len(main(
                        "select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
                    return redirect('/tea_index')
                info = main(
                    "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
                # print(info)
                class_info = [info[0][0], info[0][1]]
                # print(class_info)
                student_info = {i[2]: i[3] for i in info}
                # print(student_info)

                # print("请求类型为：", request.method)
                tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

                return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                                       tasks=tasks,
                                       **{'msg2': '修改任务成功'})
            else:
                if len(main(
                        "select * from TC where Cno='" + cno + "' and Tno='" + user_info + "'")) == 0:  # 判断用户是否有权限访问课程详细信息
                    return redirect('/tea_index')
                info = main(
                    "select Course.Cname,Course.Cno,Student.Sno,Student.sname from Course,SC,Student where Course.Cno='" + cno + "' and SC.Cno=Course.Cno and Student.Sno=SC.Sno")
                # print(info)
                class_info = [info[0][0], info[0][1]]
                # print(class_info)
                student_info = {i[2]: i[3] for i in info}
                # print(student_info)

                # print("请求类型为：", request.method)
                tasks = main("select task_name,task_content,task_type from class_task where Cno='" + cno + "'")

                return render_template('tea_detail.html', Cname=class_info[0], Cno=class_info[1], students=student_info,
                                       tasks=tasks,
                                       **{'msg2': '修改任务失败'})


@app.route('/logout')
def logout():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    print('user：', session['user_info'], '正在登出')
    del session['user_info']
    return redirect('/login')


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    # request.args # 获取get传来的值
    user = request.form.get('user')  # 获取POST传过来的值
    pwd = request.form.get('pwd')
    if len(main('SELECT * from admin_users where id=' + user)) != 0:  # 判定用户存在与表中
        # 将用户信息放入session,从而防止直接进入index
        if len(main("SELECT * from admin_users where id=" + user + "and pwd='" + pwd + "'")) != 0:  # 判断密码是否正确
            # 读取登录类型
            session['user_info'] = user  # 将信息放入cookie
            session['type_info'] = 'administrator'
            return redirect('/admin_index')
        else:
            return render_template('login.html', **{'msg': '用户名或密码错误'})
    else:
        return render_template('login.html', **{'msg': '用户名或密码错误'})
        # 页面返回报错信息 也可使用 render_template('login.html',msg='用户名或密码错误')


@app.route('/admin_index')
def admin_index():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info})


@app.route('/admin_add_teacher/', methods=['POST'])
def add_teacher():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    tno = request.form.get('id')
    tname = request.form.get('name')
    tage = request.form.get('choose_age')
    academy = request.form.get('choose_academy')
    sdept = request.form.get("choose_sdept")

    if sql_add_teacher(tno, tname, tage, academy, sdept):
        wrongmsg = "增加老师成功！"

    else:
        wrongmsg = "增加老师失败！"

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info,
                              'wrongmsg_add_teacher': wrongmsg})


@app.route('/admin_add_student/', methods=['POST'])
def add_student():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    sno = request.form.get('id')
    sname = request.form.get('name')
    sage = request.form.get('choose_age')
    academy = request.form.get('choose_academy')
    sdept = request.form.get("choose_sdept")

    if sql_add_student(sno, sname, sage, academy, sdept):
        wrongmsg = "增加学生成功！"

    else:
        wrongmsg = "增加学生失败！"

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info,
                              'wrongmsg_add_student': wrongmsg})


@app.route('/admin_reset_pwd/', methods=['POST'])
def reset_pwd():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    sql_id = request.form.get('id')
    print(sql_id)

    if sql_reset_pwd(sql_id):
        wrongmsg = "重置密码成功！"

    else:
        wrongmsg = "重置密码失败！"

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info,
                              'wrongmsg_reset_pwd': wrongmsg})


@app.route('/admin_delete_user/', methods=['POST'])
def delete_user():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    # print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    # print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    sql_id = request.form.get('delete_id')
    # print(sql_id)

    wrongmsg = '未知错误'

    if sql_delete_user(sql_id):
        wrongmsg = "删除用户成功！"

    else:
        wrongmsg = "删除用户失败！"

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info,
                              'wrongmsg_delete_user': wrongmsg})


@app.route('/admin_add_course/', methods=['POST'])
def add_course():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    # print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    # print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    sql_cno = request.form.get('cno')
    sql_cname = request.form.get('cname')
    sql_ccredit = request.form.get('ccredit')

    wrongmsg = '未知错误'

    if sql_add_course(sql_cno, sql_cname, sql_ccredit):
        wrongmsg = "增加课程成功！"

    else:
        wrongmsg = "增加课程失败！"

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info,
                              'wrongmsg_add_course': wrongmsg})


@app.route('/admin_choose_course/', methods=['POST'])
def choose_course():
    user_info = session.get('user_info')
    user_type = session.get('user_type')
    if not user_info:
        return redirect('/login')
    if user_type != 'administrator':
        redirect('/logout')

    choose_academy = main("select distinct academy from academy")
    # print(choose_academy)
    choose_sdept = main("select Sdept from academy")
    # print(choose_sdept)
    ids = main("select id from Users")
    courses = main("select Cno from Course")

    sql_id_type = request.form.get('id_type')
    sql_id = request.form.get('id')
    sql_course = request.form.get('add_choose_course')

    wrongmsg='未知错误'

    if sql_id_type == 'T':
        if len(main("select * from teacher where Tno='" + sql_id + "'")) == 0:
            wrongmsg = "输入信息有误！"

        elif sql_add_TC(sql_id, sql_course):
            wrongmsg = "增加老师授课信息成功"
        else:
            wrongmsg = "增加老师授课信息失败"

    elif sql_id_type == 'S':
        if len(main("select * from Student where Sno='" + sql_id + "'")) == 0:
            wrongmsg = "输入信息有误！"

        elif sql_add_SC(sql_id, sql_course):
            wrongmsg = "增加学生选课信息成功"
        else:
            wrongmsg = "增加学生选课信息失败"

    return render_template('admin_index.html',
                           academys=choose_academy, sdepts=choose_sdept, ids=ids, courses=courses,
                           **{'msg': user_info,
                              'wrongmsg_choose_course': wrongmsg})


if __name__ == '__main__':
    app.run(debug=True)
