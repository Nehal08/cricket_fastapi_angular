from sqlalchemy import func
from sqlalchemy.orm import Session
import model
import schema
import logic_driver as ld
import logging



def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Teams).offset(skip).limit(limit).all()

def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Players).offset(skip).limit(limit).all()

def get_matches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Matches).offset(skip).limit(limit).all()

def get_innings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Innings).offset(skip).limit(limit).all()

def get_overs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Overs).offset(skip).limit(limit).all()


def add_team_details_to_db(db: Session, team: schema.TeamBase):
    team_details = model.Teams(
        name=team.name
    )
    db.add(team_details)
    db.commit()
    db.refresh(team_details)
    return model.Teams(**team.dict())

def add_player_details_to_db(db: Session, player: schema.PlayerBase):
    player_details = model.Players(
        team_id = player.team_id,
        name = player.name,
        age = player.age,
        role =player.role,
        runs = player.runs
    )
    db.add(player_details)
    db.commit()
    db.refresh(player_details)
    return model.Players(**player.dict())


def delete_team_details_by_id(db: Session, t_id: int):
    try:
        db.query(model.Teams).filter(model.Teams.team_id == t_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

def get_team_by_id(db: Session, t_id: int):
    return db.query(model.Teams).filter(model.Teams.team_id == t_id).first()

def get_match_by_id(db: Session,m_id: int):
    return db.query(model.Matches).filter(model.Matches.match_id == m_id).first()

def get_inning_by_id(db: Session,m_id: int):
    return db.query(model.Innings).filter(model.Innings.m_id == m_id).all()

def get_overs_by_match_id(db: Session,m_id: int):
    return db.query(model.Overs).filter(model.Overs.m_id == m_id).all()


def delete_player_details_by_id(db: Session, p_id: int):
    try:
        db.query(model.Players).filter(model.Players.player_id == p_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    
def delete_inning_details_by_id(db: Session, i_id: int):
    try:
        db.query(model.Innings).filter(model.Innings.id == i_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

def delete_over_details_by_id(db: Session, o_id: int):
    try:
        db.query(model.Overs).filter(model.Overs.over_id == o_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    
def delete_match_details_by_id(db: Session, m_id: int):
    try:
        db.query(model.Matches).filter(model.Matches.match_id == m_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

def get_player_by_id(db: Session, p_id: int):
    return db.query(model.Players).filter(model.Players.player_id == p_id).first()

def get_match_by_id(db: Session, m_id: int):
    return db.query(model.Matches).filter(model.Matches.match_id == m_id).first()

def get_all_players_in_team(db: Session,t_id: int):
    # pls =  db.query(model.Players).filter(model.Players.team_id == t_id).all()
    # names = []
    # for pl in pls:
    #     names.append(pl.name) 
    # print(names)
    # return names
    return db.query(model.Players).filter(model.Players.team_id == t_id).all()


def add_match_details_to_db(db: Session, match: schema.MatchBase):
    match_details = model.Matches(
        venue = match.venue,
        team_1_id = match.team_1_id,
        team_2_id = match.team_2_id
    )
    db.add(match_details)
    db.commit()
    db.refresh(match_details)
    return match_details.match_id
    # return model.Matches(**match.dict())

def add_innings_details_to_db(db: Session, inning: schema.InningBase):
    inning_details = model.Innings(
        inning_id = inning.inning_id,
        team_playing = inning.team_playing,
        m_id = inning.m_id,
    )
    db.add(inning_details)
    db.commit()
    db.refresh(inning_details)
    return inning_details

def add_over_details_to_db(db: Session, over: schema.OverBase):
    over_details = model.Overs(
        m_id = over.m_id,
        in_id = over.in_id,
        on_strike = over.on_strike,
        this_over = over.this_over,
        summary = over.summary
    )
    logging.error('%s over is ',over_details.this_over)
    db.add(over_details)
    db.commit()
    db.refresh(over_details)
    return over_details

#to add player score
def update_player_details(db: Session,p_id: int,details: schema.PlayerAdd):
    updated_dets = {
        "runs": details.runs
    }
    db.query(model.Players).filter(model.Players.player_id == p_id).update(updated_dets)
    db.commit()
    return db.query(model.Players).filter(model.Players.player_id == p_id).first()

def update_inning_details(db: Session,i_id: int,details: schema.InningBase):
    updated_dets = {
        "run": details.run,
        "wickets": details.wickets
    }
    db.query(model.Innings).filter(model.Innings.id == i_id).update(updated_dets)
    db.commit()
    return db.query(model.Innings).filter(model.Innings.id == i_id).first()

def update_match_details(db: Session,m_id: int,details: schema.MatchRead):
    updated_dets = {
        "toss_won": details.toss_won,
        "first_batting_team": details.first_batting_team,
        "result": details.result,
    }
    db.query(model.Matches).filter(model.Matches.match_id == m_id).update(updated_dets)
    db.commit()
    return db.query(model.Matches).filter(model.Matches.match_id == m_id).first()

def get_match_mvp(db: Session,t_id: int):
    players = db.query(model.Players).filter(model.Players.team_id == t_id)
    mvp = players[0]
    # logging.error('%s - initial mvp',mvp.runs)
    for player in players:
        if player.runs >= mvp.runs:
            # logging.error('%s - player runs(in if)',player.runs)
            mvp = player
    return mvp 


def get_match_results(db: Session,m_id: int):
    match = get_match_by_id(db,m_id)
    toss_result = ld.toss(team1=get_team_by_id(db,match.team_1_id),team2=get_team_by_id(db,match.team_2_id))
   
    toss_won_by_team = toss_result['team_won'] + ' - ' + toss_result['toss_decision']
    first_batting_team,second_batting_team = toss_result['first_batting_team'],toss_result['second_batting_team']
    

    overs,target,final_score = 1,None,''
    strike = first_batting_team.team_players[0]
    non_strike = first_batting_team.team_players[1]
    #logging.error('%s raised an error', strike)
    team_won = ''

    inning_details_1 = model.Innings(
        inning_id = 1,
        team_playing = first_batting_team.team_id,
        m_id = match.match_id
    )
    inning_details_2 = model.Innings(
        inning_id =  2,
        team_playing = second_batting_team.team_id,
        m_id = match.match_id
    )
    inning1 = add_innings_details_to_db(db,inning_details_1)
    inning2 = add_innings_details_to_db(db,inning_details_2)
    total_runs,total_wickets = 0,0
    player_history = {} 

    while overs<=10 and target == None:
        #team,strike,non-strike,team,target,runs,wickets,player_history
        over_result = ld.startOver(first_batting_team,strike,non_strike,target,total_runs,total_wickets,player_history)
        player_history = over_result[-3]
        final_score = str(over_result[3]) + '/' + str(over_result[4])
        #logging.error('%s raised an error', over_result[0])
        over_dets = model.Overs(
            m_id =  match.match_id,
            in_id = inning1.id,
            on_strike = over_result[-2].name,
            this_over = over_result[0],
            summary = final_score
        )
        add_over_details_to_db(db,over_dets)
        total_runs = over_result[3]
        total_wickets = over_result[4]

        for temp_player_id, temp_runs in player_history.items():
            update_player_details(db,temp_player_id,model.Players(runs=temp_runs))

        #returns [[over result - length 6],target(if exists/None),'Over'/'In Progress',runs,wickets,player_history,strike,nonStriker]
        if over_result[1] == None and overs!=10:
            #print('This over[',overs,'] - ',over_result[0])
            #print('Now on strike ',over_result[3].getName())
            strike = over_result[-2]
            non_strike = over_result[-1]

        elif over_result[1]:
            #print('This over[',overs,'] - ',over_result[0])
            #print('Inning Over with score - ',over_result[1],'/10')
            #print('Target is ',target)
            target = over_result[1]
            strike = over_result[-2]
            non_strike = over_result[-1]
            break

        if overs == 10:
            target = over_result[1]
            #print('This over[',overs,'] - ',over_result[0])
            #print('Team Score is ',Ing1.getInningScore().getRuns(),'/',Ing1.getInningScore().getWickets())
            #print('Target is ',self.target)

        overs += 1 

    inning1 = update_inning_details(db,inning1.id,model.Innings(run=str(total_runs), wickets = str(total_wickets)))
    target = total_runs + 1

    logging.info('target is ',target)

    overs,final_score = 1,''
    strike = second_batting_team.team_players[0]
    non_strike = second_batting_team.team_players[1]
    total_runs,total_wickets = 0,0
    player_history = {}

    while overs <= 10:
        over_result = ld.startOver(second_batting_team,strike,non_strike,target,total_runs,total_wickets,player_history)
        player_history = over_result[-3]
        #returns [[over result - length 6],target(if exists/None),'Over'/'In Progress',runs,wickets,player_history,strike,nonStriker]
        final_score = str(over_result[3]) + '/' + str(over_result[4])
        over_dets = model.Overs(
            m_id = match.match_id,
            in_id = inning2.id,
            on_strike = over_result[-2].name,
            this_over = over_result[0],
            summary = final_score
        )
        add_over_details_to_db(db,over_dets)
        total_runs = over_result[3]
        total_wickets = over_result[4]

        for temp_player_id, temp_runs in player_history.items():
            update_player_details(db,temp_player_id,model.Players(runs=temp_runs))
        
        if over_result[2] == 'In Progress' and overs != 10:
            #print('This over[',overs,'] - ',over_result[0])
            #print('Now on strike ',over_result[3].getName())
            strike = over_result[-2]
            non_strike = over_result[-1]

        elif over_result[2] == 'Over':
            #print('This over[',overs,'] - ',over_result[0])
            #print('Team Score is ',Ing2.getInningScore().getRuns(),'/',Ing2.getInningScore().getWickets())
            #print('Match Over')
            #print(self.second_batting_team.getTeamName(),' won')
            team_won = second_batting_team.name + ' won by ' + str(10 - over_result[4]) + ' wickets'
            overs= 11
            break

        elif overs == 10 and over_result[2]=='In Progress':
            #print('This over[',overs,'] - ',over_result[0])
            #print('Team Score is ',Ing2.getInningScore().getRuns(),'/',Ing2.getInningScore().getWickets())
            #print('Match over')
            #print(self.first_batting_team.getTeamName(),' won')
            team_won = first_batting_team.name + ' won by ' + str(target - 1 - over_result[3]) + ' runs'
            overs= 11
            break
                    
        overs += 1

    inning2 = update_inning_details(db,inning2.id,model.Innings(run=str(total_runs), wickets = str(total_wickets)))

    if first_batting_team.name in team_won:
        mvp_player = get_match_mvp(db,first_batting_team.team_id)
    else:
        mvp_player = get_match_mvp(db,second_batting_team.team_id)

    #updating match details
    updated_match_details = model.Matches(
        # match_id = match.match_id,
        # venue = match.venue,
        toss_won = toss_won_by_team,
        first_batting_team = first_batting_team.name,
        result = team_won,
        mvp = mvp_player.name + ' - ' + str(mvp_player.runs) + ' runs '
        # team_1_id = match.team_1_id,
        # team_2_id = match.team_2_id
    )
    return update_match_details(db,match.match_id,updated_match_details)









# def get_movie_by_movie_id(db: Session, movie_id: str):
#     """
#     This method will return single movie details based on movie_id
#     :param db: database session object
#     :param movie_id: movie id only
#     :return: data row if exist else None
#     """
#     return db.query(model.Movies).filter(model.Movies.movie_id == movie_id).first()


# def get_movie_by_id(db: Session, sl_id: int):
#     """
#     This method will return single movie details based on id
#     :param db: database session object
#     :param sl_id: serial id of record or Primary Key
#     :return: data row if exist else None
#     """
#     return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


# def get_movies(db: Session, skip: int = 0, limit: int = 100):
#     """
#     This method will return all movie details which are present in database
#     :param db: database session object
#     :param skip: the number of rows to skip before including them in the result
#     :param limit: to specify the maximum number of results to be returned
#     :return: all the row from database
#     """
#     return db.query(model.Movies).offset(skip).limit(limit).all()


# def add_movie_details_to_db(db: Session, movie: schema.MovieAdd):
#     """
#     this method will add a new record to database. and perform the commit and refresh operation to db
#     :param db: database session object
#     :param movie: Object of class schema.MovieAdd
#     :return: a dictionary object of the record which has inserted
#     """
#     mv_details = model.Movies(
#         movie_id=movie.movie_id,
#         movie_name=movie.movie_name,
#         director=movie.director,
#         geners=movie.geners,
#         membership_required=movie.membership_required,
#         cast=movie.cast,
#         streaming_platform=movie.streaming_platform
#     )
#     db.add(mv_details)
#     db.commit()
#     db.refresh(mv_details)
#     return model.Movies(**movie.dict())


# def update_movie_details(db: Session, sl_id: int, details: schema.UpdateMovie):
#     """
#     this method will update the database
#     :param db: database session object
#     :param sl_id: serial id of record or Primary Key
#     :param details: Object of class schema.UpdateMovie
#     :return: updated movie record
#     """
#     db.query(model.Movies).filter(model.Movies.id == sl_id).update(vars(details))
#     db.commit()
#     return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


# def delete_movie_details_by_id(db: Session, sl_id: int):
#     """
#     This will delete the record from database based on primary key
#     :param db: database session object
#     :param sl_id: serial id of record or Primary Key
#     :return: None
#     """
#     try:
#         db.query(model.Movies).filter(model.Movies.id == sl_id).delete()
#         db.commit()
#     except Exception as e:
#         raise Exception(e)