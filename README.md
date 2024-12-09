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

A long time ago, when I was conducting research at university, I had to write numerous papers and prepare conference presentation slides. These were often packed with graphics, tables, and formulas. All the presentation materials came from multiple stages of data collection, transformation, and visualization. Back then, 10–15 years ago, academic research - at least in my field of economics and finance - had not yet fully embraced advancements in the IT sphere. Journals were still accepting manuscripts without requiring any supporting materials, such as versioned code or data. Needless to say, tools like Git sounded like foreign jargon. Nevertheless, for my own sanity, I did my best to maintain order in my workflow, minimizing unnecessary manual steps from raw data to a journal submission or conference presentation.

After transitioning to a career as a data scientist in the private sector, I quickly realized just how much I had missed in terms of tooling that could have simplified my life as a university researcher. Git is now an indisputable prerequisite for data scientists at any level. Data pipelining and the automation of machine learning experiments have become essential for achieving efficiency, speed, and reproducibility. Discovering the [Data Version Control (DVC)](https://dvc.org/) Python library marked the completion of my journey to versioning everything — from data and machine learning artifacts like trained models to communication media such as presentation slides for project stakeholders. In this blog post, I will demonstrate a toy example of how I organize and version a data and machine learning workflow, starting from a remote data source and ending with polished executive slides - all in a single terminal command!

### Why Versioning Matters in Data Science

In any data science project, ensuring reproducibility and traceability is critical. Data and machine learning experiment versioning are foundational practices that allow teams to maintain a clear and organized workflow, especially as projects grow in complexity. Without proper versioning, it becomes nearly impossible to track which data, code, and configurations were used to produce specific results. This can lead to wasted time, inconsistencies, and difficulty diagnosing issues when results deviate unexpectedly.

Versioning goes beyond just tracking code. It encompasses managing data transformations, model parameters, and experiment outputs in a systematic way. By using tools like DVC, teams can ensure that every step of the pipeline is reproducible and well-documented. This not only supports collaboration within the team but also builds trust with stakeholders, who gain a transparent record of how insights and models were derived. Versioning is not just about keeping things tidy - it is about ensuring the reliability and accountability of your entire data science workflow.

### Automating Communication: Slides as a Pipeline step

As a bonus, presentation slides—an unavoidable communication medium in corporate environments - can also be automatically generated and versioned alongside data and model updates. While this may seem excessive at first glance, I have found it to be a significant time saver for streamlined and effortless communication, especially with non-technical stakeholders.

### A Toy Example: Wine Dataset to Executive slides

For the sake of simplicity of the example I will be using [Wine dataset from Scikit-Learn](https://scikit-learn.org/1.5/datasets/toy_dataset.html#wine-recognition-dataset). Starting from this remotely stored data I will build a very simple but at the same time typical machine learning pipeline composed of the following steps:

1. Download data from remote storage
2. Process data.
3. Train and save machine learning model.
4. Use processed data and the trained model to evaluate model performance and generate presentation slides with nice visuals.

The self-contained code for this task is freely available in [this repository](https://github.com/khrapovs/data-to-slides-with-dvc). DVC library mentioned above is used to organize individual steps into the pipeline, version intermediate and final artifacts such as data, model, and slides. The core ingredient of the DVC is the [dvc.yaml file](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/dvc.yaml) which defines the structure of the pipeline as well as step dependencies and outputs. The pipeline is run simply by executing `dvc repro` in the terminal. After the first run of the pipeline DVC calculates and saves certain metadata for the produced artifacts. This metadata is committed to the git repository together with the code itself. This allows DVC to track the pipeline and its artifacts over time and avoid running certain steps if their inputs did not change. Output artifacts can be stored in a cloud for easy sharing with other team members and stakeholders.

#### Step 1: Download Data

The first step involves a simple `wget` command to download a CSV file from the web to the local hard drive.

#### Step 2: Process Data

The second step runs a [simple python script](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/transform_data.py) that performs some data transformations, e.g. filling in of missing values, data type conversion, etc. The end result is a "clean" data set saved into parquet format which became a de-facto standard for data science projects.

#### Step 3: Train the Model

The next step also runs a [python script](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/train_model.py) that trains a simplistic decision tree classifier and saves it to the disk as a file.

#### Step 4: Generate Presentation Slides

The final step runs `jupyter nbconvert` command with [Jupyter notebook](https://github.com/khrapovs/data-to-slides-with-dvc/blob/main/dvc/slides.ipynb) as an input. This notebook has cells marked with special tags such as "Slide", "Sub-Slide", and "Fragment". Cells with those markings are then converted into corresponding slide elements with visually appealing smooth transitions. The output of this step is a single html file which is also versioned with DVC. I am using those slides routinely to show model performance analysis and the underlying research that leads to decisions such as algorithm or feature selection. For the sake of brevity of presentation I have only created two simple slides, one title and one containing visualization of the confusion matrix on the hold-out data set.

### Why This Matters for Communication

The final step is crucial. Data science teams often focus so heavily on data wrangling that they neglect presenting their results in a “management-friendly” format. This task typically falls to roles like product owners or business consultants, who spend significant time converting raw outputs into polished presentations. Writing slides directly in Jupyter notebooks empowers data scientists to present their findings in a clear, visually appealing format and maintain short communication loops with stakeholders.

If you have ever struggled to maintain order in your data science workflows or found yourself repeatedly recreating results, now is the time to give tools like DVC a try. Start small, and soon you’ll find your workflows not only more organized but also far more impactful. Check out the repository linked above to explore this example and see how a streamlined, automated approach can transform the way you communicate your data science results.

### References

- [Code repository](https://github.com/khrapovs/data-to-slides-with-dvc)
- [Data Versioning Control](https://dvc.org/)
- [Wine recognition dataset](https://scikit-learn.org/1.5/datasets/toy_dataset.html#wine-recognition-dataset)
- [Create Presentation from Jupyter Notebook](https://mljar.com/blog/jupyter-notebook-presentation/)
