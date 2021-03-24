from orangecontrib.wavepy.widgets.gui.ow_wavepy_process_widget import WavePyProcessWidget

from wavepy2.util.plot.plot_tools import PlottingProperties

class OWSGTShowCalculatedDPC(WavePyProcessWidget):
    name = "S.G.T. - Show Calculated DPC"
    id = "sgt_show_calculated_dpc"
    description = "S.G.T. - Show Calculated DPC"
    icon = "icons/sgt_show_calculated_dpc.png"
    priority = 6
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    CONTROL_AREA_HEIGTH = 840
    CONTROL_AREA_WIDTH  = 1500

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    must_clean_layout = True

    def __init__(self):
        super(OWSGTShowCalculatedDPC, self).__init__(show_general_option_box=True, show_automatic_box=True)

    def _get_execute_button_label(self):
        return "Show Calculated DPC"

    def _get_output_parameters(self):
        return self._process_manager.show_calculated_dpc(dpc_result=self._calculation_parameters,
                                                         initialization_parameters=self._initialization_parameters,
                                                         plotting_properties=PlottingProperties(context_widget=self._get_default_context(),
                                                                                                add_context_label=False,
                                                                                                use_unique_id=True))

