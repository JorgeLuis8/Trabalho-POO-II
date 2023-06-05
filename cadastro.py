from usuario import Usuairo
import mysql.connector

bd = mysql.connector.connect(host="localhost", username="root", password="1234")

cursor = bd.cursor()

cursor.execute("Create database usuarios")