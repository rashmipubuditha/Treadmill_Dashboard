'''
Pubuditha M.R.
E/18/268

'''

import math as m
# Define functions

# Calculate speed.
def speedcalc(rpm,radius):
    '''
    Calcuate the speed in 'km/h' 
    rpm value and radius in 'm'.
    '''

    Speed = radius * ((rpm * 2*m.pi)/60)
    return Speed

# FCalculate distance walked or ran
def distancecalc(rpm,radius,time):
    '''
    Calculate the distance in 'km' 
    given rpm value and radius in 'm' 
    '''
    
    Distance = speedcalc(rpm,radius) * time
    return Distance 

# Calculate calories burnt
def caloriescalc(gender,weight,height,rpm,radius, time,age):
    '''
    Calculate the calories by usin
    given rpm value, radius - 'm',time - 'minutes', weight - 'kg' and height - 'm'
    '''
    BMR_men = 88.362 + (13.397*weight) + (4.799*height/100) - (5.677*age)
    BMR_women = 447.593 + (9.247*weight) + (3.098*height/100) - (4.33*age)

    if rpm != 0:   
        # calories = ( (0.035*weight) + ((speedcalc(rpm,radius)**2/height)*0.029*weight) ) * (time/60)
        if gender == 0:  
            calories = ((speedcalc(rpm,radius))*(BMR_men/1440))*time
            return calories
        if gender == 1:  
            calories = ((speedcalc(rpm,radius))*(BMR_women/1440))*time
            return calories
    else:
        calories = 0
        return calories
    

# # Calculate nomber of steps taken
# def stepscalc(height,rpm,radius,time):
#     '''
#     Calcutale the steps by using given rpm value, 
#     radius - 'm', time - 'minutes' and height - 'm'
#     '''
#     gap = (height*0.413)
#     steps = distancecalc(rpm,radius,time)/gap
#     return steps


# def new_motor_variable(speed,radius):
#     new_rpm=(speed*(5/18))*60/(radius*2*m.pi)
#     return new_rpm
