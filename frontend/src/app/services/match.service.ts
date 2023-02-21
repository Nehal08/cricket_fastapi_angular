import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MatchService {

  url = `http://127.0.0.1:8000`

  constructor(private httpclient: HttpClient) { }

  getAllPlayers(){
    return this.httpclient.get(this.url + `/retrieve_all_players`)
  }

  getAllPlayersInTeam(teamid: number){
    return this.httpclient.get(this.url + `/retrieve_all_players_in_team?t_id=` + teamid)
  }

  getAllTeams(){
    return this.httpclient.get(this.url + `/retrieve_all_teams`)
  }

  getAllMatches(){
    return this.httpclient.get(this.url + `/retrieve_all_matches`)
  }

  getInningsOfMatch(matchId: number){
    return this.httpclient.get(this.url + `/retrieve_innings_of_match?m_id=` + matchId)
  }

  addTeam(team: any){
    return this.httpclient.post(this.url + `/add_new_team`,team)
  }

  addPlayer(player: any){
    return this.httpclient.post(this.url + `/add_new_player`,player)
  }

  startMatch(match: any){
    return this.httpclient.post(this.url + `/new_match_start`,match)
  }

}
