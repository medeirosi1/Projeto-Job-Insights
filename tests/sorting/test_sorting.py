from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            'job_title': 'Marketing',
            'company': 'Relief',
            'state': 'NY', 'city': 'New York',
            'min_salary': 5000, 'max_salary': 7000,
            'rating': '4.0',
            'date_posted': '2020-05-08',
            'job_type': 'FULL_TIME', 'id': '0'
        },
        {
            'job_title': 'Programmer',
            'company': 'Relief',
            'state': 'NY', 'city': 'New York',
            'min_salary': 10000, 'max_salary': 20000,
            'rating': '4.0',
            'date_posted': '2020-05-08',
            'job_type': 'FULL_TIME', 'id': '1'
        }
    ]

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 5000

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 20000

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-05-08"
