import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent {

  currentPlayerRoute: string = '';
  currentMatchRoute: string = '';

  playerRoutes = [
    {
      value: 'players',
      display: 'View all Players'
    },
    {
      value: 'register_player',
      display: 'Register Players'
    },
  ]

  matchRoutes = [
    {
      value: 'matches',
      display: 'View all Matches'
    },
    {
      value: 'begin_match',
      display: 'Register a Match'
    },
  ]
  
  constructor(private router: Router) { } 

  homepage(){
    this.currentPlayerRoute=''
    this.currentMatchRoute=''
    this.router.navigate(['/'])
  }

  registerTeam(){
    this.currentPlayerRoute=''
    this.currentMatchRoute=''
    this.router.navigate(['/register_team'])
  }

  routeTo(e: any) {
    this.router.navigate(['/' + e]);
  }


}
