import datetime
from typing import Union

def get_weather(city: str) -> str:
    """
    Ritorna le condizioni meteo attuali per una città specifica.
    """
    if not city or not isinstance(city, str):
        return "Errore: Nome città non valido."
    return f"Il meteo a {city.title()} è di 22°C, cielo sereno e vento debole."

def calculate_discount(price: float, discount: float) -> str:
    """
    Calcola il prezzo finale dopo l'applicazione di uno sconto percentuale.
    price: il prezzo originale (> 0)
    discount: la percentuale di sconto (0-100)
    """
    try:
        # Conversione forzata per gestire eventuali stringhe passate dall'LLM
        f_price = float(price)
        f_discount = float(discount) 
        
        if f_price < 0 or not (0 <= f_discount <= 100):
            return "Errore: Il prezzo deve essere positivo e lo sconto tra 0 e 100."
        
        final_price = f_price * (1 - f_discount / 100)
        return f"Il prezzo originale di {f_price:.2f}€, scontato del {f_discount}%, diventa {final_price:.2f}€."
    except (ValueError, TypeError):
        return "Errore: I parametri prezzo e sconto devono essere numeri validi."

def count_words(text: str) -> str:
    """
    Riceve un testo già filtrato dall'agente e conta il numero di parole.
    Nota per l'agente: passa solo il contenuto da analizzare, escludendo il comando.
    """
    if not isinstance(text, str) or not text.strip():
        return "La stringa è vuota. Conteggio: 0 parole."
    
    count = len(text.split())
    return f"L'analisi è completata: la stringa contiene esattamente {count} parole."

def get_current_time(timezone: str = "UTC") -> str:
    """
    Ritorna l'ora esatta nel formato HH:MM:SS.
    """
    now = datetime.datetime.now()
    return f"L'orario attuale ({timezone}) è {now.strftime('%H:%M:%S')}."

def get_system_info() -> str:
    """
    Ritorna informazioni di base sul sistema operativo.
    """
    import platform
    return f"Sistema: {platform.system()} {platform.release()}, Python: {platform.python_version()}"
