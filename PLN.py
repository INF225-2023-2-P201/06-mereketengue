import spacy

# Cargar el modelo de lenguaje
nlp = spacy.load("es_core_news_sm")

# Texto en lenguaje natural
texto = "El nodo A no puede salir a internet"
# Bloquear internet para el nodo A

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

# Recorrer los tokens del texto
for i, token in enumerate(doc):
    # Verificar si el token es un adverbio de negación
    print(token)
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
elif (bloquear_internet == True and negacion == True) or (permitir_internet == True and negacion == False):
    print("Se permite el acceso a internet.")
else:
    print("No se especifica el acceso a internet.")
