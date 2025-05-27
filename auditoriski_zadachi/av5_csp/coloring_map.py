from constraint import *

def notEqual(c1,c2):
    return c1 !=c2
if __name__ == '__main__':
    problem = Problem()

    variables = ["WA","NT","SA","Q","NSW","V","T"]
    problem.addVariables(variables,['R','G','B'])
    pairs = [("WA","NT"),("WA","SA"),("NT","Q"),("NT","SA"),("Q","NSW"),("Q","SA"),("NSW","SA"),("NSW","V"),("V","SA")]
    for pair in pairs:
        problem.addConstraint(notEqual,pair)
    print(problem.getSolution())

    # print(problem.getSolutions())

    # res_iter = problem.getSolutionIter()

    # for i in range(5):
    #     print(next(res_iter))