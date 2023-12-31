from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pydub.playback import play
from pydub import AudioSegment
import datetime

time_list = ["00.wav", "01.wav", "02.wav", "03.wav", "04.wav", "05.wav", "06.wav", "07.wav", "08.wav",
             "09.wav", "10.wav", "11.wav", "12.wav", "13.wav", "14.wav", "15.wav", "16.wav", "17.wav",
             "18.wav", "19.wav", "20.wav", "21.wav", "22.wav", "23.wav", "24.wav", "25.wav",
             "26.wav", "27.wav ", "28.wav", "29.wav", "30.wav", "31.wav", "32.wav", "33.wav", "34.wav", "35.wav",
             "36.wav", "37.wav", "38.wav", "39.wav", "40.wav", "41.wav", "42.wav", "43.wav", "44.wav", "45.wav",
             "46.wav", "47.wav", "48.wav", "49.wav", "50.wav", "51.wav", "52.wav", "53.wav", "54.wav", "55.wav",
             "56.wav", "57.wav", "58.wav", "59.wav"]

list_na = [1, 21, 31, 41, 51]
list_ny = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 53, 53, 54]
list_n = []

Window.size = (267, 400)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)


class CatClock(App):
    def __init__(self):
        super().__init__()
        self.button = Button(text='touch me',
                             background_normal="cat.png",
                             on_press=self.btn_press)

    def btn_press(self, *args):
        my_datetime = datetime.datetime.now()
        hours = int(my_datetime.strftime("%H"))
        minutes = int(my_datetime.strftime("%M"))

        if hours in list_na:
            hours_res = AudioSegment.from_mp3("hours_na.wav")
        elif hours in list_ny:
            hours_res = AudioSegment.from_mp3("hours_ny.wav")
        else:
            hours_res = AudioSegment.from_mp3("hours_n.wav")

        if minutes in list_na:
            minutes_res = AudioSegment.from_mp3("minutes_na.wav")
        elif minutes in list_ny:
            minutes_res = AudioSegment.from_mp3("minutes_ny.wav")
        else:
            minutes_res = AudioSegment.from_mp3("minutes_n.wav")

        hours_song = AudioSegment.from_mp3(time_list[hours])
        minutes_song = AudioSegment.from_mp3(time_list[minutes])

        play(hours_song)
        play(hours_res)
        play(minutes_song)
        play(minutes_res)

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.button)
        return box


if __name__ == "__main__":
    CatClock().run()
