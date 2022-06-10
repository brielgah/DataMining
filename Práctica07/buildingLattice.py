
# A Python program to print all
# combinations of a given length
from itertools import combinations

dimensions = ['fechaId','edoCivilId','edadId', 'educacionId', 'ocupacionId', 'religionId', 'parentescoId', 'estadoResidenciaId', 'municipioResidenciaId', 'menstuacionId', 'edadSexualId', 'numeroAbortosId', 'numeroPartosId', 'anticonceptivoId', 'complicacionId','anticonceptivoPostId', 'cluesId', 'procileId', 'ilePreviosId']

table = "hechos"
measure = 'COUNT(*) as cantidad'

for i in range(1,len(dimensions)+1):
    allCombinations = combinations(dimensions, i)
    # Print the obtained combinations
    combQuery = ""
    for combination in allCombinations:
        combQuery = ""
        for item in combination:
            combQuery+=item
            combQuery+=','
        combQueryTemp = combQuery[0:len(combQuery)-1]
        print(f"SELECT {measure},{combQueryTemp} from {table} group by {combQueryTemp} order by cantidad;")
