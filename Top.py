#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kivy
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

kivy.require('1.6.0')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from os.path import join, dirname, abspath
from kivy.graphics import Canvas


class ClusterTop(Widget):
    unit = NumericProperty(1.8)
    gas_percentage = BoundedNumericProperty(0, min=0, max=100, errorvalue=0)
    miles_til_empty = BoundedNumericProperty(0, min=0, errorvalue=0)
    oil_pressure = BoundedNumericProperty(0, min=0, max=90, errorvalue=0)

    icon_size = BoundedNumericProperty(30, min=0, max=40, errorvalue=0)
    size_gauge = BoundedNumericProperty(10, min=10, max=30, errorvalue=128)
    size_text = NumericProperty(20)


    icon_status = DictProperty({"popUps": True,  # Done
                                "brights": True,  # Done
                                "leftBlinker": True,  # Done
                                "rightBlinker": True,  # Done
                                })
    path = dirname(abspath(__file__))

    # Gas percentage

    file_gas_tank_off = StringProperty(join(path, "icons/gas-good.png"))
    file_gas_tank_on = StringProperty(join(path, "icons/gas-ehh.png"))
    file_gas_tank_on_low = StringProperty(join(path, "icons/gas-low.png"))

    # Headlights
    file_headlight_on = StringProperty(join(path, "icons/headlight-blue.png"))
    file_headlight_off = StringProperty(join(path, "icons/headlight-gray.png"))
    file_headlight_bright = StringProperty(join(path, "icons/headlight-green.png"))

    # Left Blinker
    file_left_blinker_on = StringProperty(join(path, "icons/left_arrow_green.png"))
    file_left_blinker_off = StringProperty(join(path, "icons/left_arrow_gray.png"))

    # Right Blinker
    file_right_blinker_on = StringProperty(join(path, "icons/right_arrow_green.png"))
    file_right_blinker_off = StringProperty(join(path, "icons/right_arrow_gray.png"))

    # Oil Pressure
    file_oilPressure_off = StringProperty(join(path, "icons/engineOil-off.png"))



    def __init__(self, **kwargs):
        super(ClusterTop, self).__init__(**kwargs)

        # 000000000000000000000000000000000000 Layouts 000000000000000000000000000000000000000
        box = FloatLayout(size=(1800, 30))

        # self._gas_distance_label= BoxLayout(orientation="horizontal", spacing=10, size_hint=(.1, .1), pos=(1500, 470))

        timeLayout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(.1, 1), pos=(0, 470))

        # 000000000000000000000000000000000000 Variables 0000000000000000000000000000000000000
        # Time
        self._time_label = Label(font_size=self.size_text, markup=True)

        # 0000000000 Oil 0000000000
        self._oil_progress_bar = ProgressBar(max=90, height=5, value=self.oil_pressure)

        # For label of oil pressure
        oilLayout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(.05, 1),
            pos=(250, 475)
        )

        # Oil Progress Bar
        self._oilBar_Layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(.1, 1),
            pos=(200, 460)
        )

        self.oil_pressure_label = Label(
            font_size=self.size_text,
            markup=True
        )  # Font size

        # For the icon of the gas tank
        self._oil_pressure = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(1, 1),
            pos=(340, 475)
        )
        self._img_oil_pressure = Image(
            source=self.file_oilPressure_off,
            size=(self.icon_size, self.icon_size)
        )

        # 0000000000 Gas 0000000000
        self._gas_progress_bar = ProgressBar(max=100, height=5, value=self.gas_percentage)

        # For label of miles left
        gasLayout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(.05, 1),
            pos=(1550, 470)
        )

        # Gas Progress Bar
        self._gasBar_Layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(.1, 1),
            pos=(1500, 450)
        )

        self.gas_distance_label = Label(
            font_size=self.size_text,
            markup=True
        )  # Font size

        # For the icon of the gas tank
        self._gas_distance = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(1, 1),
            # pos_hint=(.2, .2)
            pos=(1650, 470)
        )
        self._img_gas_tank = Image(
            source=self.file_gas_tank_off,
            size=(self.icon_size, self.icon_size)
        )

        # 0000000000 Headlights 0000000000
        self._headlights = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(1, 1),
            # pos_hint=(.2, .2)
            pos=(700, 470)
        )
        self._img_headlights = Image(
            source=self.file_headlight_off,
            size=(self.icon_size, self.icon_size)
        )

        # 0000000000 Turn Signal 0000000000

        # 0000000000 Left
        self._left_blinker = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.2, .2),
            # pos_hint=(.2, .2)
            pos=(760, 470)
        )

        self._img_left_blinker = Image(
            source=self.file_left_blinker_off,
            size=(self.icon_size, self.icon_size),
            allow_stretch= True
        )

        #  0000000000 Right
        self._right_blinker = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.2, .2),
            pos=(1085, 470)
        )
        self._img_right_blinker = Image(
            source=self.file_right_blinker_off,
            size=(self.icon_size, self.icon_size)
        )

        # 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        # Pop-ups
        self._headlights.add_widget(self._img_headlights)

        # Blinkers #

        # Left Blinker
        self._left_blinker.add_widget(self._img_left_blinker)

        # Right Blinker
        self._right_blinker.add_widget(self._img_right_blinker)

        # Time
        timeLayout.add_widget(self._time_label)

        # Gas
        self._gas_distance.add_widget(self._img_gas_tank)  # Gas tank icon
        gasLayout.add_widget(self.gas_distance_label) # Label for gas tank
        self._gasBar_Layout.add_widget(self._gas_progress_bar) # Adding widget to bar layout

        # Oil
        self._oil_pressure.add_widget(self._img_oil_pressure)
        oilLayout.add_widget(self.oil_pressure_label)
        self._oilBar_Layout.add_widget(self._oil_progress_bar)


        # 000000000000000000000000000000000 Adding to float layout 000000000000000000000000000000000000000000000000000
        # Oil
        box.add_widget(oilLayout)
        box.add_widget(self._oil_pressure)
        box.add_widget(self._oilBar_Layout)
        # Gas
        # Adding label for miles of gas left
        box.add_widget(gasLayout)
        box.add_widget(self._gas_distance)
        box.add_widget(self._gasBar_Layout)

        # Headlights
        box.add_widget(self._headlights)

        # Adding blinkers
        box.add_widget(self._left_blinker)
        box.add_widget(self._right_blinker)

        # Adding to main widget
        self.add_widget(box)
        # 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        ''' Wee need to bind stuff here to make the data update when stuff is called in the main function'''
        self.bind(gas_percentage=self._turn)
        self.bind(miles_til_empty=self._turn)

    def UpdateGas(self, *args):
        """ Changing the colors of the gas tank
        if gas > 30 icon is white
        if between 10 and 20 it is red orange
        and anything bellow 10 is red
        """
        if self.gas_percentage >= 30:
            self._img_gas_tank.source = self.file_gas_tank_off
        elif 20 >= self.gas_percentage > 11:
            self._img_gas_tank.source = self.file_gas_tank_on
        elif self.gas_percentage <= 10:
            self._img_gas_tank.source = self.file_gas_tank_on_low

    def UpdateLights(self, *args):
        """ Changes the headlights icon if the popups are on,
         but it turns the same icon green if the brights are on """
        if self.icon_status.get('brights') is True:
            self._img_headlights.source = self.file_headlight_bright
        elif self.icon_status.get("popUps") is True and self.icon_status.get('brights') is False:
            self._img_headlights.source = self.file_headlight_on
        else:
            self._img_headlights.source = self.file_headlight_off

    def UpdateLeftBlinker(self, *args):
        """ Causes the left blinker to change color"""
        if self.icon_status.get("leftBlinker") is True:
            self._img_left_blinker.source = self.file_left_blinker_on
        else:
            self._img_left_blinker.source = self.file_left_blinker_off

    def UpdateRightBlinker(self, *args):
        """ Cuases the right blinker to change color"""
        if self.icon_status.get("leftBlinker") is True:
            self._img_right_blinker.source = self.file_right_blinker_on
        else:
            self._img_right_blinker.source = self.file_right_blinker_off

    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.
        '''

        # Gas Updates
        self.gas_distance_label.text = "[b]{0:.0f}[/b] Miles".format(self.miles_til_empty)
        self._gas_progress_bar.value = self.gas_percentage

        # Oil Pressure Updates
        self.oil_pressure_label.text = "[b]{0:.0f}[/b] Lb".format(self.oil_pressure)
        self._oil_progress_bar.value = self.oil_pressure


        # Headlights and blinkers
        self.UpdateGas()
        self.UpdateLights()
        self.UpdateLeftBlinker()
        self.UpdateRightBlinker()


