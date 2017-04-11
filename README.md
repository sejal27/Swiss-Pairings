[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

# Run tournament using swiss pairings

## Table of Contents
- [Background](#background)
- [Author](#author)
- [How to Use](#how-to-use)
- [Source Files](#source-files)
- [License](#license)

## Background
The files in this repository provide a few basic back-end functions to run a swiss pairing tournament, using postgresql db and python.
You may want to install Vagrant and Virtual-Box for running some of these files.

## Author
[Sejal Parikh](https://in.linkedin.com/in/sejalparikh)

## How to Use
1. Download all the files in the same folder, say 'tournament'.
2. Store your tournment folder under your Vagrant shared files. 
3. On your terminal, run the following to setup your database:
    - `vagrant ssh`
    - Change the path to the tournament directory
    - `psql -f tournament.sql`
    - `python tournament_test.py`
4. To view the db schema, you can run `psql tournament`

## Source Files
1. tournament.sql : Contains queries to create database and views
2. tournament.py : Contains necessary functions to generate swiss pairings and player standings.
3. tournament_test.py : Provides a unit-test framework for your tournament.py file.
4. insertdb.py : Provides a way to insert random matches and players in your database. This helps while trying out some db queries.

## License
[GNU General Public License v3](../LICENSE)
