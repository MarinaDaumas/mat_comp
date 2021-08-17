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
        binary = bin(num)[2:] #pula casas que n são o numero

        bin_2 = []
        for item in binary: # transforma em lista de ints
            bin_2.append(int(item)) 
        
        while len(bin_2) < 7: bin_2.insert(0, 0)

        return bin_2   
        

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

        while len(result) < (len(mant_1)): 
            result.append(0) 

        i = len(mant_1) - 1

        while i in range(len(mant_1)):            
            if (mant_1[i] + mant_2[i] + carry) == 3:
                result[i] = 1
                carry = 1
            
            elif (mant_1[i] + mant_2[i] + carry) == 2:
                result[i] = 0
                carry = 1

            elif (mant_1[i] + mant_2[i] + carry) == 1:
                result[i] = 1
                carry = 0

            else:
                result[i] = 0
                carry = 0  
            
            i -= 1

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
    
        return self.binary_sum(num, one)[0] # only takes result argument

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

        if self.num_1[0] != self.num_2[0]:
            if self.exp_1 > self.exp_2:
                mantissa_2 = self.complemento_2(mantissa_2)
                signal = self.num_1[0]

            elif self.exp_1 < self.exp_2:
                mantissa_1 = self.complemento_2(mantissa_1)
                signal = self.num_2[0]

            elif mantissa_1 > mantissa_2:
                mantissa_2 = self.complemento_2(mantissa_2)
                signal = self.num_1[0]

            elif mantissa_1 < mantissa_2:
                mantissa_1 = self.complemento_2(mantissa_1)
                signal = self.num_2[0]

            else:
                return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        else: 
            signal = self.num_2[0]
            
        
        result, change_exp = self.binary_sum(mantissa_1, mantissa_2)

        binary_exp = self.to_binary_plus_64(exp, change_exp)

        final_result = [signal] 
        for i in range(7): final_result.append(binary_exp[i])
        for i in range(8): final_result.append(result[i+1]) #pula o primeiro 1

        return final_result

lista_1 = eval(input("Insira lista 1: ", ))
lista_2 = eval(input("Insira lista 2: ", ))

calculator = TooComplexCalculator(lista_1, lista_2)
print("Resultado: "calculator.calcula())


