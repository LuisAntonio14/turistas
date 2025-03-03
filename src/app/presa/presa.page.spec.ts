import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PresaPage } from './presa.page';

describe('PresaPage', () => {
  let component: PresaPage;
  let fixture: ComponentFixture<PresaPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(PresaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
