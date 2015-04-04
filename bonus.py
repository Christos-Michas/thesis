import mne
import numpy

##frequencies = numpy.arange(2,20.1,0.1)
##decim = 1
##n_cycles=7
##epochs = mne.read_epochs('mne_data/thesis/epochs/subject_10_sound_620-epo.fif')
##evoked = epochs.average()
##out = mne.time_frequency.tfr_morlet(epochs=evoked,freqs=frequencies,n_cycles=n_cycles,use_fft=False,return_itc=False,decim=decim,n_jobs=1)

box = (-.3, 1.3, -.3, 1.3)
positions = numpy.zeros((32,4),dtype=float)

for i in numpy.arange(0,4):
	for j in numpy.arange(0,8):
		positions[i*8 + j%8] = [i/4.0,0.9-j/8.0,0.2,0.1]

names = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32']
ids = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32']
kind = 'Vectorview-all'
layout = mne.layouts.Layout(box,positions,names,ids,kind)
picks = mne.pick_types(evoked.info, meg=True, eeg=True)

out.plot_topo(picks=picks, baseline=None, mode=None, tmin=None, tmax=None, fmin=2, fmax=20, vmin=None, vmax=1e-10, layout=layout, cmap='jet', title='Collective 10 620', dB=False, colorbar=True, layout_scale=0.945, show=True)
