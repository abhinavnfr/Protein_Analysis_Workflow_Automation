# -*- coding: utf-8 -*-
"""fetch_FASTA_sequence.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UwdB5D-T7TTHxU8Cynx-OLjgPwaLoF3U
"""



from Bio import Entrez, SeqIO

def retrieve_fasta(accession):
    """
    Retrieves a FASTA sequence from the NCBI database.

    Parameters:
    accession (str): Accession number of the sequence.

    Returns:
    str: FASTA sequence.
    """
    Entrez.email = "abhinavrana18july@gmail.com"  # Replace with your email

    # Search for the accession in the NCBI database
    try:
        handle = Entrez.efetch(db="protein", id=accession, rettype="fasta", retmode="text")
        record = handle.read()
        handle.close()
        return record
    except Exception as e:
        return f"Failed to retrieve {accession}: {str(e)}"

def fetch_fasta_main(uploaded_file):
    if uploaded_file is not None:
        try:
            # Read accession numbers from the uploaded file
            accessions = [line.strip() for line in uploaded_file.read().decode("utf-8").splitlines()]
        except Exception as e:
            st.error("Error reading the file. Please ensure it is a text file containing accession numbers.")
            return None

        # Retrieve the FASTA sequences
        results = {}
        for accession in accessions:
            results[accession] = retrieve_fasta(accession)

        # Save the retrieved sequences to a temporary file
        output_file_path = 'sequences.fasta'
        with open(output_file_path, 'w') as file:
            for accession, sequence in results.items():
                file.write(sequence + '\n')

        return output_file_path 

# if __name__ == "__main__":
    # fetch_fasta_main()
