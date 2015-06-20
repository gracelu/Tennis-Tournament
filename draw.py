import math
import random as ran 
import operator 

"""
draw = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
#sample = draw
sample = ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
"""

#singles
draw = ['Baxter', 'Grace', 'Nitin', 'Grant', 'Michelle', 'Karen', 'Darien', 'Saeed', 'Ingrid', 'Hannah', 'Sachin', 'Tyler', 'Trevor', 'Frankie', 'Amelia', 'Kevin']
sample = ['Michelle', 'Karen', 'Darien', 'Saeed', 'Ingrid', 'Hannah', 'Sachin', 'Tyler', 'Trevor', 'Frankie', 'Amelia', 'Kevin']

#doubles
#draw = ['B. Stein and K. Stein', 'Nitin and Brodheim', 'Kushner and Ahn', 'Trevor and Lu', 'Johnson and Carter', 'Hong and Waltman', 'Richardson and Watts', 'Modak and Ling']
#sample = ['Johnson and Carter', 'Hong and Waltman', 'Richardson and Watts', 'Modak and Ling']

seeds = math.ceil(math.log(len(draw), 2))
#print "seeds:", seeds
bracketsize = math.pow(2, seeds)
#print "bracket:", bracketsize
quad_size = int(bracketsize/4)
#print "quad:", quad_size

matchings = {}
m = bracketsize/2

rounds_results = {}
num_rounds = 100
for rounds in range(0, num_rounds):
	print "\n#########"
	print "ROUND", rounds+1 
	print "#########\n"

	sample = ['Michelle', 'Karen', 'Darien', 'Saeed', 'Ingrid', 'Hannah', 'Sachin', 'Tyler', 'Trevor', 'Frankie', 'Amelia', 'Kevin']
    #sample = ['Johnson and Carter', 'Hong and Waltman', 'Richardson and Watts', 'Modak and Ling']

	for x in range(0,4):
		#print "X VALUE: ", x 
		l = []
		#random number from remaining size of sample

		seed = str(x+1) + ' ' + draw[x]

		if len(sample) == 0:
			l.append((seed,'BYE'))
		else:
			r = int(math.floor(ran.random() * len(sample)))
			#print r 

			l.append((seed,sample[r]))
			sample.remove(sample[r])

		#print "l:", l 
		for q in range(0, quad_size/2-1):
			if len(sample) == 0:
				r1_val = 'BYE'
			else:
				r1 = int(math.floor(ran.random() * len(sample)))
				#print 'r1: ', r1
				#print 'sample: ', sample 
				r1_val = sample[r1]
				sample.remove(sample[r1])

			if len(sample) == 0:
				r2_val = 'BYE'
			else:
				r2 = int(math.floor(ran.random() * len(sample)))
				r2_val = sample[r2]
				sample.remove(sample[r2])

			l.append((r1_val,r2_val))
			#print "l:", l 

		matchings[x] = l 
		#print "matchings: ", matchings

	#print matchings

	print "***************"
	print "MATCHUPS"
	print "***************"

	for s in sorted(matchings):
		print "~ Quadrant", s+1, "~"
		for m in range(0, len(matchings[s])):
			print matchings[s][m][0], 'vs', matchings[s][m][1]

	print "\n***************"
	print "RESULTS"
	print "***************"
	matchups = int(math.floor(len(matchings[1])/2))
	if matchups == 0:
		results = matchings

	#print "matchups: ", matchups
	else:
		while matchups > 0:
			results = {}
			for quad in range(0, len(matchings)):
				matches = []
				for q in range(0, matchups):
					start = 2*q
					r1 = ran.random()
					if r1 > .5 :
						w1 = matchings[quad][start][0]
						print matchings[quad][start][0], "defeated", matchings[quad][start][1]
					else:
						w1 = matchings[quad][start][1]
						print matchings[quad][start][1], "defeated", matchings[quad][start][0]

					r2 = ran.random()
					if r2 > .5 :
						w2 = matchings[quad][start+1][0]
						print matchings[quad][start+1][0], "defeated", matchings[quad][start+1][1]
					else:
						w2 = matchings[quad][start+1][1]
						print matchings[quad][start+1][1], "defeated", matchings[quad][start+1][0]


					matches.append((w1, w2))

				results[quad] = matches

			matchups = int(math.floor(len(results[1])/2))

	print "\n***************"
	print "QUARTERFINALS"
	print "***************"

	#print results
	for x in results:
		for r in range(0, len(results[0])):
			print results[x][r][0], 'vs', results[x][r][1]

	#matchups = int(math.floor(len(results[1])/2))
	#print "matchups: ", matchups

	#matchups = 0
	print "\n***************"
	print "QF RESULTS"
	print "***************"

	semi = []
	for r in results:
		#print r 
		w = ran.random()
		if w > .5:
			winner = results[r][0][0]
			print results[r][0][0], 'defeated', results[r][0][1]
		else:
			winner = results[r][0][1]
			print results[r][0][1], 'defeated', results[r][0][0]

		semi.append(winner)

	print "\n***************"
	print "SEMIFINALS"
	print "***************"
	print semi[0], 'vs', semi[1]
	print semi[2], 'vs', semi[3]

	print "\n***************"
	print "SF RESULTS"
	print "***************"
	finals = [] 
	w1 = ran.random()
	if w1 > .5:
		print semi[0], 'defeated', semi[1]
		finals.append(semi[0])
	else:
		print semi[1], 'defeated', semi[0]
		finals.append(semi[1])

	w2 = ran.random()
	if w2 > .5:
		print semi[2], 'defeated', semi[3]
		finals.append(semi[2])
	else:
		print semi[3], 'defeated', semi[2]
		finals.append(semi[3])

	print "\n***************"
	print "FINALS"
	print "***************"
	print finals[0], 'vs', finals[1]
	f = ran.random()

	
	print "\n=========================================="
	if f > .5:
		print "CATHEY HOUSE TENNIS CHAMPION: ", finals[0]
		final_winner = finals[0]
	else:
		print "CATHEY HOUSE TENNIS CHAMPION: ", finals[1]
		final_winner = finals[1]
	print "=========================================="

	try:
		#print "try"
		rounds_results[final_winner] += 1
		#print "try2"
	except:
		#print "except"
		rounds_results[final_winner] = 1
		#print "except2"

print "\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
print "After", num_rounds, "rounds here are the results:"
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
#print rounds_results

for rr in sorted(rounds_results.items(), key = operator.itemgetter(1), reverse = True):
	print rr[0],': ', rr[1]


