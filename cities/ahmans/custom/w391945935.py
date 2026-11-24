ring = citylib.ccw(ctx.footprint['outer'])
wall = ctx.mat('blank')
roof = ctx.mat('roof')
stone = 'M_Wall_Stone_limestone_Blank'
cx, cy, angle, length, width = citylib.frame(ring)
eaves = 12.5
nave_width = min(16.0, width * 0.48)
cross_length = width * 0.9
cross_width = min(15.0, width * 0.43)

ctx.geo.prism(ring, -0.25, 0.35, stone)
citylib.facade(ctx.geo, ring, 0.0, eaves, wall, bay=5.0, storey=3.0)
citylib.gable_roof(ctx.geo, cx, cy, angle, length + 0.8, nave_width,
                   eaves, 6.0, roof, ctx.mat('blank'), overhang=0.55)
citylib.gable_roof(ctx.geo, cx, cy, angle + math.pi / 2, cross_length,
                   cross_width, eaves, 5.8, roof, ctx.mat('blank'), overhang=0.45)


def wall_point(p, ux, uy, nx, ny, distance, z):
    return (p[0] + ux * distance + nx * 0.08,
            p[1] + uy * distance + ny * 0.08, z)


def trim_strip(p, ux, uy, nx, ny, start, end, thickness):
    ds, dz = end[0] - start[0], end[1] - start[1]
    span = math.hypot(ds, dz)
    ps, pz = -dz * thickness / (2 * span), ds * thickness / (2 * span)
    pts = [wall_point(p, ux, uy, nx, ny, start[0] + ps, start[1] + pz),
           wall_point(p, ux, uy, nx, ny, end[0] + ps, end[1] + pz),
           wall_point(p, ux, uy, nx, ny, end[0] - ps, end[1] - pz),
           wall_point(p, ux, uy, nx, ny, start[0] - ps, start[1] - pz)]
    ctx.geo.face(pts, stone, uvscale=1.0)


def pointed_window(p, q, count, index):
    dx, dy = q[0] - p[0], q[1] - p[1]
    span = math.hypot(dx, dy)
    ux, uy = dx / span, dy / span
    nx, ny = dy / span, -dx / span
    width_ = 1.45
    center = span * (index + 0.5) / count
    bottom, shoulder, apex = 2.6, 8.4, 9.35
    left, right = center - width_ / 2, center + width_ / 2
    pane = [wall_point(p, ux, uy, nx, ny, left, bottom),
            wall_point(p, ux, uy, nx, ny, right, bottom),
            wall_point(p, ux, uy, nx, ny, right, shoulder),
            wall_point(p, ux, uy, nx, ny, center, apex),
            wall_point(p, ux, uy, nx, ny, left, shoulder)]
    ctx.geo.face(pane, 'M_Window_Pane', uvscale=1.0)
    outline = [(left, bottom), (left, shoulder), (center, apex),
               (right, shoulder), (right, bottom)]
    for a, b in zip(outline, outline[1:]):
        trim_strip(p, ux, uy, nx, ny, a, b, 0.16)
    trim_strip(p, ux, uy, nx, ny, (center, bottom), (center, apex), 0.08)
    trim_strip(p, ux, uy, nx, ny, (left, 5.4), (right, 5.4), 0.08)


for p, q in zip(ring, ring[1:] + ring[:1]):
    span = math.dist(p, q)
    if span < 5.0:
        continue
    count = max(1, int(span / 5.6))
    dx, dy = q[0] - p[0], q[1] - p[1]
    angle_ = math.atan2(dy, dx)
    for i in range(count):
        pointed_window(p, q, count, i)
    for i in range(count + 1):
        t = i / count
        x = p[0] + dx * t + dy / span * 0.25
        y = p[1] + dy * t - dx / span * 0.25
        ctx.geo.box((x, y, eaves / 2), (0.55, 0.7, eaves),
                    stone, angle_, uvscale=1.0)

tower_u = length * 0.08
tower_x, tower_y = citylib.local(cx, cy, angle, tower_u, 0)
tower_side = 8.4
tower_bottom, tower_top = eaves - 0.8, 27.0
tower = citylib.square(tower_x, tower_y, tower_side, angle)
ctx.geo.prism(tower, tower_bottom, tower_top, ctx.mat('upper'))
ctx.geo.prism(citylib.square(tower_x, tower_y, tower_side + 0.5, angle),
              tower_top - 0.55, tower_top + 0.25, stone)

for side in (-1, 1):
    x, y = citylib.local(tower_x, tower_y, angle, 0, side * (tower_side / 2 + 0.08))
    ctx.geo.box((x, y, 22.4), (1.05, 0.14, 3.0), 'M_Window_Pane', angle)
    x, y = citylib.local(tower_x, tower_y, angle, side * (tower_side / 2 + 0.08), 0)
    ctx.geo.box((x, y, 22.4), (1.05, 0.14, 3.0),
                'M_Window_Pane', angle + math.pi / 2)

citylib.spire(ctx.geo, tower_x, tower_y, tower_side + 0.4,
              tower_top + 0.2, 19.0, angle, roof)
for u in (-1, 1):
    for w in (-1, 1):
        x, y = citylib.local(tower_x, tower_y, angle,
                             u * (tower_side / 2 + 0.45),
                             w * (tower_side / 2 + 0.45))
        citylib.spire(ctx.geo, x, y, 1.8, tower_top - 0.1,
                      6.5, angle, roof)

for u in (-length * 0.26, length * 0.26):
    for w in (-cross_length * 0.38, cross_length * 0.38):
        x, y = citylib.local(cx, cy, angle, u, w)
        citylib.spire(ctx.geo, x, y, 1.5, eaves + 2.0,
                      5.5, angle, roof)
