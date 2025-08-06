def proteins(strand):
       key = {'AUG':'Methionine',
              'UUU':'Phenylalanine','UUC':'Phenylalanine', 
              'UUA':'Leucine', 'UUG':'Leucine', 
              'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine', 
              'UAU':'Tyrosine', 'UAC':'Tyrosine', 
              'UGU':'Cysteine', 'UGC':'Cysteine',
              'UGG':'Tryptophan',
              'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'}
    
       proteins = []
       for i in range(0, len(strand), 3):
              codon = strand[i:i+3]
              protein = key.get(codon)
              if protein == 'STOP':
                     break
              if protein:
                     proteins.append(protein)
        
        
       return proteins
