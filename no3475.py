import pandas as pd
'''
+-----------+------------------+-----------+
| sample_id | dna_sequence     | species   |
+-----------+------------------+-----------+
| 1         | ATGCTAGCTAGCTAA  | Human     |
| 2         | GGGTCAATCATC     | Human     |
| 3         | ATATATCGTAGCTA   | Human     |
| 4         | ATGGGGTCATCATAA  | Mouse     |
| 5         | TCAGTCAGTCAG     | Mouse     |
| 6         | ATATCGCGCTAG     | Zebrafish |
| 7         | CGTATGCGTCGTA    | Zebrafish |
+-----------+------------------+-----------+
'''

samples = pd.DataFrame({
	'sample_id': [1, 2, 3, 4, 5, 6, 7],
	'dna_sequence': ['ATGCTAGCTAGCTAA', 'GGGTCAATCATC', 'ATATATCGTAGCTA', 'ATGGGGTCATCATAA', 'TCAGTCAGTCAG', 'ATATCGCGCTAG', 'CGTATGCGTCGTA'],
	'species': ['Human', 'Human', 'Human', 'Mouse', 'Mouse', 'Zebrafish', 'Zebrafish']
})

samples['has_start'] = samples['dna_sequence'].str.startswith('ATG').astype(int)
samples['has_stop'] = samples['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA')).astype(int)
samples['has_atat'] = samples['dna_sequence'].str.contains('ATAT').astype(int)
samples['has_ggg'] = samples['dna_sequence'].str.contains('GGG').astype(int)
result = samples.sort_values(by='sample_id').reset_index(drop=True)
print(result)