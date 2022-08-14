#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

'''
Gauge
=====
The :class:`Gauge` widget is a widget for displaying gauge.
.. note::
Source svg file provided for customing.
'''

# __all__ = ('Gauge',)
#
# __title__ = 'garden.gauge'
# __version__ = '0.2'
# __author__ = 'julien@hautefeuille.eu'

import kivy
from kivy.uix.relativelayout import RelativeLayout

kivy.require('1.6.0')
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from Gauge import Gauge
from Top import ClusterTop
from Bottom import ClusterBottom
from SmallGauge import CircularProgressBar

from kivy_garden.mapview import MapView
from kivy.core.window import Window

from datetime import datetime

from helpers.conversions import scaleRpmToGaunge
from helpers.Milage import FuelEfficiency
# Window.size = (1920, 515)
Window.size = (1920, 515)

if __name__ == '__main__':

    class ClusterApp(App):
        # params for gauge
        increasing = NumericProperty(1)
        begin = NumericProperty(50)
        step = NumericProperty(1)
        time_now = datetime.now()
        # For MPG
        gas = FuelEfficiency()

        """ Delete later"""
        testHash = {
                   "popUps" : False,
                   "brights": False,
                   "leftBlinker": False,
                   "rightBlinker":False
            }

        def build(self):
            # 000000000000000000000000000000000000 Layouts 000000000000000000000000000000000000000

            box = RelativeLayout()
            mid = RelativeLayout()

            # 000000000000000000000000000000000000 Variables 0000000000000000000000000000000000000

            self.map = MapView(zoom=10, lat=36, lon=-115, size_hint=(.5, .82), pos_hint={'x': 0, 'center_y': .5})
            self.gauge = Gauge(mph=0, rpm=0,  size_gauge=600, size_text=80, pos_hint={'x': .35, 'y': -.04})
            self.clusterTop = ClusterTop(size_hint=(1, 1), icon_size=40, icon_status= self.testHash)

            # pos_hint = {'right': 1, 'y': 0},
            self.clusterBottom = ClusterBottom(size_hint=(1, .2), icon_size=30, icon_status = {
                                "checkEngine": True,  # Done
                                "brakes": True,  # Done
                                "windshield": True,  # Done
                                "seatBelt": True,  # Done
                                "airBag": True,  # Done
                                "oilPressure": True,
            })

            self.smallGauge = CircularProgressBar(size_hint=(.5, .82), pos=(1600,200))

            # 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000

            box.add_widget(self.clusterTop)
            #
            mid.add_widget(self.map)
            mid.add_widget(self.gauge)
            box.add_widget(self.clusterBottom)

            # Small gauge for something
            box.add_widget(self.smallGauge)

            box.add_widget(mid)

            # 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000

            Clock.schedule_interval(lambda *t: self.gauge_increment(), 1)  # Gauge inc

            return box

        def gauge_increment(self):
            # Begin holds the value
            begin = self.begin
            begin += self.step * self.increasing


            if 0 < begin < 130: # 130
                # sets the gauge value
                self.gauge.mph = begin
                self.gauge.rpm = scaleRpmToGaunge(000) # Change here for RPM
            else:
                self.increasing *= -1

            self.gas.SetCurrentGallons(10)
            self.gas.SetTripMiles(begin*2.5)
            self.clusterTop.gas_percentage = self.gas.GetTankLevel() # For the gas progress bar
            self.clusterTop.miles_til_empty = self.gas.GetMilesTilEmpty() # For the label above the progress bar
            self.clusterTop.oil_pressure = 65







            # ............................................
            if begin % 2 != 0:
                self.clusterTop.icon_status = {
                    "popUps": False,
                    "brights": False,
                    "leftBlinker": False,
                    "rightBlinker": False
                }
            else:
                self.clusterTop.icon_status = {
                        "popUps": False,
                        "brights": False,
                        "leftBlinker": False,
                        "rightBlinker": False
                    }

            # time
            self.clusterBottom.time =  datetime.now().strftime("%I:%M:%S")
            self.clusterBottom.oil_temp = 150
            self.clusterBottom.ambient_temp = 98
            self.clusterBottom.coolant_temp = 200

            self.begin = begin

            # self.clusterTop()


    ClusterApp().run()
