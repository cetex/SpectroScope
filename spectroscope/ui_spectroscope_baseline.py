# Form implementation generated from reading ui file 'spectroscope_baseline.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SpectroScopeBaseline(object):
    def setupUi(self, SpectroScopeBaseline):
        SpectroScopeBaseline.setObjectName("SpectroScopeBaseline")
        SpectroScopeBaseline.resize(500, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(SpectroScopeBaseline)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SpectroScopeBaseline)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.baselineFileEdit = QtWidgets.QLineEdit(SpectroScopeBaseline)
        self.baselineFileEdit.setObjectName("baselineFileEdit")
        self.horizontalLayout.addWidget(self.baselineFileEdit)
        self.baselineFileButton = QtWidgets.QToolButton(SpectroScopeBaseline)
        self.baselineFileButton.setMinimumSize(QtCore.QSize(50, 0))
        self.baselineFileButton.setObjectName("baselineFileButton")
        self.horizontalLayout.addWidget(self.baselineFileButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpectroScopeBaseline)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.baselineFileEdit)

        self.retranslateUi(SpectroScopeBaseline)
        self.buttonBox.accepted.connect(SpectroScopeBaseline.accept) # type: ignore
        self.buttonBox.rejected.connect(SpectroScopeBaseline.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SpectroScopeBaseline)
        SpectroScopeBaseline.setTabOrder(self.baselineFileEdit, self.baselineFileButton)

    def retranslateUi(self, SpectroScopeBaseline):
        _translate = QtCore.QCoreApplication.translate
        SpectroScopeBaseline.setWindowTitle(_translate("SpectroScopeBaseline", "Baseline - SpectroScope"))
        self.label.setText(_translate("SpectroScopeBaseline", "Baseline &file:"))
        self.baselineFileButton.setText(_translate("SpectroScopeBaseline", "..."))
