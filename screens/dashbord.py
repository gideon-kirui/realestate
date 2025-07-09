from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.clock import Clock


Builder.load_file("kv/dashboard.kv")

class DashboardScreen(MDScreen):
    def on_kv_post(self, base_widget):
        self.add_vochures_pie_chart()
        self.add_landlords_donut_chart()

    def add_vochures_pie_chart(self):
        # Pie data
        labels = ['Used', 'Unused', 'Expired']
        sizes = [50, 30, 20]
        colors = ['#4CAF50', '#2196F3', '#FF5722']

        # Create the figure
        fig, ax = plt.subplots(figsize=(1.2, 1.2), dpi=100)
        fig.patch.set_facecolor('none')
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')

        # Inject into the layout
        self.ids.vochures_chart_box.add_widget(FigureCanvasKivyAgg(fig))
    
    def add_landlords_donut_chart(self):
        sizes = [60, 25, 15]
        colors = ['#4CAF50', '#FFC107', "#FF1100"]

        fig, ax = plt.subplots(figsize=(2, 2), dpi=100)
        fig.patch.set_facecolor('none')
        wedges, texts, autotexts = ax.pie(
            sizes,
            colors=colors,
            wedgeprops=dict(width=0.4),
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
        self.ids.landlords_donut_box.add_widget(donut)


class CircularProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    bar_color = ListProperty([1,0,100/255])
    bar_width = NumericProperty(10)
    value = NumericProperty(80)
    duration = NumericProperty(1.5)
    text = StringProperty("0%")
    counter = 0

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.duration/self.value)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percent_counter)

class CircularProgressBarRe(AnchorLayout):
    set_valuere = NumericProperty(0)
    bar_colorre = ListProperty([0.937, 0.658, 1.0])
    bar_widthre = NumericProperty(3)
    valuere = NumericProperty(90)
    durationre = NumericProperty(1.5)
    textre = StringProperty("0%")
    counterre = 0

    def __init__(self, **kwargs):
        super(CircularProgressBarRe, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationre/self.valuere)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counterre < self.valuere:
            self.counterre += 1
            self.textre = f"{self.counterre}%"
            self.set_valuere = self.counterre
        else:
            Clock.unschedule(self.percent_counter)

class CircularProgressBarPp(AnchorLayout):
    set_valuepp = NumericProperty(0)
    bar_colorpp = ListProperty([0, 191/255, 255/255])
    bar_widthpp = NumericProperty(3)
    valuepp = NumericProperty(70)
    durationpp = NumericProperty(1.5)
    textpp = StringProperty("0%")
    counterpp = 0

    def __init__(self, **kwargs):
        super(CircularProgressBarPp, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationpp/self.valuepp)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counterpp < self.valuepp:
            self.counterpp += 1
            self.textpp = f"{self.counterpp}%"
            self.set_valuepp = self.counterpp
        else:
            Clock.unschedule(self.percent_counter)

class CircularProgressBarLp(AnchorLayout):
    set_valuelp = NumericProperty(0)
    bar_colorlp = ListProperty([0.0, 0.0, 0.545])
    bar_widthlp = NumericProperty(3)
    valuelp = NumericProperty(86)
    durationlp = NumericProperty(1.5)
    textlp = StringProperty("0%")
    counterlp = 0

    def __init__(self, **kwargs):
        super(CircularProgressBarLp, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationlp/self.valuelp)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counterlp < self.valuelp:
            self.counterlp += 1
            self.textlp = f"{self.counterlp}%"
            self.set_valuelp = self.counterlp
        else:
            Clock.unschedule(self.percent_counter)

class TntsCircularProgressBar(AnchorLayout):
    set_valuetn = NumericProperty(0)
    bar_colortn = ListProperty([0.0, 0.0, 0.545])
    bar_widthtn = NumericProperty(3)
    valuetn = NumericProperty(86)
    durationtn = NumericProperty(1.5)
    texttn = StringProperty("0%")
    countertn = 0

    def __init__(self, **kwargs):
        super(TntsCircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationtn/self.valuetn)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.countertn < self.valuetn:
            self.countertn += 1
            self.texttn = f"{self.countertn}%"
            self.set_valuetn = self.countertn
        else:
            Clock.unschedule(self.percent_counter)

class GraphArea(AnchorLayout):
    graph_type = StringProperty("bar")

    def on_kv_post(self, base_widget):
        self.draw_graph(self.graph_type)

    def draw_graph(self, graph_type):
        self.clear_widgets()
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']

        # Simulated performance data for multiple items
        item_data = {
            'Properties': [100, 70, 45, 8],
            'Rent': [0, 65, 90, 100],
            'tenants': [55, 60, 65, 70],
            '': [55, 60, 65, 70],
        }

        fig, ax = plt.subplots(figsize=(5, 3))
        fig.patch.set_facecolor('none')
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.grid(False)
        ax.tick_params(left=True, bottom=False, labelleft=True, labelbottom=True)

        if graph_type == "line":
            for label, values in item_data.items():
                ax.plot(weeks, values, marker='o', label=label)
            ax.set_ylabel('Performance (%)')
            ax.set_xlabel('Weeks')
            ax.legend()

        elif graph_type == "bar":
            import numpy as np
            x = np.arange(len(weeks))
            width = 0.15

            for i, (label, values) in enumerate(item_data.items()):
                ax.bar(x + i * width, values, width=width, label=label)

            ax.set_xticks(x + width)
            ax.set_xticklabels(weeks)
            ax.set_ylabel('Performance (%)')
            ax.legend()

        elif graph_type == "pie":
            # Sum each item's total performance
            total_performance = {label: sum(values) for label, values in item_data.items()}
            labels = list(total_performance.keys())
            sizes = list(total_performance.values())
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#FF9999', '#66B3FF', '#99FF99'])

        elif graph_type == "donut":
            total_performance = {label: sum(values) for label, values in item_data.items()}
            labels = list(total_performance.keys())
            sizes = list(total_performance.values())
            wedges, texts, autotexts = ax.pie(sizes, wedgeprops=dict(width=0.5), labels=labels, autopct='%1.1f%%')
            ax.set(aspect="equal")

        fig.tight_layout()
        self.add_widget(FigureCanvasKivyAgg(fig))

    def set_graph_type(self, gtype):
        if gtype != self.graph_type:
            self.graph_type = gtype
            self.draw_graph(gtype)