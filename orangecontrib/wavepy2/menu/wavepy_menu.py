# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSettings

from orangecanvas.scheme.link import SchemeLink
from oasys.menus.menu import OMenu

from wavepy2.util.plot.plotter import PlotterMode
from wavepy2.util.log.logger import LoggerMode

from orangecontrib.wavepy2.util.gui.ow_wavepy_init_widget import WavePyInitWidget

base_tools_path = "orangecontrib.wavepy2.widgets.tools."
base_imaging_path = "orangecontrib.wavepy2.widgets.imaging."
base_diagnostic_path = "orangecontrib.wavepy2.widgets.diagnostic."
base_metrology_path = "orangecontrib.wavepy2.widgets.metrology."

sgt_analysis_widget_list_not_interactive = [
    [base_imaging_path + "ow_sgt_init.OWSGTInit", (0.0, 50.0), {}],
    [base_imaging_path + "ow_sgt_manager_initialization.OWSGTManagerInitialization", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_initial_image.OWSGTCropInitialImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_reference_image.OWSGTCropReferenceImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_dpc.OWSGTCalculateDPC", (50.0, 200.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_calculated_dpc.OWSGTCropCalculatedDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_show_calculated_dpc.OWSGTShowCalculatedDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_correct_zero_dpc.OWSGTCorrectZeroDPC", None, {"is_automatic_run": True, "correct_dpc_center": 0}],
    [base_imaging_path + "ow_sgt_remove_linear_fit_dpc.OWSGTRemoveLinearFitDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_dpc_profile_analysis.OWSGTDPCProfileAnalysis", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_fit_radius_dpc.OWSGTFitRadiusDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_dpc_for_integration.OWSGTCropDPCForIntegration", (50.0, 350.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_do_integration.OWSGTDoIntegration", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_thickness.OWSGTCalculateThickness", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_2nd_order_component_of_the_phase_1.OWSGTCrop2ndOrderComponentOfThePhase1", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_1.OWSGTCalculate2ndOrderComponentOfThePhase1", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_2nd_order_component_of_the_phase_2.OWSGTCrop2ndOrderComponentOfThePhase2", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_2.OWSGTCalculate2ndOrderComponentOfThePhase2", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_remove_2nd_order.OWSGTRemove2ndOrder", None, {"is_automatic_run": True}],
]

sgt_analysis_widget_list_interactive = [
    [base_imaging_path + "ow_sgt_init.OWSGTInit", (0.0, 50.0), {}],
    [base_imaging_path + "ow_sgt_manager_initialization.OWSGTManagerInitialization", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_initial_image.OWSGTCropInitialImage", None, {"is_automatic_run": False}],
    [base_imaging_path + "ow_sgt_crop_reference_image.OWSGTCropReferenceImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_dpc.OWSGTCalculateDPC", (50.0, 200.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_calculated_dpc.OWSGTCropCalculatedDPC", None, {"is_automatic_run": False}],
    [base_imaging_path + "ow_sgt_show_calculated_dpc.OWSGTShowCalculatedDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_correct_zero_dpc.OWSGTCorrectZeroDPC", None, {"is_automatic_run": True, "correct_dpc_center": 1}],
    [base_imaging_path + "ow_sgt_remove_linear_fit_dpc.OWSGTRemoveLinearFitDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_dpc_profile_analysis.OWSGTDPCProfileAnalysis", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_fit_radius_dpc.OWSGTFitRadiusDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_dpc_for_integration.OWSGTCropDPCForIntegration", (50.0, 350.0), {"is_automatic_run": False}],
    [base_imaging_path + "ow_sgt_do_integration.OWSGTDoIntegration", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_thickness.OWSGTCalculateThickness", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_2nd_order_component_of_the_phase_1.OWSGTCrop2ndOrderComponentOfThePhase1", None, {"is_automatic_run": False}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_1.OWSGTCalculate2ndOrderComponentOfThePhase1", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_2nd_order_component_of_the_phase_2.OWSGTCrop2ndOrderComponentOfThePhase2", None, {"is_automatic_run": False}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_2.OWSGTCalculate2ndOrderComponentOfThePhase2", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_remove_2nd_order.OWSGTRemove2ndOrder", None, {"is_automatic_run": True}],
]

sgz_analysis_widget_list_not_interactive = [
    [base_diagnostic_path + "ow_sgz_init.OWSGZInit", (0.0, 50.0), {}],
    [base_diagnostic_path + "ow_sgz_manager_initialization.OWSGZManagerInitialization", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_crop_initial_image.OWSGZCropInitialImage", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_crop_dark_image.OWSGZCropDarkImage", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_calculate_harmonic_periods.OWSGZCalculateHarmonicPeriods", (50.0, 200.0), {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_run_calculation.OWSGZRunCalculation", None, {"is_automatic_run": True, "show_fourier" : 0}],
    [base_diagnostic_path + "ow_sgz_sort_calculation_result.OWSGZSortCalculationResult", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_fit_calculation_result.OWSGZFitCalculationResult", None, {"is_automatic_run": True}],
]

sgz_analysis_widget_list_interactive = [
    [base_diagnostic_path + "ow_sgz_init.OWSGZInit", (0.0, 50.0), {}],
    [base_diagnostic_path + "ow_sgz_manager_initialization.OWSGZManagerInitialization", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_crop_initial_image.OWSGZCropInitialImage", None, {"is_automatic_run": False}],
    [base_diagnostic_path + "ow_sgz_crop_dark_image.OWSGZCropDarkImage", None, {"is_automatic_run": False}],
    [base_diagnostic_path + "ow_sgz_calculate_harmonic_periods.OWSGZCalculateHarmonicPeriods", (50.0, 200.0), {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_run_calculation.OWSGZRunCalculation", None, {"is_automatic_run": True, "show_fourier" : 0}],
    [base_diagnostic_path + "ow_sgz_sort_calculation_result.OWSGZSortCalculationResult", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_fit_calculation_result.OWSGZFitCalculationResult", None, {"is_automatic_run": True}],
]

frl_analysis_widget_list_not_interactive = [
    [base_metrology_path + "ow_frl_init.OWFRLInit", (0.0, 50.0), {}],
    [base_metrology_path + "ow_frl_manager_initialization.OWFRLManagerInitialization", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_crop_thickness.OWFRLCropThickness", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_manage_crop_thickness.OWFRLManageCropThickness", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_center_image.OWFRLCenterImage", (50.0, 200.0), {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_fit_radius_dpc.OWFRLFitRadiusDPC", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_do_fit.OWFRLDoFit", None, {"is_automatic_run": True}],
]

frl_analysis_widget_list_interactive = [
    [base_metrology_path + "ow_frl_init.OWFRLInit", (0.0, 50.0), {}],
    [base_metrology_path + "ow_frl_manager_initialization.OWFRLManagerInitialization", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_crop_thickness.OWFRLCropThickness", None, {"is_automatic_run": False}],
    [base_metrology_path + "ow_frl_manage_crop_thickness.OWFRLManageCropThickness", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_center_image.OWFRLCenterImage", (50.0, 200.0), {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_fit_radius_dpc.OWFRLFitRadiusDPC", None, {"is_automatic_run": True}],
    [base_metrology_path + "ow_frl_do_fit.OWFRLDoFit", None, {"is_automatic_run": True}],
]

class WavePyMenu(OMenu):

    def __init__(self):
        super().__init__(name="WavePy2")


        self.openContainer()
        self.addContainer("Imaging")
        self.addSubMenu("Create Single Grating Talbot analysis (not interactive)")
        self.addSubMenu("Create Single Grating Talbot analysis (interactive)")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Coherence")
        self.addSubMenu("Create Single Grating Z Scan analysis (not interactive)")
        self.addSubMenu("Create Single Grating Z Scan analysis (interactive)")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Metrology")
        self.addSubMenu("Create Fit Residual Lenses analysis (not interactive)")
        self.addSubMenu("Create Fit Residual Lenses analysis (interactive)")
        self.closeContainer()

        self.addSeparator()

        self.openContainer()
        self.addContainer("Plotter Options")
        self.addSubMenu("Set Plotter Mode: FULL")
        self.addSubMenu("Set Plotter Mode: DISPLAY ONLY")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Logger Options")
        self.addSubMenu("Set Logger Mode: FULL")
        self.addSubMenu("Set Logger Mode: WARNING")
        self.addSubMenu("Set Logger Mode: ERROR")
        self.addSubMenu("Set Logger Mode: NONE")
        self.closeContainer()

    def executeAction_1(self, action):
        if _showConfirmMessage("Confirm Action", "Create Single Grating Talbot analysis (not interactive)?") == QMessageBox.Yes:
            self.__create_analysis(sgt_analysis_widget_list_not_interactive)

    def executeAction_2(self, action):
        if _showConfirmMessage("Confirm Action", "Create Single Grating Talbot analysis (interactive)?") == QMessageBox.Yes:
            self.__create_analysis(sgt_analysis_widget_list_interactive)

    def executeAction_3(self, action):
        if _showConfirmMessage("Confirm Action", "Create Single Grating Z Scan analysis (not interactive)?") == QMessageBox.Yes:
            self.__create_analysis(sgz_analysis_widget_list_not_interactive)

    def executeAction_4(self, action):
        if _showConfirmMessage("Confirm Action", "Create Single Grating Z Scan analysis (interactive)?") == QMessageBox.Yes:
            self.__create_analysis(sgz_analysis_widget_list_interactive)

    def executeAction_5(self, action):
        if _showConfirmMessage("Confirm Action", "Create Fit Residual Lenses analysis (not interactive)?") == QMessageBox.Yes:
            self.__create_analysis(frl_analysis_widget_list_not_interactive)

    def executeAction_6(self, action):
        if _showConfirmMessage("Confirm Action", "Create Fit Residual Lenses analysis (interactive)?") == QMessageBox.Yes:
            self.__create_analysis(frl_analysis_widget_list_interactive)

    def executeAction_7(self, action):
        self.__switch_plotter_mode(PlotterMode.FULL, "FULL")

    def executeAction_8(self, action):
        self.__switch_plotter_mode(PlotterMode.DISPLAY_ONLY, "DISPLAY ONLY")

    def executeAction_9(self, action):
        self.__switch_logger_mode(LoggerMode.FULL, "FULL")

    def executeAction_10(self, action):
        self.__switch_logger_mode(LoggerMode.WARNING, "WARNING")

    def executeAction_11(self, action):
        self.__switch_logger_mode(LoggerMode.ERROR, "ERROR")

    def executeAction_12(self, action):
        self.__switch_logger_mode(LoggerMode.NONE, "NONE")

    #################################################################
    #
    # PRIVATE METHODS
    #
    #################################################################

    def __create_analysis(self, widgets_list):
        nodes = []
        lower_row_position = self.__get_lower_row_position()

        for widget, position, attributes in widgets_list:
            if not position is None: position = (position[0], position[1] + lower_row_position)

            nodes.extend(self.createNewNodeAndWidget(widget_desc=self.getWidgetDesc(widget),
                                                     position=position,
                                                     attributes=attributes))
        self.createLinks(nodes)

    def __get_lower_row_position(self):
        try:
            lower_row_position = max([link.sink_node.position[1] for link in self.canvas_main_window.current_document().scheme().links])
            if lower_row_position != 0.0: return 150.0 + lower_row_position
        except: return 0.0

    def __switch_plotter_mode(self, plotter_mode, plotter_name):
        existing_plotter_mode = QSettings().value("wavepy/plotter_mode", PlotterMode.FULL, type=int)
        try:
            QSettings().setValue("wavepy/plotter_mode", plotter_mode)

            for node in self.canvas_main_window.current_document().scheme().nodes:
                widget = self.canvas_main_window.current_document().scheme().widget_for_node(node)
                if isinstance(widget, WavePyInitWidget):
                    widget.initialize_plotter(replace=True)
                    widget.initialize_process_manager()

            _showInfoMessage("Plotter Mode set to: " + plotter_name + "\nRestart any analysis from Init widget to make it effective")
        except Exception as exception:
            QSettings().setValue("wavepy/plotter_mode", existing_plotter_mode)
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

    def __switch_logger_mode(self, logger_mode, logger_name):
        existing_logger_mode = QSettings().value("wavepy/logger_mode", LoggerMode.FULL, type=int)
        try:
            QSettings().setValue("wavepy/logger_mode", logger_mode)

            for node in self.canvas_main_window.current_document().scheme().nodes:
                widget = self.canvas_main_window.current_document().scheme().widget_for_node(node)
                if isinstance(widget, WavePyInitWidget):
                    widget.initialize_logger(replace=True)
                    widget.initialize_process_manager()

            _showInfoMessage("Logger Mode set to: " + logger_name + "\nRestart any analysis from Init widget to make it effective")
        except Exception as exception:
            QSettings().setValue("wavepy/logger_mode", existing_logger_mode)
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

    #################################################################
    #
    # SCHEME MANAGEMENT
    #
    #################################################################

    def getWidgetFromNode(self, node):
        return self.canvas_main_window.current_document().scheme().widget_for_node(node)

    def createLinks(self, nodes):
        previous_node = None
        for node in nodes:
            if not previous_node is None:
                link = SchemeLink(source_node=previous_node, source_channel="WavePy Data", sink_node=node, sink_channel="WavePy Data")
                self.canvas_main_window.current_document().addLink(link=link)
            previous_node = node

    def getWidgetDesc(self, widget_name):
        return self.canvas_main_window.widget_registry.widget(widget_name)

    def createNewNode(self, widget_desc, position=None):
        return self.canvas_main_window.current_document().createNewNode(widget_desc, position=position)

    def createNewNodeAndWidget(self, widget_desc, position=None, attributes={}):
        nodes = []

        nodes.append(self.createNewNode(widget_desc, position))
        widget = self.getWidgetFromNode(nodes[0])

        for attribute in attributes.keys(): setattr(widget, attribute, attributes[attribute])

        return nodes


def _showInfoMessage(message):
    _create_message_box(QMessageBox.Information, message, QMessageBox.Ok).exec_()

def _showWarningMessage(message):
    _create_message_box(QMessageBox.Warning, message, QMessageBox.Ok).exec_()

def _showCriticalMessage(message):
    _create_message_box(QMessageBox.Critical, message, QMessageBox.Ok).exec_()

def _showConfirmMessage(text, message):
    msgBox = _create_message_box(QMessageBox.Question, message, QMessageBox.Yes | QMessageBox.No)
    msgBox.setInformativeText(message)
    msgBox.setDefaultButton(QMessageBox.No)

    return msgBox.exec_()

def _create_message_box(icon, message, std_buttons):
    msgBox = QMessageBox()
    msgBox.setIcon(icon)
    msgBox.setText(message)
    msgBox.setStandardButtons(std_buttons)
    return msgBox
