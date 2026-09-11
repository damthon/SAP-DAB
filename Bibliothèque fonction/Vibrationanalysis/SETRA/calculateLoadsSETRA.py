# -*- coding: utf-8 -*-

def calculateLoadsSETRA(Class,Frequency,Direction,Type,A_deck):
    """
    This function calculates the laods required for assessing the vibrational behavior of a footbridge using the method in SETRA  
    Input:
        - Class: Footbridge class
        -  Frequency: Frequency of the mode considered
        -  Direction: Direction of the accelerations, 'V' for vertical, 'La' for lateral (transverse) and 'Lo' for longitudinal
        - Type: Footbridge type, 'RC'(reinforced concrete), 'PC' (prestressed concrete), 'CO' (composite), 'S' (steel), 'T' (timber)
        - A_deck: Total deck area
    
    Output:
        - p_SETRA: Pedestrian load in N/m2

    """    
    # Load models
    # Critical damping ratio
    if Type == 'RC':
        eta = 0.013
    elif Type == 'PC' or Type == 'T':
        eta = 0.01
    elif Type == 'CO':
        eta = 0.006
    elif Type == 'S':
        eta = 0.004
    
    # Resonance risk 
    if Direction == 'V' or Direction == 'Lo': # Vertical and longitudinal vibrations
        if Frequency <=2.1 and Frequency>=1.7:
            risk_resonance = 1 # Maximum risk
        elif (Frequency <=2.6 and Frequency>=2.1) or (Frequency <1.7 and Frequency>=1.0):
            risk_resonance = 2 # Medium risk
        elif (Frequency >2.6 and Frequency<=5):
            risk_resonance = 3 # Low risk
        else:
            risk_resonance = 4 # Negligible risk
    else: # Lateral vibrations
        if Frequency <=1.1 and Frequency>=0.5:
            risk_resonance = 1 # Maximum risk
        elif (Frequency <=1.3 and Frequency>=1.1) or (Frequency <0.5 and Frequency>=0.3):
            risk_resonance = 2 # Medium risk
        elif (Frequency >1.3 and Frequency<=2.5):
            risk_resonance = 3 # Low risk
        else:
            risk_resonance = 4 # Negligible risk
     
    # Dynamic load cases
    LC = []
    if (Class == 'II' or Class == 'III') and (risk_resonance == 1 or risk_resonance == 2):
        LC.append(1)
    elif Class == 'I':
        LC.append(2)
    if (Class == 'I' or Class == 'II'): # Second harmonic
        LC.append(3)
    
    # Crowd density [pedestrian/m2] and equivalent number of pedestrians
    Crowd_D = []
    N_eq = []
    if 1 in LC and Class == 'II':
        Crowd_D.append(0.8)
        n = 0.8*A_deck
        n_eq = 10.8*(eta*n)**0.5
        N_eq.append(n_eq)
    elif 1 in LC and Class == 'III':
        Crowd_D.append(0.5)
        n = 0.5*A_deck
        n_eq = 10.8*(eta*n)**0.5
        N_eq.append(n_eq)
    elif 2 in LC:
        Crowd_D.append(1.0)
        n = 1.0*A_deck
        n_eq = 1.85*(n)**0.5
        N_eq.append(n_eq)
    # Second harmonic
    if 3 in LC and Class == 'I':
        Crowd_D.append(1.0)
        n = 1.0*A_deck
        n_eq = 1.85*(n)**0.5
        N_eq.append(n_eq)
    elif  3 in LC and Class == 'II':
        Crowd_D.append(0.8)
        n = 0.8*A_deck
        n_eq = 10.8*(eta*n)**0.5
        N_eq.append(n_eq)
    
    # Reduction coefficients (accounts for probability that footfall frequency approaches critical range of natural frequencies)
    if Direction == 'V' or Direction == 'Lo':
        # Vertical and longitudinal vibrations
        psi_ver = []
        if 1 in LC or 2 in LC:
            if Frequency<=2.1 and Frequency>=1.7:
                psi_ver_temp = 1.0
            elif Frequency<1.7 and Frequency>=1.0:
                psi_ver_temp = (Frequency - 1.0)/0.7
            elif Frequency>2.1 and Frequency<=2.6:
                psi_ver_temp = (2.6 - Frequency )/0.5
            else:
                psi_ver_temp = 0
            psi_ver.append(psi_ver_temp)
        if 3 in LC:
            if Frequency<=4.2 and Frequency>=3.4:
                psi_ver_temp = 1.0
            elif Frequency<3.4 and Frequency>=2.6:
                psi_ver_temp = (Frequency - 2.6)/0.8
            elif Frequency>4.2 and Frequency<=5:
                psi_ver_temp = (5 - Frequency )/0.8
            else:
                psi_ver_temp = 0
            psi_ver.append(psi_ver_temp)
    else:
        # Lateral vibrations
        psi_lat = []
        if 1 in LC or 2 in LC:
            if Frequency<=1.1 and Frequency>=0.5:
                psi_lat_temp = 1.0
            elif Frequency<0.5 and Frequency>=0.3:
                psi_lat_temp = (Frequency - 0.3)/0.2
            elif Frequency>1.1 and Frequency<=1.3:
                psi_lat_temp = (1.3 - Frequency )/0.3
            else:
                psi_lat_temp = 0
            psi_lat.append(psi_lat_temp)
        if 3 in LC:
            if Frequency<=2.1 and Frequency>=1.7:
                psi_lat_temp = 1.0
            elif Frequency<1.7 and Frequency>=1.3:
                psi_lat_temp = (Frequency - 1.3)/0.4
            elif Frequency>2.1 and Frequency<=2.5:
                psi_lat_temp = (2.5 - Frequency )/0.4
            else:
                psi_lat_temp = 0
            psi_lat.append(psi_lat_temp)
    
    # Load Case Models
    # F = p_uni*cos*(2πtfv*t)
    if Direction == 'V':
        P = 280 # Component due to single pedestrian [N]
        p_uni_V = []
        for i in range(len(LC)):
            if LC[i] == 3:
                P = 70
            p_uni_V.append(N_eq[i]*P*psi_ver[i]/A_deck)
    elif Direction == 'Lo':
        P = 140 # Component due to single pedestrian [N]
        p_uni_Lo = []
        for i in range(len(LC)):
            if LC[i] == 3:
                P = 35
            p_uni_Lo.append(N_eq[i]*P*psi_ver[i]/A_deck)
    elif Direction == 'La':
        P = 35 # Component due to single pedestrian [N]
        p_uni_La = []
        for i in range(len(LC)):
            if LC[i] == 3:
                P = 7
            p_uni_La.append(N_eq[i]*P*psi_lat[i]/A_deck)
    
    if Direction == 'V':
        p_SETRA = p_uni_V
    elif Direction == 'La':
        p_SETRA = p_uni_La
    else:
        p_SETRA = p_uni_Lo
    
    return p_SETRA
            