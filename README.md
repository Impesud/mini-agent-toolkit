# Mini Agent Toolkit (Python) — LLM Router + Tool Registry

Mini progetto didattico che implementa un **mini-agente con “tool calling”**:

a partire da un prompt testuale, un modello OpenAI (configurato nel codice) decide **se** usare uno dei tool disponibili e **con quali parametri**. La scelta avviene chiedendo al modello di rispondere in **JSON** con uno schema fisso; se viene selezionato un tool valido, il tool viene eseguito e l’azione viene **loggata** su file.

## Cosa include

- **ToolRegistry**: registro dei tool disponibili (nome → funzione + descrizione).
- **MiniAgent**: router basato su LLM che decide `tool` e `params`.
- **4 tool** (in `app/tools.py`):
  - `get_weather(city)` → meteo *mock* per una città
  - `calculate_discount(price, discount)` → calcolo sconto percentuale
  - `count_words(text)` → conteggio parole
  - `get_current_time(timezone='UTC')` → orario corrente (timezone è una label)
- **Logging** su `agent_activity.log` quando viene eseguito un tool.
- **Test** con `pytest` che **mockano** l’API OpenAI (esecuzione deterministica).

## Requisiti

- Python **3.9+** (consigliato 3.10+)
- `pip`
- Una **OpenAI API Key** (solo per eseguire `main.py` in modalità reale)

## Installazione

1) Clona/copìa il progetto ed entra nella cartella:

```bash
cd mini_agent_toolkit
```

2) (Consigliato) Crea e attiva un virtual environment:

```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\\Scripts\\activate
```

3) Installa le dipendenze:

```bash
pip install -r requirements.txt
```

## Configurazione: variabili d’ambiente

Per eseguire la demo reale serve `OPENAI_API_KEY`. Crea un file **`.env`** nella root del progetto:

```env
OPENAI_API_KEY=la_tua_chiave
```

Il file `.env` viene caricato da `main.py` tramite `python-dotenv`.

Suggerimento sicurezza:
- aggiungi `.env` a `.gitignore`
- non committare mai chiavi o segreti

## Come eseguire

Esegui la demo (usa la lista di prompt “golden set” già pronta in `main.py`):

```bash
python main.py
```

Output atteso:
- per i prompt che attivano un tool, la risposta ha il formato `"[TOOL <nome>] <risultato>"`
- per prompt generici, l’agente restituisce una **risposta diretta** del modello (senza tool)

Al termine, controlla il file `agent_activity.log` (viene aggiornato **solo** quando un tool viene eseguito).

## Esempi input/output

Di seguito esempi coerenti con i prompt presenti in `main.py`.

### 1) Meteo (tool: `get_weather`)

**Input**

```
Che tempo fa a Roma?
```

**Output (tool)**

```
[TOOL get_weather] Il meteo a Roma è di 22°C, cielo sereno e vento debole.
```

> Nota: `get_weather` è un **mock** (non chiama servizi meteo esterni).

### 2) Sconto (tool: `calculate_discount`)

**Input**

```
Quanto costa un prodotto da 150€ con lo sconto del 20%?
```

**Output (tool)**

```
[TOOL calculate_discount] Il prezzo originale di 150.00€, scontato del 20.0%, diventa 120.00€.
```

### 3) Conteggio parole (tool: `count_words`)

**Input**

```
conta queste parole: l'agente funziona molto bene
```

**Output (tool)**

```
[TOOL count_words] L'analisi è completata: la stringa contiene esattamente 7 parole.
```

### 4) Ora corrente (tool: `get_current_time`)

**Input**

```
Che ore sono adesso?
```

**Output (tool)**

```
[TOOL get_current_time] L'orario attuale (UTC) è 14:22:09.
```

> L’orario varia a runtime.

### 5) Domanda generale (nessun tool)

**Input**

```
Chi ha scritto la Divina Commedia?
```

**Output (risposta diretta LLM)**

```
La Divina Commedia è stata scritta da Dante Alighieri.
```

> Le risposte dirette del modello possono variare (non sono “hard-coded”).

## Eseguire i test

I test non richiedono la chiave API perché **mockano** il client OpenAI.

```bash
pytest -q
```

## Struttura del progetto

```
mini_agent_toolkit/
├─ app/
│  ├─ agent.py        # MiniAgent: chiama l’LLM e interpreta la risposta JSON
│  ├─ registry.py     # ToolRegistry: registro tool (nome → func + description)
│  ├─ tools.py        # Implementazioni dei 4 tool
│  ├─ logger.py       # log_action: scrive su agent_activity.log
│  └─ __init__.py
├─ tests/
│  ├─ test_agent.py   # unit test (mock OpenAI)
│  └─ __init__.py
├─ main.py            # demo di consegna (golden set)
├─ requirements.txt
└─ agent_activity.log # file di log (append) generato/aggiornato a runtime
```

## Spiegazione teorica

### 1) Pattern “Agent + Tools”

L’architettura separa due responsabilità:

1. **Decisione (routing / planning)**: il modello decide se serve un tool e quali parametri usare.
2. **Esecuzione (acting)**: i tool sono funzioni Python deterministiche che producono un risultato.

Questo pattern è tipico dei sistemi agentici: il modello *pianifica*, il codice *esegue*.

### 2) Perché un Tool Registry

`ToolRegistry` centralizza le capability disponibili:

- aggiungere un tool richiede solo: implementazione + registrazione (nome, descrizione)
- l’agente non dipende dai dettagli dei tool (disaccoppiamento)
- il catalogo è riutilizzabile (es. UI, docs, “tool list” nel prompt di sistema)

### 3) Controllo dell’output del modello con JSON

In `app/agent.py` il modello riceve un **system prompt** che impone un output JSON con chiavi:

- `tool`: nome del tool oppure `null`
- `params`: dizionario dei parametri da passare al tool
- `answer`: testo di risposta diretta se non serve un tool

Questo rende il routing **parsabile** e riduce l’ambiguità rispetto a testo libero.

### 4) Osservabilità: logging delle azioni

Quando un tool viene eseguito, `log_action(...)` registra:

- timestamp
- tool invocato
- prompt originale
- output del tool

Esempio di riga log:

```
[2026-02-11 14:22:09] ACTION: get_weather | IN: Che tempo fa a Roma? | OUT: Il meteo a Roma è di 22°C, cielo sereno e vento debole.
```

### 5) Testabilità (mock del modello)

I test in `tests/test_agent.py`:

- patchano `OpenAI` per evitare chiamate reali
- forzano la “risposta del modello” (JSON) per verificare:
  - happy path (tool corretto + params corretti)
  - gestione input incompleto (risposta diretta)
  - limiti/validazione (es. sconto > 100%)
  - resistenza base a prompt injection (via risposta diretta)

## Livello di difficoltà

**Intermedio (Beginner+)**

- Python: funzioni, moduli, classi semplici
- comprensione base di: environment variables, logging, test mocking
- introduzione pratica a “agentic pattern” (routing + tools)

## A chi è rivolto

- chi sta studiando **AI Agents** e vuole un esempio minimale ma realistico
- studenti/junior dev che vogliono vedere un flusso completo: registry → LLM routing → tool → log → test
- chi vuole una base da estendere verso tool più “veri” (API esterne, DB, RAG, ecc.)
