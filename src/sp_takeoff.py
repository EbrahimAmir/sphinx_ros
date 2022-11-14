#!/usr/bin/env python

import rospy

import olympe
import os
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing


class TakeOff_Class:

    def __init__(self):
        self.DRONE_IP = os.environ.get("DRONE_IP", "10.202.0.1")



    def test_takeoff(self):
        drone = olympe.Drone(self.DRONE_IP)
        drone.connect()
        assert drone(TakeOff()).wait().success()
        time.sleep(10)
        assert drone(Landing()).wait().success()
        drone.disconnect()


if __name__ == "__main__":

    rospy.init_node('drone_takeoff_node', anonymous=False)
    rospy.loginfo("Takeoff Initiated!")

    take_off = TakeOff_Class()

    take_off.test_takeoff()
