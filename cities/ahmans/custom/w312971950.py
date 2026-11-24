import math
import housekit

ring = ctx.footprint['outer']
wall = ctx.mat('upper')
trim = 'M_Wall_Plaster_ivory_Blank'
roof = ctx.mat('roof')

h = housekit.House(ctx, ring=ring, levels=3, storey=3.15, ground=3.55,
                   wall=wall, trim=trim, frame=trim, plinth='M_StoneWall',
                   door='M_Wall_Wood_brown_Blank')
h.facades(window=(1.45, 1.9), pitch=4.2, kind='arched', upper_kind='arched',
          margin=1.25, cornice=False, plinth_h=0.85, downpipes=False)
h.roof(shape='hipped', pitch=24, mat=roof, overhang=0.35,
       gable_mat=wall, max_rise=3.2)

for facade in h.walls:
    if facade.L < 5.0:
        continue
    for z in (h.ground, h.ground + h.storey):
        facade.ledge(0.0, facade.L, z - 0.08, z + 0.08, trim, 0.08)
    facade.ledge(0.0, facade.L, h.eave - 0.28, h.eave - 0.08, trim, 0.16)

window_width, window_height, pitch, margin = 1.45, 1.9, 4.2, 1.25
for wall_index, facade in enumerate(h.walls):
    if wall_index in h.party:
        continue
    room = facade.L - 2 * margin
    count = int((room - window_width) // pitch) + 1 if room >= window_width else 0
    if count <= 0:
        continue
    start = margin + (room - ((count - 1) * pitch + window_width)) / 2
    for storey in range(1, h.levels):
        z0 = h.ground + (storey - 1) * h.storey + 0.85
        spring = z0 + window_height - window_width / 2
        radius = window_width / 2
        outer_radius = radius + 0.12
        for index in range(count):
            xc = start + index * pitch + window_width / 2
            for segment in range(10):
                a0 = math.pi * segment / 10
                a1 = math.pi * (segment + 1) / 10
                points = [
                    (xc + radius * math.cos(a0), spring + radius * math.sin(a0)),
                    (xc + radius * math.cos(a1), spring + radius * math.sin(a1)),
                    (xc + outer_radius * math.cos(a1), spring + outer_radius * math.sin(a1)),
                    (xc + outer_radius * math.cos(a0), spring + outer_radius * math.sin(a0)),
                ]
                facade.poly(points[::-1], trim, d=0.07, scale=3.0)
            facade.rect(xc - outer_radius, xc - radius, z0, spring, trim, d=0.07, scale=3.0)
            facade.rect(xc + radius, xc + outer_radius, z0, spring, trim, d=0.07, scale=3.0)

h.chimney(0.28, 0.36, mat='M_Wall_Plaster_yellow_Blank',
          size=(0.6, 0.7), above=0.75)
h.chimney(0.72, 0.64, mat='M_Wall_Plaster_yellow_Blank',
          size=(0.6, 0.7), above=0.75)
