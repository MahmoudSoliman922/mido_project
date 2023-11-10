import CoolProp.CoolProp as CP


def hamada():
    T_b = float(input('enter T_b: '))
    delta_T_sup_b = float(input('enter delta_T_sup_b: '))
    T_cond = float(input('enter T_cond: '))
    T_ev = float(input('enter T_ev: '))
    delta_T_sup_ev = float(input('enter delta_T_sup_ev: '))
    P_ev = float(input('enter P_ev: '))
    Fluid_name = input('enter Fluid_name: ')
    P_t = float(input('enter P_t: '))

    h_gen =  CP.PropsSI('H', 'T', T_b + delta_T_sup_b, 'Q', 1, Fluid_name)

    h_cond = CP.PropsSI('H', 'T', T_cond, 'Q', 0, Fluid_name)

    h_evap = CP.PropsSI('H', 'T', T_ev + delta_T_sup_ev, 'Q', 1, Fluid_name)

    rho_gen = CP.PropsSI('D', 'T', T_b + delta_T_sup_b, 'P', P_ev, Fluid_name)

    rho_evap = CP.PropsSI('D', 'T', T_ev + delta_T_sup_ev, 'P', P_ev, Fluid_name)

    print('h_gen: ', h_gen)
    print('h_cond: ', h_cond)
    print('h_evap: ', h_evap)
    print('rho_gen: ', rho_gen)
    print('rho_evap: ', rho_evap)

hamada()