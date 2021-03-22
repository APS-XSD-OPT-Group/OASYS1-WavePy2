from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings

from oasys.menus.menu import OMenu
from wavepy2.util.plot.plotter import PlotterMode
from wavepy2.util.log.logger import LoggerMode

class WavePyMenu(OMenu):

    def __init__(self):
        super().__init__(name="WavePy")

        self.openContainer()
        self.addContainer("Plotter Options")
        self.addSubMenu("Set Plotter Mode: FULL")
        self.addSubMenu("Set Plotter Mode: DISPLAY ONLY")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Logger Options")
        self.addSubMenu("Set Logger Mode: FULL")
        self.addSubMenu("Set Logger Mode: WARNING")
        self.addSubMenu("Set Logger Mode: ERROR")
        self.addSubMenu("Set Logger Mode: NONE")
        self.closeContainer()

    def executeAction_1(self, action):
        QSettings().setValue("wavepy/plotter_mode", PlotterMode.FULL)
        showInfoMessage("Plotter Mode set to: FULL\nReload the workspace to make it effective")

    def executeAction_2(self, action):
        QSettings().setValue("wavepy/plotter_mode", PlotterMode.DISPLAY_ONLY)
        showInfoMessage("Plotter Mode set to: DISPLAY ONLY\nReload the workspace to make it effective")

    def executeAction_3(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.FULL)
        showInfoMessage("Logger Mode set to: FULL\nReload the workspace to make it effective")

    def executeAction_4(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.WARNING)
        showInfoMessage("Logger Mode set to: WARNING\nReload the workspace to make it effective")

    def executeAction_5(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.ERROR)
        showInfoMessage("Logger Mode set to: ERROR\nReload the workspace to make it effective")

    def executeAction_6(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.NONE)
        showInfoMessage("Logger Mode set to: NONE\nReload the workspace to make it effective")

def showInfoMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def showConfirmMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Question)
    msgBox.setText(message)
    msgBox.setInformativeText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
    ret = msgBox.exec_()
    return ret

def showWarningMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def showCriticalMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()
