import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# -------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------
st.set_page_config(
    page_title="Manual de Ciencia de Datos",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de sesión
if 'completados' not in st.session_state:
    st.session_state.completados = set()
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
if 'flashcard_actual' not in st.session_state:
    st.session_state.flashcard_actual = None
if 'mostrar_respuesta' not in st.session_state:
    st.session_state.mostrar_respuesta = False

# -------------------------------
# CONTENIDO TEÓRICO
# -------------------------------
temas = {
    "💻 Programación en Python": {
        "Variables": {
            "definicion": "Una variable almacena un valor que puede cambiar durante la ejecución del programa.",
            "ejemplo": "x = 10\nnombre = 'Santiago'\nprint(nombre)",
            "pregunta": "¿Qué imprime este código?\nx = 5\ny = x + 3\nprint(y)",
            "opciones": ["5", "8", "3", "53"],
            "respuesta_correcta": "8"
        },
        "Listas": {
            "definicion": "Una lista es una colección ordenada y modificable de elementos. Se define entre corchetes [].",
            "ejemplo": "frutas = ['manzana', 'banana', 'pera']\nprint(frutas[0])",
            "pregunta": "¿Qué devuelve frutas[1] si frutas = ['manzana', 'banana', 'pera']?",
            "opciones": ["manzana", "banana", "pera", "Error"],
            "respuesta_correcta": "banana"
        },
        "Diccionarios": {
            "definicion": "Un diccionario almacena datos en pares clave-valor. Se define entre llaves {}.",
            "ejemplo": "persona = {'nombre': 'Santiago', 'edad': 24}\nprint(persona['nombre'])",
            "pregunta": "¿Cómo accedes al valor 'Juan' en persona = {'nombre': 'Juan', 'edad': 30}?",
            "opciones": ["persona.nombre", "persona['nombre']", "persona[0]", "persona(nombre)"],
            "respuesta_correcta": "persona['nombre']"
        },
        "Bucles": {
            "definicion": "Los bucles permiten repetir una acción varias veces. En Python los más usados son for y while.",
            "ejemplo": "for i in range(5):\n    print('Iteración', i)",
            "pregunta": "¿Cuántas veces se ejecuta el bucle? for i in range(3):",
            "opciones": ["2", "3", "4", "Infinitas"],
            "respuesta_correcta": "3"
        },
        "Condicionales": {
            "definicion": "Permiten ejecutar bloques de código solo si se cumple una condición.",
            "ejemplo": "edad = 18\nif edad >= 18:\n    print('Mayor de edad')",
            "pregunta": "¿Qué imprime? x = 10\nif x > 5:\n    print('A')\nelse:\n    print('B')",
            "opciones": ["A", "B", "AB", "Nada"],
            "respuesta_correcta": "A"
        },
        "Funciones": {
            "definicion": "Una función agrupa un bloque de código que se puede reutilizar. Se define con def.",
            "ejemplo": "def saludar(nombre):\n    return f'Hola {nombre}'",
            "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
            "opciones": ["function", "def", "func", "define"],
            "respuesta_correcta": "def"
        }
    },

    "🧮 Ciencia de Datos con pandas": {
        "DataFrames": {
            "definicion": "Un DataFrame es una estructura de datos de dos dimensiones (filas y columnas) en pandas.",
            "ejemplo": "df = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Edad': [23, 30]})",
            "mostrar_visual": True,
            "pregunta": "¿Qué librería se usa para crear DataFrames?",
            "opciones": ["numpy", "pandas", "matplotlib", "scipy"],
            "respuesta_correcta": "pandas"
        },
        "Series": {
            "definicion": "Una Serie es una columna individual de un DataFrame. Es un arreglo unidimensional con etiquetas.",
            "ejemplo": "serie = pd.Series([10, 20, 30])",
            "pregunta": "¿Cuántas dimensiones tiene una Serie de pandas?",
            "opciones": ["0", "1", "2", "3"],
            "respuesta_correcta": "1"
        },
        "Limpieza de datos": {
            "definicion": "Proceso de preparar datos eliminando valores nulos, duplicados o erróneos.",
            "ejemplo": "df = df.dropna()\ndf = df.drop_duplicates()",
            "pregunta": "¿Qué método elimina filas con valores nulos?",
            "opciones": ["remove_null()", "dropna()", "delete_na()", "clear_null()"],
            "respuesta_correcta": "dropna()"
        },
        "Filtrado de datos": {
            "definicion": "Permite seleccionar filas de un DataFrame que cumplen con una condición específica.",
            "ejemplo": "df_filtrado = df[df['Edad'] > 25]",
            "pregunta": "¿Cómo filtras filas donde Edad > 30?",
            "opciones": ["df.filter(Edad > 30)", "df[df['Edad'] > 30]", "df.where(Edad > 30)", "df(Edad > 30)"],
            "respuesta_correcta": "df[df['Edad'] > 30]"
        },
        "Agrupamiento (groupby)": {
            "definicion": "Permite agrupar datos según columnas y aplicar funciones de agregación.",
            "ejemplo": "df.groupby('Departamento').mean()",
            "pregunta": "¿Qué método se usa para agrupar datos en pandas?",
            "opciones": ["group()", "groupby()", "aggregate()", "cluster()"],
            "respuesta_correcta": "groupby()"
        }
    },

    "🗄️ Bases de Datos y SQL": {
        "SELECT": {
            "definicion": "SELECT se usa para recuperar datos de una base de datos.",
            "ejemplo": "SELECT nombre, edad FROM clientes WHERE edad > 30;",
            "pregunta": "¿Qué palabra clave se usa para seleccionar todas las columnas?",
            "opciones": ["ALL", "*", "EVERYTHING", "COLUMNS"],
            "respuesta_correcta": "*"
        },
        "WHERE": {
            "definicion": "WHERE filtra registros según una condición.",
            "ejemplo": "SELECT * FROM productos WHERE precio > 100;",
            "pregunta": "¿Qué cláusula filtra resultados en SQL?",
            "opciones": ["FILTER", "WHERE", "IF", "WHEN"],
            "respuesta_correcta": "WHERE"
        },
        "JOIN": {
            "definicion": "JOIN combina filas de dos o más tablas basadas en una columna relacionada.",
            "ejemplo": "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id;",
            "pregunta": "¿Qué tipo de JOIN devuelve solo registros con coincidencias en ambas tablas?",
            "opciones": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "OUTER JOIN"],
            "respuesta_correcta": "INNER JOIN"
        }
    },

    "📊 Visualización de Datos": {
        "Gráfico de barras": {
            "definicion": "Se utiliza para comparar cantidades entre diferentes categorías.",
            "ejemplo": "plt.bar(categorias, valores)",
            "mostrar_visual": True,
            "pregunta": "¿Qué tipo de gráfico es mejor para comparar categorías?",
            "opciones": ["Líneas", "Barras", "Dispersión", "Pastel"],
            "respuesta_correcta": "Barras"
        },
        "Histograma": {
            "definicion": "Muestra la distribución de una variable numérica.",
            "ejemplo": "plt.hist(datos, bins=30)",
            "mostrar_visual": True,
            "pregunta": "¿Qué gráfico muestra la distribución de frecuencias?",
            "opciones": ["Barras", "Líneas", "Histograma", "Dispersión"],
            "respuesta_correcta": "Histograma"
        },
        "Gráfico de líneas": {
            "definicion": "Se utiliza para mostrar tendencias a lo largo del tiempo.",
            "ejemplo": "plt.plot(x, y)",
            "mostrar_visual": True,
            "pregunta": "¿Qué gráfico es ideal para mostrar tendencias temporales?",
            "opciones": ["Barras", "Líneas", "Pastel", "Histograma"],
            "respuesta_correcta": "Líneas"
        }
    },

    "🤖 Machine Learning": {
        "Regresión lineal": {
            "definicion": "Modelo que predice una variable continua a partir de variables independientes.",
            "ejemplo": "from sklearn.linear_model import LinearRegression\nmodelo = LinearRegression()",
            "pregunta": "¿Qué tipo de variable predice la regresión lineal?",
            "opciones": ["Categórica", "Binaria", "Continua", "Ordinal"],
            "respuesta_correcta": "Continua"
        },
        "Clasificación": {
            "definicion": "Modelo que asigna etiquetas a observaciones según sus características.",
            "ejemplo": "from sklearn.tree import DecisionTreeClassifier",
            "pregunta": "¿Qué tipo de variable predice un modelo de clasificación?",
            "opciones": ["Continua", "Categórica", "Numérica", "Temporal"],
            "respuesta_correcta": "Categórica"
        },
        "Validación cruzada": {
            "definicion": "Técnica para evaluar el rendimiento dividiendo datos en múltiples subconjuntos.",
            "ejemplo": "from sklearn.model_selection import cross_val_score",
            "pregunta": "¿Para qué sirve la validación cruzada?",
            "opciones": ["Limpiar datos", "Evaluar modelos", "Crear variables", "Visualizar datos"],
            "respuesta_correcta": "Evaluar modelos"
        }
    }
}

# -------------------------------
# FUNCIONES AUXILIARES
# -------------------------------
def mostrar_contenido_simple(area_nombre, tema, contenido):
    tema_id = f"{area_nombre}_{tema}"
    completado = tema_id in st.session_state.completados
    
    with st.expander(f"{'✅' if completado else '📖'} {tema}"):
        st.write(f"**{contenido['definicion']}**")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.code(contenido["ejemplo"], language="python")
        
        with col2:
            if st.button("✓ Marcar", key=f"btn_{tema_id}", use_container_width=True):
                if tema_id in st.session_state.completados:
                    st.session_state.completados.discard(tema_id)
                else:
                    st.session_state.completados.add(tema_id)
                st.rerun()
        
        # Mostrar visualización si aplica
        if contenido.get("mostrar_visual"):
            if "pandas" in area_nombre.lower():
                df = pd.DataFrame({"Nombre": ["Ana", "Luis", "Carlos"], "Edad": [23, 30, 25]})
                st.dataframe(df, use_container_width=True)
            
            elif "Visualización" in area_nombre:
                fig, ax = plt.subplots(figsize=(6, 3))
                
                if "barras" in tema.lower():
                    ax.bar(['A', 'B', 'C', 'D'], [10, 20, 15, 25], color='steelblue')
                elif "Histograma" in tema:
                    ax.hist(np.random.normal(100, 15, 1000), bins=30, color='coral', edgecolor='black')
                elif "líneas" in tema.lower():
                    x = list(range(1, 11))
                    y = [i**1.5 for i in x]
                    ax.plot(x, y, marker='o')
                    ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
                plt.close()

def obtener_todas_preguntas():
    """Obtiene todas las preguntas disponibles"""
    preguntas = []
    for area, contenidos in temas.items():
        for tema, info in contenidos.items():
            if 'pregunta' in info:
                preguntas.append({
                    'area': area,
                    'tema': tema,
                    'pregunta': info['pregunta'],
                    'opciones': info['opciones'],
                    'respuesta_correcta': info['respuesta_correcta'],
                    'definicion': info['definicion']
                })
    return preguntas

def juego_flashcards():
    st.subheader("🎴 Flashcards - Repaso Rápido")
    st.write("Estudia los conceptos. Haz clic para ver la respuesta.")
    
    preguntas = obtener_todas_preguntas()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔀 Nueva tarjeta", use_container_width=True):
            st.session_state.flashcard_actual = random.choice(preguntas)
            st.session_state.mostrar_respuesta = False
        
        if st.session_state.flashcard_actual is None:
            st.session_state.flashcard_actual = random.choice(preguntas)
        
        flashcard = st.session_state.flashcard_actual
        
        # Tarjeta
        st.markdown("---")
        st.markdown(f"### {flashcard['area']}")
        st.markdown(f"#### 📌 {flashcard['tema']}")
        st.markdown("---")
        
        if not st.session_state.mostrar_respuesta:
            st.markdown(f"### ❓ {flashcard['pregunta']}")
            if st.button("👁️ Ver respuesta", use_container_width=True):
                st.session_state.mostrar_respuesta = True
                st.rerun()
        else:
            st.markdown(f"### ✅ {flashcard['respuesta_correcta']}")
            st.info(f"💡 {flashcard['definicion']}")
            if st.button("➡️ Siguiente", use_container_width=True):
                st.session_state.flashcard_actual = random.choice(preguntas)
                st.session_state.mostrar_respuesta = False
                st.rerun()

def juego_multiplechoice():
    st.subheader("🎯 Quiz - Multiple Choice")
    st.write("Responde correctamente para ganar puntos.")
    
    # Mostrar puntuación
    col1, col2, col3 = st.columns(3)
    with col2:
        st.metric("🏆 Puntos totales", st.session_state.puntos)
    
    preguntas = obtener_todas_preguntas()
    
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)
    
    pregunta = st.session_state.pregunta_actual
    
    st.markdown("---")
    st.markdown(f"**📚 {pregunta['area']} - {pregunta['tema']}**")
    st.markdown(f"### {pregunta['pregunta']}")
    
    # Opciones
    respuesta_usuario = st.radio(
        "Selecciona tu respuesta:",
        pregunta['opciones'],
        key="quiz_respuesta"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✓ Verificar", use_container_width=True):
            if respuesta_usuario == pregunta['respuesta_correcta']:
                st.success("¡Correcto! 🎉 +10 puntos")
                st.session_state.puntos += 10
                st.balloons()
            else:
                st.error(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta_correcta']}")
            
            st.info(f"💡 {pregunta['definicion']}")
    
    with col2:
        if st.button("➡️ Siguiente pregunta", use_container_width=True):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
    
    # Resetear puntos
    st.markdown("---")
    if st.button("🔄 Reiniciar puntuación"):
        st.session_state.puntos = 0
        st.rerun()

# -------------------------------
# BARRA LATERAL
# -------------------------------
st.sidebar.title("📘 Manual de Ciencia de Datos")

modo = st.sidebar.radio(
    "Selecciona un modo:",
    ["📚 Aprender", "🎴 Flashcards", "🎯 Quiz"]
)

st.sidebar.markdown("---")

if modo == "📚 Aprender":
    st.sidebar.subheader("Áreas de estudio")
    area = st.sidebar.selectbox("", list(temas.keys()))
    
    # Progreso simplificado
    total_temas = sum(len(c) for c in temas.values())
    completados = len(st.session_state.completados)
    
    st.sidebar.markdown("---")
    st.sidebar.metric("✅ Progreso", f"{completados}/{total_temas}")
    st.sidebar.progress(completados / total_temas if total_temas > 0 else 0)

st.sidebar.markdown("---")
st.sidebar.metric("🏆 Puntos", st.session_state.puntos)

st.sidebar.markdown("---")
if st.sidebar.button("🔄 Reiniciar todo"):
    st.session_state.completados = set()
    st.session_state.puntos = 0
    st.rerun()

# -------------------------------
# CONTENIDO PRINCIPAL
# -------------------------------
if modo == "📚 Aprender":
    st.title(f"{area}")
    st.markdown("Explora los conceptos y marca los que ya domines.")
    st.markdown("---")
    
    for tema, contenido in temas[area].items():
        mostrar_contenido_simple(area, tema, contenido)

elif modo == "🎴 Flashcards":
    juego_flashcards()

elif modo == "🎯 Quiz":
    juego_multiplechoice()

# Pie de página
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "💡 Creado para aprender Ciencia de Datos"
    "</div>",
    unsafe_allow_html=True
)

