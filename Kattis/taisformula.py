trap = 0.0

for i in range(int(input())):
    if i == 0:
        init = input().split()
        ms_init = int(init[0])
        glu_init = float(init[1])
    else:
        curr = input().split()
        ms_curr = int(curr[0])
        glu_curr = float(curr[1])
        
        trap_curr = (glu_curr + glu_init) / 2
        trap_curr *= ms_curr - ms_init
        trap += trap_curr
        
        ms_init = ms_curr
        glu_init = glu_curr

print(trap / 1000)
