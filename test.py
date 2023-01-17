# def display(board):
#     width = len(board[0])
#     height = len(board)
#     for i in range(width):
#         print(chr(i + 97), end=' ')
#     print()
#     for y in range(height):
#         for x in range(width):
#             element = board[y][x]
#             if type(element) is dict: # Si l'élèment est un dictionnaire, alors c'est un bloc d'une shape
#                 print(colored(element["content"], element["color"]), end=' ')
#             elif element == 2:
#                 print(" ", end=' ')
#             else:
#                 print(".", end=' ')
#         print(chr(y + 65))
#     print() 

# print("triangle")
# display(map_triangle)
# print()
# print("============")
# print()
# print("losange")
# display(map_losange)
# print()
# print("============")
# print()
# print("cercle")
# display(map_cercle)