from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform


class Gps(BoxLayout):
    my_lat = 0
    my_lon = 0
    def run(self):
        pass


    def update_position(self, *args, **kwargs):
        self.my_lat = kwargs['lat']
        self.my_lon = kwargs['lon']

    def OnSubmit(self):
      
        if platform == 'android':
            from plyer import gps
            gps.configure(on_location=self.update_position, on_status=self.on_auth_status)
            gps.start(minTime=1000*60*60, minDistance = 1000)
        else:
            self.my_lat = 30
            self.my_lon = 30


        OutputLabel = self.ids.OutputLabel
        OutputLabel.text = f'latlon: {self.my_lat} {self.my_lon}'
        #TextInput.text = ''
        





class MyBoxLayout(BoxLayout):
   def OnSubmit(self):
      TextInput = self.ids.TextInput
      InputText = TextInput.text
      OutputLabel = self.ids.OutputLabel
      OutputLabel.text = InputText
      #TextInput.text = ''



class GPSApp(App):
  def build(self):
     return Gps()

if __name__ == '__main__':
    GPSApp().run()

