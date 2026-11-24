import housekit

ring = ctx.footprint['outer']
wall = ctx.mat('upper')
trim = 'M_Wall_Plaster_white_Blank'
roof = ctx.mat('roof')
h = housekit.House(ctx, ring=ring, levels=3, storey=3.0, ground=3.3, wall=wall,
                   trim=trim, frame=trim, plinth='M_Concrete',
                   door='M_Wall_Wood_brown_Blank')
h.facades(window=(1.0, 1.65), pitch=3.25, kind='sash', margin=1.25,
          cornice=True, plinth_h=0.65)
h.roof(shape='hipped', pitch=28, mat=roof, overhang=0.35,
       gable_mat=wall, max_rise=4.4)
for u in (0.18, 0.49, 0.81):
    h.chimney(u, 0.5, mat=trim, size=(0.8, 0.9), above=1.25)

cx, cy, angle, _, _ = citylib.frame(ring)
lantern_side = 4.8
lantern_bottom = h.eave + 1.0
lantern_top = lantern_bottom + 5.0
lantern = citylib.square(cx, cy, lantern_side, angle)
ctx.geo.prism(lantern, lantern_bottom, lantern_top, wall)
ctx.geo.prism(citylib.square(cx, cy, lantern_side + 0.35, angle),
              lantern_top - 0.35, lantern_top + 0.15, trim)
for side in (-1, 1):
    x, y = citylib.local(cx, cy, angle, 0, side * (lantern_side / 2 + 0.08))
    ctx.geo.box((x, y, lantern_bottom + 2.6), (0.9, 0.12, 2.0),
                'M_Window_Pane', angle)
    x, y = citylib.local(cx, cy, angle, side * (lantern_side / 2 + 0.08), 0)
    ctx.geo.box((x, y, lantern_bottom + 2.6), (0.9, 0.12, 2.0),
                'M_Window_Pane', angle + math.pi / 2)
citylib.spire(ctx.geo, cx, cy, lantern_side + 0.3, lantern_top + 0.12,
              2.0, angle, roof)
