import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {
  IonContent, IonHeader, IonTitle, IonToolbar, IonMenu, IonItem, IonButtons,
  IonMenuButton, IonLabel, IonList, IonRefresher, IonRefresherContent, IonDatetime, IonButton
} from '@ionic/angular/standalone';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@Component({
  selector: 'app-presa',
  templateUrl: './presa.page.html',
  styleUrls: ['./presa.page.scss'],
  standalone: true,
  imports: [
    IonButtons, IonButton, IonItem, IonContent, IonHeader, IonTitle, IonToolbar,
    CommonModule, FormsModule, IonMenu, IonMenuButton, IonLabel, IonList,
    IonRefresher, IonRefresherContent, IonDatetime
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class PresaPage implements OnInit {
  turistas: any[] = [];
  showDateTime = false;
  selectedDate: string = '';

  constructor(private router: Router, private http: HttpClient, private cdRef: ChangeDetectorRef) {}

  ngOnInit() {
    this.getTuristas();
  }

  toggleDateTime() {
    this.showDateTime = !this.showDateTime;
  }

  // Función para buscar registros filtrados por fecha en Presa
  fetchRecordsByDate() {
    if (!this.selectedDate) {
      console.error('No se ha seleccionado una fecha');
      return;
    }
    const formattedDate = new Date(this.selectedDate)
      .toISOString()
      .split('T')[0]
      .slice(0, 7);
    console.log('Fecha seleccionada y formateada (YYYY-MM):', formattedDate);

    // Se asume que existe un endpoint para filtrar Presa
    this.http
      .get<any[]>(`https://turistas.onrender.com/turistas/filtrar_fecha_presa?fecha=${formattedDate}`)
      .subscribe(
        (data) => {
          console.log('Datos filtrados:', data);
          this.turistas = data.map((turista, index) => ({
            numero: index + 1,
            horaRegistro: turista.hora,
            fechaRegistro: turista.fecha,
          }));
          this.cdRef.detectChanges();
        },
        (error) => {
          console.error('Error al filtrar turistas por fecha', error);
        }
      );
  }

  // Función para obtener todos los registros de Presa
  getTuristas(event?: CustomEvent) {
    this.http.get<any[]>('https://turistas.onrender.com/turistas/presa')
      .subscribe(data => {
        console.log('Datos recibidos de la API:', data);
        this.turistas = data.map((turista, index) => ({
          numero: index + 1,
          horaRegistro: turista.hora,
          fechaRegistro: turista.fecha
        }));
        this.cdRef.detectChanges();
        if (event) {
          (event.target as HTMLIonRefresherElement).complete();
        }
      }, error => {
        console.error('Error al obtener los turistas', error);
        if (event) {
          (event.target as HTMLIonRefresherElement).complete();
        }
      });
  }

  irAlugares() {
    this.router.navigate(['lugares']);
  }
}
