from PIL import Image
import numpy as np




def bitplanes(im):
    im = Image.open(im)
    data = np.array(im)
    out = []
    # create an image for each k bit plane
    for k in range(7,-1,-1):
    # extract kth bit (from 0 to 7)
        res = data // 2**k & 1
        out.append(res*255)
    # stack generated images
    b = np.hstack(out)
    return Image.fromarray(b)
number = 0
tested = 0




def take_number():
    number = input()
    if number=='think_different':
        return 1212316
    else:
        try:
            number = int(number)
            if number>0 and number<16:
                return number
            else:
                print("Тут должно быть валидное число")
                print('Выбери номер картинки')
                take_number()
        except:
            print("Тут должно быть число")
            print('Выбери номер картинки')
            take_number()


def show_image(numbers):
    if numbers==1:
        bitplanes("/content/ccc-part2-qqq-try/image1.png").show()
    if numbers==2:
        bitplanes("/content/ccc-part2-qqq-try/image2.png").show()
    if numbers==3:
        bitplanes("/content/ccc-part2-qqq-try/image3.png").show()
    if numbers==4:
        bitplanes("/content/ccc-part2-qqq-try/image4.png").show()
    if numbers==5:
        bitplanes("/content/ccc-part2-qqq-try/image5.png").show()
    if numbers==6:
        bitplanes("/content/ccc-part2-qqq-try/image6.png").show()
    if numbers==7:
        bitplanes("/content/ccc-part2-qqq-try/image7.png").show()
    if numbers==8:
        bitplanes("/content/ccc-part2-qqq-try/image8.png").show()
    if numbers==9:
        bitplanes("/content/ccc-part2-qqq-try/image9.png").show()
    if numbers==10:
        bitplanes("/content/ccc-part2-qqq-try/image10.png").show()
    if numbers==11:
        bitplanes("/content/ccc-part2-qqq-try/image11.png").show()
    if numbers==12:
        bitplanes("/content/ccc-part2-qqq-try/image12.png").show()
    if numbers==13:
        bitplanes("/content/ccc-part2-qqq-try/image13.png").show()
    if numbers==14:
        bitplanes("/content/ccc-part2-qqq-try/image14.png").show()
    if numbers==15:
        bitplanes("/content/ccc-part2-qqq-try/image15.png").show()



if tested==0:
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1


if tested==1:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==2:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==3:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==4:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==5:
    print('Повторять одни и те же действия - безумие!')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==6:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==7:
    print('Правильно (нет)')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==8:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==9:
    print('Иногда неплохо сделать перерыв для иновационных идей')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==10:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==11:
    print('В некоторых ситуациях остаётся только поступать иначе')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==12:
    print('Неправильно')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1

if tested==13:
    print('Возможен бан')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==14:
    print('Бан?')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
if tested==15:
    print('Бан!?!?')
    print('Выбери номер картинки')
    number = take_number()
    if number==1212316:
        print("И это правильный ответ!")
        bitplanes("/content/ccc-part2-qqq-try/image0.png").show()
    else:
        show_image(number)
        tested+=1
