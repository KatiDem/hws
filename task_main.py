n = 1


def in_to_cm(inch):
    return inch * 2.54


def cm_to_in(cm):
    return cm / 2.54


def mile_to_km(mile):
    return mile * 1.609344


def km_to_mile(km):
    return km * 0.6213711922373


def lb_to_kg(lb):
    return lb * 0.45359237


def kg_to_lb(kg):
    return kg * 2.44192843875


def ozt_to_gr(ozt):
    return ozt * 28.349523125


def gr_to_ozt(gr):
    return gr * 0.03527396194958


def gal_to_l(gal):
    return gal * 3.785411784


def l_to_gal(l):
    return l * 0.2641720523581


def pt_to_l(pt):
    return pt * 0.473176473


def l_to_pt(l):
    return l * 2.113376418865


# options = {1: 'Дюймы в сантиметры', 2:'Сантиметры в дюймы', 3:'Мили в километры', 4:'Километры в мили', 5:'Фунты в килограммы', 6: 'Килограммы в фунты', 7: 'Унции в граммы', 8: 'Граммы в унции', 9: 'Галлон в литры', 10: 'Литры в галлоны', 11: 'Пинты в литры', 12: 'Литры в пинты'}
while True:
    print('1.Дюймы в сантиметры 2.Сантиметры в дюймы 3.Мили в километры 4.Километры в мили\n5.Фунты в килограммы 6.Килограммы в фунты 7.Унции в граммы 8.Граммы в унции\n9.Галлон в литры 10.Литры в галлоны 11.Пинты в литры 12.Литры в пинты')
    n = int(input('choose conversion type\nfor EXIT type 0\noption № : '))
    if n == 0:
        break
    if n > 12 or n < 0:
        print('Input numbers from 1 to 12')
        continue
    user_input = int(input('What number u want to convert : '))
    if n == 1:
        print(f'Дюймы в сантиметры. {user_input} in = {in_to_cm(user_input)} cm')
    elif n == 2:
        print(f'Сантиметры в дюймы. {user_input} cm = {cm_to_in(user_input)} in')
    elif n == 3:
        print(f'Мили в километры. {user_input} miles = {mile_to_km(user_input)} km')
    elif n == 4:
        print(f'Километры в мили. {user_input} km = {km_to_mile(user_input)} miles')
    elif n == 5:
        print(f'Фунты в килограммы. {user_input} lb = {lb_to_kg(user_input)} kg')
    elif n == 6:
        print(f'Килограммы в фунты. {user_input} kg = {cm_to_in(user_input)} lb')
    elif n == 7:
        print(f'Унции в граммы. {user_input} ozt = {ozt_to_gr(user_input)} gr')
    elif n == 8:
        print(f'Граммы в унции. {user_input} gr = {gr_to_ozt(user_input)} miles')
    elif n == 9:
        print(f'Галлон в литры. {user_input} gal = {gal_to_l(user_input)} l')
    elif n == 10:
        print(f'Литры в галлоны. {user_input} l = {l_to_gal(user_input)} gal')
    elif n == 11:
        print(f'Пинты в литры. {user_input} pt = {pt_to_l(user_input)} l')
    elif n == 9:
        print(f'Литры в пинты. {user_input} l = {l_to_pt(user_input)} pt')
