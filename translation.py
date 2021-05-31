import translators as ts

text = "Hola como estas? aca estamos todo bien"

print(ts.google(text, from_language='es', to_language='en'))

def translate(text):
    traduced = ts.google(text, from_language='es', to_language='en')
    print(traduced)
    return traduced