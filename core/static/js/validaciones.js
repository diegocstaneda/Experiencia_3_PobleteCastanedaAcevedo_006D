
$(function() 
    {
      $("#registro").validate({
           rules: {
                  email: {
                      required: true,
                      email: true
                  },
                  nombre:"required",
                  apellido: "required",
                  telefono: "required",
                  fecha: "required",
                  password: "required",
                  password2: {
                      required: true,
                      equalTo: "#password"
                  }   
                  
              }, 
          messages: {
              nombre:{
                  required: 'Ingresa tu nombre'
              },
              apellido:{
                  required: 'Ingresa tu apellido'
              },
              email: {
                  required: 'Ingresa tu correo electrónico',
                  email: 'Formato de correo no válido'
              },
              password: {
                  required: 'Ingresa una contraseña',
                  minlength: 'Caracteres insuficientes'
              },
              telefono:{
                  required: 'Ingrese un número de celular',
                  minlength: 'Cantidad de digitos insuficiente'
              },
              fecha:{
                  required: 'Seleccione una fecha válida',
                  min: 'Fecha no corresponde'
              },
              password2: {
                  required: 'Reingresa la contraseña',
                  equalTo: 'Las contraseñas ingresadas no coinciden',
                  minlength: 'Caracteres insuficientes'

              }
          }
      }); 
  }); 

$(function() 
{
    $("#direccion").validate({
         rules: {
                nombre:"required",
                apellido: "required",
                comuna1: "required",
                telefono: "required",
                direccion1: "required",
                numeroc: "required"         
                
            }, 
        messages: {
            nombre:{
                required: 'Ingresa tu nombre'
            },
            apellido:{
                required: 'Ingresa tu apellido'
            },
            comuna1:{
                required: 'Ingresa tu comuna'
              },
            direccion1:{
                required: 'Ingresa tu dirección'
            },
            numeroc: {
                required: 'Ingrese un número de casa',
                minlength: 'Cantidad de digitos insuficiente'
              },
            telefono:{
                required: 'Ingrese un número de celular',
                minlength: 'Cantidad de digitos insuficiente'
            },
        }
    }); 
}); 
