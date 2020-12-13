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
        "1. Matrix":
        {
        # Insert function here
            '1. Addition': 'matrix.add_sub("add")',
            '2. Subtraction': 'matrix.add_sub("sub")',
            '3. Multiplication': 'matrix.multi()',
            '4. Determinant': 'matrix.find_det()',
            '5. Cramer\'s rule': 'matrix.find_cramer()',
            '0. Back': 'maincontent_selection()'
        },
        "2. Sets":
        {
        # Insert function here
            ''
        },
        "3. Surface area and Volume":
        {
        # Insert function here
            ''
        },
        "4. Statistics":
        {
        # Insert function here
            '1. Statistics Part 1': 'statistics1.statistics1()',
            '2. Statistics Part 2': 'statistics2.statistics2()',
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

    }
}
