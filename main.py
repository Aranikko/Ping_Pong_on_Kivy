from ssl import SSLEOFError
from time import sleep
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.properties import Clock
from kivy.metrics import dp

class MainWidget(RelativeLayout):
    
    fst_player = None
    sd_player = None
    
    ball = None
    size_ball = dp(50)
    
    # x vector speed
    x_v_s = 5
    # y vector speed
    y_v_s = 5
    
    width_window = 0
    height_window = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_obj()
        
        Clock.schedule_interval(self.update, 1/144)
    
    def init_obj(self):
        with self.canvas:
            self.fst_player = Rectangle(size = (50, 100))
            self.sd_player = Rectangle(size = (50, 100))
            self.ball = Ellipse(size=(self.size_ball, self.size_ball))
    
    def on_size(self, *args):
        self.fst_player.pos = (20, self.center_y-50)
        self.sd_player.pos = (self.width-70, self.center_y-50)
        self.ball.pos = (self.center_x-25, self.center_y-25)
        self.width_window = self.width
        self.height_window = self.height 
        
    def update(self, dt):
        x, y = self.ball.pos
        
        
        x += self.x_v_s
        y += self.y_v_s
        
        self.ball.pos = (x, y)
class Ping_Pong(App):
    pass

Ping_Pong().run()