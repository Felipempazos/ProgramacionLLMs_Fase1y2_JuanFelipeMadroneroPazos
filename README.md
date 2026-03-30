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
myquestions/
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

* Análisis de datos con agrupación (`groupby`)
* Se identifica el tipo de aprendizaje dominante
* Se genera una recomendación personalizada
* Se define explícitamente el criterio en caso de empate

---

### 2️⃣ Física

* Reconstrucción de datos a partir de información incompleta
* Se calcula la velocidad usando diferencias de posición
* Se manejan valores faltantes (NaN) de forma controlada
* Se detectan mediciones inconsistentes mediante un umbral bien definido

---

### 3️⃣ Música

* Machine Learning no supervisado (`KMeans`)
* Se agrupan usuarios según hábitos de escucha
* Se interpretan los clusters (no solo se asignan)
* Se define un criterio claro para clasificar perfiles ("especializado" vs "diverso")

---

### 4️⃣ Literatura

* Machine Learning supervisado (`LogisticRegression`)
* Se analizan hábitos de lectura
* Se usan probabilidades (`predict_proba`) en lugar de predicciones directas
* Se identifican casos de baja confianza del modelo

---

## Librerías utilizadas

* pandas
* numpy
* scikit-learn

---

## Objetivo

Más que solo usar librerías, la idea fue:

* aplicar conceptos del curso de forma práctica
* evitar problemas genéricos o repetidos
* diseñar ejercicios con sentido real

---

## Validación

Se probaron los generadores y las funciones con múltiples casos aleatorios para asegurar que:

* cada generador produce entradas válidas
* el output esperado coincide exactamente con la solución
* no hay inconsistencias entre enunciado y código
* los casos cubren situaciones normales y casos borde

---

## Nota final

Los generadores fueron diseñados para que:

* generen datos diferentes cada vez
* sean reproducibles en su lógica
* funcionen correctamente con un autograder

---

## Comentario 

Intenté que el trabajo no fuera lo típico de "entrene un modelo y ya", sino que cada problema tuviera una lógica clara y una aplicación más real. Algunos son más de análisis, otros de machine learning, pero todos buscan resolver algo concreto y entendible.


