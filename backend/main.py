from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_players', response_model=List[schema.PlayerAdd])
def retrieve_all_player_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db=db, skip=skip, limit=limit)
    return players

@app.get('/retrieve_all_teams', response_model=List[schema.TeamAdd])
def retrieve_all_team_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud.get_teams(db=db, skip=skip, limit=limit)
    return teams

@app.get('/retrieve_all_matches', response_model=List[schema.MatchRead])
def retrieve_all_matches_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matches = crud.get_matches(db=db, skip=skip, limit=limit)
    return matches

@app.get('/retrieve_all_innings', response_model=List[schema.InningBase])
def retrieve_all_innings_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    innings = crud.get_innings(db=db, skip=skip, limit=limit)
    return innings

@app.get('/retrieve_all_overs', response_model=List[schema.OverBase])
def retrieve_all_overs_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    overs = crud.get_overs(db=db, skip=skip, limit=limit)
    return overs

@app.get('/retrieve_all_players_in_team', response_model=List[schema.PlayerAdd])
def retrieve_all_player_from_team(t_id: int, db: Session = Depends(get_db)):
    players = crud.get_all_players_in_team(db=db, t_id=t_id)
    return players

@app.get('/retrieve_innings_of_match', response_model=List[schema.InningBase])
def retrieve_innings_of_match(m_id: int, db: Session = Depends(get_db)):
    innings = crud.get_inning_by_id(db=db,m_id=m_id)
    return innings

# @app.get('/retrieve_mvp_of_match', response_model=schema.PlayerBase)
# def retrieve_mvp_of_match(t_id: int, db: Session = Depends(get_db)):
#     mvp = crud.get_match_mvp(db=db, t_id=t_id)
#     return mvp


@app.post('/add_new_player', response_model=schema.PlayerBase)
def add_new_player(player: schema.PlayerBase, db: Session = Depends(get_db)):
    # player_id = crud.get_player_by_id(db=db, p_id=player.player_id)
    # if player_id:
    #     raise HTTPException(status_code=400, detail=f"Player id {player.player_id} already exist in database: {player_id}")
    return crud.add_player_details_to_db(db=db, player=player)

@app.post('/add_new_team', response_model=schema.TeamBase)
def add_new_team(team: schema.TeamBase, db: Session = Depends(get_db)):
    # team_id = crud.get_team_by_id(db=db, t_id=team.team_id)
    # if team_id:
    #     raise HTTPException(status_code=400, detail=f"Team id {team.team_id} already exist in database: {team_id}")
    return crud.add_team_details_to_db(db=db, team=team)

@app.post('/add_new_match', response_model=schema.MatchBase)
def add_new_team(match: schema.MatchBase, db: Session = Depends(get_db)):
    # team_id = crud.get_team_by_id(db=db, t_id=team.team_id)
    # if team_id:
    #     raise HTTPException(status_code=400, detail=f"Team id {team.team_id} already exist in database: {team_id}")
    return crud.add_match_details_to_db(db=db, match=match)

@app.post('/new_match_start', response_model=schema.MatchRead)
def new_match_start(match: schema.MatchBase, db: Session = Depends(get_db)):
    # team_id = crud.get_team_by_id(db=db, t_id=team.team_id)
    # if team_id:
    #     raise HTTPException(status_code=400, detail=f"Team id {team.team_id} already exist in database: {team_id}")
    m_id = crud.add_match_details_to_db(db=db,match=match)
    return crud.get_match_results(db=db,m_id=m_id)

@app.delete('/delete_team_by_id')
def delete_team_by_id(t_id: int, db: Session = Depends(get_db)):
    details = crud.get_team_by_id(db=db, t_id=t_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_team_details_by_id(db=db, t_id=t_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.delete('/delete_player_by_id')
def delete_player_by_id(p_id: int, db: Session = Depends(get_db)):
    details = crud.get_player_by_id(db=db, p_id=p_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_player_details_by_id(db=db, p_id=p_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.delete('/delete_inning_by_id')
def delete_inning_by_id(i_id: int, db: Session = Depends(get_db)):
    # details = crud.get_player_by_id(db=db, p_id=p_id)
    # if not details:
    #     raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_inning_details_by_id(db=db, i_id=i_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.delete('/delete_over_by_id')
def delete_over_by_id(o_id: int, db: Session = Depends(get_db)):
    # details = crud.get_player_by_id(db=db, p_id=p_id)
    # if not details:
    #     raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_over_details_by_id(db=db, o_id=o_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.delete('/delete_match_by_id')
def delete_match_by_id(m_id: int, db: Session = Depends(get_db)):
    # details = crud.get_player_by_id(db=db, p_id=p_id)
    # if not details:
    #     raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_match_details_by_id(db=db, m_id=m_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

# @app.get('/retrieve_all_movies_details', response_model=List[schema.Movie])
# def retrieve_all_movies_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     movies = crud.get_movies(db=db, skip=skip, limit=limit)
#     return movies


# @app.post('/add_new_movie', response_model=schema.MovieAdd)
# def add_new_movie(movie: schema.MovieAdd, db: Session = Depends(get_db)):
#     movie_id = crud.get_movie_by_movie_id(db=db, movie_id=movie.movie_id)
#     if movie_id:
#         raise HTTPException(status_code=400, detail=f"Movie id {movie.movie_id} already exist in database: {movie_id}")
#     return crud.add_movie_details_to_db(db=db, movie=movie)


# @app.delete('/delete_movie_by_id')
# def delete_movie_by_id(sl_id: int, db: Session = Depends(get_db)):
#     details = crud.get_movie_by_id(db=db, sl_id=sl_id)
#     if not details:
#         raise HTTPException(status_code=404, detail=f"No record found to delete")

#     try:
#         crud.delete_movie_details_by_id(db=db, sl_id=sl_id)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
#     return {"delete status": "success"}


# @app.put('/update_movie_details', response_model=schema.Movie)
# def update_movie_details(sl_id: int, update_param: schema.UpdateMovie, db: Session = Depends(get_db)):
#     details = crud.get_movie_by_id(db=db, sl_id=sl_id)
#     if not details:
#         raise HTTPException(status_code=404, detail=f"No record found to update")

#     return crud.update_movie_details(db=db, details=update_param, sl_id=sl_id)