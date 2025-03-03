import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LugaresPage } from './lugares.page';

describe('LugaresPage', () => {
  let component: LugaresPage;
  let fixture: ComponentFixture<LugaresPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(LugaresPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
