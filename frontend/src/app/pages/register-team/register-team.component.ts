import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-register-team',
  templateUrl: './register-team.component.html',
  styleUrls: ['./register-team.component.css']
})
export class RegisterTeamComponent {

  teamDeatil!: FormGroup

  constructor(private matchservice: MatchService) { }

  ngOnInit(): void {

    this.teamDeatil = new FormGroup({
      teamName: new FormControl('')
    });

  }

  handleSubmit(teamDeatil: FormGroup){
    const team = {
      "name": teamDeatil.value.teamName,
    }
    this.matchservice.addTeam(team).subscribe(data => {
      console.log('team added succesfully')
      this.teamDeatil.reset()
    })
  }

}
