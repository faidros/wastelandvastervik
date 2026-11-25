"""Hand-modelled Åhmans gatukök, placed from its OpenStreetMap point."""
import housekit

cx, cy = 1287.304, -717.027
a, length, width = -math.pi / 4, 20.0, 12.0
eaves, roof_rise = 3.1, 1.15
wall = 'M_Wall_Wood_black_Blank'

ring = citylib.ccw([
    citylib.local(cx, cy, a, -length / 2, -width / 2),
    citylib.local(cx, cy, a, length / 2, -width / 2),
    citylib.local(cx, cy, a, length / 2, width / 2),
    citylib.local(cx, cy, a, -length / 2, width / 2),
])
ctx.geo.prism(ring, -0.12, 0.12, 'M_Concrete', top=False)
for p, q in zip(ring, ring[1:] + ring[:1]):
    ctx.geo.wall(p, q, 0.12, eaves, wall)
citylib.gable_roof(ctx.geo, cx, cy, a, length, width, eaves, roof_rise,
                   mat='M_Roof_Metal_black', gable=wall, overhang=0.45)

def front_panel(u, z, panel_width, panel_height, depth, material, offset=0.12):
    x, y = citylib.local(cx, cy, a, u, -width / 2 - offset)
    ctx.geo.box((x, y, z), (panel_width, depth, panel_height), material, a, uvscale=1.5)

frame = 'M_Wall_Metal_grey_Blank'
front_panel(-7.2, 1.18, 1.35, 2.15, 0.16, 'M_Window_Pane')
front_panel(-3.3, 1.55, 4.7, 1.55, 0.16, 'M_Window_Pane')
front_panel(3.0, 1.55, 5.2, 1.55, 0.16, 'M_Window_Pane')

for u, panel_width, panel_height, z in ((-7.95, 0.12, 2.3, 1.2), (-6.45, 0.12, 2.3, 1.2),
                                        (-5.35, 0.12, 1.7, 1.55), (-1.0, 0.12, 1.7, 1.55),
                                        (0.4, 0.12, 1.7, 1.55), (5.6, 0.12, 1.7, 1.55),
                                        (-3.3, 4.9, 0.1, 2.32), (3.0, 5.4, 0.1, 2.32)):
    front_panel(u, z, panel_width, panel_height, 0.2, frame)

front_panel(0.0, 2.76, 15.2, 0.66, 0.32, 'M_Roof_Metal_red', offset=-0.2)
front_panel(0.5, 2.42, 13.2, 0.16, 0.95, 'M_Roof_Metal_red', offset=0.6)
housekit.House(ctx, ring=ring, levels=1, ground=eaves, street=[0]).sign(
    'Åhmans', wall=0, x=length / 2, z=2.48, size=0.58, mat='M_Furniture_LampGlass')
for u in (-5.4, -1.0, 3.0, 5.4):
    x, y = citylib.local(cx, cy, a, u, -width / 2 - 0.6)
    ctx.geo.box((x, y, 2.15), (0.09, 0.1, 0.42), 'M_Furniture_Metal', a)

vx, vy = citylib.local(cx, cy, a, 5.0, 1.8)
ctx.geo.cyl(vx, vy, eaves + roof_rise * (1 - 1.8 / (width / 2)) - 0.1,
            0.28, 1.35, 'M_Furniture_Metal', 8, cap=True)
