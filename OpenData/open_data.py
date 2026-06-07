import csv

fileCSV = open("student_placement_2026.csv")
reader = csv.DictReader(fileCSV)
    
contatore = 0
totale = 0
for riga in reader:
    totale +=1
    if float(riga["coding_skill_score"]) > 75:
        contatore +=1
        
print(contatore*100/totale)