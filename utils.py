def validar_inteiro(valor, minimo=1):
    try:
        inteiro = int(valor)
        if inteiro < minimo:
            return False, f"⚠️ MÍNIMO {minimo}"
        return True, inteiro
    except ValueError:
        return False, "⚠️ APENAS NÚMEROS"
