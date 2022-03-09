[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# NerdyLib-Docs

<!-- PROJECT LOGO -->
[<img src="assets/img/687vex_logo.png" align="right" width="150">](https://github.com/687vex/NerdyLib-Docs)

The official documentation for NerdyLib

<!-- BUILT WITH -->
### Built With

- Python 3:
  - sphinx
  - furo
    - myst-parser
    - sphinx-favicon
- Visual Studio Code

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
    git clone https://github.com/687vex/NerdyLib-Docs.git
    ```
2. Install project requirments (administrator permissions may be required)
    ```sh
    pip install -r requirements.txt
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

## Structure

- `docs/index.rst` - index file restructured text
- `docs/*.md` - myST markdown files (new ones should be added to the `index.rst` table of contents)
- `docs/conf.py` - site configuration (only modified when absolutely necessary)


<!-- CONTRIBUTING -->
## Contributing

Contributions are always welcome! Please create a Pull Request and include a description of how your Pull Request will improve the overall robot code and what it does.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

This project is licensed under the [TBD]() License. See `LICENSE.txt` for more information.

<!-- SUPPORT US -->
## Support Us!

Give this repo a ⭐️ if you found this project helpful!

## Acknowledgments

- [othneildrew's Best README Template](https://github.com/othneildrew/Best-README-Template)
- [PROS 3 Documentation](https://pros.cs.purdue.edu/v5/index.html)
- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
- [GitHub Pages with Python Sphinx](https://github.com/peaceiris/test-sphinx)
- Documentation formatting heavily inspired by [DeepwaterExploration/DeepwaterExplorationDocs](https://github.com/DeepwaterExploration/DeepwaterExplorationDocs)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/687vex/NerdyLib-Docs.svg?style=for-the-badge
[contributors-url]: https://github.com/687vex/NerdyLib-Docs/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/687vex/NerdyLib-Docs.svg?style=for-the-badge
[forks-url]: https://github.com/687vex/NerdyLib-Docs/network/members
[stars-shield]: https://img.shields.io/github/stars/687vex/NerdyLib-Docs.svg?style=for-the-badge
[stars-url]: https://github.com/687vex/NerdyLib-Docs/stargazers
[issues-shield]: https://img.shields.io/github/issues/687vex/NerdyLib-Docs.svg?style=for-the-badge
[issues-url]: https://github.com/687vex/NerdyLib-Docs/issues
[license-shield]: https://img.shields.io/github/license/687vex/NerdyLib-Docs.svg?style=for-the-badge
[license-url]: https://github.com/687vex/NerdyLib-Docs/blob/master/LICENSE.txt
