import speech_recognition as sr
import json


filename = "./audiotest1.wav"
rec = sr.Recognizer()
list_words = ['voo', 'viagem', 'viagens', 'passagem', 'embarque', 'check in', 'bagagem', 'Casas Bahia', 'Extra']
json_file = "./infos.json"


#Função pegar audio em tempo real do microfone
def get_mic():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        input_audio = rec.listen(mic)
        text_from_audio = rec.recognize_google(input_audio, language="pt-BR")
        print(text_from_audio)



# Função para buscar palavra-chave no JSON
def get_info(key_word, data):
    results = []

    def search_in_objects(obj, key_word):
        if isinstance(obj, dict):
            for v in obj.values():
                if isinstance(v, str) and key_word.lower() in v.lower():
                    results.append(obj)
                elif isinstance(v, (dict, list)):
                    search_in_objects(v, key_word)
        elif isinstance(obj, list):
            for item in obj:
                search_in_objects(item, key_word)

    search_in_objects(data, key_word)
    return results




with sr.AudioFile(filename) as source:
    audio_data = rec.record(source)
    #Convertendo audio para texto
    text = rec.recognize_google(audio_data, language="pt-BR")
    print(text)


#Em tese seria um While chamada_ativa, iria procurar por informações uteis no arquivo estabelecido
for word in list_words:
    if word in text:
        print("contains the word:", word)
        #get_info(word)
        break
    else:
        print("Does not contains")
    find_word = word

#Abrindo arquivo Json
with open(json_file, 'r', encoding='utf-8') as arq:
        json_data = json.load(arq)


#Chamando funções
help = get_info(find_word, json_data)
print(help)