window.CREDENCIALES = window.BTCCRuntime ? window.BTCCRuntime.loadJson('/data/credenciales_alumnos.json', []) : [];
window.validarCredencial = function(numero, password) {
  var alumno = window.CREDENCIALES.find(function(item) { return item.num === numero; });
  return !!(alumno && alumno.password === password);
};
window.obtenerAlumnoPorNumero = function(numero) {
  return window.CREDENCIALES.find(function(item) { return item.num === numero; });
};
