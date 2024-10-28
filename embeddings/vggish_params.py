# vggish_params.py

# Constants for the VGGish model configuration
# Input dimensions
VGGISH_INPUT_SHAPE = (96, 64, 1)  # Height, Width, Channels

# Number of classes for output layer (not used in this version)
NUM_CLASSES = 128

# The number of mel bands used in the input to the model
NUM_MEL_BANDS = 64

# The dimensionality of the output embedding
EMBEDDING_DIMENSION = 128

# Hyperparameters for the VGGish architecture
# Kernel sizes for convolutional layers
CONV_KERNELS = [
    (3, 3),  # Kernel size for the first convolutional layer
    (3, 3),  # Kernel size for the second convolutional layer
    (3, 3),  # Kernel size for the third convolutional layer
    (3, 3),  # Kernel size for the fourth convolutional layer
]

# Number of filters for each convolutional layer
NUM_FILTERS = [
    64,  # Number of filters for the first layer
    128,  # Number of filters for the second layer
    256,  # Number of filters for the third layer
    256,  # Number of filters for the fourth layer
]

# Strides for the pooling layers
POOL_STRIDES = [2, 2, 2, 2]  # Stride for max pooling after each conv layer

# The dropout rate applied to the fully connected layers (if any)
DROPOUT_RATE = 0.5

# Learning rate settings for the optimizer
LEARNING_RATE = 0.001
