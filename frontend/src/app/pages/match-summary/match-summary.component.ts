import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-match-summary',
  templateUrl: './match-summary.component.html',
  styleUrls: ['./match-summary.component.css']
})
export class MatchSummaryComponent {

  match_id!: number;
  match!: any;
  innings!: any;
  inning1over: any[] = []; 
  inning2over: any[] = []; 
  team1players: any[] = [];
  team2players: any[] = [];
  team1name: string = '';
  team2name: string = '';
  toss_won_by!: string;
  mvp!: any;

  constructor(private route: ActivatedRoute,private matchservice: MatchService) { }

  ngOnInit(): void {

    this.route.params.subscribe(params => {
      this.match_id = +params['match_id'];

    });

    this.getMatch(this.match_id)

  }

  getMatch(id: number){

    this.matchservice.getMatchById(id).subscribe(data => {
      let obj = data
      this.match = obj
      console.log(this.match)


      if(this.match.result.includes(this.match.team_1.name)){
        console.log('in if clause')
        this.matchservice.getPlayerOfThematch(this.match.team_1.team_id).subscribe(data => {
          let obj: any = data
          this.mvp = obj.name
          console.log(data)
        })
      }
      else{
        console.log('in else clause')
        this.matchservice.getPlayerOfThematch(this.match.team_2.team_id).subscribe(data => {
          let obj: any = data
          this.mvp = obj.name
        })
      }

      this.toss_won_by = this.match.toss_won.split('-')[0] + 'won the toss & choose to' + this.match.toss_won.split('-')[1]

      this.matchservice.getOversOfMatch(id).subscribe(data => {
        let obj = data
        let overs: any = obj

        for(let i=0; i<overs.length; i++){
          if ((overs[i].in_id%2) == 1){
            this.inning1over.push({"over_id": overs[i].over_id, "on_strike": overs[i].on_strike, "summary": overs[i].summary ,"this_over": overs[i].this_over})
          }
          else{
            this.inning2over.push({"over_id": overs[i].over_id, "on_strike": overs[i].on_strike, "summary": overs[i].summary ,"this_over": overs[i].this_over})
          }
        }

      })

      this.matchservice.getInningsOfMatch(this.match.match_id).subscribe(data => {
        let obj = data
        this.innings = obj

        if(this.innings[0].team_playing == this.match.team_1_id){
          this.team1name = this.match.team_1.name
          this.team2name = this.match.team_2.name
        }
        else{
          this.team1name = this.match.team_2.name
          this.team2name = this.match.team_1.name
        }

        this.matchservice.getAllPlayersInTeam(this.innings[0].team_playing).subscribe(data => {
          let obj = data
          let team1p: any = obj
          let temp: number = 11;
          if(parseInt(this.innings[0].wickets) != 10){
            temp = parseInt(this.innings[0].wickets)  + 2
          } 
          for(let i=0; i<(temp); i++){
              this.team1players.push({"name": team1p[i].name, "runs": team1p[i].runs})
          }
        })

        this.matchservice.getAllPlayersInTeam(this.innings[1].team_playing).subscribe(data => {
          let obj = data
          let team2p: any = obj
          let temp: number = 11;
          if(parseInt(this.innings[1].wickets) != 10){
            temp = parseInt(this.innings[1].wickets)  + 2
          } 
          for(let i=0; i<(temp); i++){
              this.team2players.push({"name": team2p[i].name, "runs": team2p[i].runs})
          }
        })
      })

    })
  }


}
