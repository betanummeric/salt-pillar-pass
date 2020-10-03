# salt-pillar-pass

This is an external pillar for salt that offers [pass](https://passwordstore.org) as storage for pillar data.

## Installation

To use salt-pillar-pass, put this in your salt-master configuration (`/etc/salt/master`):
```yaml
extension_modules: modules
ext_pillar:
  - salt-pillar-pass:
      prefix: salt
```

You need to put the `salt-pillar-pass.py` file to `<root_dir>/<extension_modules>/pillar/salt-pillar-pass.py`, with `<root_dir>` and `extension_modules>` as configured in the salt-master configuration.
Adjust the `prefix` value as needed. It will be prepended to all paths fetched from _pass_.
You don't need to include something in your `top.sls` at your `pillar_roots`.

## Usage

edit/create a secret: `pass edit <prefix>/<minon_id>`

check, what the minion sees: `salt <minion_id> pillar.get pass`--out=yaml`

