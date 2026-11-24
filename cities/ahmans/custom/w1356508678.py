"""Street View interpretation of the light timber house at Rådjursstigen 15."""
import housekit

wall = 'M_Wall_Wood_white_Blank'
trim = 'M_Wall_Wood_white_Blank'
roof = 'M_Roof_Tiles_red'
h = housekit.House(
    ctx, levels=1, storey=2.9, ground=3.0,
    wall=wall, trim=trim, frame=trim,
    plinth='M_Concrete', door='M_Wall_Wood_brown_Blank',
)
h.facades(
    window=(1.1, 1.45), pitch=2.8, margin=0.7,
    door_at=0.5, cornice=False, plinth_h=0.6,
    downpipes=False,
)
h.roof(
    shape='gabled', pitch=30, mat=roof,
    overhang=0.48, ridge='long', gable_mat=wall,
    gable_windows=False,
)
