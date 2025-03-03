import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SantuarioPage } from './santuario.page';

describe('SantuarioPage', () => {
  let component: SantuarioPage;
  let fixture: ComponentFixture<SantuarioPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(SantuarioPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
