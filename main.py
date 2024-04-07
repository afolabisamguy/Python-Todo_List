import sys

from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import *
from PyQt5 import uic
from todo import Todo
sams = Todo()
replay = True
sams.my_delete()


class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("opening.ui", self)
        self.show()

        self.create.clicked.connect(self.creates)
        self.viewing.clicked.connect(self.views)
        self.sam = None
        self.sama = None

    def views(self):
        if not self.sama:
            self.sama = ListWindow()
            self.sama.show()
            items = ['sam1', 'sam2', 'sam3']
            # self.sama.add_items_to_list_view(items)

    def creates(self):
        if not self.sam:
            self.sam = CreateWindow()
            self.sam.show()
            self.sam.createOk.clicked.connect(lambda: self.saveit(self.sam.title_edit.toPlainText(),
                                                              self.sam.desc_edit.toPlainText(),
                                                              self.sam.date_edit.date().toString('yyyy-MM-dd'),
                                                              self.sam.priority_edit.value(),
                                                              self.sam.status_combo.currentText()))

    def saveit(self, title, desc, date, priority, status):
        print(title)
        print(desc)
        print(date)
        print(priority)
        print(status)
        sams.create(title, desc, date, priority, status)
        self.sam.close()

class CreateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("creater.ui", self)
        self.createOk = self.findChild(QPushButton, "createOk")
        self.priority_edit = self.findChild(QSpinBox, "priority_edit")
        self.priority_edit.setMaximum(5)
        self.priority_edit.setMinimum(1)


class ListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pry_view", self)
        self.todo_list = self.findChild(QListView, "todo_list")
        # self.list_model = QStringListModel()
        # self.todo_list.setModel(self.list_model)

    def add_items_to_list_view(self, items):
        pass
        # self.list_model.setStringList(items)



def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

main()
# while replay:
#     # TODO make sure you're able to read the todo even when you've quit the application
#     # TODO Research if you can make it a gui
#     print('Welcome to the Todo Application')
#     print('Press 1 to add a task')
#     print('Press 2 to view todo\'s')
#     print('Press 3 to delete the task')
#     print('Press 4 to edit the task')
#     print('Press 5 to quit the application')
#     choice = int(input())
#     if choice == 1:
#         sam.create()
#     elif choice == 2:
#         sam.view_instances()
#     elif choice == 3:
#         sam.delete_instance()
#     elif choice == 4:
#         sam.edit_instance()
#     elif choice == 5:
#         replay = False
#
# #
# # sam.introduction()
# # sam.printer()
