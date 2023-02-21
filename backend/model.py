from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db_handler import Base


class Teams(Base):
    __tablename__ = "teams"
    team_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    name = Column(String,nullable=False)
    #one to many relationship b/w team and players 
    team_players: Mapped[List["Players"]] = relationship(back_populates="team")

class Players(Base):
    __tablename__ = "players"
    player_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    role = Column(String,nullable=False)
    runs = Column(Integer,nullable=False,default=0) 
    team: Mapped["Teams"] = relationship(back_populates="team_players")

    
class Matches(Base):
    __tablename__ = "matches"
    match_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    venue = Column(String, nullable=False)
    toss_won = Column(String, default=None)
    first_batting_team = Column(String,  default=None)
    result = Column(String,  default=None)
    mvp = Column(String,default=None)

    team_1_id = mapped_column(Integer, ForeignKey("teams.team_id"))
    team_2_id = mapped_column(Integer, ForeignKey("teams.team_id"))

    team_1 = relationship("Teams", foreign_keys=[team_1_id])
    team_2 = relationship("Teams", foreign_keys=[team_2_id])

class Innings(Base):
    __tablename__="innings"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    inning_id = Column(Integer,default=None) # indicating first inning(1) or second inning(2)
    team_playing: Mapped[int] = mapped_column(ForeignKey("teams.team_id")) #associated team 
    m_id: Mapped[int] = mapped_column(ForeignKey("matches.match_id")) # associated match
    score = Column(String,default=None)

class Overs(Base):
    __tablename__ = "overs"
    over_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    m_id: Mapped[int] = mapped_column(ForeignKey("matches.match_id")) # associated match
    in_id: Mapped[int] = mapped_column(ForeignKey("innings.id")) # associated inning
    # on_strike = Column(String,default=None)
    this_over =  Column(String,default=None)
    summary = Column(String,default=None)


class MatchSummary(Base):
    __tablename__ = "matchsummary"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    overs = Mapped[List["Overs"]]



# class Movies(Base):
#     """
#     This is a model class. which is having the movie table structure with all the constraint
#     """
#     __tablename__ = "movie"
#     id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
#     movie_id = Column(String, unique=True, index=True, nullable=False)
#     movie_name = Column(String(255), index=True, nullable=False)
#     director = Column(String(100), index=True, nullable=False)
#     geners = Column(String, index=True, nullable=False)
#     membership_required = Column(Boolean, nullable=False, default=True)
#     cast = Column(String(255), index=True, nullable=False)
#     streaming_platform = Column(String, index=True)