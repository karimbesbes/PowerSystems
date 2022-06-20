from pymodelica import compile_fmu
from pyfmi import load_fmu
import os
import matplotlib.pyplot as plt
#exec(open("./main.py").read())

model_name = 'PowerSystems.Examples.Wind.WindTurbine_DFIG'


modelica_path =\
["D:/_gitModelicaLibraries/PowerSystems/PowerSystems"]

target_directory = 'D:/FMUs'
options = {
#'c_compiler': 'msvs',
# propagate_derivatives: 'False',
#"source_code_fmu": True,
#'check_local_balancing':True,
#'generate_html_diagnostics': True,
# 'generate_json_statistics': True,
# 'generate_html_diagnostics_output_directory': 'D:/FMUs',
# 'generate_json_statistics_output_directory': 'D:/FMUs',
# 'write_iteration_variables_to_file': True,
# 'write_tearing_pairs_to_file': True,
#'state_initial_equations':True
#'enable_modelon_istoplevel_annotation': True,
#'constant_parameters': True,
# 'external_constant_evaluation_dynamic': False,
# 'convert_free_dependent_parameters_to_algebraics': False,
# 'eliminate_alias_constants': False,
# 'eliminate_alias_parameters': False,
#'msvs_path':'C:/apps/MVS14/VC',
#'msvs_version':'2015',
#'exclude_internal_variables':'*',
#'state_initial_equations':True,
#'state_start_values_fixed':True,
#'automatic_add_initial_equations':True,
#'variability_propagation_initial':True,
#'log_level':8,
#'convert_free_dependent_parameters_to_algebraics':False,
#'divide_by_vars_in_tearing':True,
#'event_indicator_structure':False,
#'event_output_vars':False,
}

my_fmu = compile_fmu(model_name, modelica_path,compile_to=target_directory,target="me", jvm_args="-Xmx32g", compiler_options=options)
# #my_fmu = compile_fmu('D:/modelica_icon.fmu')
# vdp=load_fmu(my_fmu, log_level=7)

# opts = vdp.simulate_options()
# opts["ncp"] = 1000
# #opts['solver'] = 'Dassl'

# res = vdp.simulate(options=opts,final_time=1000)
# x1 = res['TestCentrifugalPump7.Motor1.Cm']
# t = res['time']
# plt.figure(1)
# plt.plot(t, x1)
# plt.legend('X')
# plt.title('X')
# plt.ylabel('-')
# plt.xlabel('Time (s)')
# plt.show()