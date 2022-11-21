# Table 5.3.2-1: Maximum transmission bandwidth configuration NRB

bandWidth = ['5 MHz','10 MHz', '15 MHz', '20 MHz', '25 MHz', '30 MHz', '40 MHz', '50 MHz', '60 MHz', '80 MHz', '90 MHz' '100 MHz']
space15 = [25, 52, 79, 106, 133, 160, 216, 270, 'N/A', 'N/A', 'N/A', 'N/A']
space30 = [11, 24, 38, 51, 65, 78, 106, 133, 162, 217, 245, 273]
space60 = ['N/A', 11, 18, 24, 31, 38, 51, 65, 79, 107, 121, 135]

nPBRs = {'15 MHz': space15, '30 MHz': space30, '60 MHz': space60}

def nBW_PBR(bw, SCS):
    idPBRBW = bandWidth.index(bw)
    return nPBRs[SCS][idPBRBW]

# Frenquency Range

fr_value = {'FR1': 0.14, 'FR2': 0.18}
def nFR(fR):
    return fr_value[fR]

# Tabela de dados 2: MIMO

mimo_value = {'2x2': 2 , '4x4': 4, '8x8': 8}
def MIMO(mimo):  # deve receber a configuração de antenas (ex.: 2x2)
    return mimo_value[mimo]

# Modulation

modulation_value = {'QPSK': 2, '16QAM': 4, '64QAM': 6, '256QAM': 8}
def nModulation(modulation):
    return modulation_value[modulation]
