#progrm to calculate gross sal from basic saL
basic_sal=int(input('enter basic sal -  '))
TA=(40*basic_sal)/100
HRA=(30*basic_sal)/100
DA=(20*basic_sal)/100
gross_sal=basic_sal+(TA+HRA+DA)
print(gross_sal)
