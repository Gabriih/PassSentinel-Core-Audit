import re

def mask_sensitive_data(text: str) -> str:
    """
    Substitui textos sensíveis como chaves senhas e tokens por máscaras [REDACTED].
    """
    if not text:
        return ""

    # mascara senhas longas e mantem só os dois primeiros e os dois últimos caracteres
    if len(text) <= 4:
        return "****"

    return f"{text[:2]}{'*' * (len(text) - 4)}{text[-2:]}"

def safe_log(message: str, is_sensitive: bool = False) -> str:
    """
    Formata o log e garante que os dados sensiveis não apareçam na tela
    """
    if is_sensitive:
        return f"[LOG ASSEGURADO] {mask_sensitive_data(message)}"
    return f"[LOG NORMAL] {message}"