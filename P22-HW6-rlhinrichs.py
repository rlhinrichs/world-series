# PROGRAMMING 2022 ASSIGNMENT 6
# Author: Rebecca Hinrichs
# 12 August 2022

# Write a program that reads the file P22-HW6-Input.txt containing the names of all the baseball teams
# who have won the World Series. The program should create a dictionary in which the keys are the names of
# the teams, and each key’s associated value is the number of times the team has won the World Series. The program should
# also create a dictionary in which the keys are the years, and each key’s associated value is the name of the team that
# won that year. The program should prompt the user for a year in the range of 1903 through 2021. It should then display
# the name of the team that won the World Series that year, and the number of times that team has won the World Series.

# Main Function Definition
def main():
    winners = []     # list to store names of winners
    
    try:
        # Open the file
        infile = open('P22-HW6-Input.txt', 'r')
        
        # Process each line
        for line in infile:
            winners.append(line.strip())
        
        # Close the file
        infile.close()
        
        # Prompt the user to search for a year, return team info
        year = int(input('Enter a year from 1903 to 2021 to see who won the World Series:  '))
        query = year_lookup(winners).get(year, 'No Game Played')
        print('\n', query, sep = '')
        
        # Display number of games won (if available)
        if query != 'No Game Played':
            more_info = team_lookup(winners).get(query, 'ERROR')
            print('\nThe', query, 'have won a total of', more_info, 'World Series games!')
        
    except IOError:
        print('There was an error reading the file.')
        
    except:
        print('Who knows what happened, but I can\'t read that...')
    
    
# World Series Database Function
def year_lookup(names):
    year = []            # list to store years of games played
    series_games = {}    # dictionary to store year: team
    
    # Create the list of years of world series games
    for line, item in enumerate(names):
        if line == 0:
            year.append(1903 + line)           # beginning with year 1903
        elif line == 1 or line == 90:
            year.append(year[line - 1] + 2)    # skip years 1904, 1994
        else:
            year.append(year[line - 1] + 1)
    
    # Create dictionary of game year : winning team
    for team in range(len(names)):
        series_games[year[team]] = names[team]
    
    return series_games
    
    
def team_lookup(names):
    num_wins = []          # list to store number of wins
    series_winners = {}    # dictionary to store teams: # of years
    
    # Create dictionary of team : # of years won
    teams = list(set(names))
    for team in teams:
        num_wins.append(names.count(team))        
    for team in range(len(teams)):
        series_winners[teams[team]] = num_wins[team]
    
    return series_winners

    
# Run Program
main()