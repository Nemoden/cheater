import sys
import argparse


def runserver(args):
  from cheater import app
  app.run(debug = args.debug)

def db(args):
  if args.create_all:
    from cheater.database import create_all
    create_all()

parser = argparse.ArgumentParser(description = "Cheater actions", usage="python %(prog)s action [action params]")
subparsers = parser.add_subparsers(title='actions', dest='action')
runserver_parser = subparsers.add_parser('runserver', help='runserver help')
runserver_parser.add_argument('port', nargs='?', default=5000)
runserver_parser.add_argument('--debug', '-d', action='store_true')
runserver_parser.set_defaults(func=runserver)
db_parser = subparsers.add_parser('db', help='db management help')
db_parser.add_argument('--create-all', '-a', dest='create_all', action='store_true', help = 'Create all tables')
db_parser.set_defaults(func=db)

if not sys.argv[1:]:
  parser.print_help()
else:
  args = parser.parse_args(sys.argv[1:])
  args.func(args)
