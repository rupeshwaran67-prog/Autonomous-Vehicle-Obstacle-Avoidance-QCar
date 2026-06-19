# region: package imports
import os
import numpy as np
import math

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar import QLabsQCar
from qvl.free_camera import QLabsFreeCamera
from qvl.real_time import QLabsRealTime
from qvl.animal import QLabsAnimal

# environment objects
from qvl.crosswalk import QLabsCrosswalk
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.yield_sign import QLabsYieldSign
from qvl.traffic_light import QLabsTrafficLight
from qvl.basic_shape import QLabsBasicShape
from qvl.stop_sign import QLabsStopSign
import pal.resources.rtmodels as rtmodels


#endregion

def setup(
        initialPosition=[3.527, 10.122, 2.345],
        initialOrientation=[0, 0, 0],
        rtModel=rtmodels.QCAR
    ):

    # Try to connect to Qlabs
    os.system('cls')
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
        print("Connected to QLabs")
    except:
        print("Unable to connect to QLabs")
        quit()

    # Delete any previous QCar instances and stop any running spawn models
    qlabs.destroy_all_spawned_actors()
    QLabsRealTime().terminate_all_real_time_models()

    # region: QCar spawn description


    # Spawn a QCar at the given initial pose
    hqcar = QLabsQCar(qlabs)
    hqcar.spawn_id(
        actorNumber=0,
        location=[x for x in initialPosition],
        rotation=initialOrientation,
        waitForConfirmation=True
    )

    # Create a new camera view and attach it to the QCar
    hcamera = QLabsFreeCamera(qlabs)
    hcamera.spawn([-10, 2.5, 7],[0, 0.2, 0])
    hqcar.possess()
    # endregion

    cube0 = QLabsBasicShape(qlabs, True)
    
 

# spawn the cubes using radians
    cube0.spawn_id(actorNumber=0, location=[160, 10, 2], rotation=[0,0,0], scale=[3,3,3], configuration=cube0.SHAPE_CUBE, waitForConfirmation=True)
    

    # Start spawn model
    QLabsRealTime().start_real_time_model(rtModel)


    return hqcar


if __name__ == '__main__':
    # XXX Add processing of command line arguments
    setup()