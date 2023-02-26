# Detectar caras APP

Esta aplicación reconocerá caras en una imagen y las delimita, via amazon rekognition.

Esta aplicación usa ApiRest con Flask.

## Usará los siguientes servicios de AWS:
- Rekognition (Detecta caras en una imagen)

## Requisitos
- Python 3.6 o superior
- Cuenta de AWS

## Uso
- Clonar el repositorio
- Crear un entorno virtual
- Instalar los requerimientos
  - `pip install -r requirements.txt`
- Lanzar la aplicación
- Abrir el navegador en la dirección http://localhost:5000
- Subir una o más imágenes con caras y darle al botón "Subir"
- Ver el resultado