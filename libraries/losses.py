# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:40:42 2018
@author: murali.sai
"""
import tensorflow as tf

def categorical_crossentropy(y_true, y_pred):
    loss = tf.nn.softmax_cross_entropy_with_logits(labels=y_true,logits=y_pred)
    return loss
# Using only basic tensorflow ops, implement the following functions
# TODO: cosine distance
def cosine_distance(y_true, y_pred):
    """
    Cosine_distance_loss = 1 - cosine_similarity
    cosine distance using only basic tensorflow ops.
    (Do not use tf.losses, tf.nn, etc.)
    """
    # Correctness check
    tf.assert_equal(tf.shape(y_true),tf.shape(y_pred), name='assert_cond')
    epsilon = 0.001
    # Denominator; Norms
    y_true_norm = tf.sqrt(tf.reduce_sum(tf.multiply(y_true,y_true)),name='y_true_norm')
    y_pred_norm = tf.sqrt(tf.reduce_sum(tf.multiply(y_pred,y_pred)),name='y_pred_norm')
    den_ = tf.multiply(y_true_norm,y_pred_norm)+epsilon;
    # Numerator; Cross-multiplication
    cross_multiply = tf.reduce_sum(tf.multiply(y_true,y_pred),name='cross_multiply')
    num_ = cross_multiply+epsilon;
    loss = 1-tf.div(num_,den_)
    return loss
# TODO: regression error
# mean absolute error ^ n
def regression_error(y_true, y_pred, p=2):
    """
    Regression error using only basic tensorflow ops.
    (Do not use tf.losses, tf.nn, etc.)
    """
    abs_diff = tf.abs(tf.subtract(y_true,y_pred))
    loss = tf.reduce_mean(tf.pow(abs_diff,p), name='regression_error')
    return loss
# TODO: hinge loss
def hinge_loss(y_true, y_pred):
    """
    Hinge loss loss using only basic tensorflow ops.
    (Do not use tf.losses, tf.nn, etc.)
    """
    # (Differentiable) Hinge Loss as defined in https://en.wikipedia.org/wiki/Hinge_loss
    # Input: y_true are labels having values 0.0 or 1.0, y_pred are logits or unnormalized predicted class scores
    # Convert labels to +1/-1 floats and multiply with logits
    y_true = 2*y_true-1;
    out_ = 1-tf.multiply(y_true,y_pred)
    # relu operation #loss_ = tf.nn.relu(1-out_)
    comparison = tf.less( out_, tf.constant( 0 ) )  
    loss_ = out_.assign( tf.where (comparison, tf.zeros_like(out_), out_) )
    loss = tf.reduce_mean(loss_);
    return loss











