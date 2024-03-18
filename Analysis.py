

def player_analysis_mean(stats):

    stats_sum = sum(stats)

    avg_stats = stats_sum / len(stats)

    return avg_stats

def player_analysis_frequency(stats):

    frequency = {
        "0-5": 0,
        "5-10": 0,
        "10-15": 0,
        "15-20": 0,
        "20-25": 0,
        "25-30":0,
        "30+":0
    }

    for stat in stats:
        if stat >= 30:
            frequency["30+"] += 1
        elif stat >= 25:
            frequency["25-30"] += 1
        elif stat >= 20:
            frequency["20-25"] += 1
        elif stat >= 15:
            frequency["15-20"] += 1
        elif stat >= 10:
            frequency["10-15"] += 1
        elif stat >= 5:
            frequency["5-10"] += 1
        else:
            frequency["0-5"] += 1

    return frequency

def player_analysis_frequency_percentage(frequency):
    frequency_sum = sum(frequency)
    list_freq = [frequency['30+'], frequency['25-30'], frequency['20-25'], frequency['15-20'], frequency['10-15'], frequency['5-10'], frequency['0-5']]
