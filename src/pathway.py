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
            '1. Addition': 'add_sub(add)',
            '2. Subtraction': 'add_sub(sub)',
            '3. Multiplication': 'multi()',
            '4. Determinant': 'find_det()',
            '5. Cramer\'s rule': 'find_cramer()',
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
        "4. Staticstic":
        {
        # Insert function here
            '1. Statistics Part 1': 'statistics1()',
            '2. Statistics Part 2': 'statistics2()'
        },
        "0. Back":
        {
            ''
        }
    },

    # Physics
    2:
    {

    }
}
