from cs50 import get_string


while True:
    ccNum = get_string("Number: ")
    if ccNum.isdigit():
        break


ccArr = list(ccNum)

val0 = []
val1 = []


if len(ccArr) < 13 or len(ccArr) > 16:
    print('INVALID')


else:

    for i in range(len(ccArr) - 2, -1, -2):
        tmpInt = int(ccArr[i]) * 2


        if tmpInt > 9:
            tmpStr = str(tmpInt)
            tmpArr = list(tmpStr)
            tmpProd = int(tmpArr[0]) + int(tmpArr[1])
            val0.append(tmpProd)
        else:
            val0.append(int(ccArr[i]) * 2)


    for i in range(len(ccArr) - 1, -1, -2):
        val1.append(int(ccArr[i]))
    ver = sum(val1) + sum(val0)

    if ver % 10 == 0:

        if len(ccArr) == 16 and int(ccArr[0]) == 5 and int(ccArr[1]) >= 1 and int(ccArr[1]) <= 5:
            print('MASTERCARD')

        elif len(ccArr) == 15 and int(ccArr[0]) == 3 and int(ccArr[1]) == 7 or int(ccArr[1]) == 4:
            print('AMEX')

        elif int(ccArr[0]) == 4:
            print('VISA')

        else:
            print('INVALID')

    else:
        print('INVALID')
