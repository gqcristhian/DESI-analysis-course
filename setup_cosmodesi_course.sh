#!/usr/bin/env bash
set -e

echo ">>> Creating conda environment: cosmodesi_course"
conda create -n cosmodesi_course python=3.10 -y
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate cosmodesi_course

# 1️⃣ (Optional) Install Jupyter early for dependencies only
echo ">>> Preinstalling Jupyter base stack"
pip install jupyterlab notebook ipywidgets seaborn tabulate

# 2️⃣ Install numeric stack
echo ">>> Installing core scientific packages"
pip install --no-deps \
  numpy==1.26.4 scipy==1.12.0 matplotlib==3.10.6 pandas==2.1.4 \
  h5py==3.14.0 mpi4py==4.1.0 getdist==1.7.0 fitsio==1.2.8

# 3️⃣ Install pyclass first
pip install --no-deps git+https://github.com/adematti/pyclass

# 4️⃣ Install cosmodesi core packages
pip install --no-deps \
  git+https://github.com/cosmodesi/cosmoprimo#egg=cosmoprimo[class,camb,astropy,extras] \
  git+https://github.com/cosmodesi/desilike#egg=desilike[plotting,jax] \
  git+https://github.com/cosmodesi/pycorr#egg=pycorr[corrfunc] \
  git+https://github.com/cosmodesi/pyrecon#egg=pyrecon[extras] \
  git+https://github.com/cosmodesi/pypower#egg=pypower \
  cobaya==3.5.7

# 5️⃣ Install JAX + ML ecosystem
pip install --no-deps jax==0.4.23 jaxlib==0.4.23 jaxopt==0.8.3 optax==0.1.8 \
  jaxtyping==0.2.25 ml_dtypes==0.5.3

# 6️⃣ Now register kernel (after all packages exist)
python -m ipykernel install --user --name cosmodesi_course --display-name "cosmodesi_course"

echo "✅ cosmodesi_course environment ready!"
