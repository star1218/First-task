# n1=int(input("Ведите число:")) #Домашка задание 1
# n2=int(input("Ведите число:"))
# n3=int(input("Ведите число:"))
# operation=input("Выберите Операцию Максимум или Минимум или Среднее:")
# if operation=="Максимум":
#     if n1 >= n2:
#         if n1 >= n3:  #находим максимум
#             result = n1
#         elif n2 >= n1 and n2 >= n3:
#             result = n2
#         else:
#             result = n3
#             print("Максимум:",result)
#     elif n2 >= n1 and n2 >= n3:
#         result = n2
#     else:
#         result = n3
#         print("Максимум:",result)
# elif operation =="Минимум":
#     if n1 <= n2:
#         if n1 <= n3: #находим минимум
#             result = n1
#         elif n2 <= n1 and n2 <= n3:
#             result = n2
#         else:
#             result = n3
#             print("Минимум",result)
#     elif n2 <= n1 and n2 <= n3:
#         result = n2
#     else:
#         result = n3
#         print("Минимум",result)
# elif operation =="Среднее":
#     result=(n1+n2+n3)/3 #Находим Среднее арифметическое по формуле
#     print("Среднее",result)
# else:
#     print("Ошибка")
#
#
# meters=float(input("Ведите число:")) #Домашка задание 2
# operation=input("Выберите операцию Мили , Дюймы , Ярды:")
# if operation=="Мили":
#     miles= meters / 1609.34
#     print("Метры в мили", miles)
# elif operation=="Дюймы":
#     inches = meters * 39.3701
#     print("Метры в Дюймы", inches)
# elif operation=="Ярды":
#     yards = meters * 1.09361
#     print("Метры в Ярды", yards)
# else:
#     print("Ошибка")