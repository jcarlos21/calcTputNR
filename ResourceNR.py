

class ResourceNR:
    def __init__(self, frequencyRange, bandWidth, carrieAggregation):
        pass










ca = 1

pot10e6 = pow(10, -6)
v = 4
qam = 6
scalingFactor = 1
uNumerology = 0
Rmax = 948/1024
N_BW_PBR = 52
Ts_U = pow(10, -3) / (14*pow(2, uNumerology))
OH = 0.14

calc = pot10e6 * (v * qam * scalingFactor * Rmax * ((N_BW_PBR * 12) / Ts_U) * (1 - OH))

print(calc)