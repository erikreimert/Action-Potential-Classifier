import keras
from keras import layers


# This is where the input is going to go to
#has to a be a tensor(N, 48)
input =

'''
    Encoder part
        "encoded" is the encoded representation of the input
        its output is a (tensor(N,10), tensor(N,3))
            the first tensor is a categorical head
            the second tensor is a gaussian head of encoding

    we need to pass encoded into two dense layers first one to produce each tensor
'''
encoded = layers.Dense(100, activation='elu')(input)
encoded = layers.Dense(100, activation='elu')(encoded)

'''
    Second layers that produce the tensors
'''

categoricalGaussian_Head = layers.Dense(10, activation='lin')(encoded) #returns tensor(N,10)
gaussian_Head = layers.Dense(3, activation='lin')(encoded) #returns tensor(N,3)

'''
    Decoder part
'''
decode1 = layers.Dense(100, activation='lin')(categoricalGaussian_Head)
decode2 = layers.Dense(100, activation ='lin')(gaussian_Head)

#sum both tensors together
decoded = decode1 + decode2

decoded = layers.Dense(100, activation = 'elu')(decoded)
decoded = layers.Dense(48, activation = 'tanh')(decoded)



# This model maps an input to its reconstruction
autoencoder = keras.Model(input_img, decoded)
