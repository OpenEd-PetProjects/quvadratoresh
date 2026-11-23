test:
    python3 -B -c 'from solver import solve; roots, found = solve(1, -3, 2); assert found is True and sorted(roots) == [1.0, 2.0]'
