subjects = [
    "1. MATH",
    "2. PHYSICS",
    "0. TERMINATE"
]

content = {
    # Math
    1:
    {
    # Add more sub-subject here
        "1. Complex number":
        {
            '1. Find I^N': 'complex_num.find_i()',
            '2. Normal complex number': 'complex_num.normal_complex_number()',
            '3. Polar complex number': 'complex_num.polar_complex_number()',
            '0. Back': 'maincontent_selection()'
        },
        "2. Conic Section":
        {
            '1. Distance between Point and Point': 'conic.distance_ptop()',
            '2. Distance between Point and Line': 'conic.distance_ptol()',
            '3. Distance between Point and Line': 'conic.distance_parallel()',
            '4. Middle Point between 2 points': 'conic.half_2p()',
            '5. Circle Equation': 'conic.circle_equation()',
            '6. Parabola Equation': 'conic.parabola_equation()',
            '7. Ellipse Equation': 'conic.ellipse_equation()',
            '8. Hyperbola Equation': 'conic.hyperbola_equation()',
            '0. Back': 'maincontent_selection()'
        },
        "3. Matrix":
        {
        # Insert function here
            '1. Addition': 'matrix.add_sub("add")',
            '2. Subtraction': 'matrix.add_sub("sub")',
            '3. Multiplication': 'matrix.multi()',
            '4. Determinant': 'matrix.find_det()',
            '5. Cramer\'s rule': 'matrix.find_cramer()',
            '0. Back': 'maincontent_selection()'
        },
        "4. Sequence series":
        {
            '1. Sequence': 'sequence.sequence()',
            '2. Sigma': 'sequence.sigma()',
            '3. Series': 'sequence.series()',
            '0. Back': 'maincontent_selection()'
        },
        "5. Sets":
        {
        # Insert function here
            '1. Union': 'mathset.union_finder()',
            '2. Intersect': 'mathset.intersect_finder()',
            '3. Difference': 'mathset.difference_finder()',
            '0. Back': 'maincontent_selection()'
        },
        "6. Statistics Part 1":
        {
        # Insert function here
            '1. Mean': 'statistics1.mean()',
            '2. Median': 'statistics1.med()',
            '3. Mode': 'statistics1.mod()',
            '0. Back': 'maincontent_selection()'
        },
        "7. Statistics Part 2":
        {
        # Insert function here
            '1. Relative position': 'statistics2.relative_position()',
            '2. Range': 'statistics2.range_finder()',
            '3. Quartile Deviation': 'statistics2.quartile_deviation()',
            '4. Mean Deviation': 'statistics2.mean_deviation()',
            '5. Standard Deviation': 'statistics2.standard_deviation()',
            '6. Variance': 'statistics2.variance()',
            '0. Back': 'maincontent_selection()'
        },
        "8. Surface area":
        {
        # Insert function here
            '1. Triangle': 'surface.triangle()',
            '2. Cube': 'surface.cube()',
            '3. Circle': 'surface.circle()',
            '0. Back': 'maincontent_selection()'
        },
        "9. Volume":
        {
        # Insert function here
            '1. Cylinder': 'volume.cylinder()',
            '2. Cube': 'volume.cube()',
            '3. Circle': 'volume.circle()',
            '4. Pyramid': 'volume.pyramid()',
            '5. Conical': 'volume.conical()',
            '6. Prism': 'volume.prism()',
            '0. Back': 'maincontent_selection()'
        },
        "0. Back":
        {
            ''# Don't Touch me na kub :)
        }
    },

    # Physics
    2:
    {
        "1. Circular motion":
        {
            '1. Find Linear Velocity': 'circular.linear_velocity()',
            '2. Find Angular Velocity': 'circular.angular_velocity()',
            '3. Find Acceleration into the center': 'circular.acceleration_tocenter()',
            '4. Find Centripetal Force': 'circular.centipetal_force()',
            '0. Back': 'maincontent_selection()'
        },
        "2. Horizontal motion":
        {
            '0. Back': 'maincontent_selection()'
        },
        "3. Projectile":
        {
            '1. U Vector': 'projectile.u_vector()',
            '2. X Axis': 'projectile.x_axis()',
            '3. Y Axis': 'projectile.y_axis()',
            '4. Find Angle that make Sy/Sx max ': 'projectile.max_angle()',
            '5. Find Sy Max': 'projectile.sy_max()',
            '6. Find Sx Max': 'projectile.sx_max()',
            '7. Find Total Time': 'projectile.time_total()',
            '0. Back': 'maincontent_selection()'
        },
        "4. Vertical motion":
        {
            '0. Back': 'maincontent_selection()'
        },
        "5. Work energy":
        {
            '1. Find Work': 'work.work()',
            '2. Find Energy': 'work.energy()',
            '3. Find Power': 'work.power()',
            '0. Back': 'maincontent_selection()'
        },
        '0. Back':
        {
            ''
        }
    }
}
