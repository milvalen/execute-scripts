import os
import sys
import io
import traceback

SCRIPTS_DIR = "scripts"

for i, script_file in enumerate([f for f in os.listdir(SCRIPTS_DIR) if f.endswith('.py')]):
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    stdstream = io.StringIO()
    sys.stdout = stdstream
    sys.stderr = stdstream
    
    try:
        with open(os.path.join(SCRIPTS_DIR, script_file), 'r') as file:
            exec(file.read())
        result_message = f"Script {script_file} executed successfully"
    except Exception as e:
        exception = traceback.format_exc().split('\n')[-2]
        result_message = f"\nError in script at index {i} ({script_file}):\n{exception}\n"
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
    print(result_message)
