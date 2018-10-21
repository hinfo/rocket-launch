# Instala o pacote tweepy
#!pip install tweepy

# Importando os módulos Tweepy, Datetime e Json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json

# Consumer Key
consumer_key = "consumer_key"

# AConsumer Secret 
consumer_secret = "consumer_secret"

# Access Token
access_token = "access_token"

# Access Token Secret
access_token_secret = "access_token_secret"

# Criar as chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Classe para capturar os stream de dados do Twitter e armazenar no MongoDB(Banco de Dados)
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        in_reply_to_screen_name = tweet["in_reply_to_screen_name"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str, "in_reply_to_screen_name": in_reply_to_screen_name, "text":text, } #"name" : ["user"]["name"], "screen_name" : ["user"]["screen_name"],
        tweetind = col.insert_one(obj)#.inserted_id
        print (obj)
        return True

# Criando o objeto mylistener
mylistener = MyListener()

# Criando o objeto mystream
mystream = Stream(auth, listener = mylistener)

# Importando do PyMongo o módulo MongoClient
from pymongo import MongoClient  

# Conexão ao MongoDB
client = MongoClient('localhost', 27017)

# Criando o banco de dados twitterdb
db = client.twitterdb

# Criando a collection "col"
col = db.tweets

# Lista de palavras chave para buscar nos Tweets - Agências Espaciais
keywords = ['@NASA', '@SANSA7', '@AFSpace', '@CNSA_en', '@esa', '@isa', '@ILSpaceAgency', '@ASI_spazio', '@isro', '@JAXA_en', '@CNES', '@roscosmos',]

# Iniciando o filtro e gravando os tweets no MongoDB
mystream.filter(track=keywords)

#Fechando conexão com mystream
mystream.disconnect()
