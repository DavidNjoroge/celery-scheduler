from __future__ import absolute_import, unicode_literals
from celery import Celery
from app import crawler

app = Celery('app',
             broker_url='amqp://chutha:root@localhost:15672/pure_vhost',
             backend='rpc://chutha:root@localhost:15672/pure_vhost',
             # include=['app.tasks']
             )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    setup tasks schedule
    :param sender:
    :param kwargs:
    :return:
    """

    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(15.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task
def test(arg):
    all_matches = crawler.get_todays_games()
    print(arg, all_matches)


if __name__ == '__main__':
    app.start()
