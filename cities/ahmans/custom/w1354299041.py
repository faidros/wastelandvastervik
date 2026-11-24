"""Street View interpretation of the half-timbered house at Sillgatan 9."""
import housekit

wall = 'M_Wall_Plaster_white_Blank'
timber = 'M_Wall_Wood_brown_Blank'
roof = 'M_Roof_Tiles_brown'
h = housekit.House(
    ctx, levels=1, storey=3.0, ground=3.1,
    wall=wall, trim=timber, frame=timber,
    plinth='M_Concrete', door='M_Wall_Wood_brown_Blank',
    timber=True,
)
h.facades(
    window=(1.15, 1.4), pitch=2.8, margin=0.75,
    door_at=0.4, cornice=False, plinth_h=0.5,
    downpipes=False,
)
h.roof(
    shape='hipped', pitch=22, mat=roof,
    overhang=0.4, ridge='long', max_rise=3.4,
)
h.dormers(
    [0.72], width=1.35, height=1.0, side='street',
    mat=wall, roof_mat=roof, kind='flat',
)
