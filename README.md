# ApiLatam

Prueba tecnica de backend con python django rest_framework postgres y docker

## Recursos para funcionalidad de api
python 3.8,
docker
postgres

Clone el repositorio

`$ git clone url`

## ejecucion

Puedes iniciar el imagen 

`$ docker-compose up --build -d`
`$ docker-compose up`
## pruebas en postman
### signup user (post)
` http://127.0.0.1:8000/users/signup/`
### login user (post)
` http://127.0.0.1:8000/users/login/`
### verify user (post)
` http://127.0.0.1:8000/users/verify/`
### verify user_profile (put, patch) de profile
` http://127.0.0.1:8000/users/id/profile/`
### login user (post)
` http://127.0.0.1:8000/users/2/`
### login user (get)
` http://127.0.0.1:8000/users/`
### login product (get)
` http://127.0.0.1:8000/products/`
### login product (put)
` http://127.0.0.1:8000/products/2/`
### login product (destroy)
` http://127.0.0.1:8000/products/2/`


## peticiones de api 
get, post, put patch, delete
 en postman recomendable u otros 

## Cómo trabajar en aws solo descripcion un resumen EC2

### Primer paso 
crear una cuenta  en aws ya sea personal o empresa
### segundo paso 
crear una instancia en EcS2, como un servidor linux u otros o una computadora en la nube, 
### tercero paso 
Configurar la nesecidades del instancia ip
### cuarto paso 
generar las credenciales para conectarce al instancia 
### quinto paso 
actualizar el servidor linux si es nesessario y y subir la aplicacion 


## si se require trabajar con diferentes instacias de aws IAM, EC2, S3, RDS, Lambda
### crear cada instancia 



## Cómo contribuir

Puedes crear un pull request al proyecto

## Licencia

## :c palta algunas configuracion  .env configuracion de setting tanto para produccion y dev d

MIT
