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
import copy

class OasysWavePyData(object):
    def __init__(self, process_manager=None, initialization_parameters=None, calculation_parameters=None, **parameters):
        self.__process_manager = process_manager
        self.__initialization_parameters = initialization_parameters
        self.__calculation_parameters = calculation_parameters
        self.__parameters = parameters

    def get_process_manager(self):
        return self.__process_manager

    def set_process_manager(self, process_manager=None):
        self.__process_manager = process_manager

    def get_initialization_parameters(self):
        return self.__initialization_parameters

    def set_initialization_parameters(self, initialization_parameters=None):
        self.__initialization_parameters = initialization_parameters

    def get_calculation_parameters(self):
        return self.__calculation_parameters

    def set_calculation_parameters(self, calculation_parameters=None):
        self.__calculation_parameters = calculation_parameters

    def get_parameters(self):
        return self.__parameters

    def get_parameter(self, parameter_name, default_value=None):
        try:
            return self.__parameters[parameter_name]
        except:
            return default_value

    def set_parameter(self, parameter_name, value):
        self.__parameters[parameter_name] = value

    def duplicate(self):
        duplicated = OasysWavePyData(self.__process_manager,
                                     None if self.__initialization_parameters is None else self.__initialization_parameters.duplicate(),
                                     None if self.__calculation_parameters is None else self.__calculation_parameters.duplicate())

        if not self.__parameters is None:
            for parameter_name in self.__parameters.keys():
                duplicated.set_parameter(parameter_name, copy.deepcopy(self.get_parameter(parameter_name)))

        return duplicated

from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QTextCursor

from aps.common.widgets.log_stream_widget import LogStreamWidget
from aps.common.singleton import Singleton, synchronized_method
from aps.common.registry import GenericRegistry

@Singleton
class __LogStreamRegistry(GenericRegistry):
    def __init__(self):
        GenericRegistry.__init__(self, registry_name="Log Stream")

    @synchronized_method
    def register_log_stream(self, log_stream, application_name=None, replace=False):
        super().register_instance(log_stream, application_name, replace)

    @synchronized_method
    def reset(self, application_name=None):
        super().reset(application_name)

    def get_log_stream_instance(self, application_name=None):
        return super().get_instance(application_name)

def register_log_stream_widget_instance(application_name=None, reset=False, replace=False):
    if reset: __LogStreamRegistry.Instance().reset(application_name)
    __LogStreamRegistry.Instance().register_log_stream(LogStreamWidget(width=1095, height=450), application_name, replace)

def get_registered_log_stream_instance(application_name=None):
    return __LogStreamRegistry.Instance().get_log_stream_instance(application_name)
