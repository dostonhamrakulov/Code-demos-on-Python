from pyschedule import Scenario, solvers, plotters, alt
S = Scenario('schedule_cost',horizon=10)
R = S.Resource('R')

# not setting a schedule cost will set it to None
T0 = S.Task('T0',length=2,delay_cost=1)
# setting the schedule cost of T1 to -1
T1 = S.Task('T1',length=2,delay_cost=1,schedule_cost=-1)

T0 += R
T1 += R
solvers.mip.solve(S,msg=1)
print(S.solution())

plotters.matplotlib.plot(S,img_filename='pyschedule_2.png')
