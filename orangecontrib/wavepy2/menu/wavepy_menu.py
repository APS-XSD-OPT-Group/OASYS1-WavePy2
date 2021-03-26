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
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings

from orangecanvas.scheme.link import SchemeLink

from oasys.menus.menu import OMenu
from wavepy2.util.plot.plotter import PlotterMode
from wavepy2.util.log.logger import LoggerMode

base_tools_path = "orangecontrib.wavepy2.widgets.tools."
base_imaging_path = "orangecontrib.wavepy2.widgets.imaging."
base_diagnostic_path = "orangecontrib.wavepy2.widgets.diagnostic."
base_metrology_path = "orangecontrib.wavepy2.widgets.metrology."

sgt_analysis_widget_list_no_interactions = [
    [base_imaging_path + "ow_sgt_init.OWSGTInit", (0.0, 50.0), {}],
    [base_imaging_path + "ow_sgt_manager_initialization.OWSGTManagerInitialization", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_initial_image.OWSGTCropInitialImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_reference_image.OWSGTCropReferenceImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_dpc.OWSGTCalculateDPC", (50.0, 200.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_show_calculated_dpc.OWSGTShowCalculatedDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_correct_zero_dpc.OWSGTCorrectZeroDPC", None, {"is_automatic_run": True, "correct_dpc_center": False}],
    [base_imaging_path + "ow_sgt_remove_linear_fit_dpc.OWSGTRemoveLinearFitDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_dpc_profile_analysis.OWSGTDPCProfileAnalysis", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_fit_radius_dpc.OWSGTFitRadiusDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_do_integration.OWSGTDoIntegration", (50.0, 400.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_thickness.OWSGTCalculateThickness", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_1.OWSGTCalculate2ndOrderComponentOfThePhase1", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_2.OWSGTCalculate2ndOrderComponentOfThePhase2", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_remove_2nd_order.OWSGTRemove2ndOrder", None, {"is_automatic_run": True}],
]

sgt_analysis_widget_list = [
    [base_imaging_path + "ow_sgt_init.OWSGTInit", (0.0, 50.0), {}],
    [base_imaging_path + "ow_sgt_manager_initialization.OWSGTManagerInitialization", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_initial_image.OWSGTCropInitialImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_reference_image.OWSGTCropReferenceImage", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_dpc.OWSGTCalculateDPC", (50.0, 200.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_calculated_dpc.OWSGTCropCalculatedDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_show_calculated_dpc.OWSGTShowCalculatedDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_correct_zero_dpc.OWSGTCorrectZeroDPC", None, {"is_automatic_run": True, "correct_dpc_center": True}],
    [base_imaging_path + "ow_sgt_remove_linear_fit_dpc.OWSGTRemoveLinearFitDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_dpc_profile_analysis.OWSGTDPCProfileAnalysis", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_fit_radius_dpc.OWSGTFitRadiusDPC", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_dpc_for_integration.OWSGTCropDPCForIntegration", (50.0, 400.0), {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_do_integration.OWSGTDoIntegration", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_thickness.OWSGTCalculateThickness", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_2nd_order_component_of_the_phase_1.OWSGTCrop2ndOrderComponentOfThePhase1", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_1.OWSGTCalculate2ndOrderComponentOfThePhase1", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_crop_2nd_order_component_of_the_phase_2.OWSGTCrop2ndOrderComponentOfThePhase2", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_calculate_2nd_order_component_of_the_phase_2.OWSGTCalculate2ndOrderComponentOfThePhase2", None, {"is_automatic_run": True}],
    [base_imaging_path + "ow_sgt_remove_2nd_order.OWSGTRemove2ndOrder", None, {"is_automatic_run": True}],
]

sgz_analysis_widget_list = [
    [base_diagnostic_path + "ow_sgz_init.OWSGZInit", (0.0, 50.0), {}],
    [base_diagnostic_path + "ow_sgz_manager_initialization.OWSGZManagerInitialization", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_crop_initial_image.OWSGZCropInitialImage", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_crop_dark_image.OWSGZCropDarkImage", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_calculate_harmonic_periods.OWSGZCalculateHarmonicPeriods", (50.0, 200.0), {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_run_calculation.OWSGZRunCalculation", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_sort_calculation_result.OWSGZSortCalculationResult", None, {"is_automatic_run": True}],
    [base_diagnostic_path + "ow_sgz_fit_calculation_result.OWSGZFitCalculationResult", None, {"is_automatic_run": True}],
]

def showInfoMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def showConfirmMessage(text, message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Question)
    msgBox.setText(text)
    msgBox.setInformativeText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
    ret = msgBox.exec_()
    return ret

def showWarningMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def showCriticalMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

class WavePyMenu(OMenu):

    def __init__(self):
        super().__init__(name="WavePy2")


        self.openContainer()
        self.addContainer("Imaging")
        self.addSubMenu("Create Single Grating Talbot Analysis")
        self.addSubMenu("Create Single Grating Talbot Analysis (No Interactions)")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Coherence")
        self.addSubMenu("Create Single Grating Z Scan Analysis")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Metrology")
        self.addSubMenu("Create Fit Residual Lenses Analysis")
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
        if showConfirmMessage("Confirm Action", "Create Single Grating Talbot Analysis?") == QtWidgets.QMessageBox.Yes:
            self.create_analysis(sgt_analysis_widget_list)

    def executeAction_2(self, action):
        if showConfirmMessage("Confirm Action", "Create Single Grating Talbot Analysis (No Interactions)?") == QtWidgets.QMessageBox.Yes:
            self.create_analysis(sgt_analysis_widget_list_no_interactions)

    def executeAction_3(self, action):
        if showConfirmMessage("Confirm Action", "Create Single Grating Z Scan Analysis?") == QtWidgets.QMessageBox.Yes:
            self.create_analysis(sgz_analysis_widget_list)

    def executeAction_4(self, action):
        pass

    def executeAction_5(self, action):
        QSettings().setValue("wavepy/plotter_mode", PlotterMode.FULL)
        showInfoMessage("Plotter Mode set to: FULL\nReload the workspace to make it effective")

    def executeAction_6(self, action):
        QSettings().setValue("wavepy/plotter_mode", PlotterMode.DISPLAY_ONLY)
        showInfoMessage("Plotter Mode set to: DISPLAY ONLY\nReload the workspace to make it effective")

    def executeAction_7(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.FULL)
        showInfoMessage("Logger Mode set to: FULL\nReload the workspace to make it effective")

    def executeAction_8(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.WARNING)
        showInfoMessage("Logger Mode set to: WARNING\nReload the workspace to make it effective")

    def executeAction_9(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.ERROR)
        showInfoMessage("Logger Mode set to: ERROR\nReload the workspace to make it effective")

    def executeAction_10(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.NONE)
        showInfoMessage("Logger Mode set to: NONE\nReload the workspace to make it effective")


    def create_analysis(self, widgets_list):
        nodes = []
        for widget, position, attributes in widgets_list: nodes.extend(self.createNewNodeAndWidget(widget_desc=self.getWidgetDesc(widget),
                                                                                                   position=position,
                                                                                                   attributes=attributes))
        self.createLinks(nodes)


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
