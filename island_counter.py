from typing import List, Tuple
from exceptions import InvalidBoardFormat


# 8 direcciones (incluye diagonales)
DIRECTIONS: Tuple[Tuple[int, int], ...] = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)


def parse_board(lines: List[str]) -> List[List[int]]:
    """
    Convierte líneas de texto en una matriz validada.

    Se valida:
    - No vacío
    - Rectangular
    - Solo caracteres 0 y 1

    Se lanza InvalidBoardFormat si algo no cumple.
    """
    if not lines:
        raise InvalidBoardFormat("El fichero está vacío.")

    cleaned = [line.strip() for line in lines if line.strip()]
    if not cleaned:
        raise InvalidBoardFormat("El fichero no contiene datos válidos.")

    row_length = len(cleaned[0])

    for row in cleaned:
        if len(row) != row_length:
            raise InvalidBoardFormat("El tablero no es rectangular.")

        if any(c not in {"0", "1"} for c in row):
            raise InvalidBoardFormat("Solo se permiten caracteres 0 y 1.")

    # Convertimos a enteros por eficiencia en comparación
    return [[int(c) for c in row] for row in cleaned]


def count_islands(board: List[List[int]]) -> int:
    """
    Cuenta el número de islas usando DFS iterativo.

    Diseño:
    - Usamos un set para visited → O(1) lookup.
    - DFS con pila explícita → evita stack overflow.
    - No modificamos el tablero original.
    """
    if not board:
        return 0

    rows = len(board)
    cols = len(board[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1 and (r, c) not in visited:
                islands += 1
                _explore(board, r, c, visited)

    return islands


def _explore(board: List[List[int]], start_r: int, start_c: int, visited: set):
    """
    DFS iterativo.

    Elegimos versión iterativa porque:
    - Es más robusta en mapas grandes.
    - Evita límite de recursión de Python.
    """
    stack = [(start_r, start_c)]
    rows = len(board)
    cols = len(board[0])

    while stack:
        r, c = stack.pop()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                board[nr][nc] == 1 and
                (nr, nc) not in visited
            ):
                stack.append((nr, nc))