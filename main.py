from PyQt5.QtWidgets import QWidget, QApplication
from design import Ui_Form as Design
import sys


class Chrestick(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tek = ''
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        self.pushButton_8.setVisible(False)
        self.pushButton_9.setVisible(False)
        self.pushButton_10.setVisible(False)
        self.pushButton.clicked.connect(self.choice)
        self.pushButton_2.clicked.connect(self.p_2)
        self.pushButton_3.clicked.connect(self.p_3)
        self.pushButton_4.clicked.connect(self.p_4)
        self.pushButton_5.clicked.connect(self.p_5)
        self.pushButton_6.clicked.connect(self.p_6)
        self.pushButton_7.clicked.connect(self.p_7)
        self.pushButton_8.clicked.connect(self.p_8)
        self.pushButton_9.clicked.connect(self.p_9)
        self.pushButton_10.clicked.connect(self.p_10)

    def choice(self):
        if not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
            self.label_2.setText("Не выбран пользователь для первого хода")
        else:
            self.label_2.setText("")
            self.pushButton.setVisible(False)
            self.pushButton_2.setVisible(True)
            self.pushButton_3.setVisible(True)
            self.pushButton_4.setVisible(True)
            self.pushButton_5.setVisible(True)
            self.pushButton_6.setVisible(True)
            self.pushButton_7.setVisible(True)
            self.pushButton_8.setVisible(True)
            self.pushButton_9.setVisible(True)
            self.pushButton_10.setVisible(True)
            self.label_2.setVisible(True)
            self.label.setVisible(False)
            if self.radioButton_2.isChecked():
                self.label_2.setText('x')
                self.tek = 'x'
            else:
                self.label_2.setText('o')
                self.tek = 'o'
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)

    def reverser(self):
        if self.tek == 'x':
            self.tek = 'o'
        else:
            self.tek = 'x'
        self.updater()

    def p_2(self):
        self.board[0][0] = self.tek
        self.pushButton_2.setText(self.tek)
        self.pushButton_2.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_3(self):
        self.board[0][1] = self.tek
        self.pushButton_3.setText(self.tek)
        self.pushButton_3.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_4(self):
        self.board[0][2] = self.tek
        self.pushButton_4.setText(self.tek)
        self.pushButton_4.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_5(self):
        self.board[1][0] = self.tek
        self.pushButton_5.setText(self.tek)
        self.pushButton_5.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_6(self):
        self.board[1][1] = self.tek
        self.pushButton_6.setText(self.tek)
        self.pushButton_6.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_7(self):
        self.board[1][2] = self.tek
        self.pushButton_7.setText(self.tek)
        self.pushButton_7.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_8(self):
        self.board[2][0] = self.tek
        self.pushButton_8.setText(self.tek)
        self.pushButton_8.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_9(self):
        self.board[2][1] = self.tek
        self.pushButton_9.setText(self.tek)
        self.pushButton_9.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def p_10(self):
        self.board[2][2] = self.tek
        self.pushButton_10.setText(self.tek)
        self.pushButton_10.setEnabled(False)
        self.reverser()
        self.label_2.setText(self.tek)

    def updater(self):
        winner = ''
        for i in range(3):
            if self.board[i].count('x') == 3:
                winner = 'x'
                break
            if self.board[i].count('o') == 3:
                winner = 'o'
                break
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[2][i] != '-':
                winner = self.board[0][i]
                break
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[2][2] != '-':
            winner = self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[0][2] != '-':
            winner = self.board[2][0]
        if winner != '':
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            self.pushButton_4.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_6.setVisible(False)
            self.pushButton_7.setVisible(False)
            self.pushButton_8.setVisible(False)
            self.pushButton_9.setVisible(False)
            self.pushButton_10.setVisible(False)
            self.label_2.setVisible(False)
            self.label_3.setText(winner)
        else:
            count = 0
            for i in self.board:
                for j in i:
                    if j != '-':
                        count += 1
            if count == 9:
                self.pushButton_2.setVisible(False)
                self.pushButton_3.setVisible(False)
                self.pushButton_4.setVisible(False)
                self.pushButton_5.setVisible(False)
                self.pushButton_6.setVisible(False)
                self.pushButton_7.setVisible(False)
                self.pushButton_8.setVisible(False)
                self.pushButton_9.setVisible(False)
                self.pushButton_10.setVisible(False)
                self.label_2.setVisible(False)
                self.label_3.setText('Ничья')



app = QApplication(sys.argv)
ex = Chrestick()
ex.show()
sys.exit(app.exec_())