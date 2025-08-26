import secrets
import string as s

Sr = secrets.SystemRandom()

def gerar_senhas(qtd_caracteres, qtd_senhas, incluir_maiusculas=True,
                 incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    
    senha_ = ""
    if incluir_maiusculas:
        senha_ += s.ascii_uppercase
    if incluir_minusculas:
        senha_ += s.ascii_lowercase
    if incluir_numeros:
        senha_ += s.digits
    if incluir_simbolos:
        senha_ += s.punctuation

    if not senha_:
        raise ValueError("Nenhum tipo de caractere selecionado.")

    return ["".join(Sr.choices(senha_, k=qtd_caracteres)) for _ in range(qtd_senhas)]
