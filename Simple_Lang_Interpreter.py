import googletrans

translator = googletrans.Translator()
translated = translator.translate('I AM ARNAB SARKAR', dest='hi')
print(translated.text)
print(googletrans.LANGUAGES)
