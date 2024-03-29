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

from orangecontrib.wavepy2.util.gui.ow_wavepy_widget import WavePyWidget
from orangecontrib.wavepy2.util.wavepy_objects import OasysWavePyData


class WavePyInteractiveWidget(WavePyWidget):
    inputs = [("WavePy Data", OasysWavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": OasysWavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    must_clean_layout = True

    CONTROL_AREA_HEIGTH = 840
    CONTROL_AREA_WIDTH  = 950

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    def __init__(self, show_general_option_box=True, show_automatic_box=True):
        super(WavePyInteractiveWidget, self).__init__(show_general_option_box=show_general_option_box, show_automatic_box=show_automatic_box)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.button(self._button_box, self, self._get_cancel_button_label(), callback=self._cancel, height=45)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            self.progressBarInit()
            if not self.is_automatic_run:
                self.information(self._get_input_message())
                self.setFixedHeight(self.MAX_HEIGHT+40)

            data = data.duplicate()

            self._initialization_parameters = data.get_initialization_parameters()
            self._calculation_parameters    = data.get_calculation_parameters()
            self._process_manager           = data.get_process_manager()

            if self.must_clean_layout: self._clear_wavepy_layout()

            self.progressBarSet(10)

            self._interactive_widget = self._get_interactive_widget()

            self.progressBarSet(90)

            self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
            self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

            gui.rubber(self.controlArea)

            self.progressBarSet(100)
            self.progressBarFinished()

            if self.is_automatic_run: self._cancel()
            else: self.show()

    def _get_input_message(self):
        return "Waiting User Input"

    def _get_cancel_button_label(self):
        return "Initial Crop"

    def _get_interactive_widget(self):
        raise NotImplementedError()

    def __send_result(self, widget_output_data):
        if not self._interactive_widget is None:
            if not self.is_automatic_run:
                self.information("")
                self.setFixedHeight(self.MAX_HEIGHT)

            output_calculation_parameters = self._get_output_parameters(widget_output_data)

            output = OasysWavePyData()

            output.set_process_manager(self._process_manager)
            output.set_initialization_parameters(self._initialization_parameters)
            output.set_calculation_parameters(output_calculation_parameters)

            self.send("WavePy Data", output)

    def _get_output_parameters(self, widget_output_data):
        raise NotImplementedError()

    def _execute(self):
        self.__send_result(self._get_accepted_output())

    def _cancel(self):
        self.__send_result(self._get_rejected_output())

    def _get_accepted_output(self):
        return self._interactive_widget.get_accepted_output()

    def _get_rejected_output(self):
        return self._interactive_widget.get_rejected_output()
