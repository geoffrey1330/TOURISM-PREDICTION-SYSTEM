import sys
import os
import numpy as np
import pickle


# The first step is to get our machine learning dataset:
# 


def logic_layer(x):
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in


	# it loads the trained model into environment which is saved in same directory named as "xgboost_model.pkl"
	with open(os.path.join(workpath, 'diabetics_model.pkl'), 'rb') as f:
		clf = pickle.load(f)
	f.close()

	predictions=clf.predict(x)

	
	return predictions



def logic_layer2(x):
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in


	# it loads the trained model into environment which is saved in same directory named as "xgboost_model.pkl"
	with open(os.path.join(workpath, 'breast_model.pkl'), 'rb') as f:
		clf = pickle.load(f)
	f.close()

	predictions=clf.predict(x)

	
	return predictions


def logic_layer3(x):
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in


	# it loads the trained model into environment which is saved in same directory named as "xgboost_model.pkl"
	with open(os.path.join(workpath, 'heart_model.pkl'), 'rb') as f:
		clf = pickle.load(f)
	f.close()

	predictions=clf.predict(x)

	
	return predictions



# This is used for testing purpose in local environment as x, y, z three datasets are given as example	

