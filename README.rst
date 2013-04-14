iphy - hip nanoblogging
========================
enjoy.

INSTALL
========================
You need:

* local py27 env with Fabric and clone of this repo
* py27 on remote server

You do:

* copy and adjust env dict in fabfile.py.sample
* fab build_env:target=production # not tested!,
  i usually do this by myself
* configure supervisord.conf (see sample) in root
* start supervisord
* configure settings.py (see sample) in var/iphy-instance
* install mongo in the same virtualenv (e.g. place binaries in bin)
* fab deploy:target=production # and that's it, app runs port 5000!

