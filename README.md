# 🎯 Reto: Contador de Islas en un Mapa Binario

## 📌 Requisitos Funcionales

El programa debe:

- Recibir exactamente 1 argumento por línea de comandos:
`python islands.py <ruta_fichero>`

- Leer un fichero de texto que contenga un tablero rectangular o cuadrado.

- El tablero solo puede contener caracteres 0 y 1,cada línea representa una fila, y todas las filas deben tener la misma longitud.

- Definición de isla:
	- Conjunto de celdas 1
	- Adyacencia en 4 direcciones (arriba, abajo, izquierda, derecha)
	- Rodeadas por 0 o límites del tablero

- Manejo de errores:
	- Número incorrecto de argumentos
	- Fichero inexistente o no legible
	- Formato inválido

- Debe soportar:
	- Tableros de cualquier tamaño
	- Todo agua
	- Todo tierra
	- Una sola celda
	- Muchas islas

## 🚀 Cómo ejecutar el reto

### Instalar pytest:

`pip install pytest`

### Ejecutar:

`pytest`

### Ejecutar CLI:

`python cli.py [file_with_map.txt`