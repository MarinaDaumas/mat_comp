"""
 0 --> positivo; 1 --> negativo
  O tipo de arrendondamento será sempre para baixo, isto é, por abandono dos bits que excedam o tamanho da mantissa. Entretanto, durante a operação, mantenha todos os bits e apenas abandone bits ao devolver o resultad
inputs:
[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0] e [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0] e [1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0] e [0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0]
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] e [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] e [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] e [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]
"""

def test():

    result_1 =  0.3-0.2-0.1 
    result_2 = 0.3-(0.2+0.1)
    return result_1, result_2
    

class TooComplexCalculator():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def is_zero(self):
        """
        Procura valores iguais a zero nos vetores 1 e 2
        """
        if sum(self.num_1) == 0 and sum(self.num_2) == 0:
            return 1
        elif sum(self.num_1) == 0:
            return 1
        elif sum(self.num_1) == 0:
            return 2
        else:
            return 0

    def to_decimal_minus_64(self, bin_num):
        """
        Calcula o valor do expoente em decimal
        """
        decimal = 0
        for i in range(len(bin_num)):
            if bin_num[-i-1] == 1:
                decimal += 2**i
        
        minus_64 = decimal - 64   
        return minus_64 

    def to_binary_plus_64(self, num, change_exp):
        """
        Calcula o valor do expoente em binário
        """
        if change_exp:
            num += 1

        num += 64
        binary = bin(num)[2:]
        for item in binary: item = int(item)

        return binary   
        

    def exponentiate_mantissa(self, mant, dif):
        """
        Adiciona zeros à esquerda para diminuir o valor da mantissa de menor exponencial
        """
        complete_mant = []
        for i in range(dif): complete_mant.append(0)
        complete_mant.append(1)
        for i in mant: complete_mant.append(mant[i])

        return complete_mant

    def complete_mantissa(self, mant, comp):
        """
        Iguala o comprimento da mantissa de maior valor ao da menor 
        """
        complete_mant = [1]
        for i in mant: complete_mant.append(mant[i])
        for i in range(comp): complete_mant.append(0)

        return complete_mant

    def eq_exponent(self):
        """
        Iguala o exponencial dos números
        """
        exp_1 = self.num_1[1:8]
        mantissa_1 = self.num_1[8:]
        exp_2 = self.num_2[1:8]
        mantissa_2 = self.num_2[8:]
        
        self.exp_1 = self.to_decimal_minus_64(exp_1)
        self.exp_2 = self.to_decimal_minus_64(exp_2)
  
        if self.exp_1 > self.exp_2:
            mantissa_2 = self.exponentiate_mantissa(mantissa_2, self.exp_1-self.exp_2)
            mantissa_1 = self.complete_mantissa(mantissa_1, self.exp_1-self.exp_2)
            exp  = self.exp_1

        else:
            mantissa_1 = self.exponentiate_mantissa(mantissa_1, self.exp_2-self.exp_1)
            mantissa_2 = self.complete_mantissa(mantissa_2, self.exp_2-self.exp_1)
            exp  = self.exp_2

        return mantissa_1, mantissa_2, exp

    def binary_sum(self, mant_1, mant_2):
        """
        Soma bit a bit com carry. Avisa caso o carry out seja 1
        """
        change_exp = False
        carry = 0 
        result = []
        for i in range(len(mant_1)): result.append(0) 

        for i in range(len(mant_1)):
            if (mant_1[-i-1] + mant_2[-i-1] + carry) == 3:
                result[-i-1] = 1
                carry = 1
            
            elif (mant_1[-i-1] + mant_2[-i-1] + carry) == 2:
                result[-i-1] = 0
                carry = 1

            elif (mant_1[-i-1] + mant_2[-i-1] + carry) == 1:
                result[-i-1] = 1
                carry = 0

            else:
                result[-i-1] = 0
                carry = 0  

        if carry == 1:
            result.insert(0, 1)
            change_exp = True

        return result, change_exp

    def complemento_2(self, num):
        """
        Transforma um número negativo em seu complemento a 2
        """
        one = []
        for i in range(len(num)-1): one.append(0)
        one.append(1)

        for item in num:
            if item == 1:
                item = 0
            else:
                item = 1
    
        return self.binary_sum(num, one)

    def calcula(self):
        """
        Função principal
        """

        zeros = self.is_zero()
        if zeros == 1:
            return self.num_2
        elif zeros == 2:
            return self.num_1

        mantissa_1, mantissa_2, exp = self.eq_exponent()
        print(mantissa_1, mantissa_2, exp)
        if self.num_1[0] != self.num_2[0]:
            if self.exp_1 > self.exp_2:
                mantissa_2 = self.complemento_2(mantissa_2)
                signal = self.num_1[0]

            elif self.exp_1 > self.exp_2:
                mantissa_1 = self.complemento_2(mantissa_1)
                signal = self.num_2[0]

            elif mantissa_1 > mantissa_2:
                mantissa_2 = self.complemento_2(mantissa_2)
                signal = self.num_1[0]

            else:
                mantissa_1 = self.complemento_2(mantissa_1)
                signal = self.num_2[0]
        else: 
            signal = self.num_2[0]

        result, change_exp = self.binary_sum(mantissa_1, mantissa_2)
        print(result, change_exp)
        binary_exp = self.to_binary_plus_64(exp, change_exp)
        final_result = [signal] 

        for i in range(7): final_result.append(binary_exp[i])
        
        for i in range(8): final_result.append(result[i+1]) #pula o primeiro 1

        print(final_result)
        return final_result
       

calculator = TooComplexCalculator([0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0], [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
calculator.calcula()
#calculator.exponentiate_mantissa([0,0,0,0,0,0,0,0], 4)

