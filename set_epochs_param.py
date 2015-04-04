##goal is to set IDs correctly in IDs matrix
##ID is set to 1 for accepted trials, to 2 for rejected trials

import numpy
##get sound durations for all 110 trials
durations = numpy.genfromtxt('mne_data/thesis/DATA/durations.txt')
durations = numpy.int32(1000*durations)

##instantiate matrices##

##initial has for each subject ids of the 110 trials in the order they appear in the experiment (subject x trial)
initial = numpy.ones((10,110),dtype=int)

##IDs has IDs in order (subject x sound x trial)
IDs = numpy.ones((10,11,10),dtype=int)


##set rejected ids##

##subject 2
initial[1,0] = 2
initial[1,1] = 2
initial[1,10] = 2
initial[1,13] = 2
initial[1,34] = 2
initial[1,61] = 2
initial[1,98] = 2

##subject 3
initial[2,0] = 2
initial[2,1] = 2
initial[2,2] = 2
initial[2,3] = 2
initial[2,4] = 2
initial[2,5] = 2
initial[2,6] = 2
initial[2,7] = 2
initial[2,37] = 2
initial[2,39] = 2
initial[2,44] = 2
initial[2,63] = 2
initial[2,69] = 2
initial[2,80] = 2
initial[2,90] = 2
initial[2,92] = 2
initial[2,94] = 2
initial[2,95] = 2
initial[2,96] = 2
initial[2,107] = 2
initial[2,109] = 2


##subject 4
initial[3,0] = 2
initial[3,29] = 2
initial[3,36] = 2
initial[3,80] = 2


#subject 5
initial[4,0] = 2
initial[4,1] = 2
initial[4,2] = 2
initial[4,3] = 2
initial[4,4] = 2
initial[4,5] = 2
initial[4,6] = 2
initial[4,7] = 2
initial[4,8] = 2
initial[4,10] = 2
initial[4,46] = 2
initial[4,68] = 2
initial[4,78] = 2
initial[4,84] = 2
initial[4,85] = 2


#subject 6
initial[5,0] = 2
initial[5,1] = 2


##subject 7
initial[6,0] = 2
initial[6,1] = 2
initial[6,2] = 2
initial[6,3] = 2
initial[6,4] = 2
initial[6,5] = 2
initial[6,6] = 2
initial[6,7] = 2
initial[6,8] = 2
initial[6,23] = 2
initial[6,34] = 2
initial[6,44] = 2
initial[6,51] = 2
initial[6,60] = 2
initial[6,83] = 2


#subject 10
initial[9,0] = 2
initial[9,1] = 2
initial[9,2] = 2


##copy ids from "initial" to "IDs"##

for i in numpy.arange(0,10):
	trials = numpy.zeros(11,dtype=int)
	for k in numpy.arange(0,110):
		l = (durations[k]-420)/20
		number = trials[l]
		trials[l]+=1
		IDs[i,l,number] = initial[i,k]
		


