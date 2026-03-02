import sys
from island_counter import parse_board, count_islands
from exceptions import IslandError


def main():
    if len(sys.argv) != 2:
        print("Error: Uso correcto -> python cli.py <fichero>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        board = parse_board(lines)
        result = count_islands(board)

        print(f"Número de islas: {result}")

    except FileNotFoundError:
        print("Error: No se pudo leer el fichero.")
        sys.exit(1)

    except IslandError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()