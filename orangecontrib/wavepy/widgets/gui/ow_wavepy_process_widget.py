from orangewidget import gui

from orangecontrib.wavepy.widgets.gui.ow_wavepy_widget import WavePyWidget
from orangecontrib.wavepy.util.wavepy_objects import OasysWavePyData
from wavepy2.util.plot.plot_tools import DefaultContextWidget


class WavePyProcessWidget(WavePyWidget):
    inputs = [("WavePy Data", OasysWavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": OasysWavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    want_main_area = 0
    must_clean_layout = True

    def __init__(self, show_general_option_box=True, show_automatic_box=True):
        super(WavePyProcessWidget, self).__init__(show_general_option_box=show_general_option_box, show_automatic_box=show_automatic_box)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            data = data.duplicate()

            self._initialization_parameters = data.get_initialization_parameters()
            self._calculation_parameters    = data.get_calculation_parameters()
            self._process_manager           = data.get_process_manager()

            if self.is_automatic_run: self._execute()

    def _execute(self):
        if self.must_clean_layout: self._clear_wavepy_layout()

        output_calculation_parameters = self._get_output_parameters()

        self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
        self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

        gui.rubber(self.controlArea)

        output = OasysWavePyData()
        output.set_process_manager(self._process_manager)
        output.set_initialization_parameters(self._initialization_parameters)
        output.set_calculation_parameters(output_calculation_parameters)

        self.send("WavePy Data", output)

    def _get_output_parameters(self):
        raise NotImplementedError()

    def _get_default_context(self):
        return DefaultContextWidget(self._wavepy_widget_area)
