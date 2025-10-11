import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------
st.set_page_config(
    page_title="Manual de Ciencia de Datos",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📘 Manual Interactivo de Ciencia de Datos con Python y Streamlit")
st.markdown("Seleccioná un área en el menú lateral para explorar definiciones, ejemplos y ejercicios prácticos.")

# -------------------------------
# CONTENIDO TEÓRICO AGRUPADO
# -------------------------------
temas = {
    "💻 Programación en Python": {
        "Variables": {
            "definicion": "Una variable almacena un valor que puede cambiar durante la ejecución del programa. Se utiliza para guardar datos.",
            "ejemplo": "x = 10\nnombre = 'Santiago'\nprint(nombre)"
        },
        "Listas": {
            "definicion": "Una lista es una colección ordenada y modificable de elementos. Se define entre corchetes [].",
            "ejemplo": "frutas = ['manzana', 'banana', 'pera']\nprint(frutas[0])"
        },
        "Diccionarios": {
            "definicion": "Un diccionario almacena datos en pares clave-valor. Se define entre llaves {}.",
            "ejemplo": "persona = {'nombre': 'Santiago', 'edad': 24}\nprint(persona['nombre'])"
        },
        "Bucles": {
            "definicion": "Los bucles permiten repetir una acción varias veces. En Python los más usados son for y while.",
            "ejemplo": "for i in range(5):\n    print('Iteración', i)"
        },
        "Condicionales": {
            "definicion": "Permiten ejecutar bloques de código solo si se cumple una condición.",
            "ejemplo": "edad = 18\nif edad >= 18:\n    print('Es mayor de edad')\nelse:\n    print('Es menor de edad')"
        },
        "Funciones": {
            "definicion": "Una función agrupa un bloque de código que se puede reutilizar. Se define con la palabra clave def.",
            "ejemplo": "def saludar(nombre):\n    print('Hola', nombre)\nsaludar('Santiago')"
        },
        "Tuplas": {
            "definicion": "Una tupla es una colección ordenada e inmutable de elementos. Se define entre paréntesis ().",
            "ejemplo": "coordenadas = (10, 20)\nprint(coordenadas[0])"
        },
        "Conjuntos": {
            "definicion": "Un conjunto es una colección no ordenada de elementos únicos. Se define con llaves {} o con la función set().",
            "ejemplo": "numeros = {1, 2, 3, 3, 2}\nprint(numeros)"
        },
        "Comprensión de listas": {
            "definicion": "Permite crear listas de forma concisa usando una expresión dentro de corchetes.",
            "ejemplo": "cuadrados = [x**2 for x in range(5)]\nprint(cuadrados)"
        },
        "Manejo de errores": {
            "definicion": "Se utiliza try-except para manejar errores durante la ejecución del programa.",
            "ejemplo": "try:\n    resultado = 10 / 0\nexcept ZeroDivisionError:\n    print('No se puede dividir por cero')"
        },
        "Módulos y paquetes": {
            "definicion": "Los módulos son archivos de Python que contienen funciones y clases. Los paquetes son colecciones de módulos.",
            "ejemplo": "import math\nprint(math.sqrt(16))"
        }
    },

    "🧮 Ciencia de Datos con pandas": {
        "DataFrames": {
            "definicion": "Un DataFrame es una estructura de datos de dos dimensiones (filas y columnas) usada en pandas para analizar datos.",
            "ejemplo": "df = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Edad': [23, 30]})\nst.write(df)"
        },
        "Series": {
            "definicion": "Una Serie es una columna individual de un DataFrame. Es un arreglo unidimensional con etiquetas.",
            "ejemplo": "serie = pd.Series([10, 20, 30])\nst.write(serie)"
        },
        "Limpieza de datos": {
            "definicion": "Proceso de preparar y corregir un conjunto de datos eliminando valores nulos, duplicados o erróneos.",
            "ejemplo": "df = df.dropna()\ndf = df.drop_duplicates()"
        },
        "Filtrado de datos": {
            "definicion": "Permite seleccionar filas de un DataFrame que cumplen con una condición específica.",
            "ejemplo": "df = df[df['Edad'] > 25]"
        },
        "Agrupamiento (groupby)": {
            "definicion": "Permite agrupar datos según una o más columnas y aplicar funciones de agregación.",
            "ejemplo": "df.groupby('Departamento').mean()"
        },
        "Merge y Join": {
            "definicion": "Permite combinar dos DataFrames basados en columnas comunes.",
            "ejemplo": "pd.merge(df1, df2, on='id')"
        },
        "Pivot tables": {
            "definicion": "Permite reorganizar datos en forma de tabla dinámica.",
            "ejemplo": "df.pivot_table(values='Ventas', index='Mes', columns='Producto')"
        },
        "Apply": {
            "definicion": "Permite aplicar una función a lo largo de un eje de un DataFrame.",
            "ejemplo": "df['columna'].apply(lambda x: x*2)"
        }
    },

    "🗄️ Bases de Datos y SQL": {
        "Definición de Base de Datos": {
            "definicion": "Una base de datos es una colección organizada de información o datos, generalmente almacenada y accedida electrónicamente.",
            "ejemplo": "-- Ejemplo en SQL\nCREATE TABLE clientes (\n  id INTEGER PRIMARY KEY,\n  nombre TEXT,\n  edad INTEGER\n);"
        },
        "Consulta SELECT": {
            "definicion": "SELECT se usa para recuperar datos de una base de datos.",
            "ejemplo": "SELECT nombre, edad FROM clientes WHERE edad > 30;"
        },
        "JOIN": {
            "definicion": "JOIN se utiliza para combinar filas de dos o más tablas basadas en una columna relacionada.",
            "ejemplo": "SELECT pedidos.id, clientes.nombre\nFROM pedidos\nJOIN clientes ON pedidos.cliente_id = clientes.id;"
        }
    },

    "📊 Visualización de Datos": {
        "Gráfico de barras": {
            "definicion": "Se utiliza para comparar cantidades entre diferentes categorías.",
            "ejemplo": "categorias = ['A', 'B', 'C']\nvalores = [10, 20, 15]\nplt.bar(categorias, valores)\nplt.title('Gráfico de barras')\nplt.show()"
        },
        "Histograma": {
            "definicion": "Muestra la distribución de una variable numérica dividiendo los datos en intervalos.",
            "ejemplo": "datos = [1,2,2,3,3,3,4,4,5]\nplt.hist(datos, bins=5)\nplt.title('Histograma')\nplt.show()"
        },
        "Gráfico de líneas": {
            "definicion": "Se utiliza para mostrar tendencias a lo largo del tiempo.",
            "ejemplo": "x = [1, 2, 3, 4]\ny = [10, 20, 25, 30]\nplt.plot(x, y)\nplt.title('Gráfico de líneas')\nplt.show()"
        },
        "Gráfico de dispersión": {
            "definicion": "Muestra la relación entre dos variables numéricas.",
            "ejemplo": "x = [1, 2, 3, 4]\ny = [10, 20, 25, 30]\nplt.scatter(x, y)\nplt.title('Gráfico de dispersión')\nplt.show()"
        },
        "Mapa de calor": {
            "definicion": "Representa datos en forma de matriz con colores que indican intensidad.",
            "ejemplo": "datos = [[1, 2], [3, 4]]\nsns.heatmap(datos, annot=True)\nplt.title('Mapa de calor')\nplt.show()"
        }
    },

    "🤖 Machine Learning": {
        "Regresión lineal": {
            "definicion": "Modelo que predice una variable continua a partir de una o más variables independientes.",
            "ejemplo": "from sklearn.linear_model import LinearRegression\nmodelo = LinearRegression()\nmodelo.fit(X, y)"
        },
        "Clasificación": {
            "definicion": "Modelo que asigna etiquetas a observaciones según sus características.",
            "ejemplo": "from sklearn.tree import DecisionTreeClassifier\nmodelo = DecisionTreeClassifier()\nmodelo.fit(X, y)"
        },
        "Validación cruzada": {
            "definicion": "Técnica para evaluar el rendimiento de un modelo dividiendo los datos en múltiples subconjuntos.",
            "ejemplo": "from sklearn.model_selection import cross_val_score\nscores = cross_val_score(modelo, X, y, cv=5)"
        }
    }
}

# -------------------------------
# FUNCIONES AUXILIARES
# -------------------------------
def mostrar_contenido(tema, contenido):
    with st.expander(f"📖 {tema}"):
        st.write(f"**Definición:** {contenido['definicion']}")
        st.subheader("💡 Ejemplo de código:")
        st.code(contenido["ejemplo"], language="python")
        if tema == "DataFrames":
            df = pd.DataFrame({"Nombre": ["Ana", "Luis"], "Edad": [23, 30]})
            st.dataframe(df)

# -------------------------------
# BARRA LATERAL
# -------------------------------
st.sidebar.header("📂 Áreas de estudio")
opciones_menu = list(temas.keys())
area = st.sidebar.radio("Seleccioná una categoría:", opciones_menu)

st.sidebar.markdown("---")
st.sidebar.markdown("👨‍🏫 *Manual creado para clases de Ciencia de Datos*")

# -------------------------------
# CONTENIDO PRINCIPAL
# -------------------------------
st.subheader(area)
for tema, contenido in temas[area].items():
    mostrar_contenido(tema, contenido)
