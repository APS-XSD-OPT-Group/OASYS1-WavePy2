from PyQt5.QtCore import QSettings

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

class OWSGTManagerInitialization(WavePyWidget):
    name = "S.G.T. Manager Initialization"
    id = "sgt_manager_initialization"
    description = "S.G.T. Manager Initialization"
    icon = "icons/sgt_manager_initialization.png"
    priority = 2
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    inputs = [("WavePy Data", OasysWavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": OasysWavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    want_main_area = 0

    CONTROL_AREA_HEIGTH = 150
    CONTROL_AREA_WIDTH  = 400

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    def __init__(self):
        super(OWSGTManagerInitialization, self).__init__(show_general_option_box=True, show_automatic_box=True)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            data = data.duplicate()

            self._initialization_parameters = data.get_initialization_parameters()
            self._process_manager = data.get_process_manager()

            if self.is_automatic_run:
                self._execute()

    def _get_execute_button_label(self):
        return "Manager Initialization"

    def _execute(self):
        self._process_manager.manager_initialization(initialization_parameters=self._initialization_parameters,
                                                      script_logger_mode=QSettings().value("wavepy/logger_mode", LoggerMode.FULL, type=int))

        self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
        self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

        gui.rubber(self.controlArea)

        output = OasysWavePyData()

        output.set_process_manager(self._process_manager)
        output.set_initialization_parameters(self._initialization_parameters)

        self.send("WavePy Data", output)
