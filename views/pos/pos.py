from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty
from kivy.metrics import dp, sp
from kivy.lang import Builder

Builder.load_file('views/pos/pos.kv')

class Pos(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.render, .1)
    def render(self, _):
        pass 