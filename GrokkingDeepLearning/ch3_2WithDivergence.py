knob_weight = 0.5
goal_prediction = 0.8
input = 2.5
i=0
for iteration in range(300):
	prediction = input * knob_weight
	error = (goal_prediction - prediction) ** 2
	direction_and_amount = (goal_prediction - prediction) * input
	knob_weight = knob_weight + direction_and_amount
	print ("Iteration("+str(i)+")\t Error:" + str(error) + "\t Prediction:" + str(prediction)+"\t knob_weight="+str(knob_weight))
	if(error< 0.00000000000000001):
		break
	i=i+1;
print ("Train complete on Iteration("+str(i)+")\t with Error:" + str(error) +"\t knob_weight value equal "+str(knob_weight))