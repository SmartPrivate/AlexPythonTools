import pymysql
import os


class ModelGenerator(object):
    def __init__(self, host='localhost', port=3306, db_name='', user='', password='', charset=''):
        self.__host = host
        self.__port = port
        self.__db = db_name
        self.__user = user
        self.__password = password
        self.__charset = charset
        self.__table_names = []
        self.__table_name = ''
        self.__class_name = ''
        self.__session = pymysql.connect(host=self.__host,
                                         port=self.__port,
                                         user=self.__user,
                                         password=self.__password,
                                         charset=self.__charset,
                                         cursorclass=pymysql.cursors.DictCursor)
        self.__cursor = self.__session.cursor()
        self.__locate_table()

    def __locate_table(self):
        sql = "select table_name from information_schema.tables where table_schema = '{0}'".format(self.__db)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        self.__table_names = list(map(lambda o: o['TABLE_NAME'], result))
        table_count = len(self.__table_names)
        print('数据库 {0} 中共有{1}张表'.format(self.__db, str(table_count)))
        for i in range(table_count):
            print('(' + str(i + 1) + ') ' + self.__table_names[i])
        while True:
            generate_all = input('是否全部生成？(y/n)\n')
            if not generate_all or generate_all == 'y':
                self.__generate_all_models()
                print('生成完成！')
                exit(0)
            elif generate_all == 'n':
                while True:
                    table_index = input('请输入表序号进行选择：\n')
                    try:
                        table_index = int(table_index)
                        self.__table_name = self.__table_names[table_index]
                        self.__generate_model()
                        print('生成完成！')
                        while True:
                            continue_generate = input('是否继续生成？\n')
                            if not continue_generate or continue_generate == 'n':
                                exit(0)
                            elif continue_generate == 'y':
                                break
                            else:
                                print('输入有误，请确认！')
                                continue
                    except ValueError:
                        print('请输入正确的表序号！')
                        continue
                break
            else:
                print('请输入正确的选项！')
                continue

    def __generate_all_models(self):
        for table_name in self.__table_names:
            self.__table_name = table_name
            self.__generate_model()

    def __generate_model(self):
        sql = "select column_name,data_type,character_maximum_length from information_schema.columns where table_schema ='{0}' and table_name ='{1}'".format(
            self.__db, self.__table_name)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        while True:
            self.__class_name = input('请输入表{0}需要生成的类名：\n'.format(self.__table_name))
            if not self.__class_name_checker():
                print('请输入正确的类名！')
                continue
            break
        if not os.path.exists('data_model.py'):
            writer = open('data_model.py', 'a', encoding='utf-8')
            writer.write("from sqlalchemy import Column, Integer, TEXT, DATETIME, BOOLEAN, VARCHAR, FLOAT\n")
            writer.write("from sqlalchemy.ext.declarative import declarative_base\n")
            writer.write('\n\n')
            writer.write("Base = declarative_base()\n")
            writer.write('\n\n')
            writer.close()

        writer = open('data_model.py', 'a', encoding='utf-8')
        writer.write('class {0}(Base):\n'.format(self.__class_name))
        writer.write("\t__tablename__ = '{0}'\n".format(self.__table_name))
        for item in result:
            line = '\t' + item['COLUMN_NAME'] + ' = Column({0})\n'.format(item['DATA_TYPE'].upper())
            if item['DATA_TYPE'] == 'int':
                line = '\t' + item['COLUMN_NAME'] + ' = Column(Integer)\n'
            elif item['DATA_TYPE'] == 'varchar':
                line = '\t' + item['COLUMN_NAME'] + ' = Column(VARCHAR({0}))\n'.format(item['CHARACTER_MAXIMUM_LENGTH'])
            writer.write(line)
        writer.write('\n\n')
        writer.close()

    def __class_name_checker(self):
        if not self.__class_name:
            return False
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '/', '*', '{', '}', '[', ']',
                         '\\', '|', '"', ';', ':', '/', '?', '.', '<', '>']
        for char in self.__class_name:
            if char in special_chars:
                return False
        try:
            int(self.__class_name)
            return False
        except ValueError:
            return True



