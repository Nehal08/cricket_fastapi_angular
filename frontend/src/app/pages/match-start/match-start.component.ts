import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-match-start',
  templateUrl: './match-start.component.html',
  styleUrls: ['./match-start.component.css']
})
export class MatchStartComponent {

  matchDetails!: FormGroup
  teams!: any;

  constructor(private matchservice: MatchService) { }

  ngOnInit(): void {

    this.matchservice.getAllTeams().subscribe(data => {
      let obj = data
      this.teams = obj
    })

    this.matchDetails = new FormGroup({
      matchVenue: new FormControl(''),
      team1: new FormControl(''),
      team2: new FormControl(''),
    });

  }

  handleSubmit(matchDetail: FormGroup){
    const match = {
      "venue": matchDetail.value.matchVenue,
      "team_1_id": matchDetail.value.team1,
      "team_2_id": matchDetail.value.team2
    }
    this.matchservice.startMatch(match).subscribe(data => {
      console.log(data)
    })
  }

}
