#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kivy

from kivy.uix.floatlayout import FloatLayout

kivy.require('1.6.0')

from kivy.properties import NumericProperty, DictProperty
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from os.path import join, dirname, abspath


class ClusterBottom(Widget):
    unit = NumericProperty(1.8)
    value = BoundedNumericProperty(10, min=0, max=113, errorvalue=0)
    coolant_temp = BoundedNumericProperty(80, min=0, max=240, errorvalue=0)
    ambient_temp = BoundedNumericProperty(10, min=0, max=150, errorvalue=0)
    oil_temp = BoundedNumericProperty(80, min=0, max=250, errorvalue=0)

    time = StringProperty("time")
    icon_size = NumericProperty(30)
    text_size_temp = NumericProperty(20)

    icon_status = DictProperty({"checkEngine": True,  # Done
                                "brakes": True,  # Done
                                "windshield": True,  # Done
                                "seatBelt": True,  # Done
                                "airBag": True,  # Done
                                "oilPressure": True
                                })

    path = dirname(abspath(__file__))
    # Temp
    file_temp_off = StringProperty(join(path, "icons/temp-off.png"))
    file_temp_on = StringProperty(join(path, "icons/temp-on.png"))
    file_temp = file_temp_off

    # Ambient Temp
    file_ambient_temp = StringProperty(join(path, "icons/ambient_temp2.png"))

    # Oil Temp
    file_oil_temp = StringProperty(join(path, "icons/oil_temp.png"))

    # Check Engine
    file_checkEngine_on = StringProperty(join(path, "icons/checkEngine-on.png"))
    file_checkEngine_off = StringProperty(join(path, "icons/checkEngine-off.png"))
    file_checkEngine = file_checkEngine_on

    # Brakes
    file_brakes_on = StringProperty(join(path, "icons/brakeWarning_on.png"))
    file_brakes_off = StringProperty(join(path, "icons/brakeWarning-off.png"))
    file_brakes = file_brakes_on

    # Windshield washer
    file_ws_fluid_on = StringProperty(join(path, "icons/washerFluid-on.png"))
    file_ws_fluid_off = StringProperty(join(path, "icons/washerFluid_off.png"))
    file_ws = file_ws_fluid_on

    # Seatbelt
    file_seatbelt_on = StringProperty(join(path, "icons/seatBeltWarning-on.png"))
    file_seatbelt_off = StringProperty(join(path, "icons/seatBeltWarning-off.png"))
    file_seatbelt = file_seatbelt_on

    # Airbag
    file_airbag_on = StringProperty(join(path, "icons/airBagWarning-on.png"))
    file_airbag_off = StringProperty(join(path, "icons/airBagWarning-off.png"))
    file_airbag = file_airbag_on

    # Oil Pressure Low
    file_oilPressure_on = StringProperty(join(path, "icons/engineOil-on.png"))
    file_oilPressure_off = StringProperty(join(path, "icons/engineOil-off.png"))
    file_oilPressure = file_oilPressure_on

    size_gauge = BoundedNumericProperty(300, min=128, max=600, errorvalue=128)
    size_text = NumericProperty(30)

    def __init__(self, **kwargs):
        super(ClusterBottom, self).__init__(**kwargs)
        # 000000000000000000000000000000000000 Layouts 000000000000000000000000000000000000000

        # make sure to set the pos_hint
        # box = BoxLayout(orientation='horizontal', spacing=100, size=(1800, 40), size_hint=(1, None))
        box = FloatLayout(size=(1800, 30))
        warningLayout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            # size=(60, 30),
            size_hint=(.3, .1),
            pos=(1300, 60)
        )

        # Time
        timeLayout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(.1, 1), pos=(725, 10))

        # 000000000000000000000000000000000000 Variables 0000000000000000000000000000000000000

        # ..................................... Time .............................................
        self._time_label = Label(font_size=self.size_text - 5, markup=True)

        # ..................................... Oil .............................................

        # Holds the label that show the number of temperature
        oilTempLayout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size=(50, 30),
            size_hint=(.05, .1),
            pos=(1550, 20)
        )

        self._oil_temp_label = Label(font_size=self.text_size_temp, markup=True, text="--- C")  # Font size

        # Ambient temp Icon
        self._check_oil_temp = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1650, 8)
        )
        _img_oil_temp = Image(source=self.file_oil_temp, size=(self.icon_size, self.icon_size))

        #  Oil Temp Progress Bar
        self._oil_temp_progress_bar = ProgressBar(max=250, height=10, value=self.oil_temp)

        # Holds the progress bar for the coolant temperature
        self._oil_temp_bar_Layout = BoxLayout(
            orientation='horizontal',
            size_hint=(.1, 1),
            pos=(1500, 25)
        )

        # ..................................... Ambient.............................................

        # Holds the label that show the number of temperature
        ambientTempLayout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size=(50, 30),
            size_hint=(.05, .1),
            pos=(1000, 20)
        )

        self._ambient_temp_label = Label(font_size=self.text_size_temp, markup=True, text="--- C")  # Font size

        # Ambient temp Icon
        self._check_ambient_temp = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1100, 8)
        )
        _img_ambient_temp = Image(source=self.file_ambient_temp, size=(self.icon_size, self.icon_size))

        # .............................. Coolant ....................................................
        # Holds the label that show the number of temperature
        self.coolantTempLayout = BoxLayout(
            orientation='horizontal',
            spacing=10,

            size_hint=(.05, .1),
            pos=(250, 20)
        )

        self._coolant_temp_label = Label(font_size=self.text_size_temp, markup=True, text="--- C")  # Font size

        # Coolant temp Icon
        self._check_coolant_temp = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(340, 8)
        )
        _img_temp = Image(source=self.file_temp, size=(self.icon_size, self.icon_size))

        # Coolant Temp Progress Bar
        self._coolant_temp_progress_bar = ProgressBar(max=250, height=10, value=self.coolant_temp)

        # Holds the progress bar for the coolant temperature
        self._temp_bar_Layout = BoxLayout(
            orientation='horizontal',
            size_hint=(.1, 1),
            pos=(200, 25)
        )
        # .........

        # Check Engine Light
        if self.icon_status.get("checkEngine") is True:
            self.file_checkEngine = self.file_checkEngine_on
        else:
            self.file_checkEngine = self.file_checkEngine_off

        self._check_engine_warning = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1085, 470)
        )

        _img_checkEngine = Image(source=self.file_checkEngine, size=(self.icon_size, self.icon_size))

        # Brakes Light
        if self.icon_status.get("brakes") is True:
            self.file_brakes = self.file_brakes_on
        else:
            self.file_brakes = self.file_brakes_off

        self._check_brakes_warning = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1085, 470)
        )
        _img_brakes = Image(source=self.file_brakes, size=(self.icon_size, self.icon_size))

        # Windshield Fluid Light
        if self.icon_status.get("windshield") is True:
            self.file_ws = self.file_ws_fluid_on
        else:
            self.file_ws = self.file_ws_fluid_off

        self._check_ws_warning = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1085, 470)
        )
        _img_ws_fluid = Image(source=self.file_ws, size=(self.icon_size, self.icon_size))

        # Seatbelt Light
        if self.icon_status.get("seatBelt") is True:
            self.file_seatbelt = self.file_seatbelt_on
        else:
            self.file_seatbelt = self.file_seatbelt_off

        self._check_seatbelt_warning = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1085, 470)
        )
        _img_seatBelt = Image(source=self.file_seatbelt, size=(self.icon_size, self.icon_size))

        # Airbag Light
        if self.icon_status.get("airBag") is True:
            self.file_airbag = self.file_airbag_on
        else:
            self.file_airbag = self.file_airbag_off

        self._check_airbag_warning = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1085, 470)
        )

        _img_airbag = Image(source=self.file_airbag, size=(self.icon_size, self.icon_size))

        # Oil Pressure Light
        if self.icon_status.get("oilPressure") is True:
            self.file_oilPressure = self.file_oilPressure_on
        else:
            self.file_oilPressure = self.file_oilPressure_off

        self._check_oil_pressure_warning = Scatter(
            size=(self.icon_size, self.icon_size),
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            size_hint=(.1, .1),
            pos=(1085, 470)
        )

        _img_oil_pressure = Image(source=self.file_oilPressure, size=(self.icon_size, self.icon_size))

        # 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        # Time
        timeLayout.add_widget(self._time_label)

        # 000000000000000000 Adding to Layouts 000000000000000000000000000000000000000000000000
        # Adding to oil temp Layout
        self._oil_temp_bar_Layout.add_widget(self._oil_temp_progress_bar)
        self._check_oil_temp.add_widget(_img_oil_temp)
        oilTempLayout.add_widget(self._oil_temp_label)

        # Adding to Ambient temp Layout
        self._check_ambient_temp.add_widget(_img_ambient_temp)
        ambientTempLayout.add_widget(self._ambient_temp_label)

        # Adding to the self.coolantTempLayout
        self._temp_bar_Layout.add_widget(self._coolant_temp_progress_bar)

        self._check_coolant_temp.add_widget(_img_temp)
        self.coolantTempLayout.add_widget(self._coolant_temp_label)

        # 000000000000000000 Warning Lights 000000000000000000000000000000000000000000000000
        # Check Engine
        self._check_engine_warning.add_widget(_img_checkEngine)

        # Check Brakes
        self._check_brakes_warning.add_widget(_img_brakes)

        # Check Windshield Fluid
        self._check_ws_warning.add_widget(_img_ws_fluid)

        # Check Seatbelt
        self._check_seatbelt_warning.add_widget(_img_seatBelt)

        # Check Airbag
        self._check_airbag_warning.add_widget(_img_airbag)

        # Check Oil
        self._check_oil_pressure_warning.add_widget(_img_oil_pressure)

        # Adding to warning lights section
        warningLayout.add_widget(self._check_engine_warning)
        warningLayout.add_widget(self._check_brakes_warning)
        warningLayout.add_widget(self._check_ws_warning)
        warningLayout.add_widget(self._check_seatbelt_warning)
        warningLayout.add_widget(self._check_airbag_warning)
        warningLayout.add_widget(self._check_oil_pressure_warning)

        # 000000000000000000 Adding to Main 000000000000000000000000000000000000000000000000000

        # Coolant
        box.add_widget(self._temp_bar_Layout)
        box.add_widget(self._check_coolant_temp)
        box.add_widget(self.coolantTempLayout)

        # Ambient
        box.add_widget(ambientTempLayout)
        box.add_widget(self._check_ambient_temp)

        # Oil
        box.add_widget(self._oil_temp_bar_Layout)
        box.add_widget(self._check_oil_temp)
        box.add_widget(oilTempLayout)

        box.add_widget(warningLayout)

        # Time
        box.add_widget(timeLayout)

        self.add_widget(box)
        # 0000000000000000000000000000000000 Binding 0000000000000000000000000000000000000000000000
        self.bind(coolant_temp=self._turn)
        self.bind(ambient_temp=self._turn)
        self.bind(oil_temp=self._turn)
        self.bind(time=self._turn)

    def _update(self, *args):
        '''
        Update gauge and needle positions after sizing or positioning.
        '''

    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.
        '''

        # Coolant Temp Update
        self._coolant_temp_label.text = "[b]{0:.0f}[/b] C".format(self.coolant_temp)
        self._coolant_temp_progress_bar.value = self.coolant_temp
        # Ambient Temp Update
        self._ambient_temp_label.text = "[b]{0:.0f}[/b] C".format(self.ambient_temp)
        # Oil Temp Update
        self._oil_temp_label.text = "[b]{0:.0f}[/b] C".format(self.oil_temp)
        self._oil_temp_progress_bar.value = self.oil_temp

        # TIME
        self._time_label.text = self.time
