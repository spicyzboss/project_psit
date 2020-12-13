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
            '1. Complex number': 'complex_num.complex_number()',
            '0. Back': 'maincontent_selection()'
        },
        "2. Conic":
        {
            '1. Conic': 'conic.conic()',
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
            '1. Sequence': 'sequence.sequence_sigma_series()',
            '0. Back': 'maincontent_selection()'
        },
        "5. Sets":
        {
        # Insert function here
            '1. Set': 'mathset.set_topic()',
            '0. Back': 'maincontent_selection()'
        },
        "6. Statistics":
        {
        # Insert function here
            '1. Statistics Part 1': 'statistics1.statistics1()',
            '2. Statistics Part 2': 'statistics2.statistics2()',
            '0. Back': 'maincontent_selection()'
        },
        "7. Surface area and Volume":
        {
        # Insert function here
            '1. Surface area and Volume': '',
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
            '1. Circular motion': 'circular.circular_motion()',
            '0. Back': 'maincontent_selection()'
        },
        "2. Projectile":
        {
            '1. Projectile': 'projectile.projectile()',
            '0. Back': 'maincontent_selection()'
        },
        "3. Work energy":
        {
            '1. Work energy': 'work.work_energy()',
            '0. Back': 'maincontent_selection()'
        },
        '0. Back':
        {
            ''
        }
    }
}
