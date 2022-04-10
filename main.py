from database.models import db_connect
from database.seeds.Classificador import Classificador

def main():
    conn = db_connect()
    obj = Classificador(1, conn)
    obj.run()

if __name__ == "__main__":
   main()  