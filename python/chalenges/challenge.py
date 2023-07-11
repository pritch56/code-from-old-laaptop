def findmax(score):      #defining subroutine 
	length = len(score) #setting length
	maxvalue = score[0] #setting maxvalue
	for i in range (1,length):   #starting a itiration/ loop
		if score[i] > maxvalue: #selection
			maxvalue = score[i] 
	return maxvalue  #returning the value 
newscore = 0 #setting newscore 
playerscore = []
while newscore != -1: #setting a loop 
	newscore = int(input('Please enter player score, -1 to exit:')) #inputing values 
	if newscore != -1:  #selection
		playerscore.append(newscore)

print('the scores entered were:', playerscore) #printing the scores 
print(findmax(playerscore), 'is the highest score') #calling function and outputing value 