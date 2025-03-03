import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonGrid, IonRow, IonCol, IonButton, IonImg, IonCard, IonMenu, IonMenuButton, IonButtons, IonList, IonItem } from '@ionic/angular/standalone';
import { Router } from '@angular/router';

@Component({
  selector: 'app-lugares',
  templateUrl: './lugares.page.html',
  styleUrls: ['./lugares.page.scss'],
  standalone: true,
  imports: [IonButton, IonCol, IonRow, IonGrid, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonImg, IonCard, IonMenu, IonMenuButton, IonButtons, IonList, IonItem]
})
export class LugaresPage implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  irACruz() {
    this.router.navigate(['cruz']);  
  }
  
  irAlacueva() {
    this.router.navigate(['lacueva']);  
  }

  irApresa() {
    this.router.navigate(['presa']);  
  }

  irAsantuario() {
    this.router.navigate(['santuario']);  
  }

  irAlogin() {
    this.router.navigate(['login']);  
  }
}