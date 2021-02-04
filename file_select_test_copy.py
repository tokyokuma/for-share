# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QStringListModel, Qt
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QListView, QListWidgetItem, QPushButton, QWidget, QApplication
from file_select import Ui_Form

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args,**kwargs)
        
        self.test_list = QStringListModel(["1","2"])
        self.initUI()
        
        
    def initUI(self):
        self.ui_form = Ui_Form()
        self.ui_form.setupUi(self) 


        
    def show_dialog(self, btn=0):

        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        fname = QFileDialog.getOpenFileName(self, 'Open file')

        # fname[0]は選択したファイルのパス（ファイル名を含む）
        if fname[0]:
            if btn == 1:
                self.ui_form.lineEdit.setText(fname[0])   
            elif btn == 2:    
                self.ui_form.lineEdit_2.setText(fname[0])
            else:
                pass
        else:
            print("ファイルを選択してください")
               
    def show_list(self):

        files = ['Doug','Kevin','Amy','Melissa','John']

        for f in files:
            item = QListWidgetItem(f)
            item.setCheckState(0)
            self.ui_form.listWidget.addItem(item)
        
        print(self.ui_form.listWidget)

    def auto_insert(self):
        #out = self.ui_form.listWidget.findItems(Qt.Checked)
        items = []
        for index in range(self.ui_form.listWidget.count()):
            items.append(self.ui_form.listWidget.item(index).text())
        
        print(items)
                   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())