import os
import sys
import numpy as np
import tensorflow as tf
import vggish_input
import vggish_slim
import vggish_postprocess

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Paths to the model and PCA parameter files
MODEL_PATH = 'embeddings/vggish_model/vggish_model.ckpt'
PCA_PARAMS_PATH = 'embeddings/vggish_model/vggish_pca_params.npz'

# Load VGGish model
def load_vggish_model():
    """
    Load the VGGish model for generating audio embeddings.
    """
    with tf.Graph().as_default():
        sess = tf.Session()
        vggish_slim.define_vggish_slim(training=False)
        saver = tf.train.Saver()
        saver.restore(sess, MODEL_PATH)
    return sess

# Embedding postprocessor
pproc = vggish_postprocess.Postprocessor(PCA_PARAMS_PATH)

def get_vggish_embedding(audio_file):
    """
    Generate audio embeddings using VGGish model.
    
    :param audio_file: Path to the audio file.
    :return: Embeddings (numpy array).
    """
    sess = load_vggish_model()
    
    # Convert audio to VGGish input format
    input_batch = vggish_input.wavfile_to_examples(audio_file)
    
    features_tensor = sess.graph.get_tensor_by_name('vggish/input_features:0')
    embedding_tensor = sess.graph.get_tensor_by_name('vggish/embedding:0')
    
    # Run inference and postprocess
    [embedding_batch] = sess.run([embedding_tensor], feed_dict={features_tensor: input_batch})
    embeddings = pproc.postprocess(embedding_batch)
    
    return embeddings

def get_audio_embedding():
    pass
