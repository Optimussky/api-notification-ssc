from rest_framework import status
from rest_framework.response import Response

def created_response(data, message="Registro guardado correctamente",): 
    return Response({"message": message, "data": data, "code": 201}, status.HTTP_201_CREATED)

def ok_logout(
    data=None,
    message="Cierre de Sesion con éxito",
): return Response({"message": message, "data": data, "code": 200}, status.HTTP_200_OK)

def ok_responsePing(
    data=None,
    message="Pop!, backend arriba",
): return Response({"message": message, "data": data, "code": 200}, status.HTTP_200_OK)

def permission_denied_response(
    data = None,
    message="correo o contraseña son incorrectos",
    error="Acceso denegado"
): return Response({"error": error, "message": message, "data": data, "code": 403}, status=status.HTTP_403_FORBIDDEN)

def ok_response(
    data,
    message="Acción realizada correctamente",
): return Response({"message": message, "data": data, "code": 200}, status.HTTP_200_OK)

def internal_error_response(
    data=None,
    error="Error servidor",
    message="Ha ocurrido un error inesperado al procesar la petición",
): return Response({"error": error, "message": message, "data": data, "code": 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def no_unauthorized_response(
    data=None,
    message="Contraseña incorrecta xxx"
): return Response({"data": data, "message": message, "code": 401}, status=status.HTTP_401_UNAUTHORIZED)

def not_found_response(
    data=None,
    error="Usuario no encontrado",
    message="Ha ocurrido un error, el objeto no existe"
): return Response({"error": error, "message": message, "data": data, "code": 404}, status=status.HTTP_404_NOT_FOUND)

def no_content_response(
    data=None,
    message="Sin contenido indica que la respuesta ha sido entregada con éxito",
): return Response({"data": data, "message": message, "code": 204}, status=status.HTTP_204_NO_CONTENT)

def bad_request_response(
    data,
    error="petición mala",
    message="Ha ocurrido un error, valida los campos",
): return Response({"error": error, "message": message, "data": data, "code": 400}, status=status.HTTP_400_BAD_REQUEST)