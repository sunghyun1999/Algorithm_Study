def convertDateToDays(date):
    y, m, d = map(int, date.split('.'))
    
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    term_dict = {name: int(months) for name, months in (t.split() for t in terms)}
    today_days = convertDateToDays(today)
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        if today_days >= convertDateToDays(date) + term_dict[term] * 28:
            answer.append(i + 1)
    
    return answer