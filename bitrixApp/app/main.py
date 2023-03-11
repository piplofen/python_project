import base64
import pprint
import sys
import time

from PyQt6 import QtWidgets
from PyQt6.QtGui import QBrush, QColor
import webbrowser

from PyQt6.QtWidgets import QMessageBox

import mainDesign, database, regDesign, dealDesign
import sqlite
import utils as u


class RegClass(QtWidgets.QMainWindow, regDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(self)
        self.pushButton.clicked.connect(self.checkReg)

    def show_popup(self, type, head, body):
        msg = QMessageBox(text=head, parent=self)
        msg.setWindowTitle("Информация")  # автоматихирирвоать
        msg.setIcon(eval(f"QMessageBox.Icon.{type}"))
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setInformativeText(body)
        ret = msg.exec()

    def checkReg(self):
        token = u.createToken()
        if self.rb.isChecked():
            print("Вход с галочкой")
            flag = u.login(self.lineEdit_2.text(), self.lineEdit_3.text(), 1, token)
            sql = sqlite.Database()
            sql.cur.execute(f"update auth set token = '{token}', type = 1 where login = {self.lineEdit_2.text()}")
            sql.conn.commit()
            sql.firstData(int(self.lineEdit_2.text()), str(self.lineEdit_3.text()), str(self.rb.isChecked()))
            if flag:
                self.show_popup("Information", "Успешный вход!", "Вы успшено вошли в програму.")
                self.close()
                window.show()
                window.search(self.lineEdit_2.text())
            else:
                self.show_popup("Information", "Некорректный ввод!", "Не заполнено поле ID или пароль")
        else:
            print("Вход без галочки")
            flag = u.simpleLogin(self.lineEdit_2.text(), self.lineEdit_3.text(), 0)
            if flag:
                sql = sqlite.Database()
                sql.cur.execute(f"update auth set type = 0 where login = {self.lineEdit_2.text()}")
                sql.conn.commit()
                sql.firstData(int(self.lineEdit_2.text()), str(self.lineEdit_3.text()), str(self.rb.isChecked()))
                self.show_popup("Information", "Успешный вход!", "Вы успшено вошли в програму.")
                self.close()
                window.show()
                window.search(self.lineEdit_2.text())
            else:
                self.show_popup("Information", "Некорректный ввод!", "Не заполнено поле ID или пароль")
        # flag = u.login(self.lineEdit_2.text(), self.lineEdit_3.text(), self.rb.isChecked())
        # if not flag:
        #     self.show_popup("Information", "Некорректный ввод!", "Не заполнено поле ID или пароль")
        # else:
        #     self.show_popup("Information", "Успешный вход!", "Вы успшено вошли в програму.")
        #     db = database.Database()
        #     name = db.getName(self.lineEdit_2.text())
        #     sql = sqlite.Database(str(name))
        #     # ниже идем на сервер
        #     serverOutPut = "ниже идем на сервер"
        #     print(str(self.rb.isChecked()))
        #     sql.firstData(int(self.lineEdit_2.text()), str(self.lineEdit_3.text()), str(self.rb.isChecked())) # !!!
        #     self.close()
        #     window.show()
        #     window.search(self.lineEdit_2.text())


class MainClass(QtWidgets.QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bttnExit.clicked.connect(self.close)
        self.bttnSearch.clicked.connect(self.searchOther)

        self.tableWidget.setColumnWidth(0, 90)
        self.tableWidget.setColumnWidth(1, 395)
        self.tableWidget.setColumnWidth(2, 90)
        self.tableWidget.setColumnWidth(3, 125)
        self.tableWidget.setColumnWidth(4, 170)
        self.tableWidget.setColumnWidth(5, 225)
        self.tableWidget.verticalHeader().setVisible(False)

        self.tableWidget.cellDoubleClicked.connect(self.openLink)

        self.bttnSwitch.clicked.connect(self.switchUser)

    def switchUser(self):
        self.close()
        reg.lineEdit_2.clear()
        reg.lineEdit_2.setFocus()
        reg.lineEdit_3.clear()
        reg.rb.setChecked(False)
        reg.show()

    def openLink(self, r, c):
        if c == 5:
            webbrowser.open(self.tableWidget.item(r, c).text())
        elif c == 0:
            webbrowser.open(f"url/{self.tableWidget.item(r, c).text()}/")
        elif c == 2:
            webbrowser.open(f"url/{self.tableWidget.item(r, c).text()}/")
        elif c == 1:
            # Deal().__int__(123)
            deal.firstData(self.tableWidget.item(r, c).text(), self.tableWidget.item(r, 0).text())
            deal.show()

    def searchOther(self):
        self.search(self.lineEdit.text())

    def search(self, id):
        try:
            self.lineEdit.setText(str(id))
            db = database.Database()
            db.cur.execute(
                f"select idbitrix, title, contact, otv, kadrarbitrnomerdela, kadarbitrlink from newnewdeal where otv = {id};")
            res = db.cur.fetchall()
            self.insertData(res)
            db.cur.execute(f"select name, second_name, last_name from employees where idbitrix = {id}")
            otv = db.cur.fetchall()
            self.label.setText(f"Ответственный: {otv[0][2]} {otv[0][0]} {otv[0][1]}\n"
                               f"Сделок: {len(res)}")
        except:
            self.label.setText(f"Ответственный: Некорректный ввод ID\n"
                               f"Сделок: Некорректный ввод ID")

    def insertData(self, list):
        try:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(list))
            k = 0
            item = len(list[0]) - 1
            for i in range(len(list)):
                while item >= k:
                    self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(list[i][k])))
                    if i == 0:
                        self.tableWidget.item(i, k).setBackground(QBrush(QColor(220, 220, 220)))
                    elif i % 2 == 0:
                        self.tableWidget.item(i, k).setBackground(QBrush(QColor(220, 220, 220)))
                    k += 1
                k = 0
        except:
            pass

# для лэйблов тоже сделать
# ключ: название столбца и поля (они соответствуют друг другу), значение: индекс из списка с бд
class Deal:
    def __int__(self, data):
        for i in range(len(data[0])):
            try:
                print(data[0][i], i)
                if data[0][i] is None:
                    eval(f"deal.LC{i}.setText('-')")
                else:
                    try:
                        eval(f"deal.LC{i}.setText(str(u.deleteBirthdate(data[0][i])))")
                    except:
                        eval(f"deal.LC{i}.setText(str(data[0][{i}]))")
            except:
                break


class DealClass(QtWidgets.QMainWindow, dealDesign.Ui_CardWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bttnExit.clicked.connect(self.close)


    def firstData(self, title, id):
        self.setWindowTitle(f"{str(title)} {id}")
        db = database.Database()
        db.cur.execute(f"""select * from newnewdeal n
                        left join employees e on n.otv = e.idbitrix
                        left join contactfu c on n.contactfu = c.idbitrix
                        left join contacts c2 on n.contact = c2.idbitrix
                        where n.idbitrix = {id}""")
        result = db.cur.fetchall()
        Deal().__int__(result)


def main():
    global window, deal, reg
    app = QtWidgets.QApplication(sys.argv)
    flag = checkState() # !
    if type(flag) == int:
        reg = RegClass()
        window = MainClass()
        deal = DealClass()
        window.show()
        window.search(flag) # !
        app.exec()
    else:
        reg = RegClass()
        window = MainClass()
        deal = DealClass()
        reg.show()
        app.exec()


def checkState():
    sql = sqlite.Database()
    sql.cur.execute("select login, token, type from auth;")
    res = sql.cur.fetchall()
    print(res)
    if res[0][2] == "1":
        try:
            db = database.Database()
            db.cur.execute(f"select id, token from auth where id = {res[0][0]}")
            res1 = db.cur.fetchall()
            for item in res1:
                if str(res[0][1]) == base64.b64decode(item[1]).decode("utf-8"):
                    return int(res[0][0])
        except:
            print("ERror1")
            return False
    else:
        print("ERror2")
        return False


    # data = u.openFile("cfg", "json")
    # # return False
    # if data[idmemb]["remember"]:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    main()
