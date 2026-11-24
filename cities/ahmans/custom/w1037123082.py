"""Hand-built interpretation of Västervik rådhus on Stora torget."""
import housekit

wall = 'M_Wall_Plaster_ivory_Blank'
trim = 'M_Wall_Plaster_white_Blank'
frame = 'M_Wall_Wood_brown_Blank'
roof = 'M_Roof_Metal_black'
h = housekit.House(
    ctx, ring=ctx.footprint['outer'], levels=2, storey=3.0, ground=3.15,
    wall=wall, trim=trim, frame=frame,
    plinth='M_StoneWall', door='M_Wall_Wood_brown_Blank',
    timber=False,
)
h.facades(
    window=(1.15, 1.8), pitch=2.7, margin=1.2,
    kind='sash', door_at=0.5, cornice=True, plinth_h=0.75,
    downpipes=False,
)
h.roof(
    shape='mansard', pitch=55, mat=roof, overhang=0.25,
    gable_mat=wall, mansard_break=2.3, ridge='long',
)
for position in (0.18, 0.82):
    h.chimney(
        position, 0.72, mat=trim,
        size=(0.8, 0.8), above=1.0,
    )

roof_rect, roof_height, _, _ = h.main_roof()
s0, s1, t0, t1 = roof_rect
ridge_z = roof_height((s0 + s1) / 2, (t0 + t1) / 2)
attic_length = min(6.6, h.L * 0.32)
attic_width = min(3.2, h.W * 0.3)
attic_height = 1.8
ctx.geo.box(
    (h.cx, h.cy, ridge_z + attic_height / 2),
    (attic_length, attic_width, attic_height), wall, h.a,
)
ctx.geo.box(
    (h.cx, h.cy, ridge_z + 0.08),
    (attic_length + 0.3, attic_width + 0.3, 0.16), trim, h.a,
)
ctx.geo.box(
    (h.cx, h.cy, ridge_z + attic_height - 0.08),
    (attic_length + 0.3, attic_width + 0.3, 0.16), trim, h.a,
)

clock_z = ridge_z + attic_height * 0.62
for side in (-1, 1):
    front = side * (attic_width / 2 + 0.1)

    def clock_face(radius, material, depth):
        points = []
        for i in range(32):
            angle = 2 * math.pi * i / 32
            x, y = citylib.local(
                h.cx, h.cy, h.a,
                radius * math.cos(angle), front + side * depth,
            )
            points.append((x, y, clock_z + radius * math.sin(angle)))
        ctx.geo.face(points, material, uvscale=1.0)
        ctx.geo.face(points[::-1], material, uvscale=1.0)

    clock_face(0.62, 'M_Roof_Metal_black', 0.0)
    clock_face(0.52, trim, 0.03)
    x, y = citylib.local(h.cx, h.cy, h.a, 0.0, front + side * 0.07)
    ctx.geo.box((x, y, clock_z), (0.42, 0.06, 0.06), 'M_Roof_Metal_black', h.a)
    ctx.geo.box((x, y, clock_z + 0.08), (0.06, 0.06, 0.32), 'M_Roof_Metal_black', h.a)

attic_top = ridge_z + attic_height
lantern_size = 2.4
lantern_height = 2.6
lantern_mid = attic_top + lantern_height / 2
ctx.geo.box(
    (h.cx, h.cy, lantern_mid),
    (lantern_size, lantern_size, lantern_height), wall, h.a,
)
for side in (-1, 1):
    x, y = citylib.local(
        h.cx, h.cy, h.a, 0.0, side * (lantern_size / 2 + 0.06),
    )
    ctx.geo.box(
        (x, y, lantern_mid), (0.9, 0.08, 1.35), 'M_Window_Pane', h.a,
    )
    x, y = citylib.local(
        h.cx, h.cy, h.a, side * (lantern_size / 2 + 0.06), 0.0,
    )
    ctx.geo.box(
        (x, y, lantern_mid), (0.08, 0.9, 1.35),
        'M_Window_Pane', h.a + math.pi / 2,
    )

lantern_top = attic_top + lantern_height
ctx.geo.box(
    (h.cx, h.cy, lantern_top + 0.08),
    (lantern_size + 0.35, lantern_size + 0.35, 0.16), trim, h.a,
)
citylib.spire(
    ctx.geo, h.cx, h.cy, lantern_size + 0.35,
    lantern_top + 0.16, 1.6, h.a, roof,
)
ctx.geo.cyl(
    h.cx, h.cy, lantern_top + 1.62, 0.08, 0.38,
    'M_Furniture_Metal', seg=8, r2=0.04,
)
