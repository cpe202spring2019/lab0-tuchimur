def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    weight_mars = weight*0.38
    weight_jupiter = weight*2.34   
    output = "\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds."
    print(output.format(weight_mars, weight_jupiter))	
   
if __name__ == '__main__':
   weight_on_planets()
