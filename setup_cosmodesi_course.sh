#!/usr/bin/env bash
set -e

echo ">>> Creating conda environment: cosmodesi_course"
conda create -n cosmodesi_course python=3.10 -y
conda activate cosmodesi_course || source "$(conda info --base)/etc/profile.d/conda.sh" && conda activate cosmodesi_course

echo ">>> Installing JAX (CPU)"
pip install jax==0.4.23 jaxlib==0.4.23

echo ">>> Installing DESI cosmology stack"
pip install \
  git+https://github.com/cosmodesi/cosmoprimo#egg=cosmoprimo[class,camb,astropy,extras] \
  git+https://github.com/cosmodesi/desilike#egg=desilike[plotting,jax] \
  git+https://github.com/cosmodesi/pycorr#egg=pycorr[corrfunc] \
  git+https://github.com/cosmodesi/pyrecon#egg=pyrecon[extras] \
  git+https://github.com/cosmodesi/pypower#egg=pypower \
  cobaya==3.5.7

echo ">>> Installing JAX ecosystem and scientific stack"
pip install \
  equinox==0.11.3 optax==0.1.8 chex==0.1.90 lineax==0.0.8 jaxtyping==0.2.25 ml_dtypes==0.5.3 jaxopt==0.8.3 \
  numpy==1.26.4 scipy==1.12.0 matplotlib==3.10.6 pandas==2.1.4 h5py==3.14.0 mpi4py==4.1.0 getdist==1.7.0 fitsio==1.2.8

echo ">>> Installing Jupyter and helpers"
pip install jupyterlab notebook ipywidgets seaborn tabulate
python -m ipykernel install --user --name cosmodesi_course --display-name "cosmodesi_course"

echo "✅ cosmodesi_course environment ready!"
