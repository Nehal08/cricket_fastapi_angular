import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AllMatchesComponent } from './pages/all-matches/all-matches.component';
import { AllPlayersComponent } from './pages/all-players/all-players.component';
import { HomeComponent } from './pages/home/home.component';
import { MatchStartComponent } from './pages/match-start/match-start.component';
import { PlayersInTeamComponent } from './pages/players-in-team/players-in-team.component';
import { RegisterPlayerComponent } from './pages/register-player/register-player.component';
import { RegisterTeamComponent } from './pages/register-team/register-team.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'register_player',
    component: RegisterPlayerComponent
  },
  {
    path: 'players',
    component: AllPlayersComponent
  },
  {
    path: 'register_team',
    component: RegisterTeamComponent
  },
  {
    path: 'team/:team_id',
    component: PlayersInTeamComponent
  },
  {
    path: 'matches',
    component: AllMatchesComponent
  },
  {
    path: 'begin_match',
    component: MatchStartComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
