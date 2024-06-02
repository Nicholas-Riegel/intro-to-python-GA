import os

tools = [
    {
        "name": "teeth",
        "cost": 0,
        "roi": 1
    },
    {
        "name": "scissors",
        "cost": 5,
        "roi": 5
    },
    {
        "name": "push-lawnmower",
        "cost": 25,
        "roi": 50
    },
    {
        "name": "electric-lawnmower",
        "cost": 250,
        "roi": 100
    },
    {
        "name": "starving-students",
        "cost": 500,
        "roi": 250
    },
]

bankAccount = 0
playerTools = ['teeth']
toolInUseName = 'teeth'

while bankAccount < 1000:
    
    toolInuse = next((obj for obj in tools if obj['name'] == toolInUseName), None)

    os.system("clear")
    print("Landscaper: Your goal is to make $1000.")
    print("You can type control + c at any time to exit the game.")
    print("\nCurrent balance: " + str(bankAccount))
    print("\nTool prices and daily income:")
    for tool in tools:
        print(tool['name'] + ": cost: $"+str(tool['cost']) +", daily income: $" + str(tool['roi']))
    print("\nYour tools are: " + ", ".join(playerTools))
    print("\nTool in use: " + toolInUseName)
    answer = input("\nPlease select one of the following options: \n1. Mow lawns using current tool. \n2. Purchase new tool. \n3. Select different tool.\nEnter number 1, 2, or 3: ")
    if answer == "1":
        bankAccount += toolInuse['roi']
    elif answer == '2':
        os.system('clear')
        toolsAvailable = []
        for x in tools:
            if x['cost'] <= bankAccount and x['name'] not in playerTools:
                toolsAvailable.append(x)
        if toolsAvailable:
            print("\nCurrent balance: " + str(bankAccount))
            print("\nYou can purchase:")
            for tool in toolsAvailable:
                print(tool['name'] + ": cost: $"+str(tool['cost']) +", daily income: $" + str(tool['roi']))
            answer2 = input("\nPlease enter the name of the tool you would like to purchase: ")
            if answer2 in [x['name'] for x in toolsAvailable]:
                selectedTool = next((x for x in toolsAvailable if x['name'] == answer2), None)
                bankAccount -= selectedTool['cost']
                playerTools.append(selectedTool['name'])
        else:
            print("You can't afford any new tools yet. Make more money!")
            answer = input("Hit enter/return to return to the previous screen.")
    elif answer == '3':
        os.system('clear')
        print("\nYour tools are: " + ", ".join(playerTools))
        print("\nTool in use: " + toolInUseName)
        answer3 = input("\nPlease enter the name of the tool you would like to use: ")
        if answer3 in playerTools:
            toolInUseName = answer3

print("You win! You made over $1000!")