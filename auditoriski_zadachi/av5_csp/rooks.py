from constraint import *
def not_attacking(c1,c2):
    
    return True if c1[0] != c2[0] and c1[1] != c2[1] else False
if __name__ == '__main__':
    problem = Problem()
    variables = ["cannon_"+str(n) for n in range(8)]
    domain = [(row,col) for row in range(8) for col in range (8)]
    problem.addVariables(variables,domain)
    
    for cannon1 in variables:
        for cannon2 in variables:
            if(cannon1!=cannon2):
                problem.addConstraint(not_attacking,(cannon1,cannon2))
    print(problem.getSolution().values())
    
    for i in range(8):
        for j in range(8):
            print("T" if (i,j) in problem.getSolution().values() else "_",end="")
        print()