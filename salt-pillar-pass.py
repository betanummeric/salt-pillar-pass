#!/usr/bin/env python3

# Import salt modules
#import salt.loader
#import salt.utils.minions
import subprocess
import yaml
import re

CONFIG={'prefix': 'salt'}
ALLOWED_PATHS=re.compile('[-_a-zA-Z0-9]+(/[-_a-zA-Z0-9]+)+')

def ext_pillar(minion_id, pillar, *args, **kwargs):
  """ Main handler. Compile pillar data for the specified minion ID
  """
  new_pillar = {'pass': {}}
  for key in CONFIG:
    if key in kwargs:
      CONFIG[key] = kwargs[key]

  new_pillar['pass'] = read_pass(minion_id, CONFIG)
  return new_pillar


def read_pass(minion_id, CONFIG):
  path = '/'.join([CONFIG['prefix'].strip('/'), minion_id.strip('/')])
  # todo sanity check path 
  if ALLOWED_PATHS.fullmatch(path) is None:
    raise Exception(f"invalid pass path (must match '{ALLOWED_PATHS.pattern}'): {path}")
  with subprocess.Popen(['pass', 'show', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    err = proc.stderr.read()
    if err and err != "":
      raise Exception(f"invoking pass failed:\n{err}")
    yaml_pillar = proc.stdout.read()
  return yaml.load(yaml_pillar)

