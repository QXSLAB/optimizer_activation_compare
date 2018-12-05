import os

# print(1)
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation elu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> elu_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation elu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> elu_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation elu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> elu_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation elu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> elu_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation elu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> elu_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation elu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> elu_esno20.txt')
#
# print(2)
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation lrelu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> lrelu_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation lrelu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> lrelu_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation lrelu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> lrelu_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation lrelu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> lrelu_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation lrelu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> lrelu_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation lrelu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> lrelu_esno20.txt')


# print(3)
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation prelu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> prelu_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation prelu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> prelu_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation prelu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> prelu_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation prelu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> prelu_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation prelu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> prelu_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation prelu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> prelu_esno20.txt')

# print(4)
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation uninit_param '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> uninit_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation uninit_param '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> uninit_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation uninit_param '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> uninit_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation uninit_param '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> uninit_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation uninit_param '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> uninit_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer SGD --activation uninit_param '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> uninit_esno20.txt')


print(3)
os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno10.dat >> adam_prelu_qpsk_esno10.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno12.dat >> adam_prelu_qpsk_esno12.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno14.dat >> adam_prelu_qpsk_esno14.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno16.dat >> adam_prelu_qpsk_esno16.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno18.dat >> adam_prelu_qpsk_esno18.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno20.dat >> adam_prelu_qpsk_esno20.txt')


print(4)
os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation elu '
          '--root D:/qpsk_awgn_sps8_esno10.dat >> adam_elu_qpsk_esno10.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation elu '
          '--root D:/qpsk_awgn_sps8_esno12.dat >> adam_elu_qpsk_esno12.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation elu '
          '--root D:/qpsk_awgn_sps8_esno14.dat >> adam_elu_qpsk_esno14.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation elu '
          '--root D:/qpsk_awgn_sps8_esno16.dat >> adam_elu_qpsk_esno16.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation elu '
          '--root D:/qpsk_awgn_sps8_esno18.dat >> adam_elu_qpsk_esno18.txt')

os.system('python resnet_roll_off.py --cuda 0 --arch resnet18 --optimizer Adam --activation elu '
          '--root D:/qpsk_awgn_sps8_esno20.dat >> adam_elu_qpsk_esno20.txt')







