#!/bin/bash

# -p indicates play, alternatively -f opens web browser at video location
# -ql is low quality, -qh is high quality, -qk is 4k quality
# -s just does the last frame of the scene
# -a renderes all scenes instead of just the specified scene
# -i renders to gif instead of mp4

if [[ "$OSTYPE" == "darwin"* ]]; then
	/usr/local/opt/python@3.9/bin/python3.9 -m manim tape.py WhatIsAComputerProgram -qk
	#/usr/local/opt/python@3.9/bin/python3.9 -m manim tape.py TapeIntro -qk
	#/usr/local/opt/python@3.9/bin/python3.9 -m manim tape.py TapeDataRepresentations -qk
else
	python3 -m manim tape.py WhatIsAComputerProgram -qk
	#python3 -m manim tape.py TapeIntro -qk
	#python3 -m manim tape.py TapeDataRepresentations -qk
fi