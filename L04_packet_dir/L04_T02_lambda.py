def ident(x):
    return x

print(ident(10))

print( (lambda x: x)(10)  )

ident_lambda = lambda x: x

print(ident_lambda(10))

car = lambda brend, engine_volume, price: f'Car: {brend.title()}, Engine volume: {engine_volume}, Price: {price}'

print(car('volvo', 1.5, 1300000))

print(type(ident_lambda), type(ident))