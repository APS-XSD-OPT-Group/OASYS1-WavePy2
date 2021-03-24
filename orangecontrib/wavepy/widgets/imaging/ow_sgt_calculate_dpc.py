from orangecontrib.wavepy.widgets.gui.ow_wavepy_process_widget import WavePyProcessWidget

from wavepy2.util.plot.plot_tools import PlottingProperties

class OWSGTCalculateDPC(WavePyProcessWidget):
    name = "S.G.T. - Calculate DPC"
    id = "sgt_calculate_dpc"
    description = "S.G.T. - Calculate DPC"
    icon = "icons/sgt_calculate_dpc.png"
    priority = 4
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    CONTROL_AREA_HEIGTH = 840
    CONTROL_AREA_WIDTH = 1500

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    must_clean_layout = True

    def __init__(self):
        super(OWSGTCalculateDPC, self).__init__(show_general_option_box=True, show_automatic_box=True)

    def _get_execute_button_label(self):
        return "Calculate DPC"

    def _get_output_parameters(self):
        return self._process_manager.calculate_dpc(initial_crop_parameters=self._calculation_parameters,
                                                   initialization_parameters=self._initialization_parameters,
                                                   plotting_properties=PlottingProperties(context_widget=self._get_default_context(),
                                                                                          add_context_label=False,
                                                                                          use_unique_id=True))
