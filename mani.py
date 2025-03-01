meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "OSTIAS":"es un algo impactante",
            "XD":"significa algo random"}


n_words=int(input("Escribe una palabra quieres entender (1-4)"))

for i in range (n_words):
    word_to_know=input("que palabra quieres saber que significa?(En mayusculas)").upper()              
    if word_to_know in meme_dict.keys():
        print("El significado de", word_to_know,"es",meme_dict[word_to_know])
    
  
