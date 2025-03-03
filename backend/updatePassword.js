const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

mongoose.connect('mongodb://localhost:27017/turistas', { useNewUrlParser: true, useUnifiedTopology: true });

const usuarioSchema = new mongoose.Schema({
  nombre: String,
  contrasena: String,
});

const Usuario = mongoose.model('Usuario', usuarioSchema, 'usuario');

async function updatePassword() {
  const nombre = 'admin';
  const newPassword = '1'; // The current password to hash
  const hashedPassword = await bcrypt.hash(newPassword, 10); // Hash the password

  await Usuario.updateOne({ nombre }, { contrasena: hashedPassword });
  console.log('Password updated successfully');
  mongoose.connection.close();
}

updatePassword().catch(err => {
  console.error(err);
  mongoose.connection.close();
});
