
import spacy

# Cargar el modelo de lenguaje
nlp = spacy.load("es_core_news_sm")

import mysql.connector

# Configura la conexión a la base de datos
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # Por lo general, 'localhost' si está en tu máquina
    'database': 'ibn',
}
conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()
pc= 'pc3'
cursor.execute("SELECT IPv4 FROM pcserver WHERE Nombre = %s", (pc,))
resultados = cursor.fetchall()
print(resultados[0][0])
cursor.close()
conexion.close()

def analisis_texto(texto):
    # Procesar el texto con spaCy
    doc = nlp(texto)
    bloqueo = ["bloquear", "impedir", "prohibir"]
    acceso = ["conectarse", "acceso", "entrada", "salir"]

    # Definir una lista de negaciones en español
    negaciones = ["no", "nunca", "jamás", "tampoco"]

    # Variables para controlar si se bloquea o se permite el acceso a internet
    bloquear_internet = False
    permitir_internet = False
    negacion = False
    sust= ""#NODO
    next_sust = ""#A
    ip=0
    ip1=""
    # Recorrer los tokens del texto
    for i, token in enumerate(doc):

        # Verificar si el token es un adverbio de negación
        print(token,token.pos_)
        if token.pos_=="NOUN":
            sust=token.text
            if token.text in "pc" or token.text in "server" : #esto no funciona
                print("HOLAAAAAA")
                cursor.execute("SELECT IPv4 FROM pcserver WHERE Nombre = %s" , (token.text,))
                res=cursor.fetchall()
                ip=res[0][0]
        if token.pos_=="NUM":
            ip=token.text
            
        if token.text.lower() in negaciones:
            # Verificar si el token anterior está en la lista de bloqueo o acceso
            negacion = True
        if token.text.lower() in bloqueo:
            bloquear_internet = True
        elif token.text.lower() in acceso:
            permitir_internet = True

    # Determinar el resultado final
    if (bloquear_internet == True and negacion == False) or (permitir_internet == True and negacion == True):
        print("Se bloquea el acceso a internet.")
        if sust!="":
         print("Output: \n$configure terminal\n$access-list extended block-out\n$deny ip",ip,"any\n$exit\n$interface eth0\n$ip access-group block-out in\n$exit" )
        else:
           print("Output: \n$configure terminal\n$access-list extended block-out\n$deny ip",ip,"any\n$exit\n$interface eth0\n$ip access-group block-out in\n$exit" )  
    elif (bloquear_internet == True and negacion == True) or (permitir_internet == True and negacion == False):
        print("Se permite el acceso a internet.")

    else:
        print("No se especifica el acceso a internet.")

# Texto en lenguaje natural

# Bloquear internet para el nodo A
# print(analisis_texto("El 192.125.000 no puede salir a internet"))
# texto = "El 192.125.000 no puede salir a internet"
