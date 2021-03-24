from PyQt5.QtCore import QSettings

from orangecontrib.wavepy.widgets.gui.ow_wavepy_process_widget import WavePyProcessWidget
from orangecontrib.wavepy.util.wavepy_objects import OasysWavePyData

from wavepy2.util.log.logger import LoggerMode

class OWSGTManagerInitialization(WavePyProcessWidget):
    name = "S.G.T. Manager Initialization"
    id = "sgt_manager_initialization"
    description = "S.G.T. Manager Initialization"
    icon = "icons/sgt_manager_initialization.png"
    priority = 2
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    must_clean_layout = False

    CONTROL_AREA_HEIGTH = 150
    CONTROL_AREA_WIDTH  = 400

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    def __init__(self):
        super(OWSGTManagerInitialization, self).__init__(show_general_option_box=True, show_automatic_box=True)

    def _get_execute_button_label(self):
        return "Manager Initialization"

    def _get_output_parameters(self):
        self._process_manager.manager_initialization(initialization_parameters=self._initialization_parameters,
                                                      script_logger_mode=QSettings().value("wavepy/logger_mode", LoggerMode.FULL, type=int))

        return None
