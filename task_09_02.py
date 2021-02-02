old_dict = {'ab': 1, 'sda': 2, 'c1': 3, '3': 'fddf'}
func = lambda *kwargs: {str(k) + str(k): v for i in kwargs for k, v in i.items()}

print(func(old_dict))
