import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonMenu, IonItem, IonButtons, IonMenuButton } from '@ionic/angular/standalone';

import { Router } from '@angular/router';
@Component({
  selector: 'app-cruz',
  templateUrl: './cruz.page.html',
  styleUrls: ['./cruz.page.scss'],
  standalone: true,
  imports: [IonButtons, IonItem, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonMenu, IonMenuButton]

})
export class CruzPage implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  irAlugares() {
    this.router.navigate(['lugares']);  
  }
}
