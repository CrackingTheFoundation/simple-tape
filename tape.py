from manim import *

class WhatIsAComputerProgram(ZoomedScene):
    def construct(self):

        question=Text("What is a computer program?")
        self.add(question)
        self.wait(2)

        self.play(question.animate.shift(2*UP))

        trailingThought=Text("and...")
        trailingThought.next_to(question,DOWN)
        self.add(trailingThought)

        followUp=Text("")
        followUp.next_to(trailingThought,DOWN)
        self.add(followUp)

        self.play(Transform(followUp,Text("What makes them so vulnerable?")))
        self.wait(2)

        self.play(Transform(followUp,Text("What makes them so buggy?")))
        self.wait(2)

        self.play(Transform(followUp,Text("What makes them so complex?")))
        self.wait(2)

class TapeIntro(ZoomedScene):
    def construct(self):

        # 256 tape cells (random binary values)
        cells = Tex("1", "0", "1", "0", "0", "1", "0", "1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "1", "1", "0", "1", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "0", "1", "0", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0"
        )
        cells.set_color_by_tex("1",YELLOW)
        #for i in range(len(cells)):
        #    # use labeled color or Hexadecimal color (e.g. "#DC28E2")
        #    if cells[i].get_tex_string() == "1":
        #        cells[i].set_color(YELLOW)
        #    else:
        #        cells[i].set_color(WHITE)

        # points in x,y,z center screen is 0,0
        tapeTopLine = Line(Dot(cells[0].get_center()).shift(UP),Dot(cells[255].get_center()).shift(UP));
        tapeBottomLine = Line(Dot(cells[0].get_center()).shift(DOWN),Dot(cells[255].get_center()).shift(DOWN));

        tapeLines = VGroup(tapeTopLine, tapeBottomLine)
        self.play(ShowCreation(tapeLines))

        self.play(Write(cells))
        self.wait(1)

        # zoom out by shrinking the tape
        tape = VGroup(tapeLines, cells)
        self.play(ScaleInPlace(tape, 0.25))
        self.wait(2)

        zoomed_camera_text = Text("Tape Head", color=PURPLE).scale(.25)
        tape_head_arrow = Text("\u2191", color=PURPLE).scale(.25)
        zoomed_display_text = Text("Zoomed Tape Head View", color=RED).scale(.25)

        # construct zoomed camera and a display frame
        # reference https://docs.manim.community/en/v0.1.1/examples.html#movingframebox
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        zoomed_camera_frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        # set initial camera focus at center cell and construct the tape head and zoom display windows
        zoomed_camera_frame.move_to(cells[128])
        zoomed_camera_frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)
        zoom_display_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zoom_display_rect)
        unfold_camera = UpdateFromFunc(zoom_display_rect, lambda rect: rect.replace(zoomed_display))
        zoomed_camera_text.next_to(zoomed_camera_frame, DOWN)

        # initially put the tape head at the center cell and start the zoom display
        tape_head_arrow.next_to(cells[128], DOWN/4)
        self.play(ShowCreation(zoomed_camera_frame), FadeInFrom(zoomed_camera_text, direction=DOWN))
        self.play(ShowCreation(tape_head_arrow))
        tape_head = VGroup(tape_head_arrow, zoomed_camera_frame)
        self.activate_zooming()

        # animate the zoom display pop out
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        zoomed_display_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeInFrom(zoomed_display_text, direction=DOWN))

        # remove the zoom camera text label before moving
        self.play(FadeOut(zoomed_camera_text))

        # animate shift zoom camera left over tape (rewind tape to first cell
        self.play(tape_head.animate.move_to(cells[0]), run_time=3)
        #self.add_sound("assets/mixkit-reel-to-reel-fast-forward-1096.wav",gain=-8) # will synch this up in post
        self.wait(2)

        # todo consider using https://docs.manim.community/en/v0.1.1/examples.html#movingframebox
        # to show binary values can form arbitrary symbols

        blank_cells = Tex("0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"
        ).scale(.25)

        self.play(ReplacementTransform(cells, blank_cells))
        self.wait(2)

        # remove camera display
        #self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        #self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        #self.wait()
