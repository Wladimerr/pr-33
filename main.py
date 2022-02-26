from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout

class myApp(App):
    def build(self):
        fl = FloatLayout(size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        fl.add_widget(Button(
            text="Кнопка 1",
            font_size=20,
            on_press=self.btn1_press,
            background_color=[1, 0.5, 0, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}));
        fl.add_widget(Button(
            text="Кнопка 2",
            font_size=20,
            on_press=self.btn2_press,
            background_color=[0.5, 0, 1, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}));
        return fl

    def btn1_press(self, instance):
        instance.text = 'Нажата 1'

    def btn2_press(self, instance):
        instance.text = 'Нажата 2'


if __name__ == "__main__":
    myApp().run()
