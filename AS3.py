def to_decimal_mant(bin_num):
    bin_num.insert(0, 1)
    decimal = 0
    for i in range(len(bin_num)):
        decimal += bin_num[i]*2**-i  
    return decimal 
  
def to_decimal_exp(bin_num):
    decimal = 0
    for i in range(len(bin_num)):
        decimal += bin_num[-1-i]*2**i  
    return decimal -64

def fp24tofloat64(L):
  if sum(L) == 0:
    return(float(0))
  
  signal = L[0]
  exp = L[1:8]
  mantissa = L[8:]

  mantissa = to_decimal_mant(mantissa)
  exp = to_decimal_exp(exp)
  result = float(mantissa*2**exp)

  if signal == 1:
    return 0 - result
  if signal == 0:
    return result
 
  