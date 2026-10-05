<div align="center">

# Network Science

**Coursework for Network Science at the University of Zurich, Fall 2023**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-3.2-2C5BB4)
![uv](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

[Contents](#contents) · [Getting started](#getting-started) · [Data](#data) · [Release as submitted](https://github.com/HuberNicolas/network-science-uzh/releases/tag/v1.0.0)

</div>

Four graded assignments from the Network Science course, solved in Jupyter notebooks with NetworkX: degree
correlations and centralities, random graph models, community detection, power laws, maximum-entropy null models
(ERGMs), correlation networks of stocks, robustness, and epidemic spreading on networks.

> [!NOTE]
> This is unofficial study material. The notebooks and reports are shown as we submitted them in 2023: they are not
> corrected, and the repository is not developed further. The assignment sheets and other course material are not
> included. The library versions are pinned to December 2023.

> [!WARNING]
> Most notebooks delete and recreate their `output/` folder when you run them, and some computations (randomised
> networks, ERGM sampling, SIR simulations) run for a long time. Work on a copy if you want to keep the original plots.

## Contents

| Assignment | Topics | Notebook | Report |
|---|---|---|---|
| [1](assignment-1/) | Permutation matrices and irreducibility; average nearest-neighbour degree and assortativity of real and randomised networks; degree, closeness, betweenness and eigenvector centrality and their correlations | [Assignment_01.ipynb](assignment-1/Assignment_01.ipynb), [reducible.py](assignment-1/reducible.py), [lattice_n_k_generator.py](assignment-1/lattice_n_k_generator.py) | [Network_Science_Assignment_1.pdf](assignment-1/Network_Science_Assignment_1.pdf) (hand-in), [Assignment_01_Results.pdf](assignment-1/Assignment_01_Results.pdf) |
| [2](assignment-2/) | Erdős–Rényi model, Watts–Strogatz model, community detection on real and randomised networks, power-law fits of degree distributions | [Assignment_02.ipynb](assignment-2/Assignment_02.ipynb) | [Assignment_02_Results.pdf](assignment-2/Assignment_02_Results.pdf) |
| [3](assignment-3/) | T1: strength assortativity of the World Trade Web and enhanced configuration models (CReMa, NEMtropy); T2: minimum spanning trees of NYSE stock correlations; T3: robustness of synthetic and real networks under random failures and attacks | [t1](assignment-3/t1/Assignment_03.ipynb), [t2](assignment-3/t2/Assignment_03.ipynb), [t3](assignment-3/t3/Assignment_03.ipynb) | [Assignment_03_Results_1-3.pdf](assignment-3/Assignment_03_Results_1-3.pdf) |
| [4](assignment-4/) | Compartmental models (SIR) on networks; spreading ability of nodes versus their centrality | [Assignment_04.ipynb](assignment-4/Assignment_04.ipynb), [Assignment_04_T1_1_2.ipynb](assignment-4/Assignment_04_T1_1_2.ipynb), [task_1.3separated.ipynb](assignment-4/task_1.3separated.ipynb), [task_1.4separated.ipynb](assignment-4/task_1.4separated.ipynb) | [Assignment_4_Results_merged.pdf](assignment-4/Assignment_4_Results_merged.pdf) |

Each assignment folder holds its data (`assignment_0X_data/` or `datasets/`) and the generated plots (`output/`).
Assignment 3 keeps one shared data folder for its three tasks.

## Getting started

You need [uv](https://docs.astral.sh/uv/). It installs Python 3.10 and the pinned libraries from `uv.lock`.

1. Clone the repository:

   ```bash
   git clone https://github.com/HuberNicolas/network-science-uzh.git
   ```

   ```bash
   cd network-science-uzh
   ```

2. Install the environment:

   ```bash
   uv sync
   ```

3. Start Jupyter and open a notebook from the table above. Run it from its own folder, because the notebooks use
   relative paths:

   ```bash
   uv run jupyter notebook
   ```

### Tech stack

| Area | Libraries |
|---|---|
| Graphs | ![NetworkX](https://img.shields.io/badge/NetworkX-3.2-2C5BB4) ![NEMtropy](https://img.shields.io/badge/NEMtropy-2.1-555555) ![powerlaw](https://img.shields.io/badge/powerlaw-1.5-555555) |
| Numerics | ![NumPy](https://img.shields.io/badge/NumPy-1.26-013243?logo=numpy&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-1.11-8CAAE6?logo=scipy&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-2.1-150458?logo=pandas&logoColor=white) ![Numba](https://img.shields.io/badge/Numba-0.58-00A3E0?logo=numba&logoColor=white) |
| Plots and notebooks | ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-11557C) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white) |

`pyproject.toml` resolves all libraries as of 23 December 2023 (`exclude-newer`). NEMtropy imports Numba without
declaring it, so Numba is listed explicitly.

## Data

The course provided the datasets on OLAT, the UZH learning platform. The graph files contain anonymised integer node
labels and no metadata, and the course material did not document their original sources or licenses.

| Data | Used in | Notes |
|---|---|---|
| `graph_AstroPh`, `graph_CondMat`, `graph_celegansInteractomes`, `graph_chess`, `graph_eu_airlines`, `graph_facebook`, `graph_game_thrones`, `graph_internet`, `graph_jazz_collab` (GML) | Assignment 1 | The jazz network is from Gleiser and Danon (2003) |
| `graph_Korea`, `graph_eu_airlines`, `graph_hep-th`, `graph_internet`, `graph_macaque`, `graph_madrid`, `graph_starwars` (GML) | Assignment 2 | |
| World Trade Web 1992–2002 (GraphML and edge lists), NYSE correlation matrices (NumPy), `graph_eu_airlines`, `graph_power` | Assignment 3 | |
| `graph1.1`, `graph1.2`, `graph_jazz_collab`, `graph_madrid` (GML) | Assignment 4 | |

Some files match well-known public networks in their number of nodes and edges. These are likely origins, not
confirmed by the course:

| File | Nodes | Edges | Likely origin |
|---|---|---|---|
| `graph_facebook` | 4,039 | 88,234 | SNAP [ego-Facebook](https://snap.stanford.edu/data/ego-Facebook.html), McAuley and Leskovec (2012) |
| `graph_AstroPh` | 17,903 | 196,972 | Largest component of SNAP [ca-AstroPh](https://snap.stanford.edu/data/ca-AstroPh.html), Leskovec et al. (2007); SNAP lists 197,031 edges for it |
| `graph_jazz_collab` | 198 | 2,742 | Jazz musicians network, Gleiser and Danon (2003) |
| `graph_game_thrones` | 107 | 352 | Character network of *A Storm of Swords*, Beveridge and Shan (2016) |
| `graph_power` | 4,941 | 6,594 | Western US power grid, Watts and Strogatz (1998) |
| `graph_madrid` | 64 | 243 | Network of the 2004 Madrid train bombing suspects, Hayes (2006) |

The data files are here so that the notebooks run as they are. They are not covered by the MIT license of this
repository. If you own one of these datasets and want it removed, please open an issue.

## Known issues

- The notebooks were written with Python 3.8 (assignment 4), 3.10 and 3.11 (assignments 1–3). The shared environment
  uses Python 3.10: Python 3.11 no longer accepts a set in `random.sample`, which `task_1.3separated.ipynb` relies on.
- `assignment-3/t2/Assignment_03.ipynb` stops at the degree distributions of the Gaussian and one-factor models with
  `NameError: name 'tickers' is not defined`. The cell that defined `tickers` was removed before submission; the
  stored outputs come from the original session.
- The last cell of `assignment-1/Assignment_01.ipynb` and `assignment-3/t3/Assignment_03.ipynb` exports the notebook
  to PDF with `jupyter nbconvert --to pdf`. This needs a LaTeX installation and fails without one; the rest of the
  notebook is not affected.
- Answers may be wrong or incomplete in places. They are left as submitted.

## Authors

- Nicolas Huber ([@HuberNicolas](https://github.com/HuberNicolas))
- Raphael Wäspi ([@sumsumcity](https://github.com/sumsumcity))

We worked on all parts of the assignments together.

## Acknowledgements

The course Network Science (03SM22MI0019, Fall 2023, 6 ECTS) was led by Prof. Dr. Claudio J. Tessone, Blockchain &
Distributed Ledger Technologies Group, Department of Informatics, University of Zurich (UZH Blockchain Center). The
instructors were Dr. Nicolò Vallarano, Dr. Jian-Hong Lin, Yu Gao, Yu Zhang and Benjamin Kraner. The assignment tasks
and datasets come from the course.

## License

The code and notebooks are licensed under the [MIT License](LICENSE). The datasets and the assignment texts quoted in
the notebooks belong to their respective owners.
