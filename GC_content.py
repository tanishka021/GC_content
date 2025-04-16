s= """>Rosalind_1
AGCTATAG
>Rosalind_2
CGTAGCGC"""
def parse_content(data):
    seq={}
    label=""
    for line in data.strip().splitlines():
        if line.startswith(">"):
            label=line[1:]
            seq[label]=""
        else :
            seq[label] += line.strip()     
    return seq

seqs= parse_content(s)
print(seqs)

def GC_content(seq):
    gc = seq.count("G") + seq.count("C")
    d= len(seq)
    GC_con = (gc * 100 )/ d

    
    return GC_con

max_id = ""
max_gc= 0

for id, seq in seqs.items():
    gc=GC_content(seq)
    if gc> max_gc :
        max_gc=gc
        max_id=id
print(max_gc)

print(max_id)