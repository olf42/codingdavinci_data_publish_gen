# Coding Da Vinci Data Presentation Generator

Coding Da Vinci Data Presentation Generator is a tool to ease the maintenance of data 
entries on the coding da vinci website.

## Installation

Please be sure to have an up-to-date Python3 version installed on your computer.
Compatibility with Python2 is not tested.

Install all required packages from the requirements file.

```bash
$ pip install -r requirements.txt
```

## Usage

1.  Create some data entries, e.g. by copying the example.yaml and follow 
    the instructions and comments in the file.
        
    Please be sure, to change the _build_ variable to "true".
    
    ```yaml
    build: true
    ```
 
2.  Run the build script

    ```bash
    $ python3 generate_website_content.py <build_dir> <template_file> <data_dir>
    ```

3. Copy the generated code block into the _daten.html_ file in the _codingdavinci.de_ repo.


## Author

F. Rämisch <raemisch@ub.uni-leipzig.de>


## Copyright

2018, Universitätsbibliothek Leipzig