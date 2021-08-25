import numpy as np
import pandas as pd 

def data_loader(file_location):

	df = pd.read_csv(file_location)
	return df

