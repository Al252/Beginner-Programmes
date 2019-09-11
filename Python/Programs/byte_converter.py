def dec_to_byte(dec_num):
    dec_arr = ['1', '0']
    if dec_num <= 255:
        for first in dec_arr:
            for second in dec_arr:
                for third in dec_arr:
                    for fourth in dec_arr:
                        for fifth in dec_arr:
                            for sixth in dec_arr:
                                for seventh in dec_arr:
                                    for eighth in dec_arr:
                                        bin_str = (first + second + third + fourth + fifth + sixth + seventh + eighth)
                                        if bin_str[0] == '1':
                                            num0 = 128
                                        else:
                                            num0 = 0
                                        if bin_str[1] == '1':
                                            num1 = 64
                                        else:
                                            num1 = 0
                                        if bin_str[2] == '1':
                                            num2 = 32
                                        else:
                                            num2 = 0
                                        if bin_str[3] == '1':
                                            num3 = 16
                                        else:
                                            num3 = 0
                                        if bin_str[4] == '1':
                                            num4 = 8
                                        else:
                                            num4 = 0
                                        if bin_str[5] == '1':
                                            num5 = 4
                                        else:
                                            num5 = 0
                                        if bin_str[6] == '1':
                                            num6 = 2
                                        else:
                                            num6 = 0
                                        if bin_str[7] == '1':
                                            num7 = 1
                                        else:
                                            num7 = 0
                                        if (num0 + num1 + num2 + num3 + num4 + num5 + num6 + num7) == dec_num:
                                            msg = 'Binary Equivalent: ' + bin_str
                                                
    else:
        msg = 'Number cannot be converted into a byte\nShould be less than or equal to 255.'
    return msg


try:
    print(dec_to_byte(int(input('Decimal Number: '))))
except Exception:
    print('Invalid Number')
