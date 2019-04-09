from pyschedule import Scenario, solvers, plotters, alt
S = Scenario('resource_cost',horizon=10)

# assign a cost per period of 5
R = S.Resource('R',cost_per_period=5)

T = S.Task('T',length=2,delay_cost=1)
T += R
solvers.mip.solve(S,msg=1)
print(S.solution())

plotters.matplotlib.plot(S,img_filename='pyschedule_3.png')
