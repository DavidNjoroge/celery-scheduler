# celery-scheduler

a sample python3.6 celery scheduler with a crawler that you can configure to run at a specific time or run periodically depending on the time you set

#### setup
tested on ubuntu
* you need to install rabbitmq https://www.vultr.com/docs/how-to-install-rabbitmq-on-ubuntu-16-04-47
* clone the repository
* create virtual env
* install requirements ``` python3.6 -m pip install -r requirements.txt ```

#### usage
to run the scheduler in the terminal run
```
celery -A app worker -B
```
to change the interval of the scheduler update the setup_periodic_tasks() function in app module
