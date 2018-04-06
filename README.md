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
virtualenv -p /usr/bin/python3.6 venv
source venv/bin/activate
pip install -r requirements.txt

# perf
mkdir libs
cd libs/
wget http://osmot.cs.cornell.edu/kddcup/perf/perf.src.tar.gz
tar xzf perf.src.tar.gz
cd perf.src/
nano perf.c # relax max items constraint
make
cd ..
 


# analysis
docker run -d -p 8899:8888 -v ~/kaggle-talkingdata-adtracking-fraud-detection/:/home/jovyan/work/kaggle-talkingdata-adtracking-fraud-detection -e NB_UID=1000 -e GRANT_SUDO=yes --user root jupyter/datascience-notebook start-notebook.sh --NotebookApp.token=''

kaggle competitions download -c talkingdata-adtracking-fraud-detection -p ./data/raw/
unzip -j ./data/raw/'*.zip' -d ./data/raw/

python src/data/split_hourly.py data/raw/train.csv data/interim/train
python src/data/split_hourly.py data/raw/test.csv data/interim/test

export VW_TEST_FILE=data/interim/train_2017-11-08_0400
python src/data/make_dataset.py ${VW_TEST_FILE}.csv ${VW_TEST_FILE}.vw

export VW_TEST_FILE=data/interim/train_2017-11-08_0400
head -n $[ $(wc -l ${VW_TEST_FILE}.vw|cut -d" " -f1) * 40 / 100 ] ${VW_TEST_FILE}.vw > ${VW_TEST_FILE}.validate.vw
tail -n +$[ ($(wc -l ${VW_TEST_FILE}.vw|cut -d" " -f1) * 40 / 100) + 1 ] ${VW_TEST_FILE}.vw > ${VW_TEST_FILE}.test.vw

awk '{ if ($1 == "-1") print "0"; else print $1;}' ${VW_TEST_FILE}.validate.vw > ${VW_TEST_FILE}.validate.labels
awk '{ if ($1 == "-1") print "0"; else print $1;}' ${VW_TEST_FILE}.test.vw > ${VW_TEST_FILE}.test.labels


split -l 1000000 -d train.vw train.vw.

head -n 10000000 train.vw > train.vw.00
tail -n +10000001 train.vw | head -n 400000 > validate.vw.00
tail -n +10400001 train.vw | head -n 400000 > test.vw.00

# train
export VW_TRAIN_FILE=train_2017-11-07_0400
vw --data data/interim/${VW_TRAIN_FILE}.vw \
    -f models/${VW_TRAIN_FILE}.model \
    -b 29 \
    --ftrl \
    --link=logistic \
    --loss_function=logistic \
    --hash all \
    --passes 10 \
    --cache --kill_cache \
    -q ::

--classweight -1:0.75 --classweight 1:50 --learning_rate 0.15 --passes 5

# test

export VW_TRAIN_FILE=train_2017-11-07_0400
export VW_TEST_FILE=train_2017-11-07_0400
vw --data data/interim/${VW_TEST_FILE}.test.vw \
    -i models/${VW_TRAIN_FILE}.model \
    --testonly \
    -p models/${VW_TEST_FILE}.test.predictions \
    --loss_function=logistic

# audit
vw --data data/processed/train.vw \
    -i models/model \
    --audit_regressor models/model.audit
    
./libs/perf.src/perf -all -files data/interim/${VW_TEST_FILE}.test.labels models/${VW_TEST_FILE}.test.predictions

# hyperparameter optimization
docker run -p 27017:27017 --name hyperopt-mongo -d mongo

python src/models/hyper_vw.py \
    --train_data=/root/alex/kaggle-talkingdata-adtracking-fraud-detection/data/interim/train_2017-11-07_0400.vw \
    --validation_data=/root/alex/kaggle-talkingdata-adtracking-fraud-detection/data/interim/train_2017-11-08_0400.validate.vw \
    --test_data=/root/alex/kaggle-talkingdata-adtracking-fraud-detection/data/interim/train_2017-11-08_0400.test.vw \
    --vw_args="--bit_precision 29 --ftrl --link logistic --loss_function logistic --hash all -q ::" \
    --outer_loss_function='roc-auc' \
    --trials_output="trials.json" \
    --mongo=mongo://localhost:27017/train_2017-11-07_0400/jobs \
    --max_evals=200

run-hyperopt-mongo-workers.sh 15 localhost:27017/train_2017-11-07_0400

# submission
echo "click_id,is_attributed" > models/predictions/submission.csv
awk '{print $2","$1}' models/predictions/test >> models/predictions/submission.csv
zip -r models/predictions/submission.zip models/predictions/submission.csv
kaggle competitions submit -c talkingdata-adtracking-fraud-detection -f models/predictions/submission.csv -m "message"

```
