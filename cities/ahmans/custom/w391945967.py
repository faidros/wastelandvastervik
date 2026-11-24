import housekit

ring = ctx.footprint['outer']
wall = 'M_Wall_Plaster_white_Blank'
trim = 'M_Wall_Plaster_grey_Blank'
frame = 'M_Wall_Metal_grey_Blank'

h = housekit.House(ctx, ring=ring, levels=3, storey=3.0, ground=3.2,
                   wall=wall, trim=trim, frame=frame, plinth='M_Concrete',
                   door='M_Wall_Metal_grey_Blank')
h.facades(window=(1.55, 1.45), pitch=3.45, kind='modern', upper_kind='modern',
          margin=1.0, cornice=True, plinth_h=0.45, downpipes=False,
          canopy='M_Concrete')
h.roof(shape='flat', mat='M_Roof_Flat_gravel', parapet=0.55, fascia=trim)

for facade in h.walls:
    if facade.L < 5.0:
        continue
    for z in (h.ground, h.ground + h.storey):
        facade.ledge(0.0, facade.L, z - 0.06, z + 0.06, trim, 0.07)

main_wall = max(range(len(h.walls)), key=lambda index: h.walls[index].L)
h.stair_bay(main_wall, h.walls[main_wall].L * 0.53, width=3.6,
            depth=0.55, mat=trim, glazed=True)
