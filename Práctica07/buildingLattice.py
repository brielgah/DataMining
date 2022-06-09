# A Python program to print all
# combinations of a given length
from itertools import combinations

dimensions = ['fechaID','edoCivilId','edadId', 'derechoHabienteId', 'educacionId', 'ocupacionId', 'religionId', 'parentescoId', 'estadoResidenciaId', 'municipioResidenciaId', 'menstuacionId', 'edadSexualId', 'semanasGestacionId', 'numeroAbortosId', 'numeroPartosId', 'numeroCesareaId']

table = "ingresosMetro"
measure = 'AVG(ingreso)'

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
        print(f"SELECT {measure},{combQueryTemp} from {table} group by {combQueryTemp};")
