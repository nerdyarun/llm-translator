from transformers import TFMarianMTModel
from transformers import MarianTokenizer


language_models = {
    "Hindi": "Helsinki-NLP/opus-mt-en-hi",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Italian": "Helsinki-NLP/opus-mt-en-it",
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "Chinese": "Helsinki-NLP/opus-mt-en-zh",
    "Russian": "Helsinki-NLP/opus-mt-en-ru",
    "Arabic": "Helsinki-NLP/opus-mt-en-ar",
}


# Cache models to prevent reloading
cached_models = {}

def load_model_and_tokenizer(model_name):
    if model_name in cached_models:
        return cached_models[model_name]
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = TFMarianMTModel.from_pretrained(model_name)
    cached_models[model_name] = (tokenizer, model)
    return tokenizer, model

def translate_text(text):
    translations = {}
    for lang, model_name in language_models.items():
        tokenizer, model = load_model_and_tokenizer(model_name)
        inputs = tokenizer([text], return_tensors="tf", padding=True)
        translated = model.generate(**inputs)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        translations[lang] = translated_text
    return translations
