from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()
    
    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13","Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12", "Wed_13","Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13","Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]
    
    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]
    
    # ---Tuka dodadete gi promenlivite--------------------
    variables = ["AI_predavanje", "ML_predavanje", "R_predavanje", "BI_predavanje", "AI_vezbi", "ML_vezbi", "BI_vezbi"]
    problem.addVariable("AI_predavanje", AI_predavanja_domain)
    problem.addVariable("ML_predavanje", ML_predavanja_domain)
    problem.addVariable("R_predavanje", R_predavanja_domain)
    problem.addVariable("BI_predavanje", BI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(),variables)



    # ----------------------------------------------------
    solution = problem.getSolution()
    
    print(solution)