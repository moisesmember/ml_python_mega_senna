import pymongo
import json

class WebScrapingDao:

    def connection(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["MegaSenna"] # Banco de Dados
        mycol = mydb["historico_jogos"]       # Collection
        return mycol

    def salvarMegaSenna(self, data):        
        client = pymongo.MongoClient("localhost", 27017) # 172.0.0.1
        db = client.MegaSenna # Nome do Banco e da Coleção
        #db.tweetData.insert_one(data)
        print(dict(data))
        #db.historicoJogos.insert_many(data)
        db.historicoJogos.insert_one(data)
        
    def findMegaSennaByDataSorteio(self, data_sorteio):
        db_megasenna = WebScrapingDao() # Instância Objeto da Classe
        connected = db_megasenna.connection() # Realiza a conexão com o MongoDB
        return connected.find({"data_sorteio":data_sorteio})

    def listAllMegaSenna():
        db_megasenna = WebScrapingDao() # Instância Objeto da Classe
        connected = db_megasenna.connection() # Realiza a conexão com o MongoDB
        return connected.find({})