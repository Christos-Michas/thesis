import mne
## The following file produces the IDs matrix, which tells which trials should be used in the epochs.average() function
## only trials with event_id = 1 are used in the averaging
execfile('/home/christos/mne_data/thesis/set_epochs_param.py')

valid_subjects = array([2,3,4,5,6,7,10])

for subject in valid_subjects:
	for sound in numpy.arange(420,640,20):
##for subject in numpy.arange(1,2):
##	for sound in numpy.arange(420,440,20):
		raw = mne.io.Raw('mne_data/thesis/raw_files/subject'+`subject`+'_sound_'+`sound`+'_trial_1_whole_raw.fif')

		##for each sound there are 10 trials, each trial is considered an event, and all events have three parameters
		events = numpy.zeros((10,3), dtype=numpy.int)
		##first parameter is starting point
		events[0,0] = raw.first_samp
		##second parameter may remain 0
		##third parameter is the event_id, which will be extracted from IDs matrix
		l = (sound-420)/20
		events[0,2] = IDs[subject-1,l,0]
		event_id = 1
		tmin = 0
		tmax = 5.698
		picks = mne.pick_types(raw.info, eeg=True)
		baseline = (None, 0)	##what's baseline

		##append all trials of each sound in one raw
		for i in numpy.arange(2,11):
			temp = mne.io.Raw('mne_data/thesis/raw_files/subject'+`subject`+'_sound_'+`sound`+'_trial_'+`i`+'_whole_raw.fif')
			events[i-1,0] = raw.last_samp + 1
			raw.append(temp)
			events[i-1,2] = IDs[subject-1,l,i-1]

		##create epochs/events for each trial in the new raw
		epochs = mne.Epochs(raw,events,event_id,tmin,tmax,proj=False,picks=picks,baseline=baseline,preload=False)
		epochs.save('/home/christos/mne_data/thesis/epochs/subject_'+`subject`+'_sound_'+`sound`+'-epo.fif')
		evoked = epochs.average()
		##evoked.plot()
		
		##phase 2: calculate spectrum using wavelet transform

		##data = numpy.zeros((1,32,5699))
		##data[0,:,:] = evoked.data
		##picks = mne.pick_types(evoked.info, meg=True, eeg=True)
		##info = mne.pick_info(evoked.info, picks)
		##data = data[:, picks, :]
		frequencies = numpy.arange(2,40.1,0.1)
		decim = 2
		n_cycles=7
		power = mne.time_frequency.tfr_morlet(epochs=evoked,freqs=frequencies,n_cycles=n_cycles,use_fft=False,return_itc=False,decim=decim,n_jobs=1)
		##power, phase_lock = mne.time_frequency.induced_power(data, Fs=evoked.info['sfreq'], frequencies=frequencies, use_fft=False, n_cycles=n_cycles, decim=decim, n_jobs=1, zero_mean=True)
		##times = evoked.times[::decim].copy()
		##nave = len(data)
		##out = mne.time_frequency.AverageTFR(info, power, times, frequencies, nave)
		picks2 = numpy.zeros(1,dtype=int)

		for channel in numpy.arange(1,33):
			picks2[0] = channel-1
			##out.plot(picks2,vmin=0,cmap='jet',show=False)
			power.plot(picks2,vmin=0,cmap='jet',show=False)
			matplotlib.pyplot.title('Subject '+`subject`+'   Sound '+`sound`+'   Channel '+`channel`,size=16)
			matplotlib.pyplot.axvline(1200-sound,color='black',linewidth=1.3, linestyle='--')
			matplotlib.pyplot.axvline(1200-sound+500,color='black',linewidth=1.3, linestyle='--')
			matplotlib.pyplot.axvline(3700-sound,color='black',linewidth=1.3, linestyle='--')
			matplotlib.pyplot.axvline(3700,color='black',linewidth=1.3, linestyle='--')
			savefig('/home/christos/mne_data/thesis/plots/tfr_induced_power/sound_'+`sound`+'_channel_'+`channel`+'_subject_'+`subject`+'.png', bbox_inches='tight')
			close()


##DONE
##0) remove bad subjects from processing (by changing the subject for loop) and mark all trials that should not be process (by calling the set_epochs_param.py)
##1) concatenate all same acceptable trials (and define an epoch for each one) || some trials have 5699 elements instead of 5700, so epochs are set to have 5699 elements
##2) plot them together
##3) average them
##4) perform wavelet transform with trf_morlet	(says that 'EvokedArray' object has no attribute 'get_data', I edited tfr_morlet to fix this)
##5) plot and save tfr (use 'jet' colormap)
##6) loop for all subjects and sounds

##TO DO
## about baseline, there is info in tfr.py and I should probably pick the silence period before the first stimulus
##2) what to do with shifting color axis range??
