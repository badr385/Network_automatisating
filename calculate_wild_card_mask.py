#enter for exemple /26 -> return result on 255.255.255.192
mask_short = int(input('Enter ur mask info: '))
def transform_number_to_mask(number):
#Calculate fourth octet 255.255.255.x
        if number > 23:
                mask_number = 32 - number
                powers_of_number = 2 ** mask_number
                mask_of_ip = 256 - powers_of_number
                print(mask_of_ip)
                print('255.255.255.' + str(mask_of_ip))
#Calculate third octet 255.255.x.0
        elif 16 <= number <= 24:
                mask_number = 32 - number
                second_digit_number = mask_number - 8
                powers_of_number = 2 ** second_digit_number
                mask_of_ip = 256 - powers_of_number
                print('255.255.' + str(mask_of_ip) + '.0')
 #Calculate third octet 255.x.0.0                     
        elif 8 <= number <= 16 :
                mask_number = 32 - number
                second_digit_number = mask_number - 16
                powers_of_number = 2 ** second_digit_number
                mask_of_ip = 256 - powers_of_number
                print('255.' + str(mask_of_ip) + '.0.0')
#Calculate first octet x.0.0.x
        elif 0 <= number <= 8:
                mask_number = 32 - number
                second_digit_number = mask_number - 24
                powers_of_number = 2 ** second_digit_number
                mask_of_ip = 256 - powers_of_number
                print(str(mask_of_ip) + '.0.0.0')
        else:
                print(f'Number {number} entered not valid ')

transform_number_to_mask(mask_short)
                      
#try it, it's very useful, u can use it to find ur mask of an ip, where have only /24 /26, etcccccccc
