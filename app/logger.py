import datetime

def log_action(action_name, input_data, output_data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ACTION: {action_name} | IN: {input_data} | OUT: {output_data}\n"
    with open("agent_activity.log", "a") as f:
        f.write(log_entry)
    print(f"--- Log salvato in agent_activity.log ---")