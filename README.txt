# Proyecto - Programación con LLMs

## Autor

Juan Felipe Madroñero Pazos
Felipe.madronero@udea.edu.co

---

## Descripción general

Este trabajo consiste en la creación de 4 problemas relacionados con análisis de datos y machine learning, donde cada uno tiene su propio generador de casos de uso.

La idea no fue hacer ejercicios típicos, sino plantear situaciones más reales, donde los datos sirvan para tomar decisiones o analizar comportamientos, como pasaría en la vida real.

Cada problema tiene:

* su enunciado (`.txt`)
* su generador de casos (`usecase-generator.py`)

---

## Estructura del proyecto

```
question-0001.txt
question-0001-usecase-generator.py

question-0002.txt
question-0002-usecase-generator.py

question-0003.txt
question-0003-usecase-generator.py

question-0004.txt
question-0004-usecase-generator.py
```

---

## Enfoque de los problemas

Intenté que los 4 problemas fueran diferentes tanto en contexto como en la forma de resolverlos:

### 1️⃣ Pedagogía

* Análisis de datos con agrupación
* Se identifica el tipo de aprendizaje y se recomienda una estrategia

### 2️⃣ Física

* Reconstrucción de datos (cálculo)
* Se calcula velocidad a partir de posición y tiempo
* También se detectan posibles errores en sensores

### 3️⃣ Música

* Machine Learning no supervisado (KMeans)
* Se agrupan usuarios según hábitos musicales
* No solo se agrupan, también se interpreta el comportamiento

### 4️⃣ Literatura

* Machine Learning supervisado (LogisticRegression)
* Se analiza el hábito lector
* Se detectan casos donde el modelo tiene baja confianza

---

## Librerías utilizadas

* pandas
* numpy
* scikit-learn

---

## Objetivo

Más que solo usar librerías, la idea fue:

* aplicar conceptos del curso
* evitar problemas genéricos
* hacer ejercicios que tengan sentido práctico

---

## Nota final

Los generadores fueron diseñados para que:

* generen datos diferentes cada vez
* produzcan exactamente el output esperado
* funcionen correctamente con un autograder

---

## 

Intenté que el trabajo no fuera lo típico de "entrene un modelo y ya", sino que cada problema tuviera una lógica clara y una aplicación más real. Algunos fueron más de análisis, otros de ML, pero todos con intención de resolver algo concreto.

---
