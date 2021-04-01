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
from orangecontrib.wavepy2.util.gui.ow_wavepy_interactive_widget import WavePyInteractiveWidget

from wavepy2.tools.common.wavepy_data import WavePyData
from wavepy2.tools.common.bl import crop_image

class CropImageStoreParametersWidget(WavePyInteractiveWidget):
    CONTROL_AREA_HEIGTH = 920
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    def __init__(self):
        super(CropImageStoreParametersWidget, self).__init__()

    def _get_interactive_widget(self):
        img_to_crop = None
        pixelsize   = None

        if not self._calculation_parameters is None:
            img_to_crop = self._calculation_parameters.get_parameter(self._get_img_name_in_calculation_parameters())
            pixelsize   = self._calculation_parameters.get_parameter(self._get_pixelsize_name_in_calculation_parameters())

        if (img_to_crop is None or pixelsize is None) and not self._initialization_parameters is None:
            img_to_crop = self._initialization_parameters.get_parameter("img")
            pixelsize   = self._initialization_parameters.get_parameter("pixelsize")

        if not (img_to_crop is None or pixelsize is None): return self._get_crop_widget(img_to_crop, pixelsize)
        else: raise ValueError("No Image to crop found in input data")

    def _get_crop_widget(self, img_to_crop, pixelsize):
        return crop_image.draw_colorbar_crop_image(initialization_parameters=self._initialization_parameters,
                                                   plotting_properties=self._get_default_plotting_properties(),
                                                   application_name=self._get_application_name(),
                                                   img=img_to_crop,
                                                   pixelsize=pixelsize,
                                                   message=self._get_window_text(),
                                                   tab_widget_height=765,
                                                   tab_widget_width=self.CONTROL_AREA_WIDTH-20)[0]

    def _get_application_name(self):
        return None

    def _get_img_name_in_calculation_parameters(self):
        return "img"

    def _get_pixelsize_name_in_calculation_parameters(self):
        return "pixelsize"

    def _get_output_parameters(self, widget_output_data):
        img, idx4crop, img_size_o, cmap, colorlimit = widget_output_data

        return WavePyData(img=img, idx4crop=idx4crop, img_size_o=img_size_o, cmap=cmap, colorlimit=colorlimit)

    def _get_execute_button_label(self):
        return "Crop Image"

    def _get_window_text(self):
        return "Crop Image?"
