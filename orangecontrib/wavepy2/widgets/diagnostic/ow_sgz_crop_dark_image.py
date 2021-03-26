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
from orangecontrib.wavepy2.util.gui.ow_crop_image import CropImageWidget

from wavepy2.tools.common.bl import crop_image
from wavepy2.tools.diagnostic.coherence.bl.single_grating_coherence_z_scan import APPLICATION_NAME

class OWSGZCropDarkImage(CropImageWidget):
    name = "S.G.Z. - Crop Dark Image"
    id = "sgz_crop_dark_image"
    description = "S.G.Z. - Dark Image"
    icon = "icons/sgz_crop_dark_image.png"
    priority = 3.1
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    def __init__(self):
        super(OWSGZCropDarkImage, self).__init__()

    def _get_img_name_in_calculation_parameters(self):
        return "img_original"

    def _get_crop_widget(self, img_to_crop):
        cmap         = self._calculation_parameters.get_parameter("cmap")
        colorlimit   = self._calculation_parameters.get_parameter("colorlimit")

        return crop_image.draw_crop_image(initialization_parameters=self._initialization_parameters,
                                          plotting_properties=self._get_default_plotting_properties(),
                                          application_name=self._get_application_name(),
                                          img=img_to_crop,
                                          message=self._get_window_text(),
                                          default_idx4crop=[0, 20, 0, 20],
                                          kwargs4graph={'cmap': cmap, 'vmin': colorlimit[0], 'vmax': colorlimit[1]},
                                          tab_widget_height=660)[0]

    def _get_output_parameters(self, widget_output_data):
        _, idx4cropDark, _ = widget_output_data

        self._calculation_parameters.set_parameter("idx4cropDark", idx4cropDark)

        return self._calculation_parameters

    def _get_execute_button_label(self):
        return "Crop Dark Image"

    def _get_application_name(self):
        return APPLICATION_NAME
