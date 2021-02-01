# Nanome - 2D Chemical Preview

A Nanome Plugin to generate 2D images of molecules using RDKit

### Preparation

Install the latest version of [Python 3](https://www.python.org/downloads/)

| NOTE for Windows: replace `python3` in the following commands with `python` |
| --------------------------------------------------------------------------- |


Install the latest `nanome` lib:

```sh
$ python3 -m pip install nanome --upgrade
```

### Dependencies

This plugin requires `rdkit` to be installed and in the `PATH` variable.

Installation instructions for `rdkit` can be found [here](http://www.rdkit.org/docs/Install.html)

### Installation

To install 2D Chemical Preview:

```sh
$ python3 -m pip install nanome-chemical-preview
```

### Usage

To start 2D Chemical Preview:

```sh
$ nanome-chemical-preview -a <plugin_server_address> [optional args]
```

### Docker Usage

To run 2D Chemical Preview in a Docker container:

```sh
$ cd docker
$ ./build.sh
$ ./deploy.sh -a <plugin_server_address> [optional args]
```

### Development

To run 2D Chemical Preview with autoreload:

```sh
$ python3 run.py -r -a <plugin_server_address> [optional args]
```

### License

MIT
