#!/usr/bin/env python
from flask.ext.script import Manager
from iphy.app import create_app

app = create_app()
manager = Manager(app)

def main():
    global manager
    manager.run()


if __name__ == "__main__":
    main()

