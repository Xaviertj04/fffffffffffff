numberOfTeams = 4
numberOfIndividuals = 20
numberOfEvents = 5
eventTypes = []

teamScores = [0, 0, 0, 0]
individualScores = [0] * numberOfIndividuals

#rank calculation based on position
def rankCalc(position, eventType):
    if eventType == 'team':
        if position == 1:
            return 1
        elif position == 2:
            return 2
        elif position == 3:
            return 3
        elif position == 4:
            return 4
    elif eventType == 'individual':
        if position == 1:
            return 1
        elif position >= 2 and position <= 3:
            return 2
        elif position > 3 and position <= 10:
            return 3
        elif position <= 15:
            return 4
        else:
            return 0

#calculates points based on team/individuals rank
def point_calculations(rank, eventType):
    if rank == 1:
        return 20
    elif rank == 2:
        return 15
    elif rank == 3:
        return 10
    elif rank == 4:
        return 5
    else:
        return 0

#user inputs type of each event
while len(eventTypes) < numberOfEvents:
    eventInput = input(f'Enter the type of Event {len(eventTypes) + 1} (either team or individual): ')
    if eventInput == 'team' or eventInput == 'individual':
        eventTypes.append(eventInput)
    else:
        print('Please enter a valid option.')


#user inputs positions for contestants/teams per round
for event in range(numberOfEvents):
    print('\nEvent', event + 1)
    typeOfEvent = eventTypes[event]
    #team round
    if typeOfEvent == 'team':
            for team in range(numberOfTeams):
                teamPosition = int(input(f'Enter the position of Team {str(team + 1)}: '))
                teamRank = rankCalc(teamPosition, 'team')
                points = point_calculations(teamRank, typeOfEvent)
                teamScores[team] += points
            print('Current Results')
            for team in range(numberOfTeams):
                print(f'Team {team+1}: {teamScores[team]}')

    #individual round
    elif typeOfEvent == 'individual':
        for individual in range(numberOfIndividuals):
            individualPosition = int(input(f'Enter the position of Contestant {str(individual + 1)}: '))
            individualRank = rankCalc(individualPosition, 'individual')
            points = point_calculations(individualRank, typeOfEvent)
            individualScores[individual] += points
        print('Current Results:')
        for individual in range(numberOfIndividuals):
            print(f'Contestant {individual + 1}: {individualScores[individual]}')
    print('')

#prints all team and individual scores
print('\nFinal Results\n')
print('Teams:')
for team in range(numberOfTeams):
    print(f'Team {team+1}: {teamScores[team]}')

print('Individuals:')
for individual in range(numberOfIndividuals):
    print(f'Contestant {individual + 1}: {individualScores[individual]}')





