import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TeamCardComponent } from './components/team-card/team-card.component';
import { PlayerCardComponent } from './components/player-card/player-card.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { AllPlayersComponent } from './pages/all-players/all-players.component';
import { HomeComponent } from './pages/home/home.component';
import { PlayersInTeamComponent } from './pages/players-in-team/players-in-team.component';
import { RegisterPlayerComponent } from './pages/register-player/register-player.component';
import { RegisterTeamComponent } from './pages/register-team/register-team.component';
import { AllMatchesComponent } from './pages/all-matches/all-matches.component';
import { MatchCardComponent } from './components/match-card/match-card.component';
import { MatchStartComponent } from './pages/match-start/match-start.component';
import { MatchSummaryComponent } from './pages/match-summary/match-summary.component';

@NgModule({
  declarations: [
    AppComponent,
    TeamCardComponent,
    PlayerCardComponent,
    NavBarComponent,
    AllPlayersComponent,
    HomeComponent,
    PlayersInTeamComponent,
    RegisterPlayerComponent,
    RegisterTeamComponent,
    AllMatchesComponent,
    MatchCardComponent,
    MatchStartComponent,
    MatchSummaryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
