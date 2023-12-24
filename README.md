# K-Mer Finder

## Background

This project focuses on a Python script designed to identify repeating k-mers in a given nucleotide sequence obtained from the NCBI Nucleotide database. The script utilizes the NCBI E-Utilities API to fetch the nucleotide sequence corresponding to a provided NCBI Reference Sequence ID. It then identifies and prints the repeating k-mers in the sequence.

## Data Source

The nucleotide sequences are fetched from the [NCBI Nucleotide database](https://www.ncbi.nlm.nih.gov/nucleotide/). The script uses the NCBI E-Utilities API to retrieve the sequences based on the provided NCBI Reference Sequence ID.

## Requirements

- Run the command below to install the required packages

    ```python
    pip install -r requirements.txt
    ```

- An Internet connection is required to run the application (for retrieving the data from the NCBI database)

## How to run the script

```bash
python kmer_finder.py
```

## Contributing

We welcome contributions! For bug fixes, issues or suggestions. If you find a bug, have a feature request, or want to improve the code, please feel free to open an issue or submit a pull request. Ensure to follow the contribution guidelines specified in the repository under the [LICENSE](LICENSE) section.

## License

This project is licensed under the MIT License. For details, refer to the [LICENSE](LICENSE) file.

Copyright (c) 2023 Saksham Kumar
