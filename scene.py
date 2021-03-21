from manim import *

import random

#class Tape(Scene):
class Tape(MovingCameraScene):
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
        self.play(ShowCreation(tapeTopLine))

        TAPE_BOTTOM_LINE_START = (-30,-1,0)
        TAPE_BOTTOM_LINE_END =   (30,-1,0)
        tapeBottomLine = Line(TAPE_BOTTOM_LINE_START,TAPE_BOTTOM_LINE_END);
        self.play(ShowCreation(tapeBottomLine))

        # seed tape cells with random bits
        #random.seed(42)

        cells = Tex("0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")
        for i in range(len(cells)):
            # use labeled color or Hexadecimal color (e.g. "#DC28E2")
            if cells[i].get_tex_string() == "1":
                cells[i].set_color(YELLOW)
            else:
                cells[i].set_color(WHITE)

        self.play(Write(cells))
        self.wait(1)

        # zoom out by shrinking the tape
        tape = VGroup(tapeTopLine, tapeBottomLine, cells)
        self.play(ScaleInPlace(tape, 0.25))
        self.wait(2)



         # Save the state of camera
        #self.camera.frame.save_state()

        # restore saved camera state
        #self.play(Restore(self.camera.frame))
        #self.wait(2)
