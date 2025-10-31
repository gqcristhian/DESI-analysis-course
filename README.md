# DESI-analysis-course

Itinerary for the course below. I will be uploading the material a day in advance

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

*If you already have CONDA, skip step (1)*

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

# Preparation in advance
Make sure you have few Gb (~5Gb, blame the random catalogs!) of disk space free and if you want to explore the catalogs please visit:
https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/

I suggest to download:
- LRG_SGC_0_clustering.ran.fits 
- LRG_NGC_0_clustering.ran.fits 
- BGS_BRIGHT-21.5_SGC_0_clustering.ran.fits 
- BGS_BRIGHT-21.5_NGC_0_clustering.ran.fits 
- LRG_NGC_clustering.dat.fits 
- BGS_BRIGHT-21.5_SGC_clustering.dat.fits 
- ELG_LOPnotqso_NGC_clustering.dat.fits 
- LRG_SGC_clustering.dat.fits
- LRG+ELG_LOPnotqso_NGC_clustering.dat.fits
- BGS_BRIGHT-21.5_full_HPmapcut.dat.fits
- QSO_SGC_clustering.dat.fits
- ELG_LOPnotqso_SGC_clustering.dat.fits
- QSO_NGC_clustering.dat.fits
- BGS_BRIGHT-21.5_NGC_clustering.dat.fits
- LRG+ELG_LOPnotqso_SGC_clustering.dat.fits

