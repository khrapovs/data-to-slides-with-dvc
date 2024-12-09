# From raw data to management slides with DVC

![CI](https://github.com/khrapovs/data-to-slides-with-dvc/actions/workflows/workflow.yaml/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Usage

Create virtual environment:

```shell
uv venv
```

Install dependencies:

```shell
uv sync
```

Run DVC pipeline:

```shell
dvc repro -R dvc
```

Open resulting html slides in `data` folder.

## Contribute

Create virtual environment:

```shell
uv venv
```

Install dependencies:

```shell
uv sync --all-extras
```

Install pre-commit:

```shell
pre-commit install
```

## Blog Post

Long time ago as I was doing research in the university I had to write a lot of papers and conference presentation slides. They were heavy in graphics, tables, and formulas. All of the presentation materials were a result of multiple stages of data collection from multiple sources, transformation, and visualization. At that time, 10-15 years ago, academic research, at least in my field of economics and finance, was not particularly affected by the progress in IT sphere. Journals were still accepting manuscripts without any supporting materials such as versioned code and/or data. Needless to say, "git" sounded like a foreign abbreviation. Nevertheless, even if for my own sanity, I did my best to preserve some order in my workflow by minimizing as much as possible the amount of keyboard clicks required to go from a raw data source to the journal submission and a conference presentation.

After switching my career to being a data scientist in the private sector I quickly realized how much I missed in terms of tooling that could have simplified my life as a university researcher. Git is an indisputable prerequisite for a data scientist at any level. Data pipelining and automation of machine learning experimentation is a key to efficiency, speed, and reproducibility. After discovering [Data Version Control (DVC)](https://dvc.org/) Python library I have completed my journey to versioning everything, including data, machine learning artifacts such as trained models, and finally communication media such as presentation slides for a project's stakeholders. In this blog post I will demonstrate on a toy example how I organize and version data and machine learning workflow starting from a remote data source and finishing with executive slides, all in one terminal command!

In any data science project, ensuring reproducibility and traceability is critical. Data and machine learning experiment versioning are foundational practices that allow teams to maintain a clear and organized workflow, especially as projects grow in complexity. Without proper versioning, it becomes nearly impossible to keep track of which data, code, and configurations were used to produce a particular result. This can lead to wasted time, inconsistencies, and difficulty diagnosing issues when results deviate unexpectedly.

Versioning goes beyond just tracking code; it involves managing data transformations, model parameters, and experiment results in a systematic way. By using tools like DVC (Data Version Control), teams can ensure that every step in the pipeline is reproducible and well-documented. This not only supports collaboration within the team but also builds trust with stakeholders, as they can see a transparent record of how insights and models were derived. In short, versioning is not just about keeping things tidy — it is about ensuring the reliability and accountability of your entire data science workflow.

As a cherry on cake we can add presentation slides unavoidable as one of the main presentation medium in the corporate environment. These can be auto generated and versioned with every change in data sources and/or model configurations. This step may seem a bit extreme, but from my experience is still a big time saver for streamlined and effortless communication especially with non-technical stakeholders.

For the sake of simplicity of the example I will be using [Wine dataset from Scikit-Learn](https://scikit-learn.org/1.5/datasets/toy_dataset.html#wine-recognition-dataset). Starting from this remotely stored data I will build a very simple but at the same time typical machine learning pipeline composed of the following steps:

1. Download data from remote storage
2. Process data.
3. Train and save machine learning model.
4. Use processed data and the trained model to evaluate model performance and generate presentation slides with nice visuals.

The self-contained code for this task is freely available in [this repository](https://github.com/khrapovs/data-to-slides-with-dvc). DVC library mentioned above is used to organize individual steps into the pipeline, version intermediate and final artifacts such as data, model, and slides. The core ingredient of the DVC is the [dvc.yaml file](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/dvc.yaml) which defines the structure of the pipeline as well as step dependencies and outputs. The pipeline is run simply by executing `dvc repro` in the terminal. After the first run of the pipeline DVC calculates and saves certain metadata for the produced artifacts. This metadata is committed to the git repository together with the code itself. This allows DVC to track the pipeline and its artifacts over time and avoid running certain steps if their inputs did not change. Output artifacts can be stored in a cloud for easy sharing with other team members and stakeholders.

As one can see, the very first step is simply a `wget` call to download the `csv` file from the web to the local hard drive.

The second step runs a [simple python script](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/transform_data.py) that performs some data transformations, e.g. filling in of missing values, data type conversion, etc. The end result is a "clean" data set saved into parquet format which became a de-facto standard for data science projects.

The next step also runs a [python script](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/train_model.py) that trains a simplistic decision tree classifier and saves it to the disk as a file.

The final step runs `jupyter nbconvert` command with [Jupyter notebook](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/slides.ipynb) as an input. This notebook has cells marked with special tags such as "Slide", "Sub-Slide", and "Fragment". Cells with those markings are then converted into corresponding slide elements with visually appealing smooth transitions. The output of this step is a single html file which is also versioned with DVC. I am using those slides routinely to show model performance analysis and the underlying research that leads to decisions such as algorithm or feature selection. For the sake of brevity of presentation I have only created two simple slides, one title and one containing visualization of the confusion matrix on the hold-out data set.

The final step is crucial as data science teams are normally preoccupied with data wrangling to such an extent that they shy away from communicating their results in a "management friendly" format. This task is normally taken over by roles such as product owner or business consultant who then spend a lot of time converting the output of Jupyter notebook to something like MS PowerPoint slides. Writing slides in Jupyter notebook empowers data scientists to present their research in a clear visually appealing format and maintain a short communication channel with stakeholders.

If you have ever struggled to maintain order in your data science workflows or found yourself repeatedly recreating results, now is the time to give tools like DVC a try. Start with small steps, and before long, you will find your workflows not only more organized but also far more impactful. Check out the repository linked above to explore this example and see how a streamlined, automated approach can revolutionize the way you communicate your data science results.

### References

- [Code repository](https://github.com/khrapovs/data-to-slides-with-dvc)
- [Data Versioning Control](https://dvc.org/)
- [Wine recognition dataset](https://scikit-learn.org/1.5/datasets/toy_dataset.html#wine-recognition-dataset)
- [Create Presentation from Jupyter Notebook](https://mljar.com/blog/jupyter-notebook-presentation/)
