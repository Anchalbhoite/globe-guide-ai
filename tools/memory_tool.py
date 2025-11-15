from google.adk.tools import FunctionTool

USER_MEMORY = {}

def save_preference(user_id: str, key: str, value: str):
    if user_id not in USER_MEMORY:
        USER_MEMORY[user_id] = {}
    USER_MEMORY[user_id][key] = value
    return {"status": "saved"}

def read_preference(user_id: str):
    return USER_MEMORY.get(user_id, {})

memory_save = FunctionTool(save_preference, name="save_preference")
memory_read = FunctionTool(read_preference, name="read_preference")
