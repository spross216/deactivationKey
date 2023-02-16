import numpy as np

# stores the data from packet_base.txt and packet_weight.txt to a variable

baseData = np.genfromtxt('packet_base.txt', delimiter=',')
weightData = np.genfromtxt('packet_weight.txt', delimiter=',')


# converts the arrays into 2D arrays with 8 columns

numColumns = 8
numRows = baseData.size//numColumns
baseData = baseData.reshape(numRows, numColumns)
weightData = weightData.reshape(numRows, numColumns)

# multiplies the two arrays

multData = baseData * weightData

# finds the min, max and mean for each row in the new array

minValues = np.amin(multData, axis=1)
maxValues = np.amax(multData, axis=1)
meanValues = np.mean(multData, axis=1)

# calculates a new array from min, max and mean

newArray = (maxValues - meanValues) * minValues

# finds the sum of the array

sumArray = np.sum(newArray)

#find the remainder

remainder = sumArray % 4096
roundedAnswer = remainder//1

if __name__ == '__main__':
    print(roundedAnswer)