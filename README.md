# shodan query script

##

* [Usage](#usage)

## Usage

```bash

python3 shodan_query.py -h

```

```text
Perform a Shodan query, display results, and save IP addresses to a text file.

SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'  # Replace with your Shodan API Key

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Shodan query
  -o OUTPUT, --output OUTPUT
                        Output file name (default: shodan_results.txt)

Please make sure that you are using a valid Shodan API Key

SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'  # Replace with your Shodan API Key

```
Example:

```shell

python3 shodan_query.py -q 'product:xxxxx'

```
