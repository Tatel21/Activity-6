from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

      def __init__(self, **kwargs):
          super(LoginScreen, self).__init__(**kwargs)
          self.cols = 2
          self.add_widget(Label(text='User Name'))
          self.username = TextInput(multiline=False)
          self.add_widget(self.username)
          self.add_widget(Label(text='Password'))
          self.password = TextInput(password=True, multiline=False)
          self.add_widget(self.password)


class MyApp(App):

  def build(self):
     return LoginScreen()
if _name_ == 'main':
  MyApp().run()
You sent
from kivy.app import App
from kivy.lang import Builder


root = Builder.load_string('''
FloatLayout:
	canvas.before:
		Color:
			rgba: 0, 0, 255, 0.3
		Rectangle:
		    # self here refers to the widget i.e Floatlayout
		    pos: self.pos
		    size: self.size
	Button:
		text:'hello world'
		size_hint: .5, .5
		pos_hint: {'center_x' :.5, 'center_y': .5}
''')

class MainApp(App):

	def build(self):
		return root

if _name__== '__main_':
	MainApp().run()
