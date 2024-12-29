"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
import pandas as pd

def pregunta_01():
    """
    Procesa el archivo 'clusters_report.txt', estructura los datos en un DataFrame
    con columnas específicas y limpia los valores según el formato esperado.
    """
    try:
        # Leer el archivo de texto
        with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Validar si el archivo tiene líneas suficientes
        if len(lineas) <= 4:
            print("El archivo no tiene suficientes líneas para procesar.")
            return pd.DataFrame()

        datos = []  # Lista para almacenar filas procesadas
        contenido = lineas[4:]  # Omitir las primeras 4 líneas del encabezado
        fila = []  # Inicializar la fila temporal

        for linea in contenido:
            dividir = linea.strip().split()  # Dividir la línea en palabras

            if dividir:  # Si la línea no está vacía
                if not fila:  # Si es una nueva fila
                    fila = [
                        int(dividir[0]),  # Número de cluster
                        int(dividir[1]),  # Cantidad de palabras clave
                        float(dividir[2].replace(',', '.')),  # Porcentaje (convertir coma a punto)
                        " ".join(dividir[4:])  # Palabras clave iniciales
                    ]
                else:  # Si es una continuación de la fila
                    fila[3] += " " + " ".join(dividir)  # Concatenar palabras clave
            else:  # Si la línea está vacía (separador de filas)
                if fila:  # Si hay una fila pendiente
                    fila[3] = fila[3].replace('.', '')  # Eliminar puntos del texto
                    fila[3] = " ".join(fila[3].split())  # Eliminar espacios extra
                    datos.append(fila[:4])  # Agregar fila procesada a los datos
                    fila = []  # Reiniciar fila temporal

        # Procesar última fila si quedó pendiente
        if fila:
            fila[3] = fila[3].replace('.', '')
            fila[3] = " ".join(fila[3].split())
            datos.append(fila[:4])

        # Crear el DataFrame
        columnas = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
        return pd.DataFrame(datos, columns=columnas)

    except FileNotFoundError:
        print("El archivo 'clusters_report.txt' no fue encontrado.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Llamar a la función y mostrar el DataFrame resultante
    df_tabla = pregunta_01()
   

    
