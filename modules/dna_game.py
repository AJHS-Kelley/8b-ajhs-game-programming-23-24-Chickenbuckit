# casey boyce v0.5, code fix?
import time, datetime
from random import choice

def gen_dna() -> str:
   bases_generated = 0
   bases_reqested = int(input("please enter a positeve integer number of bases to generate.\n"))

def do_transcrition(dna_sequence: str) -> tuple:

   print(f"the DNA sequence is {dna_sequence}\n")
   print("You will now generate the RNA sequence that that would match.\n")
   print("Please remember, in the DNA seqence A pairs with U from the DNA sequence.\n")
   rna_start = time.time()
   rna_sequence = input("Please enter the matching RNA sequence. Leave no spaces!\nThen press enter\n").upper
   rna_stop = time.time()
   rna_time = rna_stop - rna_stop
   return (rna_sequence, rna_time)

def verify_sequence(dna_sequence: str, rna_sequence: str) -> bool:
    is_mach = False
    if len(dna_sequence) != len(rna_sequence):
        print("Sorry mate but the length of the DNA dose not match the length of the RNA")
        return is_mach
    for dna_bace, rna_bace in zip(dna_sequence, rna_sequence):
        if dna_bace == "A" and rna_bace == "U":
           is_mach = True 
        elif dna_bace == "C" and rna_bace == "G":
           is_mach = True 
        elif dna_bace == "G" and rna_bace == "C":
           is_mach = True 
        elif dna_bace == "T" and rna_bace == "A":
           is_mach = True 
        else:
           print("Sorry mate but I could'nt find wach ya needed.\n")
    return is_mach

def calc_score(rna_sequence: str, rna_time: float) -> int :
    score = 0
    if rna_time < 1.0:
      score += 99999999
    elif rna_time < 5.0:
      score += 900000
    elif rna_time < 7.5:
      score += 500000
    else:
       score += 250000

    score_multi = 0.0
    if len(rna_sequence) >= 30:
       score_multi = 5.0
    elif len(rna_sequence) >= 25:
       score_multi = 4.0
    elif len(rna_sequence) >= 20:
       score_multi = 3.0
    elif len(rna_sequence) >= 15:
       score_multi = 2.0
    elif len(rna_sequence) >= 10:
       score_multi = 1.0
    else:
       print("mate your gonna need to stop being a wuss if you want a higher score")
       score_multi = 0.25
    score *= score_multi
    return score

def save_score(dna_sequence: str, rna_sequence: str, rna_time: float, score: int) -> None:
   player_first_name = input("Please enter your first name")
   player_last_name = input("Please enter your last name")
   full_name = player_first_name + " " + player_last_name

   file_name = "dna_replicantion_score" + full_name + ".txt"
   save_data = open(file_name, "a")
   #file modes
   # "x" mode -- create file -- errors if file is allredy created
   # "w" mode -- creates file -- overrights if allredy created
   # "a" mode -- creates file -- adds info allredy created
   save_data.write(f"Dna sequence :{dna_sequence}\nRna sequence : {rna_sequence}\n")
   save_data.write(f"Transcription Time: {rna_time}\n")
   save_data.write(f"Score : {score}\n")
   save_data.write(f"{full_name}\n")
   save_data.write(f"{datetime.dateTime.now()}\n")
   save_data.close()



dna = gen_dna()
rna = do_transcrition(dna)
if verify_sequence(dna, rna[0]):
   score = (calc_score(rna[0], rna[1]))
   save_score(dna, rna[0], rna[1], score)