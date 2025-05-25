📱 AI Generator Postów Social Media

Live App ➤ https://ai-post-generator-klemanski.onrender.com

AI Generator Postów Social Media to prosta aplikacja webowa wspierająca tworzenie profesjonalnych postów na platformy społecznościowe (LinkedIn, Facebook, Instagram, X/Twitter). Dzięki wykorzystaniu modeli GPT-4 i DALL·E 3, generuje zarówno treść, jak i grafikę posta w jednym procesie.

------------
✨ Właściwości:

✅ Generowanie tekstów w różnych stylach i językach

🎯 Dostosowanie do platformy, celu i długości posta

🎨 Tworzenie wysokiej jakości grafik z DALL·E 3

🔁 Możliwość iteracyjnego ulepszania postu i grafiki

🔐 Bezpieczne użycie klucza API (dotenv + sekrety środowiskowe)

-------------
🧪 Zastosowane technologie:

Python 3.8+

Gradio

OpenAI GPT-4

OpenAI DALL·E 3

python-dotenv

Render.com

------------
👉 Uruchomienie aplikacji online:

https://ai-post-generator-klemanski.onrender.com

------------
📂 Folder structure:

ai-post-generator/
├── main.py              # Główna logika aplikacji
├── requirements.txt     # Biblioteki Pythona
├── render.yaml          # Konfiguracja dla Render.com
├── .env.example         # Szablon pliku środowiskowego
└── README.md            # Ten plik

------------
⚙️ Instalacja i uruchomienie aplikacji lokalnie:

git clone https://github.com/twoj-login/ai-post-generator.git
cd ai-post-generator

# Zainstaluj zależności
pip install -r requirements.txt

# Stwórz plik .env i wklej swój klucz OpenAI
cp .env.example .env
nano .env  # lub dowolny edytor

# Uruchom aplikację
python main.py

------------
🔐 Zmienne środowiskowe:

Ustaw zmienną środowiskową OPENAI_API_KEY w pliku .env:
OPENAI_API_KEY=sk-...twój-klucz...

------------
☁️ Deployment na platformie Render.com:

1. Połącz repozytorium GitHub z Render.com
   
2. Upewnij się, że w repo są pliki: main.py, requirements.txt, render.yaml
   
3. W Start Command wpisz: python main.py
   
4. W sekcji Environment Variables dodaj OPENAI_API_KEY
   
5. Aplikacja zostanie automatycznie uruchomiona pod adresem .onrender.com.

------------
📌 Przykład użycia:

1. Wybierz temat, styl, język i cel posta.

2. Kliknij „Generuj post” — otrzymasz gotowy tekst.

3. Kliknij „Wygeneruj grafikę do posta” — otrzymasz obraz od DALL·E 3.

4. Chcesz coś poprawić? Skorzystaj z funkcji „Ulepsz post” lub „Ulepsz grafikę”.

------------
📝 Licencja:

© 2025 Kamil Lemański. Projekt edukacyjny i demonstracyjny.

🙏 Credits:

OpenAI (GPT-4, DALL·E 3), 
Gradio Team, 
Render.com Hosting.
