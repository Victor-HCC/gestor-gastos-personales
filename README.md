# 💰 Gestor de Gastos Personales

Este proyecto es una aplicación de consola escrita en Python que permite registrar, consultar y resumir ingresos y gastos personales. Fue desarrollada como proyecto final de una materia de programación, aplicando buenas prácticas y principios del Zen de Python.

---

## 🚀 Funcionalidades

- Registrar nuevos movimientos (ingresos o gastos).
- Seleccionar categorías personalizadas según el tipo.
- Visualizar todos los movimientos en una tabla clara.
- Ver un resumen general con ingresos, gastos y balance.
- Persistencia de datos en un archivo JSON.

---

## 📂 Estructura del Proyecto
```
gastos-personales/
├── data
│   └── movimientos.json
├── datos.py
├── gastos.py
├── main.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologías y dependencias

- Python 3.10+
- [Rich](https://rich.readthedocs.io/) – para mejorar la visualización en consola.
- [Questionary](https://github.com/tmbo/questionary) – para menús interactivos.

---

## 📦 Instalación

1. Clona o descarga este repositorio.
2. Entra a la carpeta del proyecto:
3. Crea un entorno virtual y activalo:

  ```bash
  python3 -m venv venv
  source venv/bin/activate   # Linux/macOS
  venv\Scripts\activate.bat  # Windows
  ```
4. Instala las dependencias:

  ```bash
  pip install -r requirements.txt
  ```

---

## ▶️ Uso

Ejecutá el programa principal con:

  ```bash
  python3 main.py
  ```

---

## 📁 Archivos generados automáticamente

- `data/movimientos.json`: contiene todos los movimientos registrados en formato JSON.

---

## 🧑‍💻 Autor

Proyecto realizado por Victor Cori.