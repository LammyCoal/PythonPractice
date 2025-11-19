#This is a translator

def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translate(word):
        if word.lower() in translations[language]:
            return translations[language][word.lower()]
        else:
            return "Translation not available"

    return translate

translate_to_spanish = translator('spanish')
translate_to_french = translator('french')
translate_to_italian = translator('italian')

print(translate_to_spanish('hello'))
print(translate_to_spanish('goodbye'))
print(translate_to_french('hello'))
print(translate_to_french('goodbye'))
print(translate_to_italian('hello'))
print(translate_to_italian('goodbye'))
