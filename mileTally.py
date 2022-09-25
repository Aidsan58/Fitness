#
# This program tallies the number of miles walked each day during an interval chosen by the user.
#


# Takes user input and creates a list. This list will be used by the other functions.
def make_a_list(myList):
    intervalWeeks = int(input('How many weeks will you be tallying?'))
    intervalDays = intervalWeeks * 7
    intervalDays = int(intervalDays)
    for i in range(intervalDays):
        m = input(f'Enter miles walked for day {i + 1}: ')
        myList.append(m)
    return myList


# Returns a print statement with the average number of miles walked.
def avg_miles(allMiles):
    total = 0
    for i in allMiles:
        total += int(i)
    average = total / len(allMiles)
    
    output = f'The average number of miles you walked in {len(allMiles) / 7} week(s) was ' '{:.2f}.'.format(average)
    return output


# Returns the day where most miles were walked.
def bgst_val(allMiles):
    largestNumber = allMiles[0]
    for number in allMiles:
        if number > largestNumber:
            largestNumber = number
    output = (f'The most miles walked in one day was {largestNumber} miles.')
    return output
        

myList = make_a_list(myList = [])
print(avg_miles(myList))
print(bgst_val(myList))
