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
from orangewidget import gui
from oasys.widgets import gui as oasysgui

from orangecontrib.wavepy2.util.gui.ow_wavepy_widget import WavePyWidget
from orangecontrib.wavepy2.util.wavepy_objects import OasysWavePyData


class WavePyProcessWidget(WavePyWidget):
    CONTROL_AREA_HEIGTH = 900
    CONTROL_AREA_WIDTH  = 1600

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    inputs = [("WavePy Data", OasysWavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": OasysWavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    must_clean_layout = True

    def __init__(self, show_general_option_box=True, show_automatic_box=True):
        super(WavePyProcessWidget, self).__init__(show_general_option_box=show_general_option_box, show_automatic_box=show_automatic_box)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            data = data.duplicate()

            self._initialization_parameters = data.get_initialization_parameters()
            self._calculation_parameters    = data.get_calculation_parameters()
            self._process_manager           = data.get_process_manager()

            if self.is_automatic_run: self._execute()

    def _execute(self):
        self.progressBarInit()

        if self.must_clean_layout: self._clear_wavepy_layout()

        self.progressBarSet(10)

        output_calculation_parameters = self._get_output_parameters()

        self.progressBarSet(90)

        self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
        self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

        gui.rubber(self.controlArea)

        output = OasysWavePyData()
        output.set_process_manager(self._process_manager)
        output.set_initialization_parameters(self._initialization_parameters)
        output.set_calculation_parameters(output_calculation_parameters)

        self.progressBarSet(100)
        self.progressBarFinished()

        self.send("WavePy Data", output)

    def _get_output_parameters(self):
        raise NotImplementedError()

from orangecontrib.wavepy2.util.gui.ow_wavepy_widget import clear_layout
from wavepy2.util.plot.plot_tools import DefaultContextWidget

class WavePyProcessWidgetWithOptions(WavePyProcessWidget):

    def __init__(self, show_general_option_box=True, show_automatic_box=True):
        super(WavePyProcessWidgetWithOptions, self).__init__(show_general_option_box=show_general_option_box, show_automatic_box=show_automatic_box)

        self._options_area               = oasysgui.widgetBox(self._wavepy_widget_area, "Options", addSpace=False, orientation="vertical",
                                                              width=self._get_option_area_width())
        self._lateral_wavepy_widget_area = oasysgui.widgetBox(self._wavepy_widget_area, "", addSpace=False, orientation="vertical",
                                                              width=self.CONTROL_AREA_WIDTH - self._get_option_area_width())

    def _get_option_area_width(self):
        return 200

    def _clear_wavepy_layout(self):
        clear_layout(self._lateral_wavepy_widget_area.layout())

    def _get_default_context(self):
        return DefaultContextWidget(self._lateral_wavepy_widget_area)
