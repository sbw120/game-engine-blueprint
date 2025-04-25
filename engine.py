import time, tkinter as tk, sys, keyboard



window_engine_name = tk.Tk()

window_engine_name.title('engine')
canvas = tk.Canvas(master=window_engine_name, background='white', highlightbackground='white')
canvas.pack()
gravity_rects = []
classic_rects = []
lines = []

class game_screen:
    def __init__(self, screen_frames: int=30, screen_height=500, screen_width=500, screen_color='white'):
        self.screen_frames = screen_frames
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen_color = screen_color
        window_engine_name.geometry(f'{self.screen_width}x{screen_height}')
        window_engine_name.config(background=screen_color)
        canvas.config(background=screen_color, highlightbackground=screen_color, height=screen_height, width=screen_width)


    def quit(self):
        sys.exit()

    def frame(self):

        time.sleep(1 / self.screen_frames)

    def get_width(self=None):
        return screen_width

    def get_height(self=None):
        return screen_height

    def set_frames(self=None, frames=10):
        self.screen_frames = frames


    def update(self):

        for rect in gravity_rects:
            if not rect[1] >= rect[7] and not rect[1] >= rect[7] and not rect[1] + rect[5] >= rect[7]:
                rect[1] += rect[5]
                rect[3] += rect[5]
                rect[5] += rect[6]

            else:
                rect[5] = 0
        canvas.delete('all')




    class set:
        def size(width: int = 500, height: int = 500):
            global screen_width, screen_height
            window_engine_name.geometry(str(width) + 'x' + str(height))
            screen_width = width
            screen_height = height




        def title(title: str = 'engine'):
            window_engine_name.title(title)

        def background(color: str = 'black'):
            screen_color = color
            window_engine_name.config(background=screen_color)
            canvas.config(background=screen_color)


    class get:

        def frames(self):
            global game_screen
            return game_screen.frames

        def size(self=None):
            return screen_width, screen_height

        def background(self=None):
            global screen_color
            return screen_color

        def rects_info(self=None):
            return (gravity_rects, classic_rects)

    class draw:
        def rect(self=None, x1=None, y1=None, x2=None, y2=None, color=None):
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        def all_rects(self=None):
            for c in classic_rects:
                canvas.create_rectangle(c[0], c[1], c[2], c[3], fill=c[4])

            for g in gravity_rects:
                canvas.create_rectangle(g[0], g[1], g[2], g[3], fill=g[4])
        def line(self=None, x1=None, x2=None, y1=None, y2=None, color=None):
            canvas.create_line(x1, y1, x2, y2, fill=color)
        def all_lines(self=None):
            for line in lines:
                canvas.create_line(line[0], line[2], line[1], line[3], fill=line[5], width=line[6])



    class add:
        class rect:
            class graivty_rect:
                def __init__(self, x1, x2, y1, y2, gravity_amount, gravity_acceleration, stopping_y, name=None, color='black'):
                    self.x1 = x1
                    self.x2 = x2
                    self.y1 = y1
                    self.y2 = y2
                    self.color = color
                    self.gravity_amount = gravity_amount
                    self.gravity_acceleration = gravity_acceleration
                    self.stopping_y = stopping_y
                    self.name = name

                def get_y(self):
                    for i in gravity_rects:
                        if i[8] == self.name:
                            return i[1], i[3]

                def get_x(self):
                    for i in gravity_rects:
                        if i[8] == self.name:
                            return i[0], i[2]

                def change_x(self, value):
                    for gravity_rect in gravity_rects:
                        if gravity_rect[8] == self.name:
                            gravity_rect[0] += value
                            gravity_rect[2] += value

                def change_y(self, value):
                    for gravity_rect in gravity_rects:
                        if gravity_rect[8] == self.name:
                            gravity_rect[1] += value
                            gravity_rect[3] += value

                def init_rect(self):
                    gravity_rects.append([self.x1, self.y1, self.x2, self.y2, self.color, self.gravity_amount, self.gravity_acceleration, self.stopping_y, self.name])

            class classic_rect:
                def __init__(self, x1, x2, y1, y2, color='black', name=None):
                    self.x1 = x1
                    self.x2 = x2
                    self.y1 = y1
                    self.y2 = y2
                    self.color = color
                    self.name = name

                def get_y(self):
                    for i in classic_rects:
                        if i[5] == self.name:
                            return i[1], i[3]

                def get_x(self):
                    for i in classic_rects:
                        if i[5] == self.name:
                            return i[0], i[2]

                def change_x(self, value):
                    for classic_rect in classic_rects:
                        if classic_rect[5] == self.name:
                            classic_rect[0] += value
                            classic_rect[2] += value

                def change_y(self, value):
                    for classic_rect in classic_rects:
                        if classic_rect[5] == self.name:
                            classic_rect[1] += value
                            classic_rect[3] += value

                def init_rect(self=None):
                    classic_rects.append([self.x1, self.y1, self.x2, self.y2, self.color, self.name])
        class line:
            def __init__(self, x1, x2, y1, y2, name, color, thickness):
                self.x1 = x1
                self.x2 = x2
                self.y1 = y1
                self.y2 = y2
                self.name = name
                self.color = color
                self.thickness = thickness
            def init_line(self):
                lines.append([self.x1, self.x2, self.y1, self.y2, self.name, self.color, self.thickness])

    class key:
        def is_key_pressed(key=None):
            return keyboard.is_pressed(key)
        def wait_untile_pressed(key=None):
            while True:
                if keyboard.is_pressed(key):
                    break
                else:
                    window_engine_name.update()

    def loop(self):
        window_engine_name.update()
