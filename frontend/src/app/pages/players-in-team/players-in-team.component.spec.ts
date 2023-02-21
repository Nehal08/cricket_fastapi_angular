import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayersInTeamComponent } from './players-in-team.component';

describe('PlayersInTeamComponent', () => {
  let component: PlayersInTeamComponent;
  let fixture: ComponentFixture<PlayersInTeamComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlayersInTeamComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlayersInTeamComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
