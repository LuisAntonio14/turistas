import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonMenu, IonItem, IonButtons, IonMenuButton, IonLabel, IonList } from '@ionic/angular/standalone';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-cruz',
  templateUrl: './presa.page.html',
  styleUrls: ['./presa.page.scss'],
  standalone: true,
  imports: [IonButtons, IonItem, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonMenu, IonMenuButton, IonLabel, IonList]
})
export class PresaPage implements OnInit {

  turistas: any[] = [];

  constructor(private router: Router, private http: HttpClient, private cdRef: ChangeDetectorRef) { }

  ngOnInit() {
    this.getTuristas2();
  }

  getTuristas2() {
    this.http.get<any[]>('https://turistas.onrender.com/turistas/presa') // Cambia la URL por la de tu API
      .subscribe(data => {
        console.log('Datos recibidos de la API:', data); // Verifica la estructura
        this.turistas = data.map((turista, index) => ({
          numero: index + 1,
          horaRegistro: turista.hora,  // Cambié de 'horaRegistro' a 'hora'
          fechaRegistro: turista.fecha // Cambié de 'fechaRegistro' a 'fecha'
        }));
        this.cdRef.detectChanges(); // <-- Fuerza la actualización
      }, error => {
        console.error('Error al obtener los turistas', error);
      });
  }

  irAlugares() {
    this.router.navigate(['lugares']);
  }
}
