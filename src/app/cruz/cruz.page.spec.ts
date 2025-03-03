import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CruzPage } from './cruz.page';

describe('CruzPage', () => {
  let component: CruzPage;
  let fixture: ComponentFixture<CruzPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(CruzPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
