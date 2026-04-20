import os
from dotenv import load_dotenv
from app.registry import ToolRegistry
from app.agent import MiniAgent
from app.tools import get_weather, calculate_discount, count_words, get_current_time, get_system_info


# 1. Caricamento variabili d'ambiente (.env)
load_dotenv()

def main():
    # 2. Inizializzazione del ToolRegistry
    registry = ToolRegistry()
    
    # Registrazione dei 4 Tool definitivi
    registry.register("get_weather", get_weather, "Ritorna il meteo per una città specifica (param: city)")
    registry.register("calculate_discount", calculate_discount, "Calcola il prezzo scontato (params: price, discount)")
    registry.register("count_words", count_words, "Conta tutte le parole presenti dopo il comando (param: text)")
    registry.register("get_current_time", get_current_time, "Ritorna l'ora attuale (param: timezone)")
    registry.register("get_system_info", get_system_info, "Ritorna info sul sistema (No params)")


    # 3. Controllo presenza API Key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERRORE: Chiave OPENAI_API_KEY non trovata nel file .env")
        return

    # 4. Inizializzazione dell'AI Agent (Configurabile)
    agent = MiniAgent(registry)


    # 5. Casi di test per la demo (Golden Set)
    test_prompts = [
        "Che tempo fa a Roma?",                                 # Tool: get_weather
        "Quanto costa un prodotto da 150€ con lo sconto del 20%?", # Tool: calculate_discount
        "conta queste parole: l'agente funziona molto bene",     # Tool: count_words (dopo il comando)
        "Che ore sono adesso?",                                  # Tool: get_current_time
        "Chi ha scritto la Divina Commedia?"                     # Risposta diretta LLM (No tool)
    ]

    print("="*50)
    print("🤖 MINI AGENT TOOLKIT - RUN DI CONSEGNA")
    print("="*50)

    for prompt in test_prompts:
        print(f"\n➔ USER: {prompt}")
        try:
            response = agent.run(prompt)
            print(f"➔ AGENT: {response}")
        except Exception as e:
            print(f"⚠️ ERRORE durante l'esecuzione: {e}")

    print("\n" + "="*50)
    print("✅ Demo completata. Controlla 'agent_activity.log' per i dettagli.")
    print("="*50)

if __name__ == "__main__":
    main()