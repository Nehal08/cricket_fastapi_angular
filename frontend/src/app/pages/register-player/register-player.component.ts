import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-register-player',
  templateUrl: './register-player.component.html',
  styleUrls: ['./register-player.component.css']
})
export class RegisterPlayerComponent {

  playerDeatils!: FormGroup
  teams!: any;

  roles = [
    { role: 'Batsman' },
    { role: 'All-Rounder' },
    { role: 'Wicket Keeper' },
    { role: 'Bowler' }
  ]

  constructor(private matchservice: MatchService) { }

  ngOnInit(): void {

    this.matchservice.getAllTeams().subscribe(data => {
      let obj = data
      this.teams = obj
    })

    this.playerDeatils = new FormGroup({
      playerName: new FormControl(''),
      playerAge: new FormControl(''),
      playerRole: new FormControl(''),
      playerTeam: new FormControl(''),
      playerRun: new FormControl('') 
    });

  }

  handleSubmit(playerDeatils: FormGroup){
    const player = {
      "team_id": playerDeatils.value.playerTeam,
      "name": playerDeatils.value.playerName,
      "age": playerDeatils.value.playerAge,
      "role": playerDeatils.value.playerRole,
      "runs": playerDeatils.value.playerRun
    }
    this.matchservice.addPlayer(player).subscribe(data => {
      console.log('player added successfully')
      this.playerDeatils.reset()
    })
  }


}
