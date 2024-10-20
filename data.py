from datetime import datetime

def get_current_time():
    # Повертає поточний час у форматі ISO 8601
    return datetime.now().isoformat()
