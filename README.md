# API Notificaciones
"#api-notification-ssc" 

## Testing login:
	- {
		"username" : "Beto",
		"password" : "1234"
	}



	- En este proyecto se pretende crear endpoints para garantizar la autenticación y el envío de notificaciones a través de un correo electrónico.
	
	- Es necesario crear la configuración del entorno
	- Creando una app para el manejo de: usuarios y notificaciones

## Configuración del Entorno
	- pip install django==5 djangorestframework djangorestframework-simplejwt

	- django-admin startproject core .
	- django-admin startapp notitication


## 1.- Hacer el servicio de autenticación(Login)
	- Crear Modelos: Login, SendEmail
	- Crear Serializers: LoginSerializer, SendEmailSerializer
	- Crear Views(APIViews): LoginAPIView, SendAPIView

	- Manejar la autenticación

## 2.- Hacer el servicio de envío de correos(Send)
