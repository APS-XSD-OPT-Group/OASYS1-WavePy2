# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################
from oasys.widgets.widget import OWWidget
from orangewidget import gui
from oasys.widgets import gui as oasysgui
from orangewidget.widget import OWAction
from orangewidget.settings import Setting

from wavepy2.util.plot.plot_tools import DefaultContextWidget, PlottingProperties

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRect

INITIALIZATION_PARAMETERS = "initialization_parameters"
CALCULATION_PARAMETERS    = "calculation_parameters"
PROCESS_MANAGER           = "process_manager"

class WavePyWidget(OWWidget):
    want_main_area = 0

    is_automatic_run = Setting(True)

    error_id = 0
    warning_id = 0
    info_id = 0

    CONTROL_AREA_WIDTH = 405

    MAX_WIDTH_FULL = 1320
    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = 700

    def __init__(self, show_general_option_box=False, show_automatic_box=False):
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

        self._general_options_box = oasysgui.widgetBox(self.controlArea, "General Options", addSpace=True, orientation="horizontal")
        self._general_options_box.setVisible(show_general_option_box)

        if show_automatic_box :
            gui.checkBox(self._general_options_box, self, 'is_automatic_run', 'Automatic Execution')

        self._button_box = oasysgui.widgetBox(self.controlArea, "", addSpace=False, orientation="horizontal")
        gui.button(self._button_box, self, self._get_execute_button_label(), callback=self._execute, height=45)

        self._wavepy_widget_area = oasysgui.widgetBox(self.controlArea, "", addSpace=False, orientation="horizontal", width=self.CONTROL_AREA_WIDTH)

    def _execute(self):
        raise NotImplementedError("This method is abstract")

    def _get_execute_button_label(self):
        return "Execute"

    def _clear_wavepy_layout(self):
        clear_layout(self._wavepy_widget_area.layout())

    def _get_default_context(self):
        return DefaultContextWidget(self._wavepy_widget_area)

    def _get_default_plotting_properties(self):
        return PlottingProperties(context_widget=self._get_default_context(),
                                  add_context_label=False,
                                  use_unique_id=True)

def clear_layout(layout):
    for i in reversed(range(layout.count())):
        layoutItem = layout.itemAt(i)
        if layoutItem.widget() is not None:
            widgetToRemove = layoutItem.widget()
            widgetToRemove.setParent(None)
            layout.removeWidget(widgetToRemove)
        else:
            layoutToRemove = layout.itemAt(i)
            clear_layout(layoutToRemove)
