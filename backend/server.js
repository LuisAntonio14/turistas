const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config(); // Cargar variables de entorno desde .env

const app = express();
const port = process.env.PORT || 5000;

app.use(cors({
  origin: '*', // Permitir peticiones desde la app Ionic
}));

app.use(bodyParser.json());

// 🔹 Conectar a MongoDB Atlas usando la variable de entorno
const mongoURI = process.env.MONGO_URI; 

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('✅ Conectado a MongoDB Atlas'))
  .catch(err => console.error('❌ Error de conexión:', err));

// 🔹 Definir el esquema y modelo de usuario
const usuarioSchema = new mongoose.Schema({
  nombre: String,
  contrasena: String,
});

const Usuario = mongoose.model('Usuario', usuarioSchema, 'usuario');

// 🔹 Ruta para el inicio de sesión
app.post('/login', async (req, res) => {
  try {
    const { nombre, contrasena } = req.body;
    const user = await Usuario.findOne({ nombre, contrasena });

    if (user) {
      res.status(200).send({ message: 'Login exitoso' });
    } else {
      res.status(401).send({ message: 'Credenciales inválidas' });
    }
  } catch (error) {
    res.status(500).send({ message: 'Error en el servidor', error });
  }
});

// 🔹 Iniciar el servidor
app.listen(port, () => {
  console.log(`🚀 Servidor corriendo en el puerto ${port}`);
});
