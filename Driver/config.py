#!/usr/bin/env python3
import os
import numpy as np
import qualityTdModel
import qualityFdModel
import hrFDModel
import hrTDModel

import qualityFrequencyDependentModel
import powerSpec as pspec
from trackStreaming import getMinDistPeak
from constants import *

# Warn if the git hash for the model doesn't match the current set of features
qualityCalculationHashCurrent = (os.popen("git log  head -n 1").read()).rstrip()
qualityTrainingHashCurrent = (os.popen("git log  | head -n 1").read()).rstrip()

try:
    if qualityCalculationHashCurrent is None:
        print('### Warning: could not determine hash ')
    elif qualityTrainingHashCurrent is None:
        print('### Warning: could not determine hash ')
except AttributeError:
    print('### Warning: no Hash variable in one of the model files')
