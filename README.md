[![CI](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/install.yml)
[![CI](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/format.yml)
[![CI](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/lint.yml)
[![CI](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Individual_proj_1_Gavin_Li/actions/workflows/test.yml)

# IDS 706 Data Engineering Individual Project # 1

Gavin Li `gl183`

## Video Link

[The link for the demo video](https://youtu.be/u9MoUnZqlRo)

## Purpose of the Project

The purpose of the individual project #1 is to conduct data analysis using either Pandas or Polars in both Jupyter Notebook and python script. I use Pandas to conduct the analysis.

## Template

For this project, I use the ruff template as the foundation of my repo.

This template lints code using `ruff` instead of `pylint`, which was used in the first two mini projects.

### `make format` result

![Make_format_result](./resources/make_format.png)

### `make test` result

![Make_test_result](./resources/make_result.png)

### `make lint` result

![Make_lint_result](./resources/make_lint.png)

## Descriptive Statistics using Python Pandas in both python script and jupyter notebook

1. Read the csv file at `./resources/train.csv` using `pandas.read_csv()` function

2. Generated sumamry statistics for variable `Survived` in the `Titanic` dataset using `.median()`, `.mean()`, `.std()` function. The result is as follow:

![Summary_stats](./resources/desc_stats.png)

3. Generated histogram for variable `Survived` in the `Titanic` dataset using `matplotlib.pyplot`.

![Histogram](./resources/hist.png)

## References

[Professor Noah's ruff template](https://github.com/nogibjj/python-ruff-template)