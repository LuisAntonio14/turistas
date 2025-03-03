import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LacuevaPage } from './lacueva.page';

describe('LacuevaPage', () => {
  let component: LacuevaPage;
  let fixture: ComponentFixture<LacuevaPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(LacuevaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
