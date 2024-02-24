from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog


class Gps(BoxLayout):
    my_lat = 0
    my_lon = 0
    def run(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions

            def callback(permission, result):
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print("did not get all permissions")

            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback())

    def update_position(self, *args, **kwargs):
        self.my_lat = kwargs['lat']
        self.my_lon = kwargs['lon']

    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()
    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS ERROR", text="You need to enable gps access!")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y' :.5}
        dialog.open()

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

