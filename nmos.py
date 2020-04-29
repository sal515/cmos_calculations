import math

# variable setup
significantFig = 8

Cox = 1 / 1
Un = 90 / 1000000  # (A/v^2)
CoxUn = Cox * Un
w = 3
l = 1
Bn = CoxUn * (w / l)

Vtno = 0.6  # V

y = 0.5  # (v^1/2)
phi = 0.3  # V
lambda_ = 0.02  # 1/V

Vdd = 3.3  # V
Vss = 0  # V

Vg = 1  # V
Vs = 0.0  # V
Vd = 2  # V
Vb = Vss  # V

# Nmos Node Voltages
Vgs = Vg - Vs
Vds = Vd - Vs
Vsb = Vs - Vb

# Nmos

if Vs == Vb:
    Vtn = Vtno

else:
    Vtn = Vtno + y * (math.sqrt(2 * phi + Vsb) - math.sqrt(2 * phi))


VovN = Vgs - Vtn


# Calculation functions


def calculate_ids():
    # Nmos Ids calculations
    if Vb > Vs:
        print("Improper Bias")

    elif Vgs < Vtn:
        print("Cut-off mode")


    elif Vds >= VovN:
        print("Saturation Mode")
        ids = 0.5 * Bn * math.pow(VovN, 2) * (1 + lambda_ * Vds)
        print("Saturation current", round(ids, significantFig))

    elif Vds < VovN:
        print("Triode Mode")
        ids = Bn * ((VovN * Vds) - (0.5 * math.pow(Vds, 2)))
        print("Triode current", round(ids, significantFig))


# Calculation calls

calculate_ids()



# Pmos Node Voltages
# Vsg = Vs - Vg
# Vsd = Vs - Vd
# Vbs = Vb - Vs

# # Pmos
# Vtp = Vtpo + y * (math.sqrt(2 * phi + Vbs) - math.sqrt(2 * phi))
# VovP = Vsg - Vtp
