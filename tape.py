from manim import *

class WhatIsAComputerProgram(ZoomedScene):
    def construct(self):

        question=Tex("What is a computer program?")
        self.add(question)
        self.wait(2)

        self.play(question.animate.shift(2*UP))

        trailingThought=Tex("and...")
        trailingThought.next_to(question,DOWN)
        self.add(trailingThought)

        followUp=Text("")
        followUp.next_to(trailingThought,DOWN)
        self.add(followUp)

        self.play(Transform(followUp,Tex("What makes them so vulnerable?")))
        self.wait(2)

        self.play(Transform(followUp,Tex("What makes them so buggy?")))
        self.wait(2)

        self.play(Transform(followUp,Tex("What makes them so complex?")))
        self.wait(2)

        self.play(FadeOut(VGroup(question, trailingThought, followUp)))

class TapeIntro(ZoomedScene):
    def construct(self):

        # 256 tape cells (random(42) binary values)
        cells = Tex("1", "0", "1", "0", "0", "1", "0", "1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "1", "1", "0", "1", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "0", "1", "0", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0"
        ).set_color_by_tex("1",YELLOW)

        # create tape with cells
        tape_top_line = Line(Dot(cells[0].get_center()).shift(UP).shift(cells[0].get_width()*LEFT),Dot(cells[255].get_center()).shift(UP).shift(cells[0].get_width()*RIGHT));
        tape_bottom_line = Line(Dot(cells[0].get_center()).shift(DOWN).shift(cells[0].get_width()*LEFT),Dot(cells[255].get_center()).shift(DOWN).shift(cells[0].get_width()*RIGHT));
        tape_lines = VGroup(tape_top_line, tape_bottom_line)
        tape = VGroup(tape_lines, cells)
        self.play(ShowCreation(tape_lines))
        self.play(Write(cells))
        self.wait(1)

        # zoom out by shrinking the tape
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

        # draw tape cells...these are way too tight
        #tape_cell_lines = VGroup()
        #for i in range(0,3):
        #    tape_cell_lines.add(Line(Dot(tape_top_line.get_start()).shift(RIGHT*cells[i].get_width()), Dot(tape_bottom_line.get_start()).shift(RIGHT*cells[i].get_width()), stroke_width=tape_top_line.get_stroke_width()))
        #self.play(ShowCreation(tape_cell_lines),run_time=1)

        # ask value of cell[63]
        symbol_at_question1 = Tex(r"What is the $64^{th}$ symbol on the tape?").to_edge(LEFT).shift(UP*3)
        self.play(FadeInFrom(symbol_at_question1, direction=LEFT))
        ATTENTION=4
        self.play(ScaleInPlace(cells[63], ATTENTION))
        self.play(WiggleOutThenIn(cells[63], run_time=2))
        symbol_at_question2 = Tex(r"What is the symbol at tape cell 63?").to_edge(LEFT).shift(UP*2)
        self.play(TransformFromCopy(symbol_at_question1,symbol_at_question2))
        self.play(WiggleOutThenIn(cells[63], run_time=2))
        symbol_at_question3 = Tex(r"What is the symbol at $tape[63]$?").to_edge(LEFT).shift(UP)
        self.play(TransformFromCopy(symbol_at_question2,symbol_at_question3))
        self.play(WiggleOutThenIn(cells[63], run_time=2))

        # show tape cell indexer
        tape_cell_indexer = Tex("Tape Head: $tape[0]=1$").to_edge(LEFT).shift(DOWN)
        self.play(ShowCreation(tape_cell_indexer),run_time=1)

        # animate shift zoom camera right over tape
        for i in range(1,64):
            self.play(tape_head.animate.move_to(cells[i]), run_time=.05)
            tape_cell_indexer.become(Tex("Tape Head: $tape[" + str(i) + "]=" + cells[i].get_tex_string() + "$").to_edge(LEFT).shift(DOWN))

        self.play(WiggleOutThenIn(cells[63], run_time=2))
        self.play(ScaleInPlace(cells[63], 1/ATTENTION))

        symbol_at_questions = VGroup(symbol_at_question1, symbol_at_question2, symbol_at_question3)
        self.play(FadeOut(symbol_at_questions))

        # notice cell 0
        self.play(ScaleInPlace(cells[0], ATTENTION, run_time=.5))
        self.play(WiggleOutThenIn(cells[0], run_time=1))
        self.play(ScaleInPlace(cells[0], 1/ATTENTION, run_time=.5))

        # animate shift zoom camera left over tape (rewind tape to first cell)
        for i in reversed(range(0,63)):
            self.play(tape_head.animate.move_to(cells[i]), run_time=.025)
            tape_cell_indexer.become(Tex("Tape Head: $tape[" + str(i) + "]=" + cells[i].get_tex_string() + "$").to_edge(LEFT).shift(DOWN))
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
            tape_cell_indexer.become(Tex("Tape Head: $tape[" + str(i) + "]=" + data[i] + "$").to_edge(LEFT).shift(DOWN))
            self.play(ReplacementTransform(cells[i], value), run_time=.25)
            tape_head_arrow.set_color(PURPLE)
            self.wait(.25) # make writes take just a little longer
            if i < 255:
                self.play(tape_head.animate.move_to(cells[i+1]), run_time=.025)
                tape_cell_indexer.become(Tex("Tape Head: $tape[" + str(i+1) + "]=" + cells[i+1].get_tex_string() + "$").to_edge(LEFT).shift(DOWN))
                #self.wait(1) #slow down for debug

        for i in reversed(range(0,39)):
            self.play(tape_head.animate.move_to(cells[i]), run_time=.025)
            tape_cell_indexer.become(Tex("Tape Head: $tape[" + str(i) + "]=" + data[i] + "$").to_edge(LEFT).shift(DOWN))
        self.wait(2)

        # prep for next scene
        self.play(FadeOut(tape_cell_indexer))

        # remove zoom display
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(zoomed_display_text), FadeOut(zoomed_camera_frame))
        self.wait()

class TapeDataRepresentations(ZoomedScene):
    def construct(self):

        # 256 tape cells (ABCD\0 followed by random(42) binary values)
        cells = Tex("0", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "1", "1", "0", "1", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "0", "1", "0", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0"
        ).set_color_by_tex("1",YELLOW)

        # points in x,y,z center screen is 0,0
        tape_top_line = Line(Dot(cells[0].get_center()).shift(UP).shift(cells[0].get_width()*LEFT),Dot(cells[255].get_center()).shift(UP).shift(cells[0].get_width()*RIGHT));
        tape_bottom_line = Line(Dot(cells[0].get_center()).shift(DOWN).shift(cells[0].get_width()*LEFT),Dot(cells[255].get_center()).shift(DOWN).shift(cells[0].get_width()*RIGHT));

        tape_lines = VGroup(tape_top_line, tape_bottom_line)
        tape = VGroup(tape_lines, cells)

        tape_head_arrow = Text("\u2191", color=PURPLE).next_to(cells[0], DOWN)
        machine_state = VGroup(tape, tape_head_arrow)

        TAPE_SHRINK=.25
        machine_state.scale(TAPE_SHRINK)
        machine_state.to_edge(LEFT)
        self.add(machine_state)

        # grow the tape back to being large
        self.play(ScaleInPlace(machine_state, 1/TAPE_SHRINK), run_time=.75)
        self.play(machine_state.animate.to_edge(LEFT), run_time=.25)
        self.wait(1)

        byte1 = VGroup(cells[0:8])
        byte1_framebox = SurroundingRectangle(byte1, buff=.06)

        byte2 = VGroup(cells[8:16])
        byte2_framebox = SurroundingRectangle(byte2, buff=.06)

        byte3 = VGroup(cells[16:24])
        byte3_framebox = SurroundingRectangle(byte3, buff=.06)

        byte4 = VGroup(cells[24:32])
        byte4_framebox = SurroundingRectangle(byte4, buff=.06)

        byte5 = VGroup(cells[32:40])
        byte5_framebox = SurroundingRectangle(byte5, buff=.06)

        # create framebox on byte1
        self.play(ShowCreation(byte1_framebox))
        self.wait()

        # convert byte1 to ASCII and move to byte2
        symbol_A = Tex("A").move_to(byte1)
        self.play(ReplacementTransform(byte1,symbol_A), tape_head_arrow.animate.next_to(byte1, DOWN))
        self.wait()
        self.play(ReplacementTransform(byte1_framebox,byte2_framebox))
        self.wait()

        # convert byte2 to ASCII and move to byte3
        symbol_B = Tex("B").move_to(byte2)
        self.play(ReplacementTransform(byte2,symbol_B))
        self.wait()
        self.play(ReplacementTransform(byte2_framebox,byte3_framebox))
        self.wait()

        # convert byte3 to ASCII and move to byte4
        symbol_C = Tex("C").move_to(byte3)
        self.play(ReplacementTransform(byte3,symbol_C))
        self.wait()
        self.play(ReplacementTransform(byte3_framebox,byte4_framebox))
        self.wait()

        # convert byte4 to ASCII and move to byte5
        symbol_D = Tex("D").move_to(byte4)
        self.play(ReplacementTransform(byte4,symbol_D))
        self.wait()
        self.play(ReplacementTransform(byte4_framebox,byte5_framebox))
        self.wait()

        # convert byte5 to ASCII
        symbol_0 = Tex(r"$\backslash 0$").move_to(byte5)
        self.play(ReplacementTransform(byte5,symbol_0))
        self.wait()

        self.play(FadeOut(VGroup(machine_state, symbol_A, symbol_B, symbol_C, symbol_D, symbol_0, byte5_framebox)))

        # copy down idea
        #byte1_framebox_copy = byte1_framebox.copy().shift(DOWN)
        #self.play(TransformFromCopy(byte1_framebox, byte1_framebox_copy))
