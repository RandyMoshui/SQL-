# 一、创建数据库与表（部分）
## 1.创建数据库
create database online_course;

## 2.创建登录表
create table Users
(
id char(12) NOT NULL,  --用户名
pwd varchar(16) NOT NULL CHECK(len([pwd])>=8 and len([pwd])<=16), --设置密码长度需在8-16位之间
login_kind char(1) NOT NULL CHECK(login_kind='T' or login_kind='S') --登录类型（管理员,学生）
)

## 3.创建学生表
create table Student( --学生表
Sno char(12) Not Null,
sname varchar(12) Not Null,
Sage smallint check(Sage>=0 and Sage<=300) Not Null, --年龄（0-300）
academy varchar(20), --学院
Sdept varchar(20), --系别
PRIMARY KEY (Sno),
FOREIGN KEY(Sno) references Users(id)
)

## 4.创建院系表
create table academy -- 院系表
(
academy varchar(20) not null,
Sdept varchar(20) not null unique
)

## 5.创建教师表
create table teacher – 教师表
(
Tno char(12) Not Null,
Tname varchar(12) Not Null,
Tage smallint check(Tage>=0 and Tage<=300) Not Null, --年龄（0-300）
academy varchar(20), --学院
Sdept varchar(20), --系别
PRIMARY KEY (Tno),
FOREIGN KEY(Tno) references Users(id),
FOREIGN KEY(Sdept) references academy(Sdept)
)

## 6.创建课程表
-- 课程表
create table Course(
Cno char(4) not null,
Cname varchar(40) not null,
Cpno varchar(4),
Ccredit smallint,
PRIMARY KEY(Cno)
)


## 7.创建选课表
-- 选课表
create table SC(
Sno char(12) not null,
Cno char(4) not null,
Grade smallint check(Grade>=0 and Grade<=100)
FOREIGN KEY(Sno) references Student(Sno),
FOREIGN KEY(Cno) references Course(Cno)
)

## 8.创建授课表
-- 授课表
create table TC(
Tno char(12) not null,
Cno char(4) not null,
FOREIGN KEY(Tno) references Teacher(Tno),
FOREIGN KEY(Cno) references Course(Cno)
)

## 9.创建课堂任务表
create table class_task
(
Cno char(4) not null,
task_name varchar(20) not null,
task_content varchar(1000),
task_type varchar(4) check(task_type='U' or task_type='V' or task_type='R')
Foreign KEY(Cno) references Course(Cno)
)


# 二、插入数据和增加约束
## 1.部分插入记录数据
INSERT INTO Users Values ('201983290527','zjh5729.','S')

INSERT INTO Users Values ('123456789012','12345678.','T')

## 2.部分增加约束记录
alter table Student
ADD constraint fk_DPT foreign key (Sdept) references academy(Sdept)
on update cascade on delete cascade
（PS：这部分外检约束开始时未声明级联，而后通过图形化界面开启级联）

# 三、存储过程的创建
## 1.增加老师
--增加老师
create proc add_teacher
@Tno char(12),
@Tname varchar(12),
@Tage smallint,
@academy varchar(20),
@Sdept varchar(20)
as
Insert into Users(id,pwd,login_kind)
values(@Tno,'12345678','T') --默认密码12345678

Insert into teacher(Tno,Tname,Tage,academy,Sdept)
values(@Tno,@Tname,@Tage,@academy,@Sdept)

## 2.增加学生
--增加学生
create proc add_student
@Sno char(12),
@Sname varchar(12),
@sage smallint,
@academy varchar(20),
@Sdept varchar(20)
as
Insert into Users(id,pwd,login_kind)
values(@Sno,'12345678','S') --默认密码12345678

Insert into Student(Sno,Sname,sage,academy,Sdept)
values(@Sno,@Sname,@sage,@academy,@Sdept)

## 3.增加选课信息
create proc add_student_to_course
@Sno char(12),
@Cno char(4)
as 
IF exists(select * from SC where Sno=@Sno and Cno=@Cno)
print'学生已存在！';
ELSE
Insert into SC(Sno,Cno) values(@Sno,@Cno);

## 4.删除选课信息
--删除学生
create proc delete_student_from_course @Sno char(12),@Cno char(4) as Delete from SC where Sno=@Sno and Cno=@Cno

declare @Sno char(12),@Cno char(4) set @Sno='201983290531' set @Cno='0002' exec delete_student_from_course @Sno,@Cno


## 5.修改密码
--创建存储过程（修改密码）
create proc change_pwd @id char(12),@oldpwd varchar(16),@newpwd varchar(16)
as
IF @oldpwd=(select pwd from Users where id=@id)
update Users SET pwd=@newpwd where id=@id

## 6.新建课堂任务
--新建课堂任务
create proc add_class_task
@Cno char(4),
@task_name varchar(20),
@task_content varchar(1000),
@task_type varchar(4)
as
Insert into class_task(Cno,task_name,task_content,task_type)
values (@Cno,@task_name,@task_content,@task_type)

## 7.删除课堂任务
create proc delete_class_task
@Cno char(4),
@task_name varchar(20)
as
Delete from class_task where Cno=@Cno and task_name=@task_name


## 8.更改课堂任务
create proc change_class_task
@Cno char(4),
@task_name varchar(20),
@task_content varchar(1000),
@task_type varchar(4)

as

update class_task SET task_type=@task_type
where task_name=@task_name and Cno=@Cno

update class_task 
Set task_content=@task_content 
where task_name=@task_name and Cno=@Cno

## 9.重置密码
--创建存储过程（重置密码）
create proc reset_pwd
@id char(12)
as
update Users SET pwd='12345678' where id=@id

create proc delete_user
@id char(12)
as
Delete from Users where id=@id

## 10.增加课程
create proc add_course
@Cno char(4),
@Cname varchar(40),
@Ccredit smallint
as
insert into Course(Cno,Cname,Ccredit)
values (@Cno,@Cname,@Ccredit)


## 11.增加选课信息
create proc add_SC
@Sno char(12),
@Cno char(4)
as
insert into SC(Sno,Cno)
values (@Sno,@Cno)

## 12.增加授课信息

create proc add_TC
@Tno char(12),
@Cno char(4)
as
insert into TC(Tno,Cno)
values (@Tno,@Cno)

