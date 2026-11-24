import housekit

ring = ctx.footprint['outer']
wall = ctx.mat('upper')
trim = 'M_Wall_Plaster_white_Blank'
roof = ctx.mat('roof')
h = housekit.House(ctx, ring=ring, levels=3, storey=2.9, ground=3.65, wall=wall,
                   trim=trim, frame=trim, plinth='M_Concrete',
                   door='M_Wall_Wood_brown_Blank')
h.facades(window=(1.25, 1.8), pitch=3.25, kind='sash', margin=1.0,
          cornice=True, plinth_h=0.6, downpipes=False)
h.roof(shape='hipped', pitch=35, mat=roof, overhang=0.5,
       gable_mat=wall, max_rise=5.0)
h.dormers((0.24, 0.5, 0.76), width=1.5, height=1.25,
          side='both', mat=wall, roof_mat=roof)
for side in (0, 1):
    h.cross_gable(frac=0.5, width=7.0, height=1.8, side=side,
                  pitch=36, roof_mat=roof, windows=3)
h.sign('VÄSTERVIK', z=h.ground + 0.3, size=0.42, mat=trim)
