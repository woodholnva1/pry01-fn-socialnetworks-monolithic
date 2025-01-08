

//Funcion para Verificar el correo si ya Existe
URL_VAR = "http://127.0.0.1:5000/api"

// Funcion para Verificar Correo
function verifyMail() {
    fetch(URL_VAR + "/verifyMail")
    .then(response => response.json())
    .then(data => console.log(data));
  }


  

