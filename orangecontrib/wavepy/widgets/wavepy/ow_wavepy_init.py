from orangecontrib.wavepy.widgets.gui.ow_wavepy_widget import WavePyWidget


from wavepy2.tools.common.wavepy_data import WavePyData

class OWWavePyInit(WavePyWidget):
    name = "WavePy Initialization"
    id = "wavepy_init"
    description = "WavePy Initialization"
    icon = "icons/wavepy_init.png"
    priority = 0
    category = ""
    keywords = ["wavepy", "init"]

    outputs = [{"name": "WavePy Initialization",
                "type": WavePyData,
                "doc": "WavePy Initialization",
                "id": "WavePy_Initialization"}]

    want_main_area = 0

    def __init__(self):
        super(OWWavePyInit, self).__init__(show_general_option_box=False, show_automatic_box=False)

    def execute(self):

        self.send("WavePy Initialization", WavePyData(logger_mode=LoggerMode.FULL, plotter_mode=PlotterMode.FULL))


