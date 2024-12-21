from gtts import gTTS
from googletrans import Translator

def text_to_bangla_voice(text, output_file='output.mp3'):
    """
    Converts English text to Bangla voice using translation and text-to-speech.
    
    :param text: The English text to be translated and converted to Bangla voice.
    :param output_file: The file name for the output audio file.
    """
    try:
        # Translate text to Bangla
        translated_text = translate_to_bangla(text)
        
        # Convert text to speech
        tts = gTTS(text=translated_text, lang='bn')
        tts.save(output_file)
        print(f"Audio file saved as: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        raise e

def translate_to_bangla(text):
    """
    Translate English text to Bangla using Google Translate API.
    
    :param text: English text to translate.
    :return: Translated Bangla text.
    """
    translator = Translator()
    translated = translator.translate(text, src='en', dest='bn')
    return translated.text
