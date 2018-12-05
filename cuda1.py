import os

# print(1)
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer SGDM --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> SGDM_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer SGDM --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> SGDM_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer SGDM --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> SGDM_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer SGDM --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> SGDM_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer SGDM --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> SGDM_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer SGDM --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> SGDM_esno20.txt')
#
#
# print(2)
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer NAG --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> NAG_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer NAG --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> NAG_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer NAG --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> NAG_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer NAG --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> NAG_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer NAG --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> NAG_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer NAG --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> NAG_esno20.txt')


# print(3)
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> Adam_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> Adam_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> Adam_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> Adam_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> Adam_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> Adam_esno20.txt')


print(3)
os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation elu '
          '--root D:/qpsk_awgn_sps8_esno10.dat >> adamax_elu_qpsk_esno10.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation elu '
          '--root D:/qpsk_awgn_sps8_esno12.dat >> adamax_elu_qpsk_esno12.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation elu '
          '--root D:/qpsk_awgn_sps8_esno14.dat >> adamax_elu_qpsk_esno14.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation elu '
          '--root D:/qpsk_awgn_sps8_esno16.dat >> adamax_elu_qpsk_esno16.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation elu '
          '--root D:/qpsk_awgn_sps8_esno18.dat >> adamax_elu_qpsk_esno18.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation elu '
          '--root D:/qpsk_awgn_sps8_esno20.dat >> adamax_elu_qpsk_esno20.txt')

print(4)
os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno10.dat >> adamax_prelu_qpsk_esno10.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno12.dat >> adamax_prelu_qpsk_esno12.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno14.dat >> adamax_prelu_qpsk_esno14.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno16.dat >> adamax_prelu_qpsk_esno16.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno18.dat >> adamax_prelu_qpsk_esno18.txt')

os.system('python resnet_roll_off.py --cuda 1 --arch resnet18 --optimizer Adamax --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno20.dat >> adamax_prelu_qpsk_esno20.txt')



