import CoolProp.CoolProp as CP
import math


def hamada():
    T_b = 353.15
    delta_T_sup_b = 5
    T_cond = 308.15
    T_ev = 278.15
    delta_T_sup_ev = 5
    P_ev = 380000
    Fluid_name = 'R1234yf'
    # P_t = float(input('enter P_t: '))
    tolerance = 10 ** -8
    A_nozzle_p_guess = 10 ** -4
    A_nozzle_s_guess = 10 ** -3
    convergence_achieved = False
    eta_ejector = 0.97
    eta_nozzle_s = 97
    eta_diffuser = 98
    m_dot_secondary = 491

    ER = 0.1
    COP = 0.1
    AR = 0.1
    Q_evap = 6000
    eta_nozzle_p = 97


    iterator = 1
    while iterator < 1000:

        h_gen =  CP.PropsSI('H', 'T', T_b + delta_T_sup_b, 'Q', 1, Fluid_name)

        h_cond = CP.PropsSI('H', 'T', T_cond, 'Q', 0, Fluid_name)

        h_evap = CP.PropsSI('H', 'T', T_ev + delta_T_sup_ev, 'Q', 1, Fluid_name)

        rho_gen = CP.PropsSI('D', 'T', T_b + delta_T_sup_b, 'P', P_ev, Fluid_name)

        rho_evap = CP.PropsSI('D', 'T', T_ev + delta_T_sup_ev, 'P', P_ev, Fluid_name)
       
        delta_h_evap_cond = h_cond - h_evap
        m_dot = Q_evap / delta_h_evap_cond

        delta_h_gen_evap = h_evap - h_gen     
        P_ratio = delta_h_gen_evap / (m_dot * eta_nozzle_p) 

        A_nozzle_p_new = m_dot / (math.sqrt(2 * rho_gen * P_ratio))
        A_nozzle_s_new = m_dot / (math.sqrt(2 * rho_evap))

        if ((A_nozzle_p_new - A_nozzle_p_guess) < tolerance and (A_nozzle_s_new - A_nozzle_s_guess) < tolerance):
            convergence_achieved = True
            break

        A_nozzle_p_guess = A_nozzle_p_new
        A_nozzle_s_guess = A_nozzle_s_new

    if (convergence_achieved == True):
        eta_ejector = (1 - (1 - eta_nozzle_p) / (1 - eta_nozzle_s)) * eta_diffuser
        ER = m_dot / (m_dot_secondary)
        COP = Q_evap / (m_dot * (h_evap - h_cond))

        AR = A_nozzle_s_guess / A_nozzle_p_guess
        print('Primary Nozzle Area (A_nozzle_p): ', str(A_nozzle_p_guess) + ' m^2')
        print('Secondary Nozzle Area (A_nozzle_s): ', str(A_nozzle_s_guess) + ' m^2')
        print('Refrigerant Mass Flow Rate (m_dot): ', str(m_dot) + ' kg/s')
        print('Ejector Efficiency: ', str(eta_ejector))
        print('Entrainment Ratio (ER): ', str(ER))
        print('Coefficient of Performance (COP): ', str(COP))
        print('Nozzle Area Ratio (AR): ', str(AR))

hamada()