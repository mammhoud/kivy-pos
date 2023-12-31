from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.properties import ColorProperty, ListProperty

from kivy.metrics import dp, sp

Builder.load_string("""
<FlatField>:
    padding: [dp(6), (self.height - self.line_height)/2]
""")
class FlatField(TextInput):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.background_normal = ""
        self.background_active = ""
        self.background_disabled = ""
        self.background_color = [0,0,0,0]
        self.write_tab = False



class TextField(FlatField):
    bcolor = ColorProperty([0,0,0,1])
    main_color = ColorProperty([1,1,1,1])
    radius = ListProperty([1])
    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            self.border_color = Color(rgba=self.bcolor)
            self.border_draw = RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
            self.back_color = Color(rgba=self.main_color)
            self.back_draw = RoundedRectangle(
                pos=[self.pos[0]+1.5, self.pos[1]+1.5], 
                size=[self.size[0]-3, self.size[1]-3], 
                radius=self.radius
                )

        self.bind(size=self.update)
        self.bind(pos=self.update)

    def on_main_color(self, inst, value):
        self.back_color.rgba = value

    def on_bcolor(self, inst, value):
        self.border_color.rgba = value

    def update(self, *args):
        self.border_draw.pos = self.pos
        self.border_draw.size = self.size

        self.back_draw.pos=[self.pos[0]+1.5, self.pos[1]+1.5] 
        self.back_draw.size=[self.size[0]-3, self.size[1]-3]

    def on_radius(self, *args): 
        self.back_draw.radius=self.radius
        self.border_draw.radius=self.radius

class OutlineTextField(FlatField):
    bcolor = ColorProperty([0,0,0,1])
    main_color = ColorProperty([1,1,1,1])
    radius = ListProperty([1])
    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            self.border_color = Color(rgba=self.bcolor)
            self.border_draw = Line(
                width=dp(1.5),
                rounded_rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1], self.radius[0]]
            )
            # self.border_draw = RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
            # self.back_color = Color(rgba=self.main_color)
            # self.back_draw = RoundedRectangle(
            #     pos=[self.pos[0]+1.5, self.pos[1]+1.5], 
            #     size=[self.size[0]-3, self.size[1]-3], 
            #     radius=self.radius
            #     )

        self.bind(size=self.update)
        self.bind(pos=self.update)

    def on_main_color(self, inst, value):
        self.back_color.rgba = value

    def on_bcolor(self, inst, value):
        self.border_color.rgba = value

    def update(self, *args):
        self.border_draw.rounded_rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1], self.radius[0]]

    def on_radius(self, *args): 
        self.border_draw.rounded_rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1], self.radius[0]]
        
        
        
        
class SearchBar(FlatField):
    choices = ListProperty(['Product 1','Product 2', 'product 3'])
    def __init__(self, **kw):
        super().__init__(**kw)
        self.multiline= False
        self.dropdown=None
    def on_text(self, inst, text):
        try:
            
            if self.dropdown:
                self.dropdown.dismiss()
                self.dropdown = None
                
            self.show_suggestions(text)
            
        except:
            pass
        
    
    
    
    def keyboard_on_key_down(self, window,kc, text, modifiers):
        #if kc[0] == ord("\r"):
            #self.text= self.values[0]
            
        if self.dropdown:
            self.dropdown.dismiss()
            self.dropdown = None
            
                
        else:
            super().keyboard_on_key_down(window,kc,text,modifiers)
    def show_suggesitons(self, suggestions: str):
        try: 
            self.dropdown = DropDown()
            self.dropdown.autowidth= False
            self.dropdown.size_hint_x = None
            self.dropdown.width = Window.width*.4
            
            x:int = 0
            
            for c in self.choices:
                b= Button()
                b.text = c
                b.size_hint_y = None
                b.height = dp(54)
                
                self.dropdown.add_width(b)
                
                x+= 1
                
                if x> 0:
                    self.dropdown.open(self)
        except:
            pass
                        
    def open_dropdown(self, *args):
        if self.dropdown:
            self.dropdown.open(self)
            
    