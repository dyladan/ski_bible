import os
import sys
import transaction
import datetime

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Pass,
    Base,
    Skier,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = Pass(uid=1, speed=32, line=22, count=6, division="CM", date=datetime.date.today())
        DBSession.add(model)
        model = Pass(uid=1, speed=34, line=22, count=4, division="CM", date=datetime.date.today())
        DBSession.add(model)
        model = Pass(uid=2, speed=30, line=15, count=6, division="CM", date=datetime.date.today())
        DBSession.add(model)
        model = Pass(uid=2, speed=32, line=15, count=3, division="CM", date=datetime.date.today())
        DBSession.add(model)
        model = Skier(name="Danny Dyla", age=22, division="CM")
        DBSession.add(model)
        model = Skier(name="David Huisman", age=24, division="CM")
        DBSession.add(model)
