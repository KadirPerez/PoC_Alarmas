# Prueba de Concepto: Sistema de Gestión de Alarmas Multiplataforma

## Descripción

Esta prueba de concepto demuestra un sistema de gestión de alarmas multiplataforma implementado en Python. El sistema utiliza archivos CSV para almacenar y gestionar alarmas y sugerencias. La interfaz de usuario se realiza a través de la terminal, y el acceso al sistema se realiza mediante un API Gateway.

## Características

- **Generación de Alarmas**: Crear alarmas con descripción, métodos de notificación y fecha.
- **Visualización de Alarmas**: Listar todas las alarmas almacenadas.
- **Eliminación de Alarmas**: Borrar alarmas existentes.
- **Sugerencias**: Generar sugerencias basadas en las alarmas almacenadas.

## Tecnologías y Herramientas

- **Lenguaje de Programación**: Python
- **Almacenamiento de Datos**: Archivos CSV
- **Interfaz de Usuario**: Terminal
- **API Gateway**: Acceso a funcionalidades del sistema

### Requisitos

- Python 3

## Uso

1. **Ejecuta el script principal** en la terminal:

    ```bash
    python gui.py
    ```

2. **Interactúa con la interfaz de usuario** en la terminal para:

   - **Generar una alarma**: Sigue las instrucciones para ingresar una descripción, métodos de notificación y fecha.
   - **Visualizar alarmas**: Solicita la lista de todas las alarmas almacenadas.
   - **Eliminar una alarma**: Proporciona el ID de la alarma que deseas eliminar.
   - **Generar sugerencias**: Llama al API para obtener sugerencias basadas en las alarmas.

## API

El API Gateway proporciona acceso a las siguientes funcionalidades:

- **Generar Alarma**: `POST /generarAlarma`
  - Parámetros: `token`, `texto`, `metodos`, `fecha`
- **Mostrar Alarmas**: `GET /mostrarAlarmas`
  - Parámetro: `token`
- **Eliminar Alarma**: `DELETE /eliminarAlarma`
  - Parámetros: `id`, `token`
- **Generar Sugerencia**: `GET /generarSugerencia`
  - Parámetro: `token`
