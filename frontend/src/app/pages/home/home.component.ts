import { Component } from '@angular/core';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  teams!: any

  constructor(private matchservice: MatchService ) { }

  ngOnInit(): void {

    this.matchservice.getAllTeams().subscribe(data => {
      let obj:any = data
      this.teams = obj
      console.log(this.teams)
    })
    
  }

}
