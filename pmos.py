import math

# variable setup
significantFig = 8

Cox = 1 / 1
Up = (160/4) / 1000000  # (A/v^2)
CoxUp = Cox * Up
w = 1
l = 2.04
Bp = CoxUp * (w / l)

Vtpo = -0.8  # V

y = 0.5  # (v^1/2)
phi = 0.5 / 2  # V
lambda_ = 0.001  # 1/V

Vdd = 3.3  # V
Vss = 0  # V

Vg = 0  # V
Vs = 3.3  # V
Vd = .3  # V
Vb = Vdd  # V

# Pmos Node Voltages
Vsg = Vs - Vg
Vsd = Vs - Vd
Vbs = Vb - Vs

# Pmos

if Vb > Vs:
    print("Improper Bias")
    exit(1)

if Vs == Vb:
    Vtp = Vtpo

else:
    Vtp = Vtpo + y * (math.sqrt(2 * phi + Vbs) - math.sqrt(2 * phi))

VovP = Vsg - abs(Vtp)


# Calculation functions
def calculate_vt():
    global Vtp
    if Vb > Vs:
        print("Improper Bias")
        exit(1)
    else:

        Vtp = Vtpo + y * (math.sqrt(2 * phi + Vbs) - math.sqrt(2 * phi))
        print("formula Vtn: ", round(Vtp, significantFig))


def calculate_ids():
    # Pmos Ids calculations

    if Vsg < abs(Vtp):
        print("Cut-off mode")

    elif Vsd >= VovP:
        print("Saturation Mode")
        ids = 0.5 * Bp * math.pow(VovP, 2) * (1 + lambda_ * Vsd)
        print("Saturation current", round(ids, significantFig))

    elif Vsd < VovP:
        print("Triode Mode")
        ids = Bp * ((VovP * Vsd) - (0.5 * math.pow(Vsd, 2)))
        print("Triode current", round(ids, significantFig))


# Calculation calls

calculate_vt()

calculate_ids()
