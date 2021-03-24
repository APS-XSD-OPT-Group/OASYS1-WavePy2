from orangecontrib.wavepy.widgets.gui.ow_wavepy_process_widget import WavePyProcessWidget

class OWSGTCropReferenceImage(WavePyProcessWidget):
    name = "S.G.T. - Crop Reference Image"
    id = "sgt_crop_reference_image"
    description = "S.G.T. - Crop Reference Image"
    icon = "icons/sgt_crop_reference_image.png"
    priority = 3
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    CONTROL_AREA_HEIGTH = 150
    CONTROL_AREA_WIDTH  = 400

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    must_clean_layout = False

    def __init__(self):
        super(OWSGTCropReferenceImage, self).__init__(show_general_option_box=True, show_automatic_box=True)

    def _get_execute_button_label(self):
        return "Crop Reference Image"

    def _get_output_parameters(self):
        return self._process_manager.crop_reference_image(initial_crop_parameters=self._calculation_parameters,
                                                          initialization_parameters=self._initialization_parameters)
