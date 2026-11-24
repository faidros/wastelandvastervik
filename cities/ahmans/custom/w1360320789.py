"""Street View interpretation of the pale timber house at Hagaholmsgatan 7."""
import housekit

h = housekit.House(
    ctx, levels=2, storey=2.65, ground=2.9,
    wall='M_Wall_Wood_white_Blank',
    trim='M_Wall_Wood_white_Blank',
    frame='M_Wall_Wood_white_Blank',
    plinth='M_Concrete',
    door='M_Wall_Wood_brown_Blank',
    street=[0, 1, 7],
)
h.facades(
    window=(1.05, 1.4), pitch=2.7, margin=0.7,
    kind='sash', upper_kind='sash',
)
h.roof(
    shape='gabled', pitch=28, mat='M_Roof_Metal_black',
    ridge='long', overhang=0.45, gable_windows=False,
)
