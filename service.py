from data import get_current_time

def get_greeting():
    # Логіка формування привітання
    full_name = "Maksym Matsiuk"
    current_time = get_current_time()
    greeting_message = f"""
        Welcome to the Internet {full_name}, have a little fun. Time of last refresh:{current_time}
        """

    return greeting_message
