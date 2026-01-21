import math
from django.shortcuts import render
from ..forms import PbTimeForm

def to_ma(years: float) -> float:
    return years / 1e6

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

def result_for_time(U: float, Th: float, time: float) -> float:
    u_atoms  = U  * 6.022e23 / (238.029 * 100.0)
    th_atoms = Th * 6.022e23 / (232.037 * 100.0)

    return (
        0.9928 * u_atoms * (math.exp(1.55125e-10 * time) - 1.0) +
        0.0072 * u_atoms * (math.exp(9.8485e-10  * time) - 1.0) +
                th_atoms * (math.exp(4.9475e-11  * time) - 1.0)
    )


def view_pb_time(request, program):
    form = PbTimeForm(request.POST or None)
    out = None
    out_ma = None
    t_years = None
    samples = None
    Pb_atoms = None
    err = None

    if request.method == "POST" and form.is_valid():
        try:
            U = form.cleaned_data["U"]
            Th = form.cleaned_data["Th"]
            Pb = form.cleaned_data["Pb"]

            t_years = pb_time(U, Th, Pb)
            out = f"{t_years:e}"
            out_ma = to_ma(t_years)

            Pb_atoms = Pb * 6.022e23 / (207.2 * 100.0)

            # slider: nasamplujeme priebeh od 0 po t_years
            N = 250
            samples = []
            for i in range(N + 1):
                t = t_years * (i / N)
                samples.append({
                    "t": t,
                    "result": result_for_time(U, Th, t),
                })

        except Exception as e:
            err = str(e)

    return render(
        request,
        "programy/pb_time.html",
        {
            "form": form,
            "out": out,
            "out_ma": out_ma,
            "t_years": t_years,
            "samples": samples,
            "Pb_atoms": Pb_atoms,
            "err": err,
            "program": program
        }
    )



