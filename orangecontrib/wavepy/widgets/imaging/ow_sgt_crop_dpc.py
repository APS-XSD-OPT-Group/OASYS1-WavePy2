
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

class OWSGTCropDPC(WavePyWidget):
    name = "S.G.T. - Crop DPC"
    id = "crop_dpc"
    description = "S.G.T. - Crop DPC"
    icon = "icons/sgt_crop_dpc.png"
    priority = 5
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
        super(OWSGTCropDPC, self).__init__(show_general_option_box=True, show_automatic_box=True)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.button(self.button_box, self, "Cancel Crop", callback=self._cancel, height=45)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            data = data.duplicate()

            self._initialization_parameters = data.get_initialization_parameters()
            self._calculation_parameters = data.get_calculation_parameters()
            self._process_manager = data.get_process_manager()

            if not self._calculation_parameters is None:
                self._clear_wavepy_layout()

                self.__crop_widget = self._process_manager.draw_crop_dpc(dpc_result=self._calculation_parameters,
                                                                         initialization_parameters=self._initialization_parameters,
                                                                         plotting_properties=PlottingProperties(context_widget=DefaultContextWidget(self._wavepy_widget_area),
                                                                                                                add_context_label=False,
                                                                                                                use_unique_id=True),
                                                                         tab_widget_height=660)[0]

            self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
            self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

            gui.rubber(self.controlArea)

            if self.is_automatic_run: self._cancel()

    def __send_result(self, idx2ndCrop):
        self._calculation_parameters.set_parameter("idx2ndCrop", idx2ndCrop)

        output = OasysWavePyData()

        output.set_process_manager(self._process_manager)
        output.set_initialization_parameters(self._initialization_parameters)
        output.set_calculation_parameters(self._calculation_parameters)

        self.send("WavePy Data", output)

    def _get_execute_button_label(self):
        return "Crop DPC"

    def _execute(self):
        _, idx2ndCrop, _ = self.__crop_widget.get_accepted_output()

        self.__send_result(idx2ndCrop)

    def _cancel(self):
        _, idx2ndCrop, _ = self.__crop_widget.get_rejected_output()

        self.__send_result(idx2ndCrop)