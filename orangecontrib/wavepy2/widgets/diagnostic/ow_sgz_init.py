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
from multiprocessing import cpu_count

from orangewidget.settings import Setting
from orangewidget import gui
from oasys.widgets import gui as oasysgui

from orangecontrib.wavepy2.util.gui.ow_wavepy_init_widget import WavePyInitWidget

from wavepy2.tools.diagnostic.coherence.bl.single_grating_coherence_z_scan import create_single_grating_coherence_z_scan_manager, SINGLE_THREAD, APPLICATION_NAME

N_CPUS = cpu_count() - 2

class OWSGZInit(WavePyInitWidget):
    name = "S.G.Z. - Initialization"
    id = "sgz_init"
    description = "S.G.Z. - Initialization"
    icon = "icons/sgz_init.png"
    priority = 1
    category = ""
    keywords = ["wavepy", "sgz", "init"]

    parallel_mode = Setting(1)

    MAX_HEIGHT = 700

    def __init__(self):
        super(OWSGZInit, self).__init__(show_general_option_box=True)

        self.__draw_additional_input_area()

    def _get_application_name(self):
        return APPLICATION_NAME

    def _get_file_ini_name(self):
        return ".single_grating_coherence_z_scan.ini"

    def _create_process_manager(self):
        if N_CPUS > 1: return create_single_grating_coherence_z_scan_manager(mode=self.parallel_mode)
        else:          return create_single_grating_coherence_z_scan_manager(mode=SINGLE_THREAD)

    def __draw_additional_input_area(self):
        cb_parallel_mode = gui.comboBox(oasysgui.widgetBox(self._general_options_box, "", addSpace=False, orientation="vertical", width=350), self,
                                        "parallel_mode", items=["Single-Thread", "Multi-Thread"], label="Computing Mode",
                                        labelWidth=200, orientation="horizontal", callback=self.__set_parallel_mode)

        if N_CPUS < 2:
            self.parallel_mode = SINGLE_THREAD
            cb_parallel_mode.setReadOnly(True)
        else:
            self.__cpus_label = gui.label(oasysgui.widgetBox(self._general_options_box, "", addSpace=False, orientation="vertical"), self,
                                          label=("  # cpus: " + str(N_CPUS)))
            self.__set_parallel_mode()

        self.controlArea.setFixedHeight(self._init_widget.height() + 195)
        gui.rubber(self.controlArea)

    def _draw_init_widget(self):
        return self._process_manager.draw_initialization_parameters_widget(plotting_properties=self._get_default_plotting_properties(),
                                                                           widget_height=485,
                                                                           tab_widget_width=self.CONTROL_AREA_WIDTH-20)[0]

    def _execute(self):
        self._process_manager = self._create_process_manager()

        super(OWSGZInit, self)._execute()

    def __set_parallel_mode(self):
        self.__cpus_label.setVisible(self.parallel_mode==1)
