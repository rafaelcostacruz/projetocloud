from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Projeto Cloud Architeture e DevOps utilizando pipeline</h1>\Grupo:Bruno Alves Moreira - 344969 - Jonas Rodrigues de Oliveira - 344772 - Lucas Esteves Fernandes Diogo - 344774 - Rafael Costa da Cruz - 344780 - Victor Hugo Fiorotti - 344988"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0',debug=True)
