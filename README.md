# Nanome - 2D Chemical Preview

A Nanome Plugin to generate 2D images of molecules using RDKit.

## Dependencies

[Docker](https://docs.docker.com/get-docker/)

When running outside of Docker:

This plugin requires `rdkit` to be installed and in the `PATH` variable.

Installation instructions for `rdkit` can be found [here](http://www.rdkit.org/docs/Install.html)

## Usage

To run 2D Chemical Preview in a Docker container:

```sh
$ cd docker
$ ./build.sh
$ ./deploy.sh -a <plugin_server_address> [optional args]
```

## Development

To run 2D Chemical Preview with autoreload:

```sh
$ python3 -m pip install -r requirements.txt
$ python3 run.py -r -a <plugin_server_address> [optional args]
```

## License

MIT
