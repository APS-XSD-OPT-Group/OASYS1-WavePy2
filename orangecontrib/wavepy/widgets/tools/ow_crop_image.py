from orangewidget import gui

from orangecontrib.wavepy.widgets.gui.ow_wavepy_widget import WavePyWidget

from wavepy2.util.common.common_tools import AlreadyInitializedError
from wavepy2.util.log.logger import register_logger_single_instance, LoggerMode
from wavepy2.util.plot.plotter import register_plotter_instance, PlotterMode
from wavepy2.util.ini.initializer import get_registered_ini_instance, register_ini_instance, IniMode
from wavepy2.util.log.logger import LoggerMode
from wavepy2.util.plot.plot_tools import PlottingProperties, DefaultContextWidget

from wavepy2.tools.common.wavepy_data import WavePyData
from wavepy2.tools.common.bl import crop_image

class OWCropImage(WavePyWidget):
    name = "Crop Image"
    id = "crop_image"
    description = "Crop Image"
    icon = "icons/crop_image.png"
    priority = 1
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    inputs = [("WavePy Data", WavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": WavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    want_main_area = 0

    CONTROL_AREA_WIDTH = 955

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = 850

    def __init__(self):
        super(OWCropImage, self).__init__(show_general_option_box=True, show_automatic_box=True)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.button(self.button_box, self, "Initial Crop", callback=self.cancel, height=45)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        self.__initialization_parameters = data.get_parameter("initialization_parameters")
        self.__calculation_parameters    = data.get_parameter("calculation_parameters")
        self.__process_manager           = data.get_parameter("process_manager")

        img = None
        if not self.__calculation_parameters is None: img = self.__calculation_parameters.get_parameter("img")
        if img is None:                               img = self.__initialization_parameters.get_parameter("img")

        if not img is None:
            self.__crop_widget = crop_image.draw_crop_image(initialization_parameters=self.__initialization_parameters,
                                                            plotting_properties=PlottingProperties(context_widget=DefaultContextWidget(self.controlArea),
                                                                                                   add_context_label=False,
                                                                                                   use_unique_id=True),
                                                            img=img)[0]
        self.controlArea.setFixedHeight(840)

        gui.rubber(self.controlArea)

    def __send_result(self, img, idx4crop, img_size_o):
        output = WavePyData()

        output.set_parameter("input_parameters", self.__initialization_parameters)
        output.set_parameter("process_manager",  self.__process_manager)
        output.set_parameter("calculation_parameters",  WavePyData(img=img,
                                                                   idx4crop=idx4crop,
                                                                   img_size_o=img_size_o))

        self.send("WavePy Data", output)

    def _get_execute_button_label(self):
        return "Crop Image"

    def _execute(self):
        img, idx4crop, img_size_o = self.__crop_widget.get_accepted_output()

        self.__send_result(img, idx4crop, img_size_o)

    def cancel(self):
        img, idx4crop, img_size_o = self.__crop_widget.get_rejected_output()

        self.__send_result(img, idx4crop, img_size_o)
