"""Street View interpretation of the small V-DATA shop at Allén 4."""
import housekit

front = 0
h = housekit.House(
    ctx, levels=1, ground=3.2,
    wall='M_Wall_Plaster_white_Blank',
    trim='M_Wall_Plaster_white_Blank',
    frame='M_Wall_Plaster_white_Blank',
    plinth='M_Concrete',
    street=[front, 4],
    shop=True,
)
h.facades(
    window=(1.2, 1.8), pitch=3.0, margin=0.35,
    shop_bays=3.0, sign_mat='M_Wall_Plaster_white_Blank',
    entrance=False, cornice=False, plinth_h=0.25,
    downpipes=False,
)
h.roof(
    shape='gabled', pitch=24, mat='M_Roof_Metal_grey',
    ridge='long', overhang=0.45, gable_windows=False,
)
h.sign(
    'V-DATA', wall=front, x=h.walls[front].L / 2,
    z=2.48, size=0.58, mat='M_Roof_Metal_red',
    board='M_Wall_Plaster_white_Blank',
)
h.sign(
    'V-DATA', wall=2, x=h.walls[2].L / 2,
    z=2.48, size=0.58, mat='M_Roof_Metal_red',
    board='M_Wall_Plaster_white_Blank',
)
