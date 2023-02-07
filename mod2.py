mrx_field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ КРЕСТИКИ НОЛИКИ!')

#Выводим поле на экран
def print_field(my_field):
	print ("  |", 0, "|", 1, "|", 2, "|")
	for i in range(3):
		print ('  '+'-'*13)
		print (i ,"|", my_field[0][i], "|", my_field[1][i], "|", my_field[2][i], "|")

#def print_fieldx(my_field):
#	for i in my_field:
#		print(f'\n')
#		for j in i:
#			print(f' {j} ', end = " ")

#Делаем ход
def make_move(x, y, my_player):
	#Защита от "дурака" на корректный ввод
	try:
		x = int(x)
		y = int(y)
	except:
		print(f"Некорректный ввод. Вы уверены, что ввели число?")
		return False

	if (x <= 2 and x >= 0) and (y <= 2 and y >= 0):
		if mrx_field[x][y] == '-':
			mrx_field[x][y] = my_player
			return True
		else:
			print(f'ЭТА КЛЕТКА УЖЕ ЗАНЯТА!')
			return False
	else:
		print(f'Число дожно быть от 0 до 2')
		return False

#Проверяем выигррал ли кто-то
def check_win(my_field, my_player):
	result = False

	for i in my_field: #Проверяем горизонтали
		if i[0] == my_player and i[1] == my_player and i[2] == my_player:
			result = True

	#Вертикали
	if my_field[0][0] == my_player and my_field[1][0] == my_player and my_field[2][0] == my_player:
		result = True
	if my_field[0][1] == my_player and my_field[1][1] == my_player and my_field[2][1] == my_player:
		result = True
	if my_field[0][2] == my_player and my_field[1][2] == my_player and my_field[2][2] == my_player:
		result = True

	#Диагонали
	if my_field[0][0] == my_player and my_field[1][1] == my_player and my_field[2][2] == my_player:
		result = True
	if my_field[0][2] == my_player and my_field[1][1] == my_player and my_field[2][0] == my_player:
		result = True

	return result

step = 1 #Счетчик хода
player = '+' #Игрок чей ход

while step < 10:
	print(f'\nХод: {step} Игрок: {player}')
	print_field(mrx_field)

	#ПОльзователь вводит координаты
	while True:
		cx = input('Введите столбец:')
		cy = input('Введите строку:')
		if make_move(cx, cy, player):
			break

	print_field(mrx_field)

	#Проверка выигрыша
	if check_win(mrx_field, player):
		print(f"\n\nПОЗДРАВЛЯЕМ!!! ПОБЕДИЛ ИГРОК: {player}")
		break

	#Меняем игрока
	if player == '+':
		player = '0'
	else:
		player = '+'

	step += 1

	if step == 9:
		print('НИЧЬЯ!')

print(f'\n\nИГРА ЗАКОНЧЕНА.')
input('Нажмите Enter для выхода...')
