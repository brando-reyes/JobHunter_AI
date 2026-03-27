# JobHunter AI

JobHunter AI es una aplicación web desarrollada con **Python y Flask** que analiza automáticamente ofertas de trabajo remotas y detecta las habilidades más demandadas en el mercado tecnológico.

El sistema obtiene ofertas desde RemoteOK, analiza las descripciones con procesamiento de lenguaje natural (NLP) y genera estadísticas de las tecnologías más solicitadas.

---

## Características

* Web scraping de ofertas de trabajo remotas
* Análisis automático de descripciones de empleo
* Detección de habilidades técnicas (Python, SQL, AWS, etc.)
* Ranking de habilidades más demandadas
* Interfaz web simple para visualizar resultados
* Analizador manual de descripciones de trabajo

---

## Tecnologías utilizadas

* Python
* Flask
* Requests
* BeautifulSoup
* spaCy (NLP)
* HTML

---

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/jobhunter-ai.git
cd jobhunter-ai
```

2. Crear entorno virtual

```bash
python -m venv .venv
```

3. Activar entorno virtual

Windows:

```bash
.venv\Scripts\activate
```

Mac / Linux:

```bash
source .venv/bin/activate
```

4. Instalar dependencias

```bash
pip install flask requests beautifulsoup4 spacy
python -m spacy download en_core_web_sm
```

---

## Ejecutar la aplicación

```bash
python app.py
```

Luego abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## Cómo funciona

1. El sistema obtiene ofertas de trabajo desde RemoteOK
2. Se analizan las descripciones de los trabajos
3. Se detectan habilidades técnicas usando NLP
4. Se generan estadísticas de las habilidades más demandadas

---

## Ejemplo de salida

Top habilidades más demandadas:

* Python
* API
* Git
* SQL
* AWS

---

## Futuras mejoras

* Dashboard con gráficos de habilidades
* Comparación entre CV y mercado laboral
* Sistema de alertas de empleo
* Análisis automático diario de ofertas

---

## Autor

Proyecto desarrollado como parte de un portafolio de backend en Python.
