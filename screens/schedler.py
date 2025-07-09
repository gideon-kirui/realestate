from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt


Builder.load_file("kv/schedler.kv")

class PlanSchedlerScreen(MDScreen):
    def on_kv_post(self, base_widget):
        self.add_landlords_donut_chart2()
    
    def add_landlords_donut_chart2(self):
        sizes = [60, 25, 15]
        colors = ['#4CAF50', '#FFC107', "#FF1100"]

        fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
        fig.patch.set_facecolor('none')
        wedges, texts, autotexts = ax.pie(
            sizes,
            colors=colors,
            wedgeprops=dict(width=0.8),
            autopct='%1.1f%%',
            startangle=90,
            pctdistance=0.9 
        )

        for autotext in autotexts:
            autotext.set_color("black")
            autotext.set_fontsize(6)
            autotext.set_fontweight("bold")

        ax.set(aspect="equal")

        donut = FigureCanvasKivyAgg(fig)
        self.ids.landlords_donut_box2.add_widget(donut)