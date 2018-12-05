import os

# print(1)
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer AdaDelta --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> AdaDelta_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer AdaDelta --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> AdaDelta_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer AdaDelta --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> AdaDelta_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer AdaDelta --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> AdaDelta_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer AdaDelta --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> AdaDelta_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer AdaDelta --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> AdaDelta_esno20.txt')
#
# print(2)
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adagad --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> Adagad_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adagad --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> Adagad_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adagad --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> Adagad_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adagad --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> Adagad_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adagad --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> Adagad_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adagad --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> Adagad_esno20.txt')
#
# print(3)
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer SparseAdam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> SparseAdam_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer SparseAdam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> SparseAdam_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer SparseAdam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> SparseAdam_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer SparseAdam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> SparseAdam_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer SparseAdam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> SparseAdam_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer SparseAdam --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> SparseAdam_esno20.txt')
#
# print(4)
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adamax --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno10.dat >> Adamax_esno10.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adamax --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno12.dat >> Adamax_esno12.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adamax --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno14.dat >> Adamax_esno14.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adamax --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno16.dat >> Adamax_esno16.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adamax --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno18.dat >> Adamax_esno18.txt')
#
# os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer Adamax --activation relu '
#           '--root D:/qpsk_awgn_sps8_esno20.dat >> Adamax_esno20.txt')

print(3)
os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation elu '
          '--root D:/qpsk_awgn_sps8_esno10.dat >> RMSprop_elu_qpsk_esno10.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation elu '
          '--root D:/qpsk_awgn_sps8_esno12.dat >> RMSprop_elu_qpsk_esno12.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation elu '
          '--root D:/qpsk_awgn_sps8_esno14.dat >> RMSprop_elu_qpsk_esno14.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation elu '
          '--root D:/qpsk_awgn_sps8_esno16.dat >> RMSprop_elu_qpsk_esno16.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation elu '
          '--root D:/qpsk_awgn_sps8_esno18.dat >> RMSprop_elu_qpsk_esno18.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation elu '
          '--root D:/qpsk_awgn_sps8_esno20.dat >> RMSprop_elu_qpsk_esno20.txt')


print(4)
os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno10.dat >> RMSprop_prelu_qpsk_esno10.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno12.dat >> RMSprop_prelu_qpsk_esno12.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno14.dat >> RMSprop_prelu_qpsk_esno14.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno16.dat >> RMSprop_prelu_qpsk_esno16.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno18.dat >> RMSprop_prelu_qpsk_esno18.txt')

os.system('python resnet_roll_off.py --cuda 2 --arch resnet18 --optimizer RMSprop --activation prelu '
          '--root D:/qpsk_awgn_sps8_esno20.dat >> RMSprop_prelu_qpsk_esno20.txt')