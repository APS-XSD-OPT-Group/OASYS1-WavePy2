from orangewidget import gui

from orangecontrib.wavepy.widgets.gui.ow_wavepy_widget import WavePyWidget
from orangecontrib.wavepy.util.wavepy_objects import OasysWavePyData

from wavepy2.util.common.common_tools import AlreadyInitializedError
from wavepy2.util.log.logger import register_logger_single_instance, LoggerMode
from wavepy2.util.plot.plotter import register_plotter_instance, PlotterMode
from wavepy2.util.ini.initializer import get_registered_ini_instance, register_ini_instance, IniMode
from wavepy2.util.log.logger import LoggerMode
from wavepy2.util.plot.plot_tools import PlottingProperties, DefaultContextWidget

from wavepy2.tools.common.wavepy_data import WavePyData
from wavepy2.tools.common.bl import crop_image

class OWColorbarCropImage(WavePyWidget):
    name = "Crop Image & Store Params"
    id = "colorbar_crop_image"
    description = "Crop Image & Store Params"
    icon = "icons/colorbar_crop_image.png"
    priority = 2
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    inputs = [("WavePy Data", OasysWavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": OasysWavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    want_main_area = 0

    CONTROL_AREA_HEIGTH = 840
    CONTROL_AREA_WIDTH  = 950

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    def __init__(self):
        super(OWColorbarCropImage, self).__init__(show_general_option_box=True, show_automatic_box=True)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.button(self.button_box, self, "Initial Crop", callback=self._cancel, height=45)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            data = data.duplicate()

            self._initialization_parameters = data.get_initialization_parameters()
            self._calculation_parameters    = data.get_calculation_parameters()
            self._process_manager           = data.get_process_manager()

            img       = None
            pixelsize = None

            if not self._calculation_parameters is None:
                img       = self._calculation_parameters.get_parameter("img")
                pixelsize = self._calculation_parameters.get_parameter("pixelsize")

            if (img is None or pixelsize is None):
                img             = self._initialization_parameters.get_parameter("img")
                pixelsize       = self._initialization_parameters.get_parameter("pixelsize")

            if not (img is None or pixelsize is None):
                self._clear_wavepy_layout()

                self.__crop_widget = crop_image.draw_colorbar_crop_image(initialization_parameters=self._initialization_parameters,
                                                                         plotting_properties=PlottingProperties(context_widget=DefaultContextWidget(self._wavepy_widget_area),
                                                                                                                add_context_label=False,
                                                                                                                use_unique_id=True),
                                                                         img=img, pixelsize=pixelsize)[0]

            self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
            self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

            gui.rubber(self.controlArea)

            if self.is_automatic_run: self._cancel()

    def __send_result(self, img, idx4crop, img_size_o):
        output = OasysWavePyData()

        output.set_process_manager(self._process_manager)
        output.set_initialization_parameters(self._initialization_parameters)
        output.set_calculation_parameters(WavePyData(img=img,
                                                     idx4crop=idx4crop,
                                                     img_size_o=img_size_o))

        self.send("WavePy Data", output)

    def _get_execute_button_label(self):
        return "Crop Image"

    def _execute(self):
        img, idx4crop, img_size_o, _, _ = self.__crop_widget.get_accepted_output()

        self.__send_result(img, idx4crop, img_size_o)

    def _cancel(self):
        img, idx4crop, img_size_o, _, _ = self.__crop_widget.get_rejected_output()

        self.__send_result(img, idx4crop, img_size_o)
