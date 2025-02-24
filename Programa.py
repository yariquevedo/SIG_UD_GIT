
from flask import Flask

class Programa:

    def __init__(self):

        self.app=Flask(__name__)

        self.app.add_url_rule('/nuevo', view_func=self.agrega)

        #Iniciar el servidor 
        self.app.run(debug=True)
    
    def agrega(self):
        return "Hola mundo Flask"
    
miPrograma=Programa()
