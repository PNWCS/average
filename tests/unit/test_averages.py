import pytest
from metrics import average_age, average_score

@pytest.mark.parametrize(
    "ages,expected",
    [
        ([20.0], 20.0),
        ([20.0, 22.0, 24.0], 22.0),
        ([30.0, 40.0], 35.0),
        ([10.0, 20.0, 30.0, 40.0], 25.0),
    ],
)
def test_average_age_parametrized(ages, expected):
    assert average_age(ages) == pytest.approx(expected)


@pytest.mark.parametrize(
    "scores,expected",
    [
        ([100.0], 100.0),
        ([90.0, 95.0, 85.0], 90.0),
        ([80.0, 70.0], 75.0),
        ([60.0, 70.0, 80.0, 90.0], 75.0),
    ],
)
def test_average_score_parametrized(scores, expected):
    assert average_score(scores) == pytest.approx(expected)