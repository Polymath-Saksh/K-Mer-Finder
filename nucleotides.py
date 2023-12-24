from collections import Counter

def find_repeating_kmers(k, sequence):
    k_mers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    
    # Use Counter to count occurrences of each k-mer
    occurrences = Counter(k_mers)
    
    # Filter for k-mers that occur more than once
    repeating_kmers = {key: value for key, value in occurrences.items() if value > 1}
    
    # Sort the dictionary by occurrences in descending order
    sorted_repeating_kmers = dict(sorted(repeating_kmers.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_repeating_kmers.items():
        print(f'{key}: {value}')

import requests

def get_nucleotide_sequence(id):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "nucleotide",
        "id": id,
        "rettype": "fasta",
        "retmode": "text"
    }
    response = requests.get(base_url, params=params)
    return response.text

if __name__ == "__main__":
    nucleotide_id = input("Enter NCBI Reference Sequence id: (e.g. NM_001185097.2) :")
    k = int(input("Enter k: "))
    sequence = get_nucleotide_sequence(nucleotide_id)
    sequence = sequence.split('\n', 1)[1].replace('\n', '')

    find_repeating_kmers(k, sequence)
    