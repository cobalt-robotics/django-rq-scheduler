# Django RQ Scheduler

A database backed job scheduler for Django RQ.

## Requirements

See `setup.py` file.

## Usage

### Install

Install with Pip for GitHub.


### Update Django Settings

1. In `settings.py`, add `django_rq` and `scheduler` to  `INSTALLED_APPS`:

	```

	INSTALLED_APPS = [
    	...
    	'django_rq',
    	'scheduler',
    	...
	]


	```

2. Configure Django RQ. See https://github.com/ui/django-rq#installation


### Migrate

The last step is migrate the database:

```
./manage.py migrate
```

## Creating a Job

See http://python-rq.org/docs/jobs/ or https://github.com/ui/django-rq#job-decorator

An example:

**myapp.jobs.py**

```
@job
def count():
    return 1 + 1
```

If you also wish to run the underpinning **RQ Scheduler** at an interval different from its default of
once every 60 seconds you can do so by setting `DJANGO_RQ_SCHEDULER_INTERVAL` to the new preferred interval.
This is important if you want a job to either run multiple times a minute
or to schedule a job more precisely than within a 60 second window.

## Scheduling a Job

### Scheduled Job

1. Sign into the Django Admin site, http://localhost:8000/admin/ and locate the **Django RQ Scheduler** section.

2. Click on the **Add** link for Scheduled Job.

3. Enter a unique name for the job in the **Name** field.

4. In the **Callable** field, enter a Python dot notation path to the method that defines the job. For the example above, that would be `myapp.jobs.count`

5. Choose your **Queue**. Side Note: The queues listed are defined in the Django Settings.

6. Enter the time the job is to be executed in the **Scheduled time** field. Side Note: Enter the date via the browser's local timezone, the time will automatically convert UTC.

7. Click the **Save** button to schedule the job.

### Repeatable Job

1. Sign into the Django Admin site, http://localhost:8000/admin/ and locate the **Django RQ Scheduler** section.

2. Click on the **Add** link for Repeatable Job

3. Enter a unique name for the job in the **Name** field.

4. In the **Callable** field, enter a Python dot notation path to the method that defines the job. For the example above, that would be `myapp.jobs.count`

5. Choose your **Queue**. Side Note: The queues listed are defined in the Django Settings.

6. Enter the time the first job is to be executed in the **Scheduled time** field. Side Note: Enter the date via the browser's local timezone, the time will automatically convert UTC.

7. Enter an **Interval**, and choose the **Interval unit**. This will calculate the time before the function is called again.

8. In the **Repeat** field, enter the number of time the job is to be ran. Leaving the field empty, means the job will be scheduled to run forever.

9. Click the **Save** button to schedule the job.


## Reporting issues or Features

Please report issues via [GitHub Issues](https://github.com/istrategylabs/django-rq-scheduler/issues) .
