import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-players-in-team',
  templateUrl: './players-in-team.component.html',
  styleUrls: ['./players-in-team.component.css']
})
export class PlayersInTeamComponent {

  id!: number;
  players!: any;
  team!: string;

  constructor(private route: ActivatedRoute,private matchservice: MatchService) { }

  ngOnInit(): void {

    this.route.params.subscribe(params => {
      this.id = +params['team_id'];

    });

    this.getPlayers()

  }

  getPlayers(){
    this.matchservice.getAllPlayersInTeam(this.id).subscribe(data => {
      let obj = data
      this.players = obj
      this.team = this.players[0].team.name
    })
  }

}
