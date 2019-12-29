import tkinter
from tkinter import ttk


class ORMApp:
    def __init__(self, master):
        self.__master = master
        self.__init_items()
        self.__init_data()

    def __init_items(self):
        self.__label_frame_host = tkinter.LabelFrame(master=self.__master, text='数据库连接信息')
        self.__label_frame_host.place(x=10, y=5, width=300, height=150)

        self.__label_frame_db = tkinter.LabelFrame(master=self.__master, text='数据库信息')
        self.__label_frame_db.place(x=10, y=160, width=300, height=350)

        self.__label_frame_text = tkinter.LabelFrame(master=self.__master, text='ORM类生成')
        self.__label_frame_text.place(x=320, y=5, width=330, height=505)

        label_names = ['服务器', '端口号', '用户名', '密   码']
        self.__host_entries = []
        for i in range(len(label_names)):
            label = tkinter.Label(master=self.__label_frame_host, text=label_names[i], font=('Microsoft YaHei', 10))
            entry = tkinter.Entry(master=self.__label_frame_host, font=('Cascadia Code', 10))
            self.__host_entries.append(entry)
            label.place(x=10, y=int(5 + int(i * 30)))
            entry.place(x=60, y=8 + int(i * 30))

        self.__button = tkinter.Button(master=self.__label_frame_host, text='连接')
        self.__button.place(x=232, y=8, width=52, height=108)

        self.__label_db = tkinter.Label(master=self.__label_frame_db, text='数据库', font=('Microsoft YaHei', 10))
        self.__label_db.place(x=10, y=5)

        self.__combo_db = ttk.Combobox(master=self.__label_frame_db)
        self.__combo_db.place(x=60, y=6.5, width=222)

        self.__list_box_db = tkinter.Listbox(master=self.__label_frame_db)
        self.__list_box_db.place(x=10, y=40, width=272, height=280)

        self.__list_box_orm = tkinter.Text(master=self.__label_frame_text)
        self.__list_box_orm.place(x=10, y=5, width=300, height=430)

    def __init_data(self):
        self.__host_entries[0].insert(0, 'localhost')
        self.__host_entries[1].insert(0, '3306')
        self.__host_entries[2].insert(0, 'root')


main_form = tkinter.Tk()
main_form.title('ORM自动生成工具')
main_form.geometry('660x520')
ORMApp(main_form)
main_form.mainloop()
