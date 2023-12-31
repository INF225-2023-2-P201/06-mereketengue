import spacy, os, datetime, csv
#import mysql.connector

# Cargar el modelo de lenguaje
nlp = spacy.load("es_core_news_sm")

# Crea una subCarpeta llamada "Historial" 
directorio_base = os.getcwd()

# Configura la conexión a la base de datos, esta comentado debido a que no funciona correctamente.
"""
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
"""

if True != os.path.exists('Historial'): # Si la carpeta ya existe no la crea
    os.mkdir('Historial')

#Funcion que analiza la entrada texto
def analisis_texto(texto):
    # Procesar el texto con spaCy
    mensajes = []
    mensajes.append(("Analizando frase",2))
    doc = nlp(texto)
    
    bloqueo = ["bloquear", "impedir", "prohibir", "cerrar", "cortar", "incomunicar", "aislar"]
    acceso = ["conectarse", "conexion", "acceso", "entrada", "salir"]
    ping = ["pingear", "ping", "latencia"]

    # Definir una lista de adverbios de negaciones en español

    negaciones = ["no", "nada", "nunca", "jamás", "nadie", "tampoco", "ni"]

    # Variables para controlar los posibles comandos que estan implementados
    bloquear_internet = False
    permitir_internet = False
    ping_conexion = False
    negacion = False
    
    sust_1 = "" #NODO
    next_sust_1 = ""#A
    sust_2 = "" #NODO
    next_sust_2 = "" #B
    ip_1 = 0
    ip_2 = 0
    #ip = 0

    # Recorrer los tokens del texto
    for i, token in enumerate(doc):


        # Se trata de realizar un select para extraer info de la BD, pero no funciona.
        """
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
        """
        
        #print(token.text, token.pos_)
        #Guarda Nodo con nombre
        if token.text.lower() == "nodo":
            if sust_1 == "":
                sust_1 = token.text
                next_sust_1 = doc[i+1].text
            else:
                sust_2 = token.text
                next_sust_2 = doc[i+1].text
        #Guarda la(s) ip(s)
        if token.pos_== "NUM" and "." in token.text:
            if ip_1 == 0:
                ip_1 = token.text
            else:
                ip_2 = token.text

        # Verificar si el token es un adverbio de negación
        if token.text.lower() in negaciones:
            negacion = True

        # Verificar si el token anterior está en la lista de bloqueo
        if token.text.lower() in bloqueo:
            bloquear_internet = True
        # Verifica si el token esta en la lista de acceso
        elif token.text.lower() in acceso:
            permitir_internet = True
        # Verifica si el token esta en la lista de Ping
        elif token.text.lower() in ping:
            ping_conexion = True
        #Fin del for

    # Determinar el resultado final
    mensajes.append(("Determinando Resultado",2))
    #Se crea un archivo csv de nombre Historial, empieca vacio con dos columnas
    columnas = ["Fecha", "Accion", "Nodo(s) Origen/Destino"]
    with open('Historial/Historial.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(columnas)
        if (bloquear_internet == True and negacion == False) or (permitir_internet == True and negacion == True):
            if sust_1 != "":
                #COMPROBAR SI LA IP ESTA EN LA BD
                mensajes.append(("Se bloquea el acceso a internet.",0))
                fecha = datetime.datetime.now()
                fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
                archi = open('Historial/{0}.txt'.format(fecha), 'wt')
                #BUSCAR LA IP DE SUST NEXT_SUST EN LA BASE DE DATOS, TODAVIA NO LO APLICO
                text = str("Output: \n$configure terminal\n$access-list extended block-out\n$deny ip" + sust_1 + " " + next_sust_1 + " any\n$exit\n$interface eth0\n$ip access-group block-out in\n$exit")
                archi.write(text)
                archi.close()
                #"Fecha", "Accion", "Nodo(s) Origen/Destino"
                Hist = [fecha, "Se bloquea el acceso a internet", sust_1 + " " + next_sust_1]
                writer.writerow(Hist)
                
            elif ip_1 != 0:
                #COMPROBAR SI LA IP ESTA EN LA BD
                mensajes.append(("Se bloquea el acceso a internet.",0))
                fecha = datetime.datetime.now()
                fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
                archi = open('Historial/{0}.txt'.format(fecha), 'wt')
                text = str("Output: \n$configure terminal\n$access-list extended block-out\n$deny ip " + ip_1 + " any\n$exit\n$interface eth0\n$ip access-group block-out in\n$exit")
                archi.write(text)
                archi.close()
                #"Fecha", "Accion", "Nodo(s) Origen/Destino"
                Hist = [fecha, "Se bloquea el acceso a internet", ip_1]
                writer.writerow(Hist)
            else:
                mensajes.append(("Especifique un objeto valido para bloquear internet",1))
        elif (bloquear_internet == True and negacion == True) or (permitir_internet == True and negacion == False):
            #AGREGAR EL CODIGO NECESARIO
            mensajes.append(("Se permite el acceso a internet.",0))
        elif (ping_conexion == True):
            #AGREGAR CODIGO NECESARIO EN TODOS LOS IF/ELIF
            if sust_1 != "":
                if sust_2 != "":
                    fecha = datetime.datetime.now()
                    fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
                    archi = open('Historial/{0}.txt'.format(fecha), 'wt')
                    text = str("Hacer ping entre {0} {1} y {2} {3}".format(sust_1, next_sust_1, sust_2, next_sust_2))
                    mensajes.append((text,0))
                    archi.write(text)
                    archi.close()
                    #"Fecha", "Accion", "Nodo(s) Origen/Destino"
                    Hist = [fecha, "Se hace ping", sust_1 + " " + next_sust_1 + " / " + sust_2 + " " + next_sust_2]
                    writer.writerow(Hist)
                elif ip_1 != 0:
                    fecha = datetime.datetime.now()
                    fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
                    archi = open('Historial/{0}.txt'.format(fecha), 'wt')
                    text = str("Hacer ping entre {0} {1} y {2}".format(sust_1, next_sust_1, ip_1))
                    mensajes.append((text,0))
                    archi.write(text)
                    archi.close()
                    #"Fecha", "Accion", "Nodo(s) Origen/Destino"
                    Hist = [fecha, "Se hace ping", sust_1 + " " + next_sust_1 + " / " + ip_1]
                    writer.writerow(Hist)
                else:
                    mensajes.append(("Especifica una segunda conexion",1))
            elif ip_1 != 0:
                if sust_1 != "":
                    fecha = datetime.datetime.now()
                    fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
                    archi = open('Historial/{0}.txt'.format(fecha), 'wt')
                    text = str("Hacer ping entre {0} y {1} {2}".format(ip_1, sust_1, next_sust_1))
                    mensajes.append((text,0))
                    archi.write(text)
                    archi.close()
                    #"Fecha", "Accion", "Nodo(s) Origen/Destino"
                    Hist = [fecha, "Se hace ping", ip_1 + " / " + sust_1 + " " + next_sust_1]
                    writer.writerow(Hist)
                elif ip_2 != 0:
                    fecha = datetime.datetime.now()
                    fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
                    archi = open('Historial/{0}.txt'.format(fecha), 'wt')
                    text = str("Hacer ping entre {0} y {1}".format(ip_1, ip_2))
                    mensajes.append((text,0))
                    archi.write(text)
                    archi.close()
                    #"Fecha", "Accion", "Nodo(s) Origen/Destino"
                    Hist = [fecha, "Se hace ping", ip_1 + " / " + ip_2]
                    writer.writerow(Hist)
                else:
                    mensajes.append(("Especifica una segunda conexion",1))
            else:
                mensajes.append(("Especifica una conexion",1))
        #FALTAN MAS COMANDOS??
        else:
            mensajes.append(("Ningun comando conocido.",1))
        mensajes.append(("Listo",2))
    return mensajes

# Texto en lenguaje natural

# Bloquear internet para el nodo A
#print(analisis_texto("Quiero hacer ping entre el nodo A y 192.125.001"))
#texto = "El 192.125.000 no puede salir a internet"
