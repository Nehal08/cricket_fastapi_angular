import { Component } from '@angular/core';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-all-players',
  templateUrl: './all-players.component.html',
  styleUrls: ['./all-players.component.css']
})
export class AllPlayersComponent {

  players!: any;

  constructor(private matchservice: MatchService ) { }

  ngOnInit(): void {

    this.matchservice.getAllPlayers().subscribe(data => {
      let obj:any = data
      this.players = obj
      console.log(this.players)
    })
    
  }

}
