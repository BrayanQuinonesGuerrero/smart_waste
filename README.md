# Proyecto Django: Smart waste

## Requisitos previos

Asegúrate de tener instalados los siguientes programas y herramientas antes de continuar:

- **Python** (versión 3.8 o superior)
- **pip** (gestor de paquetes de Python)
- **Git**
- **Virtualenv**

## Instrucciones de instalación

Sigue estos pasos para clonar y configurar el proyecto en tu máquina local.

### 1. Clonar el repositorio

Ejecuta el siguiente comando en tu terminal en linux para clonar el repositorio o en windows utiliza git bash para ejecutar todos los comandos:

```bash
git clone https://github.com/BrayanQuinonesGuerrero/smart_waste.git
```

Luego, navega al directorio del proyecto:

```bash
cd smart_waste
```

### 2. Crear y activar un entorno virtual

Crea un entorno virtual en el directorio del proyecto:

- En Linux/macOS:
  ```bash
  virtualenv .venv
  ```
- En Windows:
  ```bash
  python3 -m venv .venv
  ```

Activa el entorno virtual:

- En Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```
- En Windows:
  ```cmd
  .venv/Scripts/activate
  ```

### 3. Instalar las dependencias

Instala los paquetes necesarios utilizando `pip`:

```bash
pip3 install -r requirements.txt
```

### 4. Configurar la base de datos

Aplica las migraciones de la base de datos:

```bash
python3 manage.py migrate
```

### 6. Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo para verificar que todo funciona correctamente:

```bash
python3 manage.py runserver
```

Accede al proyecto en tu navegador en la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


## Contribución

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b nombre-de-la-rama`).
3. Realiza tus cambios y haz un commit (`git commit -m "Descripción del cambio"`).
4. Sube los cambios a tu rama (`git push origin nombre-de-la-rama`).
5. Crea un Pull Request.

---

¡Gracias por tu interés en este proyecto!