from minke import mdctools, distribution, sources
import numpy as np

o1 = mdctools.HWFrameSet(['L1', 'H1', 'V1'])
mdcset = mdctools.MDCSet(['L1', 'H1', 'V1'])
mdcset.load_xml("sg_training.xml.gz")
mdc_folder = "/home/daniel/testframes/"
for o1frame in o1.frames:
   o1frame.generate_pcal(mdcset, mdc_folder, 'SCIENCE', rate=4096)
