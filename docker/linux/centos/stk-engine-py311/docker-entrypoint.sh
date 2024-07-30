#!/bin/bash
export DISPLAY=':0'
Xvfb ${DISPLAY} +extension GLX -screen 0 1024x768x24 &
bash
