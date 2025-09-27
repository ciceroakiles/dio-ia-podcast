from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
from pydub import AudioSegment
import soundfile as sf
import torch
import re

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-multilingual-v1.1").to(device)
tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler-tts-mini-multilingual-v1.1")
description_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)
description = "Descricao da voz"

# Para sentencas mais curtas
def short_prompt(prompt):
    input_ids = description_tokenizer(description, return_tensors="pt").input_ids.to(device)
    prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
    audio_arr = generation.cpu().numpy().squeeze()
    sf.write("output.wav", audio_arr, model.config.sampling_rate)

# Para varias frases em sequencia
def long_prompt(prompt):
    segments = re.split(". |\! |\? ", prompt)
    audio_segments = []
    for i, segment in enumerate(segments):
        if segment:
            prompt = f"{segment}"
            input_ids = description_tokenizer(description, return_tensors="pt").input_ids.to(device)
            prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
            generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
            audio_arr = generation.cpu().numpy().squeeze()
            
            sf.write(f"audio_segment_{i}.wav", audio_arr, model.config.sampling_rate)
            audio_segments.append(AudioSegment.from_wav(f"audio_segment_{i}.wav"))
    if audio_segments:
        combined_audio = AudioSegment.empty()
        for audio in audio_segments:
            combined_audio += audio
        combined_audio.export("combined_output.wav", format="wav")

prompt = "Testando uma frase mais longa. Segunda frase aqui."
short_prompt(prompt)
