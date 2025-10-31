# DESI-analysis-course

#### Day 1: 
- [ ] DESI instrument 
- [ ] Galaxy catalogs 
- [ ] Two-point measurements

#### Day 2:
- [ ] Continuation of two-point measurements (if needed)
- [ ] Measuring Baryon Acoustic Oscillations (BAO)

#### Day 3:
- [ ] From BAO to cosmological parameters
- [ ] BAO likelihood
- [ ] Cosmological constraints

#### Day 4:
- [ ] General talk


(Special thanks goes to Arnaud DeMattia for his help with the various scripts)


# Installation instruction for the DESI conda environment

[ONLY IF YOU DON'T HAVE CONDA, OTHERWISE SKIP (1)]

(1) First of all, you will need conda installed. For Linux or macOS you can do:
```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

(2) After your conda is active, you can simply do:
```sh
bash setup_cosmodesi_course.sh`
```

(3) Activate your new environment as
```sh
conda activate cosmodesi_course
```

(4) If everything is successful, you can then simply run the test.py as:
```sh
python test.py
```

You should see that **tests pass!**
