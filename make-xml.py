from minke import mdctools, distribution, sources
import numpy as np
mdcset = mdctools.MDCSet(['L1', 'H1', 'V1'])

times = np.linspace(0, 2000, 500)

qq = np.random.uniform(1,100, len(times))
ff = np.random.uniform(300, 2000, len(times))

for time, q, f in zip(times, qq, ff):
   sg = sources.SineGaussian(frequency=f, q=q, hrss=1e-23, time=time, polarisation="circular")
   mdcset + sg

mdcset.save_xml('sg_training.xml.gz')
o1 = mdctools.HWFrameSet('frame_list.dat')

mdc_folder = "/home/daniel/repositories/burst-training-waveforms/frames"
for o1frame in o1.frames:
   o1frame.generate_pcal(mdcset, mdc_folder)

# o1.full_logfile(mdcset, 'frames/logfile.txt')
