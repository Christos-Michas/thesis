import mne
import numpy

info = mne.io.meas_info.create_info(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32'],1000,["eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg"])

##get correspondance between trials and sound durations
durations = numpy.genfromtxt('mne_data/thesis/DATA/durations.txt')

##for each subject
for i in numpy.arange(1,11):
##for i in numpy.arange(2,3):

	##extract EEG from txt file
	temp = numpy.genfromtxt('mne_data/thesis/DATA/subject'+`i`+'/EEG_Data_subject'+`i`+'.txt', delimiter='\t')
	temp2 = temp.transpose()

	##convert to Volts
	temp3 = temp2/1000000.0

	##store all trials in single raw
	rawfile = mne.io.array.RawArray(temp3,info)
	rawfile.save('mne_data/thesis/raw_files/subject'+`i`+'_whole_raw.fif',picks=None, tmin=0, tmax=None, drop_small_buffer=False, proj=False, format='single', overwrite=True, split_size='2GB')

	##set trials apart and save in raw files
	trials = numpy.ones(11)
	trials = trials.astype(int)
	for k in numpy.arange(1,111):
		j = numpy.int32(1000*durations[k-1])
		l = (j-420)/20
		number = trials[l]
		trials[l]+=1
		initial = (1200-j)/1000.0
	        rawfile.save('mne_data/thesis/raw_files/subject'+`i`+'_sound_'+`j`+'_trial_'+`number`+'_whole_raw.fif',picks=None, tmin=((k-1)*5.7), tmax=(k*5.7-0.001), drop_small_buffer=False, proj=False, format='single', overwrite=True, split_size='2GB')
		##rawfile.save('mne_data/thesis/raw_files/subject'+`i`+'_sound_'+`j`+'_trial_'+`number`+'_reference_raw.fif',picks=None, tmin=((k-1)*5.7+initial), tmax=((k-1)*5.7+initial+0.499), drop_small_buffer=False, proj=False, format='single', overwrite=True, split_size='2GB')
		##rawfile.save('mne_data/thesis/raw_files/subject'+`i`+'_sound_'+`j`+'_trial_'+`number`+'_trial_raw.fif',picks=None, tmin=((k-1)*5.7+initial+1.5), tmax=((k-1)*5.7+initial+1.5+j/1000.0-0.001), drop_small_buffer=False, proj=False, format='single', overwrite=True, split_size='2GB')
	        ##rawfile.save('mne_data/thesis/raw_files/subject'+`i`+'_sound_'+`j`+'_trial_'+`number`+'_post_raw.fif',picks=None, tmin=(k*5.7-1), tmax=(k*5.7-0.001), drop_small_buffer=False, proj=False, format='single', overwrite=True, split_size='2GB')
