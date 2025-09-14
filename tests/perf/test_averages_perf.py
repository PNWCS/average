import random
import statistics
import time

import pytest

from metrics import average_age


def _best_time(fn, data, repeats=5):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn(data)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return min(times), statistics.mean(times)


EXPECTED_MAX_TIME = 0.055  # 55 milliseconds


def test_average_age_performance(capfd):
    rng = random.Random(12345)
    data = [rng.random() * 1000.0 for _ in range(3_000_000)]  # 3M floats

    best, mean = _best_time(average_age, data, repeats=5)

    # Hard-coded expected time threshold (adjust as needed for classroom environment)
    print(f"average_age(): best={best:.6f}s mean={mean:.6f}s (allowed <= {EXPECTED_MAX_TIME:.6f}s)")

    # Performance assertion
    assert best <= EXPECTED_MAX_TIME, (
        f"average_age too slow: best={best:.6f}s > allowed={EXPECTED_MAX_TIME:.6f}s"
    )

    # Correctness sanity check
    expected_value = sum(data) / len(data)
    assert average_age(data) == pytest.approx(expected_value, rel=1e-12, abs=1e-12)

    # Ensure that timing information was printed
    out, _ = capfd.readouterr()
    assert "average_age():" in out
