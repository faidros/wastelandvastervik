"""Street View interpretation of the yellow timber house at Tjustgatan 1."""
import housekit

front = 0
h = housekit.House(
    ctx, levels=2, storey=2.8, ground=3.0,
    wall='M_Wall_Wood_yellow_Blank',
    trim='M_Wall_Wood_white_Blank',
    frame='M_Wall_Wood_white_Blank',
    plinth='M_Concrete',
    door='M_Wall_Wood_brown_Blank',
    street=[front],
)
door_x = h.walls[front].L * 0.52
h.facades(
    window=(1.15, 1.4), pitch=2.7, margin=0.75,
    entrance=False, skip={front: [(door_x - 1.65, door_x + 1.65)]},
)
h.roof(
    shape='gabled', pitch=38, mat='M_Roof_Tiles_red',
    ridge='long', overhang=0.5, gable_windows=True,
)
h.porch(
    wall=front, x=door_x, width=2.8, depth=1.5,
    post='M_Wall_Wood_white_Blank',
    roof_mat='M_Roof_Tiles_red',
)
