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
import os

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPalette, QColor, QFont

from orangewidget import gui

from orangecontrib.wavepy2.util.gui.ow_wavepy_widget import WavePyWidget
from orangecontrib.wavepy2.util.wavepy_objects import OasysWavePyData, register_log_stream_widget_instance, get_registered_log_stream_instance

from wavepy2.util.common.common_tools import AlreadyInitializedError
from wavepy2.util.log.logger import register_logger_single_instance, LoggerMode
from wavepy2.util.plot.plotter import register_plotter_instance, PlotterMode
from wavepy2.util.plot.plot_tools import PlottingProperties
from wavepy2.util.ini.initializer import register_ini_instance, get_registered_ini_instance, IniMode

class WavePyInitWidget(WavePyWidget):
    outputs = [{"name": "WavePy Data",
                "type": OasysWavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    LOG_STDOUT = False if not "LOGSTDOUT" in os.environ.keys() else str(os.environ.get('LOGSTDOUT')) == "1"

    CONTROL_AREA_WIDTH = 860

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = 660

    def __init__(self, show_general_option_box=False):
        super(WavePyInitWidget, self).__init__(show_general_option_box=show_general_option_box, show_automatic_box=False)

        self._is_valid_widget = True

        try:
            self.initialize_business_logic()

            self._init_widget     = self._draw_init_widget()

            self.controlArea.setFixedHeight(self._init_widget.height() + 145)
            self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
            self.setFixedHeight(self.MAX_HEIGHT)
        except Exception as e:
            self._is_valid_widget = False

            label = gui.label(self._wavepy_widget_area, self, label="\n\n    INVALID WIDGET:\n\n    " + str(e))

            font = QFont(label.font())
            font.setBold(True)
            font.setPointSize(24)
            label.setFont(font)
            palette = QPalette(label.palette())
            palette.setColor(QPalette.Text, QColor('dark blue'))
            palette.setColor(QPalette.Base, QColor(243, 240, 160))
            label.setPalette(palette)

            self.controlArea.setFixedHeight(300)
            self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
            self.setFixedHeight(320)

            if self.IS_DEVELOP: raise e

        gui.rubber(self.controlArea)

    ##################################################################################
    # INITIALIZATION

    def initialize_business_logic(self):
        self.initialize_logger()
        self.initialize_plotter()
        self.initialize_ini()
        self.initialize_process_manager()

    def initialize_ini(self):
        try:
            register_ini_instance(IniMode.LOCAL_FILE, ini_file_name=self._get_file_ini_name(), application_name=self._get_application_name())
        except AlreadyInitializedError:
            if not get_registered_ini_instance(application_name=self._get_application_name()).get_ini_file_name() == self._get_file_ini_name():
                raise ValueError("The Oasys worspace can contain only 1 kind of analysis at a time")

    def initialize_logger(self, replace=False):
        try: register_log_stream_widget_instance(application_name=self._get_application_name())
        except AlreadyInitializedError: pass

        if not self.LOG_STDOUT:
            try: register_logger_single_instance(logger_mode=QSettings().value("wavepy/logger_mode", LoggerMode.FULL, type=int),
                                                 stream=get_registered_log_stream_instance(application_name=self._get_application_name()),
                                                 application_name=self._get_application_name(), replace=replace)
            except AlreadyInitializedError: pass
        else:
            try: register_logger_single_instance(logger_mode=QSettings().value("wavepy/logger_mode", LoggerMode.FULL, type=int),
                                                 application_name=self._get_application_name(), replace=replace)
            except AlreadyInitializedError: pass

    def initialize_plotter(self, replace=False):
        try: register_plotter_instance(plotter_mode=QSettings().value("wavepy/plotter_mode", PlotterMode.FULL, type=int),
                                       application_name=self._get_application_name(), replace=replace)
        except AlreadyInitializedError: pass

    def initialize_process_manager(self):
        self._process_manager = self._create_process_manager()

    ##################################################################################
    # ABSTRACT METHODS

    def _get_application_name(self):
        return None

    def _get_file_ini_name(self):
        raise NotImplementedError()

    def _create_process_manager(self):
        raise NotImplementedError()

    def _draw_init_widget(self):
        raise NotImplementedError()

    ##################################################################################
    # DEFAULT METHODS

    def _execute(self):
        if self._is_valid_widget:
            output = OasysWavePyData()

            output.set_process_manager(self._process_manager)
            output.set_initialization_parameters(self._init_widget.get_accepted_output())

            self.send("WavePy Data", output)

    def _get_default_plotting_properties(self):
        return PlottingProperties(context_widget=self._get_default_context(),
                                  show_runtime_options=False,
                                  add_context_label=False,
                                  use_unique_id=True)
