import DatosProcNR as nr

class ResourceNR:
    def __init__(self, frequencyRange='FR1', bandWidth='10 MHz', carrieAggregation=1, SCS='15 MHz', modulation='QPSK', mimo='2x2'):
        self.fr = frequencyRange
        self.bw = bandWidth
        self.ca = carrieAggregation
        self.scs = SCS
        self.modulation = modulation
        self.mimo = mimo
    
    def calcTputNR (self):
        max_calcNR = 0
        min_calcNR = 0
        v = nr.MIMO(self.mimo)
        qam = nr.nModulation(self.modulation)
        scalingFactor = 1
        uNumerology = 0
        Rmax = 948/1024
        nPBR, nPBR_m= nr.nBW_PBR(self.bw, self.scs)
        Ts_U = pow(10, -3) / (14*pow(2, uNumerology))
        oH = nr.nFR(self.fr)

        for i in range(0, int(self.ca)):
            if nPBR == 'N/A':
                return 'N/A'
            else:
                max_calcNR = max_calcNR + pow(10, -6) * (v * qam * scalingFactor * Rmax * ((nPBR * 12) / Ts_U) * (1 - oH))
                min_calcNR = min_calcNR + pow(10, -6) * (v * qam * scalingFactor * Rmax * ((nPBR_m * 12) / Ts_U) * (1 - oH))
        
        return max_calcNR.__round__(2), min_calcNR.__round__(2)
