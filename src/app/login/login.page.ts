import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonCard, IonCardHeader, IonCardTitle, IonInput, IonButton, IonImg, IonGrid, IonRow, IonCol } from '@ionic/angular/standalone';
import { Router } from '@angular/router'; 
import { HttpClient } from '@angular/common/http'; // Importar HttpClient

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
  standalone: true,
  imports: [IonCol, IonRow, IonGrid, IonImg, IonContent, CommonModule, FormsModule, IonCard, IonCardHeader, IonCardTitle, IonInput, IonButton],
})
export class LoginPage implements OnInit {
  nombre: string = '';
  contrasena: string = '';

  // Cambia localhost por la IP de tu PC en la red local
  private API_URL = 'http://192.168.120.185:5000'; // Cambia esta IP por la IP de tu PC

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit() { }

  irALugares() {
    this.router.navigate(['lugares']);  // Redirigir a la página de lugares
  }

  login() {
    console.log("Datos enviados:", { nombre: this.nombre, contrasena: this.contrasena });

    this.http.post(`${this.API_URL}/login`, { nombre: this.nombre, contrasena: this.contrasena })
      .subscribe(response => {
        console.log(response);
        this.irALugares();
      }, error => {
        console.error("Error en login:", error);
        alert('Credenciales inválidas');
      });
  }
}
