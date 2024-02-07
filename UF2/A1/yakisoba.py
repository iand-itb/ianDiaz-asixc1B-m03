from time import sleep
# region Declaració de funcions
def recopilar_ingredients():
    print('1.Recopilar ingredients')
    print('\tComprar al supermercat.')
    print('\tDisposar sobre el marbre.')
    sleep(1)
def cuinar_tallarines():
    print('2.Cuinar tallarines')
    print('\tPreparar aigua.')
    print('\t\tEscalfar aigua.')
    print('\t\tPosar-hi sal.')
    sleep(1)
    print('\tBullir tallarines.')
    print('\tEscórrer tallarines.')
    print('\tDeixar-les preparades.')
    sleep(1)
def cuinar_pastanagas():
    print('3.Cuinar pastanagues')
    print('\tTallar pastanagues.')
    print('\tFregir pastanagues.')
    sleep(1)
    print('\t\tPreparar paella per fregir.')
    print('\t\tRossejar pastanagues.')
    print('\t\tNetejar oli de paella.')
    sleep(1)
    print('\tDeixar pastanagues preparades.')
def cuinar_cebes():
    print('4.Cuinar cebes')
    print('\tTallar cebes.')
    print('\tFregir cebes.')
    sleep(1)
    print('\t\tPreparar paella per fregir.')
    print('\t\tRossejar cebes.')
    print('\t\tNetejar oli de paella.')
    print('\tDeixar cebes preparades.')
    sleep(1)
def preparacio_final():
    print('5.Preparació final')
    print('\tBarrejar cebes.')
    print('\tSaltar ingredients.')
    sleep(1)
    print('\t\tPreparar paella per saltar.')
    print('\t\tCuinar remenant ingredients.')
    print('\tDeixar llest per servir.')
# endregion
# region main
recopilar_ingredients()
cuinar_tallarines()
cuinar_pastanagas()
cuinar_cebes()
preparacio_final()
# endregion