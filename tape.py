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
        ).set_color_by_tex("1",YELLOW)

        # points in x,y,z center screen is 0,0
        tapeTopLine = Line(Dot(cells[0].get_center()).shift(UP).shift(cells[0].get_width()*LEFT),Dot(cells[255].get_center()).shift(UP).shift(cells[0].get_width()*RIGHT));
        tapeBottomLine = Line(Dot(cells[0].get_center()).shift(DOWN).shift(cells[0].get_width()*LEFT),Dot(cells[255].get_center()).shift(DOWN).shift(cells[0].get_width()*RIGHT));

        tapeLines = VGroup(tapeTopLine, tapeBottomLine)
        self.play(ShowCreation(tapeLines))

        self.play(Write(cells))
        self.wait(1)

        # zoom out by shrinking the tape
        tape = VGroup(tapeLines, cells)
        TAPE_SHRINK=.25
        self.play(ScaleInPlace(tape, TAPE_SHRINK))
        self.wait(1)
        self.play(tape.animate.to_edge(LEFT))
        self.wait(2)

        zoomed_camera_text = Text("Tape Head", color=PURPLE).scale(TAPE_SHRINK * 1.25)
        tape_head_arrow = Text("\u2191", color=PURPLE).scale(TAPE_SHRINK)
        zoomed_display_text = Text("Zoomed Tape Head View", color=RED).scale(TAPE_SHRINK * 1.25)

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

        # animate shift zoom camera left over tape (rewind tape to first cell)
        self.play(tape_head.animate.move_to(cells[0]), run_time=3)
        #self.add_sound("assets/mixkit-reel-to-reel-fast-forward-1096.wav",gain=-8) # will synch this up in post
        self.wait(2)

        # animate shift zoom camera right over tape
        self.play(tape_head.animate.move_to(cells[64]), run_time=1.5)
        self.wait(1)

        # animate shift zoom camera left over tape (rewind tape to first cell)
        self.play(tape_head.animate.move_to(cells[0]), run_time=1.5)
        self.wait(2)

        # write ABCD\0 to tape cells
        # 01000001 01000010 01000011 01000100 00000000
        data = "0100000101000010010000110100010000000000"
        for i in range(len(data)):
            # simulate charging write head in needed to write data
            if cells[i].get_tex_string() != data[i]:
                tape_head_arrow.set_color(YELLOW)
            # write the data
            value = Tex(data[i]).scale(TAPE_SHRINK).move_to(cells[i]).set_color_by_tex("1",YELLOW)
            tape = VGroup(tapeLines, cells, value)
            self.play(ReplacementTransform(cells[i], value), run_time=.25)
            cells[i].set(tex_string=data[i])
            tape_head_arrow.set_color(PURPLE)
            if i < 255:
                self.play(tape_head.animate.move_to(cells[i+1]), run_time=.25)

        self.play(tape_head.animate.move_to(cells[0]), run_time=1)
        self.wait(2)

        # remove zoom display
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(zoomed_display_text), FadeOut(zoomed_camera_frame))
        self.wait()

        # grow the tape back to being large
        machine_state = VGroup(tape, tape_head_arrow)
        #small_machine_state = machine_state.save_state()
        self.play(ScaleInPlace(machine_state, 1/TAPE_SHRINK), run_time=.25)
        self.play(machine_state.animate.to_edge(LEFT), run_time=.25)
        #large_machine_state = machine_state.save_state()
        self.wait(1)

        byte1 = VGroup(cells[0:8])
        byte1_framebox = SurroundingRectangle(byte1, buff=.1)

        byte2 = VGroup(cells[8:16])
        byte2_framebox = SurroundingRectangle(byte2, buff=.1)

        byte3 = VGroup(cells[16:24])
        byte3_framebox = SurroundingRectangle(byte3, buff=.1)

        byte4 = VGroup(cells[24:32])
        byte4_framebox = SurroundingRectangle(byte4, buff=.1)

        byte5 = VGroup(cells[32:40])
        byte5_framebox = SurroundingRectangle(byte5, buff=.1)

        # create framebox on byte1
        self.play(ShowCreation(byte1_framebox))
        self.wait()

        # convert byte1 to ASCII and move to byte2
        self.play(ReplacementTransform(byte1,Tex("A").move_to(byte1)), tape_head_arrow.animate.next_to(byte1, DOWN))
        self.wait()
        self.play(ReplacementTransform(byte1_framebox,byte2_framebox))
        self.wait()

        # convert byte2 to ASCII and move to byte3
        self.play(ReplacementTransform(byte2,Tex("B").move_to(byte2)))
        self.wait()
        self.play(ReplacementTransform(byte2_framebox,byte3_framebox))
        self.wait()

        # convert byte3 to ASCII and move to byte4
        self.play(ReplacementTransform(byte3,Tex("C").move_to(byte3)))
        self.wait()
        self.play(ReplacementTransform(byte3_framebox,byte4_framebox))
        self.wait()

        # convert byte4 to ASCII and move to byte5
        self.play(ReplacementTransform(byte4,Tex("D").move_to(byte4)))
        self.wait()
        self.play(ReplacementTransform(byte4_framebox,byte5_framebox))
        self.wait()

        # convert byte5 to ASCII
        self.play(ReplacementTransform(byte5,Tex(r"$\backslash 0$").move_to(byte5)))
        self.wait()

        # copy down idea
        #byte1_framebox_copy = byte1_framebox.copy().shift(DOWN)
        #self.play(TransformFromCopy(byte1_framebox, byte1_framebox_copy))
