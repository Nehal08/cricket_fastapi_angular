import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-team-card',
  templateUrl: './team-card.component.html',
  styleUrls: ['./team-card.component.css']
})
export class TeamCardComponent {

  @Input() team: any;

  constructor(private router: Router) { }
  
  navigate(){
    this.router.navigate(['team',this.team.team_id])
  }

}
