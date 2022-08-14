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

kivy.require('1.6.0')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from os.path import join, dirname, abspath


class Gauge(Widget):
    '''
    Gauge class
    '''

    unit = NumericProperty(1.8)
    mph = BoundedNumericProperty(0, min=0, max=200, errorvalue=0)
    rpm = BoundedNumericProperty(0, min=0, max=8000, errorvalue=0)
    size_gauge = BoundedNumericProperty(300, min=128, max=600, errorvalue=128)
    size_text = NumericProperty(10)

    # ........................... Images Files.................................
    path = dirname(abspath(__file__))
    file_gauge = StringProperty(join(path, "images/newCadran2.png"))
    file_needle = StringProperty(join(path, "images/needle3.png"))
    file_mx5_logo = StringProperty(join(path, "images/mx5.png"))

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)

        self._gauge = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )

        _img_gauge = Image(
            source=self.file_gauge,
            size=(self.size_gauge, self.size_gauge)
        )

        self._needle = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )

        _img_needle = Image(
            source=self.file_needle,
            size=(self.size_gauge, self.size_gauge)
        )

        self._mx5_logo = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )
        _img_mx5_logo = Image(
            source=self.file_mx5_logo,
            size=(self.size_gauge / 4, self.size_gauge / 4)
        )

        self._glab = Label(font_size=self.size_text, markup=True)  # Font size
        self._MPH = Label(font_size=15, markup=True)  # Font size

        self._progress = ProgressBar(max=200, height=20, value=self.mph)  # may need to change

        self._gauge.add_widget(_img_gauge)
        self._needle.add_widget(_img_needle)

        self._mx5_logo.add_widget(_img_mx5_logo)

        self.add_widget(self._gauge)
        self.add_widget(self._needle)
        self.add_widget(self._MPH)  # just says MPH
        self.add_widget(self._glab)
        self.add_widget(self._mx5_logo)

        self.bind(pos=self._update)
        self.bind(size=self._update)  # delete later
        self.bind(mph=self._turn)
        self.bind(rpm=self._turn)

    def _update(self, *args):
        '''
        Update gauge and needle positions after sizing or positioning.
        '''
        self._gauge.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = self._gauge.center
        self._glab.center_x = self._gauge.center_x
        self._glab.center_y = self._gauge.center_y - 50

        self._mx5_logo.center_x = self._gauge.center_x * 1.25  # Logo
        self._mx5_logo.center_y = self._gauge.center_y * 1.95  # Logo
        self._MPH.center_x = self._gauge.center_x
        self._MPH.center_y = self._gauge.center_y
        # self._progress.x = self._gauge.x
        # self._progress.y = self._gauge.y + (self.size_gauge / 4)
        # self._progress.width = self.size_gauge

    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.
        '''
        self._needle.center_x = self._gauge.center_x
        self._needle.center_y = self._gauge.center_y - 52
        # For needle rotation
        self._needle.rotation = (63 * self.unit) - (self.rpm * self.unit)  # Needle

        self._glab.text = "[b]{0:.0f}[/b]".format(self.mph)  # speed
        self._MPH.text = "MPH"  # text try to move

        self._progress.value = self.mph
