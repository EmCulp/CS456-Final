import tkinter as tk
import math

class JarvisVisuals:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("J.A.R.V.I.S. Interface")
        self.root.geometry("600x200")
        self.root.configure(bg='black')

        self.canvas = tk.Canvas(self.root, width=600, height=200, bg='black', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.speaking_animation_id = None
        self.frame = 0
        self.is_listening = False

        self._draw_listening_bars()

    def _draw_listening_bars(self):
        self.canvas.delete("all")
        if self.is_listening:
            bar_color = "yellow"
            bar_height_multiplier = 1.0
        else:
            bar_color = "cyan"
            bar_height_multiplier = 0.5

        center_x = 300
        center_y = 100
        bar_width = 10
        spacing = 15
        num_bars = 5

        for i in range(num_bars):
            base_height = 20*bar_height_multiplier
            pulse = 5*math.sin(self.frame*0.1+i)
            height = base_height+pulse

            base_height = 20 * bar_height_multiplier
            pulse = 5 * math.sin(self.frame * 0.1 + i) 
            height = base_height + pulse
            
            # Calculate position
            x1 = center_x + (i - num_bars // 2) * (bar_width + spacing)
            x2 = x1 + bar_width
            y1 = center_y - height / 2
            y2 = center_y + height / 2
            
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=bar_color, tag="bars")

        self.frame += 1 # Advance frame for animation
        # Re-schedule the update
        self.root.after(100, self._draw_listening_bars)

    def start_speaking_waveform(self):
        if self.speaking_animation_id:
            self.root.after_cancel(self.speaking_animation_id)

        self.is_listening = False
        self.frame = 0
        self._animate_speaking()

    def _animate_speaking(self):
        self.canvas.delete("all")

        width = 600
        height = 200
        points = []

        for x in range(0, width+1, 5):
            amplitude = 30+10*math.sin(self.frame*0.05)
            # y-position centered on canvas
            y = (height/2) + amplitude * math.sin(x * 0.02 + self.frame * 0.1)
            points.append(x)
            points.append(y)
        
        self.canvas.create_line(points, tags="wave", fill="lime green", width=4, smooth=True)

        self.frame += 1

        # Schedules next frame update
        self.speaking_animation_id = self.root.after(50, self._animate_speaking)

    def stop_speaking_waveform(self):
        if self.speaking_animation_id:
            self.root.after_cancel(self.speaking_animation_id)
            self.speaking_animation_id = None
        
        self.canvas.delete("all")
        self.is_listening = True # This flags the listening bars to be more active
        self.frame = 0
        # The main loop for _draw_listening_bars continues running

    def set_listening_mode(self, active=True):
        self.is_listening = active
        self.frame = 0 # Reset frame for immediate, visible change

    def start_gui_loop(self):
        self.root.mainloop()

if __name__ == '__main__':
    visuals = JarvisVisuals()
    visuals.root.after(2000, visuals.start_speaking_waveform)
    visuals.root.after(5000, visuals.stop_speaking_waveform)
    visuals.start_gui_loop()