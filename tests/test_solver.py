import pytest

from solver import solve


def test_two_real_roots() -> None:
    roots, found = solve(1, -3, 2)

    assert found is True
    assert sorted(roots) == pytest.approx([1.0, 2.0])


def test_double_root_is_returned_once() -> None:
    roots, found = solve(1, 2, 1)

    assert found is True
    assert roots == pytest.approx([-1.0])


def test_negative_discriminant_has_no_real_roots() -> None:
    roots, found = solve(1, 0, 1)

    assert found is False
    assert roots == []


def test_linear_equation_has_one_root() -> None:
    roots, found = solve(0, 3, -6)

    assert found is True
    assert len(roots) == 1


def test_nonzero_constant_has_no_roots() -> None:
    roots, found = solve(0, 0, 1)

    assert found is False
    assert roots == []


def test_identity_raises_value_error() -> None:
    with pytest.raises(ValueError):
        solve(0, 0, 0)
