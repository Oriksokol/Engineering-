import numpy as np, time as tm
def git_sin_wave_amplitude(freq,t=0.0):
    s=np.sin(2*np.pi*freq*t)
    t+=1/freq
    n_ampl=(s+1)/2
    return n_ampl
def wait_for_sampling_period(sampling_frequency):
    sampling_period=1/sampling_frequency
    tm.sleep(sampling_period)