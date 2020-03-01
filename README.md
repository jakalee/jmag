# jmag and util~
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jakalee/jmag/master?urlpath=lab)

## Running the code on your computer

1. [**Install** git](https://git-scm.com/downloads).

2. [**Download and install** Anaconda](https://www.anaconda.com/download/): choose the **Python 3.6, 64-bit** version for your operating system (macOS, Linux, or Windows).

3. **Open** a terminal (`cmd` on Windows).

4. **Clone** the repository:

```bash
$ git clone https://github.com/ipython-books/cookbook-2nd-code.git
$ cd cookbook-2nd-code
```

5. **Create** the `cookbook` [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file):

```bash
conda env create -f environment.yml
```

6. **Activate** the environment:

    * On macOS and Linux:

    ```bash
    source activate cookbook
    ```

    * On Windows:

    ```bash
    activate cookbook
    ```

7. **Launch** the [Jupyter Notebook](http://jupyter.org/install.html):

```bash
$ jupyter notebook
```
