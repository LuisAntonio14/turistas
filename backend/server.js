const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000;

// Habilitar CORS para permitir solicitudes desde cualquier origen
app.use(cors({
  origin: '*', // Esto permitirá solicitudes desde cualquier origen
}));

app.use(bodyParser.json());

// Conectar a MongoDB
mongoose.connect('mongodb://localhost:27017/turistas', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Definir el esquema y el modelo de usuario
const usuarioSchema = new mongoose.Schema({
  nombre: String,
  contrasena: String,
});

const Usuario = mongoose.model('Usuario', usuarioSchema, 'usuario');

// Ruta para el inicio de sesión
app.post('/login', async (req, res) => {
  const { nombre, contrasena } = req.body;
  console.log(`Intento de login - Nombre: ${nombre}, Contraseña: ${contrasena}`);

  const user = await Usuario.findOne({ nombre, contrasena });

  if (user) {
    console.log('Login exitoso');
    res.status(200).send({ message: 'Login successful' });
  } else {
    console.log('Credenciales inválidas');
    res.status(401).send({ message: 'Invalid credentials' });
  }
});

// Iniciar el servidor en 0.0.0.0 para aceptar conexiones externas
app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on http://0.0.0.0:${port}`);
});
