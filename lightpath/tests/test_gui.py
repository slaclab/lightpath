############
# Standard #
############
import os.path

###############
# Third Party #
###############
import pytest
from PyQt5.QtWidgets import QApplication
from pcdsdevices.sim.pv import using_fake_epics_pv

##########
# Module #
##########
from lightpath.ui import LightApp

@pytest.fixture(scope='module')
def app():
    return QApplication([])

def test_app_buttons(app, lcls):
    lightapp = LightApp(*lcls)
    #Check we initialized correctly
    assert lightapp.upstream()
    assert not lightapp.mps_only()
    #Try to change display
    assert len(lightapp.select_devices('MEC')) == 10

@using_fake_epics_pv
def test_app_from_json(app):
    #Basic configuration
    app = LightApp.from_json(os.path.join(
                             os.path.dirname(os.path.abspath(__file__)),
                             'path.json'))
    assert len(app.light.devices) == 16
    #Limit device search
    app = LightApp.from_json(os.path.join(
                             os.path.dirname(os.path.abspath(__file__)),
                             'path.json'),
                             end=900.0)
    assert len(app.light.devices) == 9