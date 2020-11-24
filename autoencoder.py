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

categoricalGaussian_Head = layers.Dense(100, activation='lin')(encoded) #returns tensor(N,10) TODO ask prof how to return this
'''
    Reshape the tensor into (N,13)
'''
# gaussian_Head = layers.Dense(100, activation='lin')(encoded) #returns tensor(N,3) TODO ask prof how to return this

'''
    Decoder part
'''

# "decoded" is the lossy reconstruction of the input
decoded = layers.Dense(784, activation='sigmoid')(encoded)

# This model maps an input to its reconstruction
autoencoder = keras.Model(input_img, decoded)
