About YOLOV3

*Dimension clusters as anchor boxes

*Objectness score  with logistic regression

*Class Prediction - Independent Logistic Classifiers instead of sofmtmax 

	(Helps when moving to more complex datasets[Open Image Dataset])

*Prediction Across Scales

	To extract features - using a similar concept to feature pyramid networks

	From the base feature extractor adding a few convolution layers.

	Last one predicts 3-D tensor encoding box, objectness and class prediction.

		COCO- 3 BOXES AT EACH SCALE - tensor is = N * N * [3*(4+1+80)]

	Take the feautre map from 2 layers previous, upsample by 2*

		Take the earlier one and merge it with upsampled ones using CONCETENATION

	Add few convolutional layers, eventually predict the a smilar tensor, but NOW TWICE THE SIZE

	Perform same design one more time, with this At 3rd scale WE BENEFIT FROM ALL PRIOR COMPUTATION AND "FINE-GRAINED" FEATURES FROM EARLY ON IN NETWORK.

	'Bounding Box Priors' is still determined with k - means clustering.

		9 clusters 3 scales (arbitrarily) then divide them up evenly across scales.

			COCO THE 9 CLUSTERS- 10*13 16*30 33*23 30*61 62*45 59*119 116*90 156*198 373*326

*Feautre Extractor

	Darknet 19 combined with residual networks. 53 convolutions - Called DARKNET 53

		Much more powerful than darknet19 - but still more efficient than Resnet-101 Resnet-152 [can cite the table]

			Highest measured floating points - utilizing the GPU better than Resnets.

*Training 

	Darknet Neural Network is used.

*How we Do ?

	COCO average mean AP metric. par with SSD 3* faster. .5 mAP still legit. 

	Past it was struggling with small objects. With the new multi scale predictions YOLOV3 has relatively high APsmall performance. (Now it is kinda solved.)

	About ACCURACY AND SPEED - YOLOV3 has significant benefits over other detection systems. Faster Better.
	
*Results

	YOLOV3 is very good at .5 metric.

	REAL TIME - the algorithm can process images at the frame rate of the camera. (24, 30) 

		Life is a movie running at 60 fps.
	