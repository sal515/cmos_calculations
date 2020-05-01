import math

# variable setup
significantFig = 8

Cox = 1 / 1
Un = 45 / 1000000  # (A/v^2)
CoxUn = Cox * Un
w = 3
l = 1
Bn = CoxUn * (w / l)

Vtno = 0.8  # V

y = 0.38  # (v^1/2)
phi = 0.6/2  # V
lambda_ = 0.0  # 1/V

Vdd = 5  # V
Vss = 0  # V

Vg = 5  # V
Vs = .2  # V
Vd = 5  # V
Vb = Vss  # V

# Nmos Node Voltages
Vgs = Vg - Vs
Vds = Vd - Vs
Vsb = Vs - Vb

# Nmos

if Vb > Vs:
    print("Improper Bias")
    exit(1)

if Vs == Vb:
    Vtp = Vtno

else:
    Vtp = Vtno + y * (math.sqrt(2 * phi + Vsb) - math.sqrt(2 * phi))

VovN = Vgs - Vtp


# Calculation functions
def calculate_vt():
    global Vtp
    if Vb > Vs:
        print("Improper Bias")
        exit(1)
    else:

        Vtn = Vtno + y * (math.sqrt(2 * phi + Vsb) - math.sqrt(2 * phi))
        print("formula Vtn: ", round(Vtn, significantFig))


def calculate_ids():
    # Nmos Ids calculations

    if Vgs < Vtp:
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

calculate_vt()

calculate_ids()

# Pmos Node Voltages
# Vsg = Vs - Vg
# Vsd = Vs - Vd
# Vbs = Vb - Vs

# # Pmos
# Vtp = Vtpo + y * (math.sqrt(2 * phi + Vbs) - math.sqrt(2 * phi))
# VovP = Vsg - Vtp
