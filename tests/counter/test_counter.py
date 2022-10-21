from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "Job") == 3454
    assert count_ocurrences("src/jobs.csv", "P") == 248262
