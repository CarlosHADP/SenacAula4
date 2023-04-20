from flask import Flask 

bla = Flask(__name__)

@bla.route('/')
def curso():
    return 
    'Ola turma'