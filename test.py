#!/usr/bin/env python
"""
Quick import test for the cosmodesi_course environment.
Checks if all major DESI analysis packages are correctly installed and importable.
"""

import sys, os
import numpy as np
import matplotlib.pyplot as plt

print("✅ Starting environment test...\n")

# ------------------------------------------------------------
# Basic scientific stack
# ------------------------------------------------------------
for pkg in ["numpy", "scipy", "matplotlib", "pandas", "h5py", "mpi4py"]:
    try:
        __import__(pkg)
        print(f"  ✓ {pkg} imported successfully")
    except Exception as e:
        print(f"  ✗ {pkg} import failed: {e}")

# ------------------------------------------------------------
# Cosmodesi core packages
# ------------------------------------------------------------
try:
    from cosmoprimo.fiducial import DESI
    cosmo = DESI()
    print(f"  ✓ cosmoprimo imported — h = {cosmo.h:.3f}, Om = {cosmo['Omega_m']:.3f}")
except Exception as e:
    print(f"  ✗ cosmoprimo failed: {e}")

try:
    from desilike import setup_logging
    from desilike.theories.galaxy_clustering import BAOPowerSpectrumTemplate
    template = BAOPowerSpectrumTemplate(z=0.5, fiducial='DESI')
    print("  ✓ desilike imported and BAO template built")
except Exception as e:
    print(f"  ✗ desilike failed: {e}")

try:
    from pycorr import TwoPointCorrelationFunction
    print("  ✓ pycorr imported")
except Exception as e:
    print(f"  ✗ pycorr failed: {e}")

try:
    from pyrecon import MultiGridReconstruction
    print("  ✓ pyrecon imported")
except Exception as e:
    print(f"  ✗ pyrecon failed: {e}")

try:
    from pypower import CatalogFFTPower
    print("  ✓ pypower imported")
except Exception as e:
    print(f"  ✗ pypower failed: {e}")

try:
    from cobaya.run import run
    print("  ✓ cobaya imported")
except Exception as e:
    print(f"  ✗ cobaya failed: {e}")

# ------------------------------------------------------------
# JAX and ecosystem
# ------------------------------------------------------------
try:
    import jax, jaxlib
    key = jax.random.PRNGKey(0)
    x = jax.numpy.linspace(0, 1, 5)
    print(f"  ✓ jax imported — backend = {jax.default_backend()}")
except Exception as e:
    print(f"  ✗ jax failed: {e}")

try:
    import optax, equinox, chex, lineax, jaxtyping, ml_dtypes, jaxopt
    print("  ✓ jax ecosystem packages imported")
except Exception as e:
    print(f"  ✗ some jax-related package failed: {e}")

# ------------------------------------------------------------
# Final output
# ------------------------------------------------------------
print("\n✅ Environment test completed.")

# Optional: make a simple BAO plot test
try:

    from desilike.theories.galaxy_clustering import BAOPowerSpectrumTemplate, FlexibleBAOWigglesTracerPowerSpectrumMultipoles
    import numpy as np
    import matplotlib.pyplot as plt
    k = np.logspace(-3, 1, 300)
    z = 0.3
    template = BAOPowerSpectrumTemplate(z=z, fiducial='DESI', apmode='qiso')
    theory = FlexibleBAOWigglesTracerPowerSpectrumMultipoles(template=template, ells=(0,), k=k)
    pk = theory(qiso=1.0, b1=2.0)[0]
    plt.loglog(k, k*pk)
    plt.xlabel(r'$k\ [h\,\mathrm{Mpc}^{-1}]$')
    plt.ylabel(r'$k P(k)$')
    plt.title("BAO template quick check")
    plt.tight_layout()
    plt.savefig("test_bao.png")
    print("   ✅ BAO plot generated: test_bao.png")
except Exception as e:
    print(f"  ⚠️ Could not generate BAO plot: {e}")
