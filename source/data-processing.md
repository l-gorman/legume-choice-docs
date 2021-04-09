# Data Processing

The data-processing is done using a series of python scripts. These can be accessed {{ '[here]({}{})'.format(githubBase,dataProcessingRepo) }}. One script `daemon.py` listens for changes in the MongoDB database. When a change occurs, the script `FormatAllData.py` is run to reformat the data, and generate a series of CSVs. These CSVs are then made available for download through folders on the linux virtual machine (see [server description](nginx.md)).

To run this script locally, and produce modified outputs, ensure the requirements are installed (see `requirments.txt`), then run the command `python3 FormatAllData.py`. The python daemon is daemonized using systemd.
