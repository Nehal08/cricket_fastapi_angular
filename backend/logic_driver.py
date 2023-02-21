import random
import model

def toss(team1: model.Teams,team2: model.Teams):
    choices = ['Bat First', 'Ball First']
    toss_res = random.randint(0,1) # who won the toss 
    toss_choice = random.randint(0,1) # bat first or ball first
    result = {}
    #team1,team2 = team1.__dict__,team2.__dict__
    team1,team2 = team1,team2
    if toss_res == 0: # team 1 won the toss
        result['team_won'] = team1.name
        if toss_choice == 0: # and choose to bat first
            result['toss_decision'] = choices[0]
            result['first_batting_team'] = team1
            result['second_batting_team'] = team2
        else: # and choose to ball first
            result['toss_decision'] = choices[1]
            result['first_batting_team'] = team2
            result['second_batting_team'] = team1
    else: # team 2 won the toss
        result['team_won'] = team2.name
        if toss_choice == 0: # and choose to bat first
            result['toss_decision'] = choices[0]
            result['first_batting_team'] = team2
            result['second_batting_team'] = team1
        else: # and choose to ball first
            result['toss_decision'] = choices[1]
            result['first_batting_team'] = team1
            result['second_batting_team'] = team2
    return result 
        

def startOver(team: model.Teams,strike:model.Players,nonStriker: model.Players,target,runs,wickets,player_history):
    ball = 1
    over_res = ''

    while(ball <=6):
        ball_result = random.randint(-1,6)
        if ball_result == -1: #wicket
            wickets += 1
            over_res += ' W ' 

            if wickets == 10 and target == None: #first inning
                target = runs
                return [over_res,target,'Over',runs,wickets,player_history,strike,nonStriker]

            elif wickets == 10 and target != None: # second inning over 
                return [over_res,target,'In Progress',runs,wickets,player_history,strike,nonStriker]


            strike = team.team_players[wickets +1]

        elif ball_result == 0:
            ball+=1
            over_res += ' 0 '
            continue

        elif (ball_result == 1) or (ball_result == 3) or (ball_result == 5):
            runs += ball_result
            
            if ball_result == 1:
                if strike.player_id in player_history.keys():
                    player_history[strike.player_id] += ball_result
                else:
                    player_history[strike.player_id] = ball_result
            elif ball_result == 3:
                #mainting strikers runs
                if strike.player_id in player_history.keys():
                    player_history[strike.player_id] += 2
                else:
                    player_history[strike.player_id] = 2
                #maintainng non strikers' runs
                if nonStriker.player_id in player_history.keys():
                    player_history[nonStriker.player_id] += 1
                else:
                    player_history[nonStriker.player_id] = 1
            else:
                #mainting strikers runs
                if strike.player_id in player_history.keys():
                    player_history[strike.player_id] += 3
                else:
                    player_history[strike.player_id] = 3
                #maintainng non strikers' runs
                if nonStriker.player_id in player_history.keys():
                    player_history[nonStriker.player_id] += 2
                else:
                    player_history[nonStriker.player_id] = 2
            over_res += ' '+ str(ball_result) + ' '

            #strike change   
            strike,nonStriker = nonStriker,strike
            if target and runs >= target:
                return[over_res,target,'Over',runs,wickets,player_history,strike,nonStriker]
        else:
            runs += ball_result
            #print('last else',strike,nonStriker)
            if strike.player_id in player_history.keys():
                player_history[strike.player_id] += ball_result
            else:
                player_history[strike.player_id] = ball_result
            over_res += ' '+ str(ball_result) + ' '

            if target and runs >= target:
                return[over_res,target,'Over',runs,wickets,player_history,strike,nonStriker]
        ball += 1

    #strike change after the over
    strike,nonStriker = nonStriker,strike
    
    return [over_res,None,'In Progress',runs,wickets,player_history,strike,nonStriker]
