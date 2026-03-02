class IslandError(Exception):
    """Excepción base del dominio."""
    pass


class InvalidBoardFormat(IslandError):
    """Se lanza cuando el tablero no cumple el formato esperado."""
    pass