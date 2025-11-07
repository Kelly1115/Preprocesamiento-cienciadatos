# DOCUMENTACION.md

## 1. Introducción

Este proyecto fue desarrollado para aplicar el uso de Git, GitHub y GitHub Actions dentro de la materia *Cultura Digital y Sociedad*. El objetivo es practicar el manejo de repositorios, creación de ramas, automatización básica y documentación.

Dentro del repositorio se incluyen:
- Un archivo `preprocesamiento.py` con funciones de preprocesamiento de datos.
- Un workflow en GitHub Actions que valida el código.
- Archivos de documentación y evidencias del proceso realizado.

El propósito principal es aprender a trabajar con control de versiones, colaborar con ramas y usar herramientas de automatización.

---

## 2. Comandos Git Utilizados

**Configuración del usuario**
git config --global user.name "Kelly1115"
git config --global user.email "kelly.merino@unach.edu.ec"
git init
git clone https://github.com/Kelly1115/preprocesamiento-cienciadatos.git
git branch feature-preprocesamiento
git checkout feature-preprocesamiento
git add .
git commit -m "Creación del archivo preprocesamiento.py"
git push origin feature-preprocesamiento
git checkout main
git merge feature-preprocesamiento
git branch -d feature-preprocesamiento
git push origin main

Descripción de comandos:

- git config: configura el nombre y correo del usuario que firma los commits.

- git init: inicializa el repositorio local.

- git clone: clona un repositorio remoto en el equipo local.

- git branch y git checkout: crean y cambian de rama respectivamente.

- git add y git commit: agregan y registran los cambios en el historial.

- git push y git pull: sincronizan los cambios entre local y remoto.

- git merge: combina ramas.

- git branch -d: elimina una rama local después de fusionarla.

---

## 3. Automatización con GitHub Actions

Se configuró un workflow dentro de la carpeta .github/workflows llamado ci.yml.
Este archivo permite automatizar tareas como la verificación de código o la ejecución de scripts al hacer commits en el repositorio.
name: CI Workflow

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del repositorio
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: pip install pandas numpy

      - name: Ejecutar script de preprocesamiento
        run: python preprocesamiento.py

Este flujo se ejecuta automáticamente cuando se hace un push o un pull request hacia la rama principal (main).
Cuando GitHub muestra el ícono en verde, significa que el flujo se ejecutó correctamente, indicando que el código fue validado sin errores.

---

## 4. Evidencias
Comandos ejecutados

Se registraron los comandos utilizados para la configuración, creación de ramas, commits y sincronización con GitHub.

![Evidencia de comandos en terminal](imagenes\Captura_1.png)
![Evidencia de comandos en terminal](imagenes\Captura_2.png)
![Evidencia de comandos en terminal](imagenes\Captura_3.png)
![Evidencia de comandos en terminal](imagenes\Captura_4.png)

Pull Request y Fusión

Se realizó un Pull Request desde la rama feature-preprocesamiento hacia main.
Después de la revisión simulada, se aprobó la fusión y se eliminó la rama de desarrollo.

![Evidencia de Pull Request y fusión](imagenes\Captura_5.png)
![Evidencia de Pull Request y fusión](imagenes\Captura_6.png)
![Evidencia de Pull Request y fusión](imagenes\Captura_7.png)
![Evidencia de Pull Request y fusión](imagenes\Captura_8.png)
![Evidencia de Pull Request y fusión](imagenes\Captura_9.png)

Ejecución exitosa del Workflow

La automatización mediante GitHub Actions se ejecutó correctamente.
El estado verde indica que el flujo completó todas las tareas sin errores.

- La ejecución del workflow fue exitosa, confirmando que la configuración del archivo ci.yml es funcional.

![Evidencia del workflow en verde](imagenes\Captura_10.png)


