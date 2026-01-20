from django.http import Http404
from django.shortcuts import render
from .programs.pb_time import view_pb_time   # napr. rozdelíš programy do modulov

PROGRAMS = {
    "pb-time": {
        "title": "Výpočet času (U, Th, Pb)",
        "view": view_pb_time,
    },
    # neskôr pridáš ďalšie:
    # "iny-program": {"title": "...", "view": view_iny_program},
}

def programy_index(request):
    return render(request, "programy/index.html", {"programs": PROGRAMS})

def program_detail(request, program_slug: str):
    program = PROGRAMS.get(program_slug)
    if not program:
        raise Http404("Program nenájdený")
    # deleguj na konkrétny view
    return program["view"](request, program)
