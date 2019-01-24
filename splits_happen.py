'''
    Slipts Happen

    Args: Takes a string representation of a line score

    Result: Total bowling score.
'''


def splits_happen(line):
    # Translate a symbol into a numeric value for scoring
    def convert_symbol_to_score(symbol):
        if symbol == 'X':
            return 10
        elif symbol == '-':
            return 0
        elif symbol in '0123456789':
            return int(symbol)
        else:
            return 0

    '''
        Handle pairs in the case where a bowler makes 2 tries or calculating the scoring of a preceding
        strike. A spare should ALWAY be the second value in the try and can never be the first
    '''

    def calc_two_try_score(sub_line):
        if sub_line[0] and sub_line[1] == '/':
            return 10
        else:
            return convert_symbol_to_score(sub_line[0]) + convert_symbol_to_score(sub_line[1])

    total_score = 0

    '''
        Base cases:
            return a score of zero is nothing is passed
            return the integer equivalent of input if a single string is passed
            treat a two element string as a two try turn
    '''
    if len(line) == 0:
        return 0

    if len(line) == 1:
        return convert_symbol_to_score(line[0])

    if len(line) == 2:
        return calc_two_try_score(line)

    '''
        Recursively handle the scoring based on the first element
    '''

    if len(line) > 2:

        if line[0] == 'X' and len(line[1:]) >= 2:
            if len(line[1:]) == 2:  # Tenth Frame
                total_score = convert_symbol_to_score(line[0]) + calc_two_try_score(line[1:3])
            else:
                total_score = convert_symbol_to_score(line[0]) + calc_two_try_score(line[1:3]) + splits_happen(line[1:])

        if line[0] in "0123456789-" and line[1] == '/':
            if len(line[2:]) == 1:  # Tenth Frame
                total_score = calc_two_try_score(line[0:2]) + convert_symbol_to_score(line[2])
            else:
                total_score = calc_two_try_score(line[0:2]) + convert_symbol_to_score(line[2]) + splits_happen(line[2:])

        if line[0] in "0123456789-" and line[1] != '/':
            total_score = convert_symbol_to_score(line[0]) + splits_happen(line[1:])

    return total_score


if __name__ == '__main__':
    score = splits_happen(line='XXXXXXXXXXXX')
    print('input=XXXXXXXXXXXX, score=%s' % score)
    score = splits_happen(line='9-9-9-9-9-9-9-9-9-9-')
    print('input=9-9-9-9-9-9-9-9-9-9-, score=%s' % score)
    score = splits_happen(line='5/5/5/5/5/5/5/5/5/5/5')
    print('input=5/5/5/5/5/5/5/5/5/5/5, score=%s' % score)
    score = splits_happen(line='X7/9-X-88/-6XXX81')
    print('input=X7/9-X-88/-6XXX81, score=%s' % score)
    score = splits_happen(line='6/726362536/54X814/X')
    print('input=6/726362536/54X814/X, score=%s' % score)
    score = splits_happen(line='725/5/61625/7-727244-')
    print('input=725/5/61625/7-727244-, score=%s' % score)
    score = splits_happen(line='5/8/5353X6/444572X8/')
    print('input=5/8/5353X6/444572X8/, score=%s' % score)
