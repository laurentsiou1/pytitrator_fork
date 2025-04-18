# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic/ui_files/phmeter_calib.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calibration_window(object):
    def setupUi(self, calibration_window):
        calibration_window.setObjectName("calibration_window")
        calibration_window.resize(418, 316)
        self.buttonBox = QtWidgets.QDialogButtonBox(calibration_window)
        self.buttonBox.setGeometry(QtCore.QRect(180, 270, 231, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.lcdNumber = QtWidgets.QLCDNumber(calibration_window)
        self.lcdNumber.setGeometry(QtCore.QRect(200, 120, 211, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(calibration_window)
        self.label.setGeometry(QtCore.QRect(240, 80, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.U_ph4 = QtWidgets.QLCDNumber(calibration_window)
        self.U_ph4.setGeometry(QtCore.QRect(20, 120, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.U_ph4.sizePolicy().hasHeightForWidth())
        self.U_ph4.setSizePolicy(sizePolicy)
        self.U_ph4.setObjectName("U_ph4")
        self.U_ph7 = QtWidgets.QLCDNumber(calibration_window)
        self.U_ph7.setGeometry(QtCore.QRect(20, 190, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.U_ph7.sizePolicy().hasHeightForWidth())
        self.U_ph7.setSizePolicy(sizePolicy)
        self.U_ph7.setObjectName("U_ph7")
        self.U_ph10 = QtWidgets.QLCDNumber(calibration_window)
        self.U_ph10.setGeometry(QtCore.QRect(20, 260, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.U_ph10.sizePolicy().hasHeightForWidth())
        self.U_ph10.setSizePolicy(sizePolicy)
        self.U_ph10.setObjectName("U_ph10")
        self.button_ph10 = QtWidgets.QPushButton(calibration_window)
        self.button_ph10.setGeometry(QtCore.QRect(130, 260, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ph10.sizePolicy().hasHeightForWidth())
        self.button_ph10.setSizePolicy(sizePolicy)
        self.button_ph10.setObjectName("button_ph10")
        self.button_ph7 = QtWidgets.QPushButton(calibration_window)
        self.button_ph7.setGeometry(QtCore.QRect(130, 190, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ph7.sizePolicy().hasHeightForWidth())
        self.button_ph7.setSizePolicy(sizePolicy)
        self.button_ph7.setObjectName("button_ph7")
        self.button_ph4 = QtWidgets.QPushButton(calibration_window)
        self.button_ph4.setGeometry(QtCore.QRect(130, 120, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ph4.sizePolicy().hasHeightForWidth())
        self.button_ph4.setSizePolicy(sizePolicy)
        self.button_ph4.setObjectName("button_ph4")
        self.label_2 = QtWidgets.QLabel(calibration_window)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_indications = QtWidgets.QLabel(calibration_window)
        self.label_indications.setGeometry(QtCore.QRect(10, 10, 401, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_indications.sizePolicy().hasHeightForWidth())
        self.label_indications.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_indications.setFont(font)
        self.label_indications.setAlignment(QtCore.Qt.AlignCenter)
        self.label_indications.setWordWrap(True)
        self.label_indications.setObjectName("label_indications")

        self.retranslateUi(calibration_window)
        self.buttonBox.accepted.connect(calibration_window.accept) # type: ignore
        self.buttonBox.rejected.connect(calibration_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(calibration_window)

    def retranslateUi(self, calibration_window):
        _translate = QtCore.QCoreApplication.translate
        calibration_window.setWindowTitle(_translate("calibration_window", "pH meter calibration"))
        self.label.setText(_translate("calibration_window", "Live voltage (mV)"))
        self.button_ph10.setText(_translate("calibration_window", "pH10"))
        self.button_ph7.setText(_translate("calibration_window", "pH7"))
        self.button_ph4.setText(_translate("calibration_window", "pH4"))
        self.label_2.setText(_translate("calibration_window", "Recorded voltages"))
        self.label_indications.setText(_translate("calibration_window", "Click on corresponding pH when voltage stabilizes\n"
"Click Apply to save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calibration_window = QtWidgets.QDialog()
    ui = Ui_calibration_window()
    ui.setupUi(calibration_window)
    calibration_window.show()
    sys.exit(app.exec_())
