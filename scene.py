from manim import *

#class Tape(Scene):
def __init__(self, **kwargs):
    ZoomedScene.__init__(
        self,
        zoom_factor=0.3,
        zoomed_display_height=1,
        zoomed_display_width=6,
        image_frame_stroke_width=20,
        zoomed_camera_config={
            "default_frame_stroke_width": 3,
            },
        **kwargs
    )

class Tape(ZoomedScene):
    def construct(self):

        # coordinate x,y,z and builtins
        #UP == np.array([0, 1, 0])
        #DOWN == np.array([0, -1, 0])
        #LEFT ==  np.array([-1, 0, 0])
        #RIGHT == np.array([1, 0, 0])
        #UL == np.array([-1, 1, 0])
        #DL == np.array([-1, -1, 0])
        #UR == np.array([1, 1, 0])
        #DR == np.array([1, -1, 0])
        TAPE_TOP_LINE_START = (-30,1,0)
        TAPE_TOP_LINE_END =   (30,1,0)
        tapeTopLine = Line(TAPE_TOP_LINE_START,TAPE_TOP_LINE_END);

        TAPE_BOTTOM_LINE_START = (-30,-1,0)
        TAPE_BOTTOM_LINE_END =   (30,-1,0)
        tapeBottomLine = Line(TAPE_BOTTOM_LINE_START,TAPE_BOTTOM_LINE_END);

        tapeLines = VGroup(tapeTopLine, tapeBottomLine)
        self.play(ShowCreation(tapeLines))

        # todo consider using https://docs.manim.community/en/v0.1.1/examples.html#movingframebox
        # for cell head

        # 256 tape cells
        #cells = Tex("0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")

        # 256 tape cells (random binary values)
        cells = Tex("1", "0", "1", "0", "0", "1", "0", "1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "1", "1", "0", "1", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "0", "1", "0", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0"
        )#.scale(1.5)

        for i in range(len(cells)):
            # use labeled color or Hexadecimal color (e.g. "#DC28E2")
            if cells[i].get_tex_string() == "1":
                cells[i].set_color(YELLOW)
            else:
                cells[i].set_color(WHITE)

        self.play(Write(cells))
        self.wait(1)

        # zoom out by shrinking the tape
        tape = VGroup(tapeLines, cells)
        self.play(ScaleInPlace(tape, 0.25))
        self.wait(2)

        zoomed_camera_text = Text("Tape Head", color=PURPLE).scale(.25)
        tape_head_arrow = Text("\u2191", color=PURPLE).scale(.25)
        zoomed_display_text = Text("Zoomed Tape Head View", color=RED).scale(.25)

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        zoomed_camera_frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        zoomed_camera_frame.move_to(cells[128]) # set initial camera focus at origin
        zoomed_camera_frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        zoom_display_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zoom_display_rect)
        unfold_camera = UpdateFromFunc(zoom_display_rect, lambda rect: rect.replace(zoomed_display))
        zoomed_camera_text.next_to(zoomed_camera_frame, DOWN)

        tape_head_arrow.next_to(cells[128], DOWN/4)
        self.play(ShowCreation(zoomed_camera_frame), FadeInFrom(zoomed_camera_text, direction=DOWN))
        self.play(ShowCreation(tape_head_arrow))
        tape_head = VGroup(tape_head_arrow, zoomed_camera_frame)

        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        zoomed_display_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeInFrom(zoomed_display_text, direction=DOWN))

        # remove the zoom text labels
        self.play(FadeOut(zoomed_camera_text))
        #self.play(FadeOut(zoomed_display_text))

        # animate shift zoom camera left over tape
        self.play(tape_head.animate.move_to(cells[0]), run_time=3.0)
        self.wait(2)

        # remove camera
        #self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        #self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        #self.wait()
