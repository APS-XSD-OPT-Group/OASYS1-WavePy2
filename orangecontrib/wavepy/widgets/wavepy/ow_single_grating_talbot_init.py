from orangewidget import gui

from orangecontrib.wavepy.widgets.gui.ow_wavepy_widget import WavePyWidget

from wavepy2.util.common.common_tools import AlreadyInitializedError
from wavepy2.util.log.logger import register_logger_single_instance, LoggerMode
from wavepy2.util.plot.plotter import register_plotter_instance, PlotterMode
from wavepy2.util.ini.initializer import get_registered_ini_instance, register_ini_instance, IniMode
from wavepy2.util.log.logger import LoggerMode
from wavepy2.util.plot.plot_tools import PlottingProperties, DefaultContextWidget

from wavepy2.tools.common.wavepy_data import WavePyData

from wavepy2.tools.imaging.single_grating.bl.single_grating_talbot import create_single_grating_talbot_manager

class OWSingleGratingTalbotInit(WavePyWidget):
    name = "Single Grating Talbot Initialization"
    id = "sgt_init"
    description = "Single Grating Talbot Initialization"
    icon = "icons/sgt_init.png"
    priority = 1
    category = ""
    keywords = ["wavepy", "sgt", "init"]

    inputs = [("WavePy Initialization", WavePyData, "set_input"),]

    outputs = [{"name": "SGT Initialization",
                "type": WavePyData,
                "doc": "SGT Initialization",
                "id": "SGT_Initialization"}]

    want_main_area = 0

    CONTROL_AREA_WIDTH = 855

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10

    def __init__(self):
        super(OWSingleGratingTalbotInit, self).__init__(show_general_option_box=True, show_automatic_box=True)

        try: register_logger_single_instance(logger_mode=LoggerMode.FULL)
        except AlreadyInitializedError: pass
        try: register_plotter_instance(plotter_mode=PlotterMode.FULL)
        except AlreadyInitializedError: pass
        try: register_ini_instance(IniMode.LOCAL_FILE, ini_file_name=".single_grating_talbot.ini")
        except AlreadyInitializedError: pass

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)

        self.__single_grating_talbot_manager = create_single_grating_talbot_manager()

        self.__init_widget = self.__single_grating_talbot_manager.draw_initialization_parameters_widget(plotting_properties=PlottingProperties(context_widget=DefaultContextWidget(self.controlArea),
                                                                                                                                               show_runtime_options=False,
                                                                                                                                               add_context_label=False,
                                                                                                                                               use_unique_id=True))[0]

        self.controlArea.setFixedHeight(self.__init_widget.height()+145)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        pass

    def execute(self):
        output = WavePyData()
        output.set_parameter("initialization_parameters", self.__init_widget.get_accepted_output())
        output.set_parameter("process_manager",           self.__single_grating_talbot_manager)

        self.send("SGT Initialization", output)


