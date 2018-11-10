#print "Hello World!"
# print("我于杀戮中绽放，亦如黎明中的花朵，只有完美才是可接受的！")

# cars = 100
# num =  "ab"
# print (cars,num)
# print ("hello %s word! " % "12" )
# print ('num is %s' % num)
# binary = "binary"
# do_not = "don't"
# y = "those who know %s and those who %s" % (binary, do_not)
# print (y)
# x = "there are %d apple" % 10
# print ("I %r" %  x)
# print ("I also say '%s'" % y)
# boolen =  False
# joke = "so funny % r"
# print (joke)
# print (joke % boolen)
# print ("abn" * 10, do_not )
# print ("How old are you?"),
# # # age = input ("input:")
# # # print ("so, you're %s old" % age)
# from sys import argv
# script, first, second, third = argv
# print ("the script is called:", script)
# print ("your first variable is", first)
# print ("Your second variable is:", second)
# print ("Your third variable is:", third)
# def print_tow(*args):
# #     arg1, arg2 = args
# #     print ("arg1: %r, arg2: %r" % (arg1, arg2))
# # print_tow("123","131")
# def print_two_again(arg1, arg2):
#     print ("arg1: %r, arg3: %r" % (arg1, arg2))
# print_two_again(123,"131a")
# def cheese_and_crackers()
# from sys import argv
# script, input_file = argv
# def print_all(f):
#     print f.read()
#
# def  rewind(f):
#     f.seek(0)

# path = r'C:\Users\DMJ\Desktop\工作日常记录\资料\test.txt'
# file_name = open(path,'r')
# a = file_name.readline()
# b = file_name.readline()
# print(a)
# print(b)
# file_name.close()

# def add(a, b):
#     print ("ADDING %d + %d" % (a, b))
#     return a + b
# age = add(12, 12)
# print (age)

# a = float(input())
# print (a)

# poem = """\tThe lovely world" \
#        12""
# print (poem)

# def break_words(stuff):
#     """This function will break up words fot us."""
#     words = stuff.split(' ')
#     return words
#
# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words)
#
# def print_first_word(words):
#     """Prints the first wors after poppint it off."""
#     word = words.pop(0)
#     print (word)
#
# def print_last_word(words):
#     """Prints the last word after poppint it off."""
#     word = words.pop(-1)
#     print (word)
#
# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)
#
# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# break_words("avsd")

# def break_words(stuff):
#     """This function will break up words for us."""
#     words = stuff.split(' ')
#     return words
#
# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words)
#
# def print_first_word(words):
#     """Prints the first word after popping it off."""
#     word = words.poop(0)
#     print (word)
#
# def print_last_word(words):
#     """Prints the last word after popping it off."""
#     word = words.pop(-1)
#     print (word)
#
# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)
#
# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
#
# print ("Let's practice everything.")
# print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#
# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explantion
# \n\t\twhere there is none.
# """
#
#
# print ("--------------")
# print (poem)
# print ("--------------")
#
# five = 10 - 2 + 3 - 5
# print ("This should be five: %s" % five)
#
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates
#
#
# start_point = 10000
# beans, jars, crates = secret_formula(start_point)
#
# print ("With a starting point of: %d" % start_point)
# print ("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))
#
# start_point = start_point / 10
#
# print ("We can also do that this way:")
# print ("We'd have %d beans, %d jars, and %d crabaapples." % secret_formula(start_point))
#
#
# sentence = "All god\tthings come to those who weight."
#
# words = break_words(sentence)
# sorted_words = sort_words(words)
#
# print_first_word(words)
# # print_last_word(words)
# # print_first_word(sorted_words)
# # print_last_word(sorted_words)
# # sorted_words = ex25.sort_sentence(sentence)
# # prin (sorted_words)
# #
# # print_irst_and_last(sentence)
# #
# # print_first_a_last_sorted(senence)

# people = 20
# cats = 30
# dogs = 15
# if people < cats:
#     print ("Too many cats!")
# elif people > cats:
#     print ("We should not take the cat!")
# else:
#     print ("Everyone can get a cat!")

# door = input("> ")
# if door == "1":
#     print ("intput number is one")

# hairs = ['brown', 'blond', 'res']
# weights = [1, 2, 3]
# for coller in hairs:
#     print ("This coller id %s" % coller)

# change = [1, 'pennies', 2, 'diems', 3, 'quarters']
# for i in change:
#     print ("I got %r" % i)
# elements = []
# for i in range(0, 3):
#      print("The number is %d." % i)
#      elements.append(i)
# for i in elements:
#     print("Element was: %d" % i)

# i = 0
# numbers = []
# count = int(input("> "))
# while i < count:
#     print ("At the top i is %d" % i)
#     numbers.append(i)
#
#     i = i + 1
#     print ("Numbers now is", numbers)
#
# print ("The numbers:")
# for num in numbers:
#     print (num)
# print (numbers[2])

# from sys import exit
# def gold_room():
#     print ("This room is full of gold. How much do you take?")
#
#     choice = input("> ")
#     if "0" in choice or "1" in choice:
#         how_much = int(choice)
#     else:
#         dead("Man, learn to type a number.")
#
#     if how_much < 50:
#         print ("Nice, you're not greedy, you win!")
#         exit(0)
#     else:
#         dead("You greedy bastard!")
#
# def dead(why):
#     print (why, "Good job!")
#     exit(0)
#
# gold_room()

# stuff = {'name': 'Zed', 'age': 39}
# print (stuff['name'])
# stuff['city'] = "dali"
# print (stuff)

# test = {}
# test['colour'] = "red"
# print (test)
# test[1] = 'blue'
# print (test)

# states = {'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'}
# print ('-' * 10)
# for state, abbrev in states.items():
#     print ("%s is abbreviated %s and has city" % (state, abbrev))
# print (states.items())
# state = states.get('Oregon')
# if not state:
#     print ("Sorry, no Texas.")

# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'}
#
# city = cities.get('CA')
# print ("the city for the state 'TX' is: %s" % city)

# import test_1
# states = test_1.test()
# print (states)

# import test_1
# test_1.test()
# print (test_1.tangerine)

# class MyStuff(object):
#     def __int__(self):
#         self.tangerine = "And now a thousa"
#
#     def apple(self):
#         print ("I AM CLASSY APPLES!")

# class Song(object):
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print (line)
# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around tha family",
#                         "With po0ckets full of shells"])
#
# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()

# class Song(object):
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print (line)
#
# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around tha family",
#                         "With pockets full of shells"])
#
# happy_bday.sing_me_a_song()
#
# bulls_on_parade.sing_me_a_song()

# class Scene(object):
#
#     def enter1(self):
#         print ("This scene is not yet configured. Subclass it and implement enter().")
#         exit(1)
# class Death(Scene):
#     quips = [
#         "You died.  You kinda suck at this.",
#          "Your mom would be proud...if she were smarter.",
#          "Such a luser.",
#          "I have a small puppy that's better at this."
#     ]
#     def enter(self):
#         print (Death.quips)
#         exit(1)
# test = Death()
# test.enter()
# test.enter1()

# class Parent(object):
#     def implicit(self):
#         print ("PARENT implicit")
# class Child(Parent):
#     pass
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()

# class Parent(object):
#
#     def override(self):
#         print ("PARENT override()")
#
# class Child(Parent):
#
#     def override(self):
#         print ("CHILD override()")
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()

# class Parent(object):
#
#     def altered(self):
#         print ("PARENT altered()")
#
# class Child(Parent):
#
#     def altered(self):
#         print ("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print ("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()

# class Parent(object):
#
#     def override(self):
#         print("parent override")
#
#     def implicit(self):
#         print ("parent implicit")
#
#     def altered(self):
#         print ("parent altered")
#
# class Child(Parent):
#
#     def override(self):
#         print ("child override")
#
#     def altered(self):
#         print ("child, before parent altered")
#         super(Child, self).altered()
#         print ("child, after parent altered")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()

# class Other(object):
#
#     def override(self):
#         print ("other override")
#
#     def implicit(self):
#         print ("other implicit")
#
#     def altered(self):
#         print ("other altered")
#
# class Child(object):
#
#     def __init__(self):
#         self.other = Other()
#
#     def altered(self):
#         print ("child, befor other altered")
#         self.other.altered()
#         print ("child, after other altered")
#
# son = Child()

# son.altered()

# stuff = input()
# words = stuff.split()
# print (words)

# first_word = ('werb', 'go')
# second_word = ('direction', 'north')
# sentence = [first_word, second_word]
# print (sentence)

# def convert_number(s):
#     try:
#  #       print ('success')
#         return int(s)
#     except ValueError:
# #        print ("error")
#         return None
#
# convert_number('a')
# print(12)

# # test = 1+\
# #     1
# print (test)

# str = 'test'
# print(str)
# print(str[1:3])

# print('ru\nsas')
# print(r'rei\n23')

# a = set('adhfak,212')
# print(a)
#
# dict = {}
# dict['one'] = '1-tesst'
# dict[2] = '2-test'
#
# dict = 23423
# # dict = str(dict)
# dict = dict - 1
# print(dict)
#
# list = [ 1, 2, 3, 4]
# it = iter(list)
# for x in it:
#     print(x,end=" ")

# list = [1, 3, 4, 2]
# for num in list:
#     print(num, end = " ")
#
# it = iter(list)
#
# import sys
# while True:
#     try:
#         print(next(it), end = " ")
#     except StopIteration:
#         sys.exit()

# class num:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a = self.a + 1
#             return x
#         else:
#             raise StopAsyncIteration
#
# myclass = num()
# myiter = iter(myclass)
#
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# for x in myiter:
#     print(x)

# def ChangeInt(a):
#     a = a.append(3)
#     return
# a = [1, 2]
# ChangeInt(a)
# print(a)
# def printme(str):
#     print(str)
#     return
#
# printme(str = "test")

# def printinfo(arg1, **vartuple):
#     print('输出:')
#     print(arg1)
#     print(vartuple)
#
# printinfo(10, a = 2, b = 3)

# f = open(r'C:\Users\DMJ\Desktop\工作日常记录\工作报告\日记\8.6.txt', 'r')
# i = f.readline()
# print(i)
# f.close()
# while True:
#     try:
#         x = int(input('pleacse enter a number:'))
#         print('You are great!')
#         break
#     except:
#         print('That was not valid number. Try again')
#     else:
#         print("plerse enter a nunber!")
# import time
# ticks = time.asctime(time.localtime(time.time()))
# print('当前时间为：', ticks)


# import _thread
# import time
#
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2, ))
#     _thread.start_new_thread(print_time, ("Thread-2", 4, ))
# except:
#     print("Error: 无法启动线程")
#
# while 1:
#     pass

# import threading
# import time
#
# exitFlag = 0
#
# class  myThread(threading.Thread):
#     def __init__(self, threadId, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadId
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程" + self.name)
#         #获取锁，实现同步
#         threadLock.acquire()
#         print_time(self.name, self.counter, 5)
#         threadLock.release()
#         print("退出线程" + self.name)
#         #释放锁，开始下一个线程
#
# def print_time(threadName, delay, counter):
#      while counter:
#          time.sleep(delay)
#          print("%s: %s" % (threadName, time.ctime(time.time())))
#          counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# print("退出主线程")

# import psycopg2
#
# def connectPostgreSQL():
#     conn = psycopg2.connect(database = "test", user = "postgres",
#                             password = "w550189", host = "10.202.62.68:22", port = "5432")
#     print ("Opened database susccessfully！")
#
# connectPostgreSQL()


# import psycopg2
# def connectPostgreSQL():
#     conn = psycopg2.connect(database="test", user="postgres",
#     password = "postgres", host = "10.202.62.68", port = "5432")
#     print ("Opened database susccessfully！")
#     cursor = conn.cursor()
#     # zs = cur.var(psycopg2.cur)
#     cursor.callproc('auth.test', ('a'))
#
#     # sql = "Exec auth.test"
#     # cur.execute(sql)
#
#     rows = cursor.fetchall()
#     print(rows)
#     for row in rows:
#         print(row[0])
#
#     conn.commit()
#     cursor.close()
#     conn.close()
# connectPostgreSQL()

# ------------xml文件生成
# import pymysql
# import xml.dom.minidom
#
# def connectPostgreSQL():
#     conn = pymysql.connect(db="upchina", user="mysql", password = "mysql", host = "47.94.1.2", port = 3306)
#     cursor = conn.cursor()
#     sql = "select  CREATETIME, UPDATETIME, END_DATE from FIN_BALA_SHORT limit 5"
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#
#     cursor.close()
#     conn.close()
#
#     doc = xml.dom.minidom.Document()
#     root = doc.createElement('Managers')
#     root.setAttribute('company', '00')
#     root.setAttribute('address', '00')
#     # 将根节点添加到文档对象中
#     doc.appendChild(root)
#     for i in rows:
#         nodeManager = doc.createElement('Manager')
#         node_id = doc.createElement('node_id')
#         node_id.setAttribute('type', 'time')
#         node_id.appendChild(doc.createTextNode(str(i[0])))
#
#         nodeManager.appendChild(node_id)
#         root.appendChild(nodeManager)
#
#         fp1 = open('./mysql.xml', 'w')
#         doc.writexml(fp1, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
#         fp1.close()
#
# connectPostgreSQL()

# import pymysql
# import xlwt

# -----------------.xls文件生成
# def  Exchange_Xls():
#     conn = pymysql.connect(db="upchina", user="mysql", password = "mysql", host = "47.94.1.2", port = 3306)
#     cursor = conn.cursor()
#     sql = "select  CREATETIME, UPDATETIME, END_DATE from FIN_BALA_SHORT limit 5"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     fields = cursor.description
#
#     cursor.close()
#     conn.close()
#
#     xls = xlwt.Workbook()
#     sheet = xls.add_sheet('table_manage', cell_overwrite_ok=True)
#     for field in range(0,len(fields)):
#         sheet.write(0,field,fields[field][0])
#
#     row = 1
#     col =0
#     for row in range(1, len(results) + 1):
#         for col in range(0, len(fields)):
#             sheet.write(row, col, u'%s' % results[row - 1][col])
#     print('输入文件名：')
#     file_name = input()
#     xls.save('%s.xls' % str(file_name))
#
# Exchange_Xls()


# import psycopg2
# def connectPostgreSQL():
#     conn = psycopg2.connect(database="test", user="postgres",
#     password = "postgres", host = "10.202.62.68", port = "5432")
#     print ("Opened database susccessfully！")
#     cursor = conn.cursor()
#     cursor.callproc('auth.test', ('a'))

# import sqlalchemy
# from sqlalchemy.engine.url import URL
# postgres_db = {'drivername': 'test',
#                'username': 'postgres',
#                'password': 'postgres',
#                'host': '10.202.62.68',
#                'port': 5432}
# print(URL(**postgres_db))
#
# sqlite_db = {'drivername': 'sqlite', 'database': 'db.sqlite'}
# print(URL(**sqlite_db))

from datetime import datetime
# ------
# 一般mysql数据库读取
# import pymysql
# from sqlalchemy import Column, String, create_engine, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# # 创建对象的基类:
# def User_list():
#     Base = declarative_base()
#
#     # 定义User对象:
#     class User(Base):
#         # 表的名字:
#         __tablename__ = 'm_user'
#         # 表的结构:
#         user_id = Column(Integer, primary_key=True)
#         user_account = Column(String(12))
#
#     class Favor(Base):
#         __tablename__ = 'm_pay'
#         pay_id = Column(Integer, primary_key = True)
#         user_id = Column(Integer)
#                          # 初始化数据库连接:
#     engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/data')
#     # 创建DBSession类型:
#     # -----------增加
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     #
#     # obj = User(user_id = False,user_account = '5')
#     # session.add(obj)
#     # session.commit()
#     # session.close()
#
#     # ret=session.query(User).all()
#     # ret = session.query(User.user_id, User.user_account).all()    #结果为一个列表
#     # ret = session.query(User).filter_by(user_id = '1').first()
#     # ret = session.query(User).filter(User.user_id  > 5).all()
#     ret = session.query(User).join(Favor, User.user_id == Favor.user_id, isouter=True).all()
#     # ret = session.quert
#
#     print(type(ret))
#     for i in ret:
#         print(i.user_account)
#
# User_list()

# ------优品数据读取
from sqlalchemy import Column, String, create_engine, Integer, DECIMAL, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
def User_list():
    Base = declarative_base()

    # 定义User对象:
    class User(Base):
        # 表的名字:
        __tablename__ = 'STK_BASIC_INFO'
        # 表的结构:
        STK_UNI_CODE = Column(DECIMAL, primary_key= True)
        ISVALID = Column(DECIMAL)
        # CREATETIME = Column(String(12))


    # class Favor(Base):
    #     __tablename__ = 'm_pay'
    #     pay_id = Column(Integer, primary_key = True)
    #     user_id = Column(Integer)
                         # 初始化数据库连接:
    engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
    # 创建DBSession类型:
# -----------增加
    Session = sessionmaker(bind=engine)
    session = Session()
    #
    # obj = User(user_id = False,user_account = '5')
    # session.add(obj)
    # session.commit()
    # session.close()

    # ret=session.query(User).all().first()
    ret = session.query(User.STK_UNI_CODE, User.ISVALID).limit(2).all()    #结果为一个列表
    # ret = session.query(User).filter_by(user_id = '1').first()
    # ret = session.query(User).filter(User.user_id  > 5).all()
    # ret = session.query(User).join(Favor, User.user_id == Favor.user_id, isouter=True).all()
    # ret = session.quert

    print(type(ret))
    # print(ret)
    for i in ret:
        print(i.STK_UNI_CODE)
User_list()


# -----postrgresql 数据库
# import psycopg2
# from sqlalchemy import Column, String, create_engine, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.engine.url import URL
# from sqlalchemy import MetaData
# from sqlalchemy import Table
    # # 创建对象的基类:
# def User_list():
#
#     engine = create_engine('postgres://postgres:postgres@10.202.62.68:5432')
#
#     engine.execute('INSERT INTO "test" '
#                    '(id,name)'
#                    "VALUES (8,'qwe')")
#     # result = engine.execute('SELECT * FROM '
#     #                         'mun.test')
#     # for _r in result:
#     #     print(_r)
#
# User_list()

import psycopg2
# from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
#
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.engine.url import URL
# from sqlalchemy import MetaData
# from sqlalchemy import Table
# from sqlalchemy.orm import sessionmaker,relationship


    # 创建对象的基类:
# def User_list():
#     engine = create_engine('postgres://postgres:postgres@10.202.62.68:5432')
#     Base = declarative_base()
    # 把表抽象成类
    # class TestTable(Base):
    #     __tablename__ = 'test'
    #     __table_args__ = {
    #         'schema': 'mun'}
    #
    #     id   = Column(Integer, primary_key = True)
    #     name  = Column(String)
    # # 连接操作
    # Base.metadata.create_all(bind = engine)
    # # 实例化一个会话
    # Session = sessionmaker(engine)
    # Session.configure(bind = engine)
    # session = Session()
# ——一新增方法一
#     try:
#         test1 = TestTable(id = 6, name = 'a')
#         session.add(test1)
#         session.commit()
#     except SQLAlchemyError as e:
#         print(e)
#     finally:
#         session.close()
 # -----新增方法二
    # data = {3:3,4:4 }
    # try:
    #     for _id,_name in data.items():
    #         row = TestTable(id = _id,name = _name)
    #         session.add(row)
    #         session.commit()
    # except SQLAlchemyError as e:
    #     print(e)
    # finally:
    #     session.close()

# -------查询
#     ret = session.query(TestTable).filter(TestTable.id == 1).all()
#     for i in ret:
#         print(i.id)


# -----关联

#     class User(Base):
#         __tablename__ = 'test'
#         __table_args__ ={'schema': 'public'}
#
#         id = Column(Integer,primary_key=True)
#         name = Column(String)
#
#     class Address(Base):
#         __tablename__ = 'test'
#         __table_args__ = {
#             'schema': 'mun'}
#
#         id = Column(Integer, primary_key=True)
#         account = Column(String)
#         test_id = Column(Integer, ForeignKey("public.test.id"))
#
#         user = relationship('User',backref="test")
#     #
#
#     Base.metadata.create_all(bind = engine)
#     # 实例化一个会话
#     Session = sessionmaker(engine)
#     Session.configure(bind = engine)
#     session = Session()
#     #
#     # sql = session.query(Address).join(User, isouter=True)
#     # print(sql)
#     ret = session.query(Address).join(User, isouter=True).all()
#     for i in ret:
#         print(i.id, i.account, i.user.name)
# User_list()


# coding:utf-8


