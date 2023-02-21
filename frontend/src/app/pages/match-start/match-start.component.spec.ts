import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MatchStartComponent } from './match-start.component';

describe('MatchStartComponent', () => {
  let component: MatchStartComponent;
  let fixture: ComponentFixture<MatchStartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MatchStartComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MatchStartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
