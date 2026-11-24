"""Street View interpretation of the low Corner restaurant at Allén 1."""
import housekit

front = 0
h = housekit.House(
    ctx, levels=1, ground=3.1,
    wall='M_Wall_Plaster_white_Blank',
    trim='M_Wall_Plaster_white_Blank',
    frame='M_Wall_Plaster_white_Blank',
    plinth='M_Concrete',
    street=[front, 1],
    shop=True,
)
h.facades(
    window=(1.4, 1.8), pitch=3.2, margin=0.45,
    shop_bays=3.4, sign_mat='M_Roof_Metal_black',
    awnings=['M_Wall_Plaster_green_Blank', 'M_Wall_Plaster_white_Blank'],
    entrance=False, cornice=False, plinth_h=0.25,
)
h.roof(
    shape='gabled', pitch=12, mat='M_Roof_Metal_black',
    ridge='long', overhang=0.3, gable_windows=False,
)
h.sign(
    'Corner', wall=front, x=h.walls[front].L / 2, z=2.45,
    size=0.88, mat='M_Furniture_LampGlass',
    board='M_Roof_Metal_black',
)
h.sign(
    'BURGERS & GRILL', wall=front, x=h.walls[front].L / 2, z=2.28,
    size=0.15, mat='M_Wall_Plaster_white_Blank',
)
