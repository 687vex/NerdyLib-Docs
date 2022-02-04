# NerdyLib-Docs


<!-- BUILT WITH -->
### Built With

- Python 3:
  - sphinx
  - furo
    - myst-parser
    - sphinx-favicon

# How to Use NerdyLib-Docs

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

- Working Python 3 >= 3.9.0 installation
  - [pip](https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/) is working

- Visual Studio Code
  - [MyST-Markdown](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) Extension
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) Extension

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/687vex/  NerdyLib-Docs.git
    ```
2. Install Python packages
    ```sh
    pip install -U sphinx
    pip install furo
    pip install myst-parser
    pip install sphinx-favicon
    ```
### Development Server

1. Move to the root directory: 
    ```sh
    cd NerdyLib-Docs
    ```
2. Run the live server: 
    ```sh
    sphinx-autobuild source build
    ````
    When a change is detected in `source/`, the documentation is rebuilt and any open browser windows are reloaded automatically. `KeyboardInterrupt` (<kbd>ctrl</kbd>+<kbd>c</kbd>) will stop the server.
3. Open the browser to view the local server: 
    ```sh
    http://localhost:8000/
    ```