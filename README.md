**# SD Turbo GenAI

Este proyecto es una herramienta para la generación de imágenes utilizando inteligencia artificial, específicamente optimizada con modelos **SD-Turbo** para un rendimiento ultra rápido.

## 🚀 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:
- **Python 3.10** o superior.
- Un entorno compatible con **CUDA** (opcional, pero altamente recomendado para que la generación con PyTorch sea rápida utilizando tu tarjeta gráfica).

---

## 🛠️ Instalación y Configuración

El proyecto utiliza `uv` como gestor de paquetes para una instalación eficiente. Sigue estos pasos para configurar tu entorno:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd sd-turbo-genai
```

### 2. Crear y activar el entorno virtual
Si no tienes `uv` instalado, puedes instalarlo con `pip install uv`. Luego ejecuta:
```bash
uv venv
# En Windows:
.venv\Scripts\activate
# En Linux/macOS:
source .venv/bin/activate
```

### 3. Instalar PyTorch y dependencias adicionales
Dado que el proyecto genera imágenes, **es obligatorio descargar PyTorch**. Dependiendo de tu hardware, ejecuta el comando correspondiente:

#### Con soporte para GPU (NVIDIA CUDA - Recomendado):
```bash
uv add torch diffusers transformers numpy accelerate
```
*(Nota: Cambia `cu121` por la versión de CUDA instalada en tu sistema si es necesario).*

#### Solo CPU (Más lento):
```bash
uv pip install torch torchvision
```

### 4. Instalar las dependencias del proyecto
Termina de instalar el resto de paquetes necesarios especificados en el `pyproject.toml`:
```bash
uv pip install -e .
```

---

## 💻 Cómo Correr el Proyecto

Una vez que todas las dependencias y PyTorch estén correctamente instalados, puedes ejecutar el script principal desde la raíz del proyecto:

```bash
python src/sd_turbo_genai/__init__.py
```

*(Nota: Modifica esta ruta si tu punto de entrada principal o script de ejecución se encuentra en otro archivo dentro de `src`).*
**# SD Turbo GenAI 🚀

Herramienta de generación de imágenes con IA optimizada con **SD-Turbo**.

## 🛠️ Instalación

Asegúrate de tener **Python 3.10+** y ejecuta los siguientes comandos en tu terminal:

```bash
# 1. Clonar el proyecto
git clone <URL_DE_TU_REPOSITORIO>
cd sd-turbo-genai

# 2. Crear y activar el entorno virtual (usando uv)
uv venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 3. Instalar PyTorch y librerías necesarias
uv add torch diffusers transformers numpy accelerate
```

## 💻 Cómo Ejecutar

Para empezar a generar imágenes, corre el script principal:

```bash
uv src/sd_turbo_genai/__init__.py
```
