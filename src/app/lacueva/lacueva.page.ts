import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { 
  IonContent, IonHeader, IonTitle, IonToolbar, IonMenu, IonItem, IonButtons, 
  IonMenuButton, IonLabel, IonList, IonRefresher, IonRefresherContent 
} from '@ionic/angular/standalone';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-lacueva',
  templateUrl: './lacueva.page.html',
  styleUrls: ['./lacueva.page.scss'],
  standalone: true,
  imports: [
    IonButtons, IonItem, IonContent, IonHeader, IonTitle, IonToolbar, 
    CommonModule, FormsModule, IonMenu, IonMenuButton, IonLabel, IonList, 
    IonRefresher, IonRefresherContent
  ]
})
export class LacuevaPage implements OnInit {
  turistas: any[] = [];

  constructor(private router: Router, private http: HttpClient, private cdRef: ChangeDetectorRef) {}

  ngOnInit() {
    this.getTuristas1();
  }

  getTuristas1(event?: CustomEvent) {
    this.http.get<any[]>('https://turistas.onrender.com/turistas/lacueva')
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
