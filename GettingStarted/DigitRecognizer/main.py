import pandas as pd
import torch

training_dataset_path = './data/train.csv'

# class MinstDataSet:
# 	def __init__(self):
# 		trainX = pd.read_csv("./data/train.csv")
# 		# trainY = trainX.label.as_matrix().tolist()
# 		# trainX = trainX.drop("label",axis=1).as_matrix().reshape(42000,1,28,28)
# 		# self.datalist = trainX
# 		# self.labellist = trainY


# 	def __getitem__(self, index):
# 		return torch.Tensor(self.datalist[index].astype(float)), self.labellist[index]

# 	def __len__(self):
# 		return self.datalist.shape[0]

if __name__ == "__main__":
    trainX = pd.read_csv(training_dataset_path)