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
  selector: 'app-cruz',
  templateUrl: './cruz.page.html',
  styleUrls: ['./cruz.page.scss'],
  standalone: true,
  imports: [
    IonButtons, IonButton, IonItem, IonContent, IonHeader, IonTitle, IonToolbar, 
    CommonModule, FormsModule, IonMenu, IonMenuButton, IonLabel, IonList, 
    IonRefresher, IonRefresherContent, IonDatetime
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CruzPage implements OnInit {
  turistas: any[] = [];
  showDateTime = false; // Controla la visibilidad del selector de fecha y el botón de búsqueda
  selectedDate: string = ''; // Fecha seleccionada por el usuario

  constructor(private router: Router, private http: HttpClient, private cdRef: ChangeDetectorRef) {}

  ngOnInit() {
    this.getTuristas();
  }

  toggleDateTime() {
    this.showDateTime = !this.showDateTime; // Alterna entre mostrar y ocultar el selector de fecha
  }

  fetchRecordsByDate() {
    if (!this.selectedDate) {
      console.error('No se ha seleccionado una fecha');
      return;
    }
  
    // Convertir la fecha seleccionada a ISO y extraer "YYYY-MM"
    const formattedDate = new Date(this.selectedDate)
      .toISOString()
      .split('T')[0]
      .slice(0, 7); // Extrae "YYYY-MM"
    console.log('Fecha seleccionada y formateada (YYYY-MM):', formattedDate);
  
    this.http
      .get<any[]>(`https://turistas.onrender.com/turistas/filtrar_fecha?fecha=${formattedDate}`)
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

  getTuristas(event?: CustomEvent) {
    this.http.get<any[]>('https://turistas.onrender.com/turistas/santa_cruz')
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
