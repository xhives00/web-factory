import math
from django.shortcuts import render
from ..forms import PbTimeForm

def pb_time(U: float, Th: float, Pb: float) -> float:
    time = 0.0
    step = 1e10
    Pb_atoms = Pb * 6.022e23 / (207.2 * 100.0)

    for _ in range(2000):
        u_atoms  = U  * 6.022e23 / (238.029 * 100.0)
        th_atoms = Th * 6.022e23 / (232.037 * 100.0)

        result = (
            0.9928 * u_atoms * (math.exp(1.55125e-10 * time) - 1.0) +
            0.0072 * u_atoms * (math.exp(9.8485e-10  * time) - 1.0) +
                    th_atoms * (math.exp(4.9475e-11  * time) - 1.0)
        )

        if result >= Pb_atoms:
            time -= step
            step /= 10.0
            time += step
            if step <= 10000:
                return time
        else:
            time += step

    raise ValueError("Výpočet nedokončil konvergenciu pre dané hodnoty.")

def view_pb_time(request, program):
    form = PbTimeForm(request.POST or None)
    out = None
    err = None

    if request.method == "POST" and form.is_valid():
        try:
            t = pb_time(form.cleaned_data["U"], form.cleaned_data["Th"], form.cleaned_data["Pb"])
            out = f"{t:e}"
        except Exception as e:
            err = str(e)

    return render(request, "programy/pb_time.html", {"form": form, "out": out, "err": err, "program": program})
