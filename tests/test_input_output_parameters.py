import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

from ansys.fluent.parametric.parameters import InputParameters, OutputParameters


def test_input_output_parameters():
    case_filepath = examples.download_file("nozzle-2D-WB.cas.h5", "pyfluent/optislang")
    session = pyfluent.launch_fluent(version="2d")
    session.solver.root.file.read(file_name=case_filepath, file_type="case")
    inp = InputParameters(session)
    assert len(inp) == 1
    assert inp["inlet_pressure"] == "0.9 [atm]"
    assert inp.get_unit_label("inlet_pressure") == "atm"

    inp["inlet_pressure"] = "0.91 [atm]"
    assert inp["inlet_pressure"] == "0.91 [atm]"
    assert inp.get_unit_label("inlet_pressure") == "atm"

    inp["inlet_pressure"] = 0.92
    assert inp["inlet_pressure"] == "0.92 [atm]"
    assert inp.get_unit_label("inlet_pressure") == "atm"

    inp["inlet_pressure"] = "90000 [Pa]"
    assert inp["inlet_pressure"] == "90000 [Pa]"
    assert inp.get_unit_label("inlet_pressure") == "Pa"

    inp["inlet_pressure"] = 90001
    assert inp["inlet_pressure"] == "90001 [Pa]"
    assert inp.get_unit_label("inlet_pressure") == "Pa"

    outp = OutputParameters(session)
    assert len(outp) == 1
    assert outp["mass-outlet-op"] == "0.0 [kg/s]"
