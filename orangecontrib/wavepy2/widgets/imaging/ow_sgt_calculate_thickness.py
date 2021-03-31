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
from orangewidget.settings import Setting
from orangewidget import gui

from orangecontrib.wavepy2.util.gui.ow_wavepy_process_widget import WavePyProcessWidgetWithOptions

class OWSGTCalculateThickness(WavePyProcessWidgetWithOptions):
    name = "S.G.T. - Calculate Thickness"
    id = "sgt_calculate_thickness"
    description = "S.G.T. - Calculate Thickness"
    icon = "icons/sgt_calculate_thickness.png"
    priority = 13
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    CONTROL_AREA_WIDTH = 1230

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10

    material_idx = Setting(1)

    def __init__(self):
        super(OWSGTCalculateThickness, self).__init__()

        gui.comboBox(self._options_area, self, "material_idx", items=["Diamond", "Beryllium"], label="Material", labelWidth=100, orientation="horizontal")

    def _get_execute_button_label(self):
        return "Calculate Thickness"

    def _get_output_parameters(self):
        self._initialization_parameters.set_parameter("material_idx", self.material_idx)
        self._initialization_parameters.set_parameter("do_integration", True)
        self._initialization_parameters.set_parameter("calc_thickness", True)

        return self._process_manager.calculate_thickness(integration_result=self._calculation_parameters,
                                                         initialization_parameters=self._initialization_parameters,
                                                         plotting_properties=self._get_default_plotting_properties(),
                                                         figure_height=650, figure_width=900)

