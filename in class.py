def P_and_S(lenght: float, width: float) -> tuple[float, float]:
    ''' P_and_S '''
    P = (lenght + width) * 2
    S = lenght * width
    return P, S

def P_and_Price_of_zabor(p: float, price:float) -> float:
    '''P_and_Price_of_zabor'''
    end_price = p * price
    return end_price

def S_and_Price_of_earth(s: float, price:float) -> float:
    '''S_and_Price_of_earth'''
    end_price = s * price *1.5
    return end_price

def main():
    lenght = int(input('Enter lenght:'))
    widht = int(input('Enter widht:'))
    price_of_zabor = int(input('Enter price of zabor:'))
    price_of_earht = int(input('Enter price of earht:'))
    
    p, s = P_and_S(lenght,widht)
    print(P_and_Price_of_zabor(p, price_of_zabor),S_and_Price_of_earth(s, price_of_earht))

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    