# don't run this script from within TextPad. TextPad can't capture input
# run in shell or cmd c:\webStormWS\BigData\GrokkingDeepLearning>python ch4_2DNetDebug.py
import numpy as np
weights = np.array([0.5,0.48,-0.7])
alpha = 0.1
streetlights = np.array( [[ 1, 0, 1 ],
[ 0, 1, 1 ],
[ 0, 0, 1 ],
[ 1, 1, 1 ],
[ 0, 1, 1 ],
[ 1, 0, 1 ] ] )
walk_vs_stop = np.array( [ 0, 1, 0, 1, 1, 0 ] )
inputArray = streetlights # [1,0,1]
goal_prediction = walk_vs_stop # equals 0... i.e. "stop"
for iteration in range(100):
	#multiply each row by weight and sum-up. So row => predict number
	prediction = inputArray.dot(weights)
	error = np.sum((prediction - goal_prediction) ** 2)
	delta = prediction - goal_prediction
	weights -= (alpha * (inputArray.T.dot(delta)))
	print ("Average Error:" + str(error))
	print ("Prediction:" + str(prediction))
	flag = input("Continue?")
	if(flag == "d"):
		print ("Weights:" + str(weights))
	
	if(flag == "n"):
		print ("Beak the loop:")
		break
	#else:print ("continue...")


print ("Training completed: Prediction:" + str(prediction))