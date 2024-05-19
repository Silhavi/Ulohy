import os

# při úkolu jsem používal Github Copilot (a Fandu Václavka)


lines = []
print()
def find_product (product, regaly, strict = True):
    ...
    for i,regal in enumerate(regaly):
        for item in regal:
            if strict:
                if product.lower() == item.lower():
                    return i, item
            else:                
                if product.lower() in item.lower():
                    return i, item
    return -1, None
    

def main():
    path = './../test_cases_6/CZE/0002_in.txt'
    lines = open(path).read().split('\n\n')
    
    #lines = [line.split('#') for line in lines]
    #lines = [line.split('\n') for line in lines]
    
    
    
    regaly = lines[0]
    seznamy = lines[1:]
    if len(seznamy) == 0:
        print("Chyba: Nebyly nalezeny žádné seznamy")
        return

    
    regaly = regaly.split('#')[1:]
    regaly = [regal.split('\n')[1:] for regal in regaly]
    
    
    
    for seznam in seznamy:
        produkty = seznam.split('\n')
    
        nalezene_itemy = []
        nenalezene_itemy = []
        
        for product in produkty:
            regal, item = find_product(product, regaly)
            if regal == -1:
                regal, item = find_product(product, regaly, False)
            if regal == -1:
                nenalezene_itemy.append(product)
            else:
                nalezene_itemy.append((product, regal, item, ))
        
        nalezene_itemy.sort(key = lambda x: x[1])
        
        
        print("Optimalizovany seznam:")
        for i, item in enumerate(nalezene_itemy):
            print(f" {i}. {item[0]} -> #{item[1]} {item[2]}")
        for i, item in enumerate(nenalezene_itemy):
            print(f" {i + len(nalezene_itemy)}. {item} -> N/A")
    
    print()

if __name__ == "__main__":
    main()