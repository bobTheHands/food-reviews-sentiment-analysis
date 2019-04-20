
### Model Architecture hyper parameters
embedding_size = 64
sequence_length = 500
LSTM_units = 128

### Training parameters
batch_size = 64
epochs = 15

### Preprocessing parameters
# words that occur less than n times to be deleted from dataset
N = 10

# test size in ratio, train size is 1 - test_size
test_size = 0.2