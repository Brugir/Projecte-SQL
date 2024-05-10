from flask import Flask, render_template
import pymongo

# Reemplaza "<username>", "<password>", "<cluster_name>" y "<database_name>" con tus propios valores
username = "Bernat"
password = "1234"
cluster_name = "contaminacionbcn"
database_name = "contaminacin"

# Construye la cadena de conexión
connection_string = f"mongodb+srv://{username}:{password}@contaminacionbcn.tacpnks.mongodb.net/"

# Establece la conexión
client = pymongo.MongoClient(connection_string)

# Selecciona la base de datos
db = client[database_name]

# Accede a una colección
# collection = db["Calidad Aire"]

# print(db)

try:
    # Establece la conexión
    client = pymongo.MongoClient(connection_string)

    # Selecciona la base de datos
    db = client[database_name]

    # Obtiene las colecciones de la base de datos
    collection_names = db.list_collection_names()

    # Si no se lanzó ninguna excepción, la conexión se ha establecido correctamente
    print(f"Conexión exitosa a la base de datos '{database_name}' en MongoDB Atlas.")
    print("Colecciones disponibles:")
    for collection_name in collection_names:
        print(collection_name)

except Exception as e:
    # Si se lanzó una excepción, indica que la conexión falló
    print("Error al conectar a MongoDB Atlas:", e)



# app = Flask(__name__)

# @app.route('/')

# def algo():
#     return()

# app.run(host='Localhost', port=5000, debug=True)