from collections import defaultdict, deque

# Keep last 5 messages per channel
chat_memory = defaultdict(lambda: deque(maxlen=5))

def add_to_memory(channel_id: str, role: str, content: str):
    chat_memory[channel_id].append({"role": role, "content": content})

def get_memory(channel_id: str):
    return list(chat_memory[channel_id])
