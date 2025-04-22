import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonGrid, IonRow, IonCol, IonButton, IonImg, IonCard, IonMenu, IonMenuButton, IonButtons, IonList, IonItem, NavController } from '@ionic/angular/standalone'; // Importa NavController
import { Router } from '@angular/router';

@Component({
  selector: 'app-lugares',
  templateUrl: './lugares.page.html',
  styleUrls: ['./lugares.page.scss'],
  standalone: true,
  imports: [IonButton, IonCol, IonRow, IonGrid, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonImg, IonCard, IonMenu, IonMenuButton, IonButtons, IonList, IonItem]
})
export class LugaresPage implements OnInit {

  constructor(private navController: NavController) { }  // Cambia Router por NavController

  ngOnInit() {
  }

  irACruz() {
    this.navController.navigateForward('/cruz');  // Usa navigateForward para navegación hacia adelante
  }
  
  irAlacueva() {
    this.navController.navigateForward('/lacueva');  // Usa navigateForward para navegación hacia adelante
  }

  irApresa() {
    this.navController.navigateForward('/presa');  // Usa navigateForward para navegación hacia adelante
  }

  irAsantuario() {
    this.navController.navigateForward('/santuario');  // Usa navigateForward para navegación hacia adelante
  }

  irAlogin() {
    this.navController.navigateRoot('/login');  // Usa navigateRoot si deseas redirigir al login y reiniciar el historial
  }
}
