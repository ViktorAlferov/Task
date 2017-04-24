# coding: utf-8



gender = input("Пол: ")
kind_of_clothes = input("Вид одежды: ")
clasp_type = input("Вид застежки: ")
Pocket_type = input("Тип карманов: ")
Seam_length = input("Длина внутреннего шва: ")
cutting = input("Крой по посадке: ")
design_effects = input("Дизайнерские эффекты: ")
season = input("Сезон: ")


with open('data/generation.txt', 'a') as file:
	print(gender[:5] + "ие" , kind_of_clothes, "на", clasp_type[:7] + "ах", 
		"декорированные", Pocket_type[:6] + "ми", "карманами. Длинные брючины", Seam_length, 
		"Крой типа", cutting, "позволяет подчеркнуть вашу фигуру, а эффект", 
		design_effects[:9] + "и", "создает небрежный образ. Подходит на", season, "сезон.", file=file)

file.close()

# todo записывать файл
# todo форматирование строк 2 способами % format


