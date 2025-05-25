import gradio as gr
import openai
from openai import OpenAI

# 🔐 Wstaw swój klucz API
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Globalna zmienna do przechowywania ostatniego posta
ostatni_post = {"tekst": "", "grafika": None, "temat": "", "styl": "", "platforma": ""}

# Funkcja generująca post
def generuj_post(temat, styl, platforma, jezyk, cel, dlugosc):
    prompt = (
        f"Jesteś doświadczonym strategiem marketingu treści i copywriterem z wieloletnim doświadczeniem. Twoim zadaniem jest przygotowanie profesjonalnego, rzeczowego i atrakcyjnego posta na platformę {platforma}, "
        f"którego fukcja i cel to {cel.lower()} i skutecznie będzie angażował odbiorców. Temat posta to: '{temat}'. "
        f"Użyj języka {jezyk.lower()}, zachowując styl komunikacji: {styl.lower()}. "
        f"Długość posta: {dlugosc.lower()}. "
        f"Post musi być precyzyjny, oparty wyłącznie na wiarygodnych i aktualnych danych, nazwach i faktach. Niedopuszczalne jest wymyślanie produktów, funkcji, nazw, modeli lub faktów, które nie istnieją. "
        f"Zadbaj o dopasowanie treści do standardów i oczekiwań konkretnej platformy społecznościowej, a także o naturalny, profesjonalny ton wypowiedzi."
    ) 
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        wynik = response.choices[0].message.content
        ostatni_post["tekst"] = wynik
        ostatni_post["temat"] = temat
        ostatni_post["styl"] = styl
        ostatni_post["platforma"] = platforma
        return wynik
    except Exception as e:
        return f"Błąd: {e}"

# Funkcja generująca grafikę
def generuj_grafike():
    if not ostatni_post["tekst"]:
        return None
    try:
        image_prompt = (
        f"Ilustracja w stylu {ostatni_post['styl'].lower()} na platformę {ostatni_post['platforma']}. "
        f"Temat: {ostatni_post['temat']}. "
        f"Jeśli umieszczasz tekst na borazie to musi być on klarowny, wyraźny i prawidłowy ortograficznie. Bardzo wysoka jakość, wyraźne i realistyczne elementy. "
        f"Unikaj zniekształceń i nieczytelnych napisów. Minimalistyczna, estetyczna kompozycja."
    )
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )
        image_url = image_response.data[0].url
        ostatni_post["grafika"] = image_url
        return image_url
    except Exception as e:
        return None

# Funkcja poprawiająca istniejący post
def ulepsz_post(instrukcja):
    if not ostatni_post["tekst"]:
        return "Najpierw wygeneruj post."

    prompt = (
        f"Oto post:\n{ostatni_post['tekst']}\n\n"
        f"Nie twórz nowego postu od zera, tylko popraw ten post zgodnie z instrukcją: {instrukcja}. "
        f"Post ma być profesjonalny, realistyczny, bez fikcyjnych danych. "
        f"Zachowaj styl komunikacji: {ostatni_post['styl'].lower()} oraz odpowiedni długość wynikającą z pierwotnych założeń posta "
        f"chyba, że użytkownik poprosi w instrukcji: {instrukcja} o zmianę długości postu. "
        f"Zadbaj o dopasowanie języka i tonu wypowiedzi do platformy {ostatni_post['platforma']}."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        poprawiony = response.choices[0].message.content
        ostatni_post["tekst"] = poprawiony
        return poprawiony
    except Exception as e:
        return f"Błąd: {e}"

# Interfejs aplikacji w Gradio
with gr.Blocks() as demo:
    gr.Markdown("## 📱 AI Generator Postów Social Media")
    gr.Markdown("""
Aplikacja AI Generator Postów Social Media to narzędzie służące do automatycznego tworzenia i ulepszania profesjonalnych postów na platformy społecznościowe (LinkedIn, Facebook, Instagram, X/Twitter). 
Dzięki zaawansowanemu wykorzystaniu sztucznej inteligencji opartej na modelach językowych (GPT-4) i generatywnych modelach obrazów (DALL·E 3), narzędzie wspiera użytkownika na każdym etapie tworzenia treści — od koncepcji i stylizacji po graficzną oprawę posta. 
Generator postów wykorzystuje dwie bilioteki: OpenAI oraz Gradio. Aplikacja opiera się na kontrolowanym prompt engineeringu, ograniczeniu halucynacji modelu, iteracyjności (wielokrotnej możliwości poprawy treści postu), synergii modeli GPT-4 i DALL·E 3 
oraz kluczu API OpenAI, który nie jest przechowywany w repozytorium kodu.

**Kamil Lemański 2025©**
""")

    with gr.Row():
        temat = gr.Textbox(label="Temat posta", placeholder="np. Jak AI zmienia marketing?")
        platforma = gr.Dropdown(["LinkedIn", "Facebook", "Instagram", "X (Twitter)"], label="Platforma")

    with gr.Row():
        styl = gr.Dropdown(["Edukacyjny", "Formalny/Profesjonalny", "Osobisty/Emocjonalny", "Zabawny", "Inspirujący/Motywacyjny", "Dla Pokolenia Z"], label="Styl komunikacji")
        jezyk = gr.Dropdown(["Polski", "Angielski"], label="Język")
        cel = gr.Dropdown(["Informacyjny", "Budowanie zaufania do marki", "Edukacyjny", "Storytelling", "Sprzedażowy/Promocja produktu"], label="Cel posta")
        dlugosc = gr.Dropdown(["Bardzo krótki", "Krótki", "Średni", "Długi", "Bardzo długi"], label="Długość posta")

    wynik = gr.Textbox(label="Wygenerowany post", lines=6)
    gr.Button("Generuj post").click(fn=generuj_post, inputs=[temat, styl, platforma, jezyk, cel, dlugosc], outputs=wynik)

    gr.Markdown("### 🔁 Ulepsz istniejący post")
    instrukcja = gr.Textbox(label="Jak chcesz poprawić ten post?", placeholder="np. Dodaj więcej humoru, skróć go")
    gr.Button("Ulepsz post").click(fn=ulepsz_post, inputs=instrukcja, outputs=wynik)

    obraz = gr.Image(label="Wygenerowana grafika")
    gr.Button("Wygeneruj grafikę do postu").click(fn=generuj_grafike, outputs=obraz)

import os
demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
