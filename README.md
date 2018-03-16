talkingdata-adtracking-fraud-detection
==============================

A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


```
kaggle competitions download -c talkingdata-adtracking-fraud-detection -p ./data/raw/
unzip '*.zip'

split -l 1000000 -d train.vw train.vw.

sed -e "s/\${i}/500/" train.vw > train.vw.500
head -n 10000000 train.vw.500 > train.vw.00
tail -n +10000001 train.vw.500 | head -n 400000 > test.vw.00

# train
vw data/processed/train.vw.00 \
    -f models/vw/baseline.model \
    -b 29 \
    --link=logistic \
    --loss_function=logistic \
    --hash all \
    --passes 10 \
    --cache --kill_cache \
    --ftrl \
    -q ::

# test
vw data/processed/train.vw.01 \
    -i models/vw/baseline.model.00 \
    --testonly \
    -p models/vw/predictions/train.vw.01.txt \
    --loss_function=logistic \
    --hash all

    
awk '{ if ($1 == "-1") print "0"; else print $1;}' /cba/alex/test.vw.00 > /cba/alex/test.labels.00
./libs/perf.linux/perf -all -files /cba/alex/test.labels.00 models/vw/predictions/test.vw.00.txt

sed -i.bak -e "s/ 500 //" /cba/alex/test.vw.00
 
./libs/vw-hyperopt/vw-hyperopt.py --train ./train_set.vw \
	--holdout ./holdout_set.vw \
	--max_evals 200 \
	--outer_loss_function roc-auc \
	--vw_space '--algorithms=ftrl,sgd --l2=1e-8..1e-1~LO --l1=1e-8..1e-1~LO -l=0.01..10~L --power_t=0.01..1 --ftrl_alpha=5e-5..8e-1~L --ftrl_beta=0.01..1 --passes=1..10~I --loss_function=logistic -q=::~O'  \
	--plot 
	
./vw-hypersearch -L -t data/processed/test.vw.00 1e-10  5e-4 vw data/processed/train.vw.00     -f models/vw/baseline.model  --l1 %   -b 29   --ftrl  --link=logistic     --loss_function=logistic     --hash all     --passes 5     --cache --kill_cache     -q :: --threads

awk '{print $2","$1}' models/vw/predictions/test.txt > models/vw/predictions/submission-1.csv


```
