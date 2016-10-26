knob_weight = 0.5
input = 0.5
goal_prediction = 0.7
step_amount = 0.001
i=0
for iteration in range(1000):
	prediction = input * knob_weight
	error = (prediction - goal_prediction) ** 2
	print ("Iteration("+str(i)+") Error:" + str(error) + " Prediction:" + str(prediction))
	i=i+1
	up_prediction = input * (knob_weight + step_amount)
	up_error = (goal_prediction - up_prediction) ** 2
	down_prediction = input * (knob_weight - step_amount)
	down_error = (goal_prediction - down_prediction) ** 2
	if(down_error < up_error):
		knob_weight = knob_weight - step_amount
	if(down_error > up_error):
		knob_weight = knob_weight + step_amount
	'print("knob_weight="+str(knob_weight)+", step_amount="+str(step_amount))'
