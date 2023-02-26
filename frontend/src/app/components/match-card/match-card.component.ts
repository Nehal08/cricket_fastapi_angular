import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { MatchService } from 'src/app/services/match.service';

@Component({
  selector: 'app-match-card',
  templateUrl: './match-card.component.html',
  styleUrls: ['./match-card.component.css']
})
export class MatchCardComponent {

  @Input() match!: any;
  toss_won_by!: string;
  innings!: any;

  constructor(private matchservice: MatchService, private router: Router) { }
  
  ngOnInit(): void {

    this.toss_won_by = this.match.toss_won.split('-')[0] + 'won the toss & choose to' + this.match.toss_won.split('-')[1]

    this.matchservice.getInningsOfMatch(this.match.match_id).subscribe(data => {
      let obj = data
      this.innings = obj

    })

  }


  navigate(){
    this.router.navigate(['match_summary',this.match.match_id])
  }

}
