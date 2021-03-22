import os

from oasys.widgets.widget import OWWidget
from orangewidget import gui
from orangewidget.widget import OWAction
from orangewidget.settings import Setting

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRect

INITIALIZATION_PARAMETERS = "initialization_parameters"
CALCULATION_PARAMETERS    = "calculation_parameters"
PROCESS_MANAGER           = "process_manager"


class WavePyWidget(OWWidget):

    want_main_area=1

    is_automatic_run = Setting(True)

    error_id = 0
    warning_id = 0
    info_id = 0

    CONTROL_AREA_WIDTH = 405
    TABS_AREA_HEIGHT = 560

    MAX_WIDTH_FULL = 1320
    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = 700

    def __init__(self, show_general_option_box=True, show_automatic_box=True):
        super().__init__()

        runaction = OWAction(self._get_execute_button_label(), self)
        runaction.triggered.connect(self._execute)
        self.addAction(runaction)

        geom = QApplication.desktop().availableGeometry()
        self.setGeometry(QRect(round(geom.width()*0.05),
                               round(geom.height()*0.05),
                               round(min(geom.width() * 0.98, self.MAX_WIDTH_FULL if self.want_main_area==1 else self.MAX_WIDTH_NO_MAIN)),
                               round(min(geom.height()*0.95, self.MAX_HEIGHT))))

        self.setMaximumHeight(self.geometry().height())
        self.setMaximumWidth(self.geometry().width())

        self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)

        self.general_options_box = gui.widgetBox(self.controlArea, "General Options", addSpace=True, orientation="horizontal")
        self.general_options_box.setVisible(show_general_option_box)

        if show_automatic_box :
            gui.checkBox(self.general_options_box, self, 'is_automatic_run', 'Automatic Execution')

        self.button_box = gui.widgetBox(self.controlArea, "", addSpace=True, orientation="horizontal")

        gui.button(self.button_box, self, self._get_execute_button_label(), callback=self._execute, height=45)

    def _execute(self):
        raise NotImplementedError("This method is abstract")

    def _get_execute_button_label(self):
        return "Execute"
