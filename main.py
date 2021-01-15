from kivy.app import App

from kivy.uix.camera import Camera

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

 

class CameraExample(App):

 

    def build(self):

        layout = BoxLayout(orientation='vertical')

       

        # create a camera object

        self.cameraObject            = Camera(play=False)

        self.cameraObject.play       = True

        self.cameraObject.resolution = (300, 300) # Define resolution

       

        # button for taking photograph( can also be defined in kv file )  

        self.camaraClick = Button(text="capture")

        self.camaraClick.size_hint=(.5, .2)

        self.camaraClick.pos_hint={'x': .25, 'y':.75}

 

       

        self.camaraClick.bind(on_press=self.onCameraClick)

       

     
        layout.add_widget(self.cameraObject)

        layout.add_widget(self.camaraClick)

       

       

        return layout

 

    # current frame of the video as the photograph       

    def onCameraClick(self, *args):

        self.cameraObject.export_to_png('selfie_{}.jpg')

       

       


if __name__ == '__main__':

     CameraExample().run() 