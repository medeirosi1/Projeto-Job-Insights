from src.jobs import read
import csv

def get_unique_job_types(path):
    readJobs = read(path)
    jobTypes = [read['job_type'] for read in readJobs ]
    print(list(set(jobTypes)))
    return list(set(jobTypes))

# get_unique_job_types('src/jobs.csv')

def filter_by_job_type(jobs, job_type):
    jobType = [job for job in  jobs if job['job_type'] == job_type]
    print(jobType)
    return jobType


def get_unique_industries(path):
    readJobs = read(path)
    jobTypes = [read['industry'] for read in readJobs if read['industry'] != '']
    print(list(set(jobTypes)))
    return list(set(jobTypes))

# get_unique_industries('src/jobs.csv')

def filter_by_industry(jobs, industry):
    industry_filter = [job for job in  jobs if job['industry'] == industry]
    print(industry_filter)
    return industry_filter


def get_max_salary(path):
    readJobs = read(path)
    maxSalary = [int(read['max_salary']) for read in readJobs if read['max_salary'].isdigit()]
    print(maxSalary)
    print(max(maxSalary))
    return max(maxSalary)

# get_max_salary('src/jobs.csv')

def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
