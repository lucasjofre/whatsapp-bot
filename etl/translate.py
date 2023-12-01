from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    # Instantiates a client
    translate_client = translate.Client()

    # Translates the text
    translation = translate_client.translate(
        text,
        target_language=target_language
    )

    # Returns the translated text
    return translation['translatedText']

# Example usage
text_to_translate = "Hello, how are you?"
target_language = "es"  # Target language code, e.g., "es" for Spanish

translated_text = translate_text(text_to_translate, target_language)
print(translated_text)
