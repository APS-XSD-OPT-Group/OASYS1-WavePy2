
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
