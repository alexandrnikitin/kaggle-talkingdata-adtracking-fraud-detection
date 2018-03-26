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





```bash

# analysis
docker run -d -p 8888:8888 -v ~/kaggle-talkingdata-adtracking-fraud-detection/:/home/jovyan/work/kaggle-talkingdata-adtracking-fraud-detection -e NB_UID=1000 -e GRANT_SUDO=yes --user root jupyter/datascience-notebook start-notebook.sh --NotebookApp.token=''

kaggle competitions download -c talkingdata-adtracking-fraud-detection -p ./data/raw/
unzip -j ./data/raw/'*.zip' -d ./data/raw/

python src/data/split_hourly.py data/raw/train_sample.csv data/interim/train_sample

split -l 1000000 -d train.vw train.vw.

head -n 10000000 train.vw > train.vw.00
tail -n +10000001 train.vw | head -n 400000 > validate.vw.00
tail -n +10400001 train.vw | head -n 400000 > test.vw.00

# train
vw data/processed/train.vw \
    -f models/model \
    --invert_hash models/model.inverted \ 
    -b 29 \
    --link=logistic \
    --loss_function=logistic \
    --hash all \
    --passes 10 \
    --cache --kill_cache \
    --ftrl \
    -q ::

# test
vw data/processed/test.vw \
    -i models/model \
    --testonly \
    -p models/predictions/test \
    --loss_function=logistic \
    --hash all

# audit
vw --data data/processed/train.vw \
    -i models/model \
    --audit_regressor models/model.audit
    
awk '{ if ($1 == "-1") print "0"; else print $1;}' data/processed/test.vw > data/processed/test.labels
./libs/perf.linux/perf -all -files data/processed/test.labels models/predictions/test

# hyperparameter optimization
docker run -p 27017:27017 --name hyperopt-mongo -d mongo

python src/models/hyperopt_vw.py \
    --train_data=/root/alex/kaggle-talkingdata-adtracking-fraud-detection/data/processed/train.medium.vw.00 \
    --test_data=/root/alex/kaggle-talkingdata-adtracking-fraud-detection/data/processed/test.medium.vw.00 \
    --vw_args="--bit_precision 25 --ftrl --link logistic --hash all -q :: --holdout_off" \
    --outer_loss_function='roc-auc' \
    --mongo=mongo://localhost:27017/exp6/jobs \
    --max_evals=1000

run-hyperopt-mongo-workers.sh 15 localhost:27017/exp5

# submission
echo "click_id,is_attributed" > models/predictions/submission.csv
awk '{print $2","$1}' models/predictions/test >> models/predictions/submission.csv
zip -r models/predictions/submission.zip models/predictions/submission.csv
kaggle competitions submit -c talkingdata-adtracking-fraud-detection -f models/predictions/submission.csv -m "message"

```
