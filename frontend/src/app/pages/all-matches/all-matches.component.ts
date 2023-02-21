import { Component } from '@angular/core';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-all-matches',
  templateUrl: './all-matches.component.html',
  styleUrls: ['./all-matches.component.css']
})
export class AllMatchesComponent {

  matches!: any;

  constructor(private matchservice: MatchService ) { }

  ngOnInit(): void {

    this.matchservice.getAllMatches().subscribe(data => {
      let obj:any = data
      this.matches = obj
      console.log(this.matches)
    })
    
  }

}
