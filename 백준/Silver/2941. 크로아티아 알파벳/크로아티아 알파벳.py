croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
word = input()
word_list = list(word)

while word_list:
    if ''.join(word_list[:3]) in croatia_alpha:
        del word_list[:3]
    elif ''.join(word_list[:2]) in croatia_alpha:
        del word_list[:2]
    else:
        del word_list[:1]
    cnt += 1

print(cnt)
