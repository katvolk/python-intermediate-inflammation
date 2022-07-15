# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/katvolk/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)


Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation
- Clone the repo ``git clone repo``
- Install via ``pip install -e .``
- Check everything runs by running ``pytest`` in the root directory


## Contributing:

Report bugs or describe feature requests by creating an issue [here](https://github.com/katvolk/python-intermediate-inflammation/issues)

If you make changes or develop new code you would like to contribute to the main repository, create a pull requests [here](https://github.com/katvolk/python-intermediate-inflammation/pulls)

## Credits/Acknowledgements: 

The base of this repo was generated from [here](https://github.com/carpentries-incubator/python-intermediate-inflammation).
Contributors to this repo include 
[Kat Volk](https://github.com/katvolk),
[Daniel Egbo](https://github.com/Danselem), 
[Markus Hundertmark](https://github.com/mpgh), and
[Alessandro Mazzi](https://github.com/Thalos12).

## Contact information

Kat Volk, kat.volk@gmail.com

## Licence: 

Inflam is released under a GNU General Public License v3.0. 
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

