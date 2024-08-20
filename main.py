import os
import traceback

SCRIPTS_DIR = "scripts"

for i, script_file in enumerate([f for f in os.listdir(SCRIPTS_DIR) if f.endswith('.py')]):
    try:
        exec(open(os.path.join(SCRIPTS_DIR, script_file), 'r').read())
        print(f"Script {script_file} executed successfully")
    except Exception:
        print(f"\nError in script at index {i} ({script_file}):\n{traceback.format_exc()}")

