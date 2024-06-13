TEXT    = 'lwthni_lnqqfw_qtb_bjnlmy_utqdstrnfq_rzqynuqjx'
ANSWER  = 'grocid gillar low weight polynomial multiples'

def word_increment(let: str, inc: int) -> str:
    num = ((ord(let) - ord('a') + inc) % (ord('z') - ord('a') + 1))
    return chr(num + ord('a'))

for i in range(27):
    decr = ''
    for let in TEXT:
        if (let == '_'):
            decr += ' '
        else:
            decr += word_increment(let, i)
    print(decr, i)

# SVAR: grocid gillar low weight polynomial multiples