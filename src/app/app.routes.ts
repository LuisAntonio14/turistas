import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.page').then((m) => m.HomePage),
  },
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full',
  },
  {
    path: 'login',
    loadComponent: () => import('./login/login.page').then( m => m.LoginPage)
  },
  {
    path: 'lugares',
    loadComponent: () => import('./lugares/lugares.page').then( m => m.LugaresPage)
  },
  {
    path: 'cruz',
    loadComponent: () => import('./cruz/cruz.page').then( m => m.CruzPage)
  },
  {
    path: 'lacueva',
    loadComponent: () => import('./lacueva/lacueva.page').then( m => m.LacuevaPage)
  },
  {
    path: 'presa',
    loadComponent: () => import('./presa/presa.page').then( m => m.PresaPage)
  },
  {
    path: 'santuario',
    loadComponent: () => import('./santuario/santuario.page').then( m => m.SantuarioPage)
  },
];