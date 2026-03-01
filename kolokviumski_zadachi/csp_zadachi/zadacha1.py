from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    domains = [0,1,2,3,4,5,6,7,8,9]

    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))
    
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)

    # problem.addConstraint(NotInSetConstraint({0}),["S","M"])

    problem.addConstraint(
        lambda S, E, N, D, M, O, R, Y:
        (1000*S + 100*E + 10*N + D) +
        (1000*M + 100*O + 10*R + E) ==
        (10000*M + 1000*O + 100*N + 10*E + Y),
        ["S", "E", "N", "D", "M", "O", "R", "Y"]
    )

    # ----------------------------------------------------
    
    print(problem.getSolution())