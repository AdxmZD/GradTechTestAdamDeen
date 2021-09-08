medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    length_results = len(results) #store length of results object
    length_podium = len(results[0]['podium']) # store length of podium dict key
    splitting = [] #create new list to store country names and placements
    countries = {
        "China": 0,
        "Germany": 0,
        "ROC": 0,
        "France": 0,
        "Italy": 0,
        "USA": 0,
        "Qatar": 0,
        "Belarus": 0,
        "Brazil": 0
    } #create dict to update country scores
    
    for i in range(length_results):
        
        for j in range(length_podium):
            splitting.append(results[i]['podium'][j].split("."))
            # nested for loop to iterate results table and podium keys using lengths stored prior
            # using split() function to separate countries from their placement numbers using "." as an indicator of where to initiate split
            # using append() to store separated countries and placement numbers in 'splitting' list created prior
            
    for i in range(len(splitting)): # for loop to iterate 'splitting' list
        
        if (splitting[i][0]) == '1': # if statements used to check placement values stored in splitting list and update country scores in 'countries' dict          
            for j in countries:    # for loop used to itterate keys (country names) in 'countries' dict   
                if splitting[i][1] == j:
                    countries[j] += 3
                    
        elif (splitting[i][0]) == '2':
            for j in countries:
                if splitting[i][1] == j:
                    countries[j] += 2
            
        elif (splitting[i][0]) == '3':
            for j in countries:
                if splitting[i][1] == j:
                    countries[j] += 1
             
    return countries


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
test_function()
