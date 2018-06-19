from minke import mdctools, distribution, sources
import numpy as np
mdcset = mdctools.MDCSet(['L1', 'H1', 'V1'])

times = distribution.even_time(start = 0, stop = 50000, rate = 630720, jitter = 20)
hrss_values = distribution.log_uniform(5e-23, 1e-20, len(times))

qq = np.random.uniform(1,100, len(times))
ff = np.random.uniform(300, 2000, len(times))

for hrss, time, q, f in zip(hrss_values, times, qq, ff):
   sg = sources.SineGaussian(frequency=f, q=q, hrss=hrss, time=time, polarisation="circular")
   mdcset + sg

mdcset.save_xml('sg_training.xml.gz')

# o1 = mdctools.FrameSet('frame_list.dat')

# mdc_folder = "frames"
# for o1frame in o1.frames:
#    o1frame.generate_gwf(mdcset, mdc_folder, 'SCIENCE')

# o1.full_logfile(mdcset, 'frames/logfile.txt')
