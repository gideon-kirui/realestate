from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

Builder.load_file("kv/landloards.kv")

class ContainerRight(MDCard):
    pass

class LandLordScreen(MDScreen):

    pass

