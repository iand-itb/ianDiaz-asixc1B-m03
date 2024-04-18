import statistics
import os

statsFile = os.path.join('.', 'student2.stats')

def getStats():
    if os.path.exists(statsFile):
        if os.path.isfile(statsFile):
            if os.access(statsFile, os.R_OK):
                with open(statsFile, 'r') as file:
                    stats = file.read()
                stats = stats.split()
                stats = [int(num) for num in stats if num.isdigit()]
    return stats

def getMinGrade(stats):
    minGrade = min(stats)
    return minGrade

def getMaxGrade(stats):
    maxGrade = max(stats)
    return maxGrade

def getMeanGrade(stats):
    return statistics.mean(stats)

stats = getStats()
print(f'Nota mínima: {getMinGrade(stats)}')
print(f'Nota máxima: {getMaxGrade(stats)}')
print(f'Nota mitjana: {getMeanGrade(stats)}')