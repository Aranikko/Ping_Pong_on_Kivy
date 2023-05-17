from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.properties import Clock
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import StringProperty

class MainWidget(RelativeLayout):
    
    fst_player = None
    sd_player = None
    
    ball = None
    size_ball = dp(50)
    
    # x vector speed
    x_v_s = 3
    # y vector speed
    y_v_s = 3
    
    colide_1 = False
    colide_2 = False
    
    lose = False
    restart = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_obj()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        Clock.schedule_interval(self.update, 1/144)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        x1, y1 = self.fst_player.pos
        x2, y2 = self.sd_player.pos
        
        s1, s2 = self.fst_player.size

        if not self.height <= y1 + s2 and keycode[1] == 'w':
            y1 += 50
        elif y1 > 0 and keycode[1] == 's':
            y1 -= 50
        elif not self.height <= y2 + s2 and keycode[1] == 'up':
            y2 += 50
        elif y2 > 0 and keycode[1] == 'down':
            y2 -= 50
        elif self.lose and keycode[1] == 'r':
            self.colide_1 = False
            self.colide_2 = False
    
            self.lose = False
            self.restart = " "
            self.on_size()
        self.fst_player.pos = (x1, y1)
        self.sd_player.pos = (x2, y2)
        return True
    
    def init_obj(self):
        with self.canvas:
            self.fst_player = Rectangle(size = (25, 150))
            self.sd_player = Rectangle(size = (25, 150))
            self.ball = Ellipse(size=(self.size_ball, self.size_ball))
    
    def on_size(self, *args):
        self.fst_player.pos = (20, self.center_y-50)
        self.sd_player.pos = (self.width-70, self.center_y-50)
        self.ball.pos = (self.center_x-25, self.center_y-25) 
        
    def update_pos_ball(self):
        x, y = self.ball.pos
        
        
        x += self.x_v_s
        y += self.y_v_s
        
        if y + self.size_ball > self.height:
            y = self.height - self.size_ball
            self.y_v_s = -self.y_v_s
        
        if self.colide_1:
            x = self.width - self.size_ball - 75
            self.x_v_s = -self.x_v_s
            self.colide_1 = False
        
        if self.colide_2:
            x = 0 + 75
            self.x_v_s = -self.x_v_s
            self.colide_2 = False
            
        if y < 0:
            y = 0
            self.y_v_s = -self.y_v_s
        
        self.ball.pos = (x, y)
    
    def collishion(self, obj1, obj2):
        x1, y1 = obj1.pos
        w1, h1 = obj1.size
        x2 = x1 + w1
        y2 = y1 + h1
        
        x3, y3 = obj2.pos
        w2, h2 = obj2.size
        x4 = x3 + w2
        y4 = y3 + h2
        
        if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
            return True
        else:
            return False
    
    def update_out_ball(self):
        x, y = self.ball.pos
        
        if x - self.size_ball > self.width and not self.colide_1:
            self.lose = True
        
        if x < 0 - self.size_ball and not self.colide_2:
            self.lose = True
    
    def update_lose(self):
        if self.lose:
            self.restart = "Press <R>"
    
    def update(self, dt):
        self.update_pos_ball()
        
        self.update_out_ball()
        
        self.update_lose()
        if self.collishion(self.sd_player, self.ball):
            self.colide_1 = True
        
        if self.collishion(self.fst_player, self.ball):
            self.colide_2 = True
        
class Ping_Pong(App):
    pass

Ping_Pong().run()