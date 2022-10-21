from src.jobs import read


def get_unique_job_types(path):
    readJobs = read(path)
    jobTypes = [read['job_type'] for read in readJobs]
    return list(set(jobTypes))


def filter_by_job_type(jobs, job_type):
    jobType = [job for job in jobs if job['job_type'] == job_type]
    print(jobType)
    return jobType


def get_unique_industries(path):
    readTop = read(path)
    jobTypes = [read['industry'] for read in readTop if read['industry'] != '']
    print(list(set(jobTypes)))
    return list(set(jobTypes))


def filter_by_industry(jobs, industry):
    industry_filter = [job for job in jobs if job['industry'] == industry]
    print(industry_filter)
    return industry_filter


def get_max_salary(path):
    readJobs = read(path)
    maxSalary = [int(read['max_salary']) for read in readJobs if (
        read['max_salary'].isdigit()
    )]
    return max(maxSalary)


def get_min_salary(path):
    readJobs = read(path)
    minSalary = [int(read['min_salary']) for read in readJobs if (
        read['min_salary'].isdigit()
        )]
    return min(minSalary)


def matches_salary_range(job, salary):
    if(
        job.get('min_salary') is None
        or job.get('max_salary') is None
        or (type(job['min_salary']) is not int)
        or (type(job['max_salary']) is not int)
        or job['min_salary'] > job['max_salary']
        or (type(salary) is not int)
    ):
        raise ValueError

    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filterJobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filterJobs.append(job)
        except ValueError:
            print('Invalid value')
    return filterJobs
