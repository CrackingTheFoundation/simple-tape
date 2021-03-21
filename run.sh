#!/bin/bash

# -p indicates play, alternatively -f opens web browser at video location
# -ql is low quality, -qh is high quality, -qk is 4k quality
# -s just does the last frame of the scene
# -a renderes all scenes instead of just the specified scene
# -i renders to gif instead of mp4
python3 -m manim scene.py Tape -pql
