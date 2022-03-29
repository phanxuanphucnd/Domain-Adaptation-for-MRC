# -*- coding: utf-8 -*-
# Copyright (c) 2022 by Phuc Phan

root_path                     = '/home/phucpx/vinbdi/Domain-Adaptation-for-MRC'
train_file                    = ['/BioASQ/train-v1.1.json', '/BioASQ/BioASQ-train-factoid-7b-full-annotated.json']
predict_file                  = f'/BioASQ/BioASQ-test-factoid-7b-1.json'
data_dir                      = root_path + '/data/'
output_dir                    = root_path + '/output/'
output_model_dir              = root_path + '/model/'
golden_data_folder            = root_path + '/data/'
domain_names                  = ['SQuAD', 'BioASQ']
model_type                    = 'deberta-v3'
original_model_name_or_path   = 'deberta-v3'
pretrained_model_name_or_path = 'microsoft/deberta-v3-base'

# change following two params for different number of training epochs & patience-threshold
num_train_epochs              = 2
patience_threshold            = 1
overwrite_cache               = False
no_cuda                       = False
device                        = "cuda"
which_gpu                     = "1"
n_gpu                         = 1
num_workers                   = 8
threads                       = 512
local_rank                    = -1
initializer_range             = 0.02
null_score_diff_threshold     = 0.0
per_gpu_eval_batch_size       = 8
tokenizer_name                = ''
config_name                   = ''
cache_dir                     = ''
n_best_size                   = 5
max_query_length              = 64
max_answer_length             = 30
verbose_logging               = False
version_2_with_negative       = True
max_seq_length                = 384
doc_stride                    = 128
emb_dim                       = 768
do_lower_case                 = True
freeze_encoder                = False
freeze_qa_output_generator    = False
freeze_discriminator_encoder  = False
freeze_aux_qa_output_generator= False
USE_AUX_QA_LOSS               = True
seed                          = 42
do_train                      = True
do_test                       = False
ALTERNATE_SOURCE_TARGET       = False
SOURCE_INDEX                  = 0
USE_AUX_QA_LOSS               = True
qa_loss_alpha                 = 1     # original task loss in the base model
reverse_layer_lambda          = 0     # gradient reversal layer
adv_loss_beta                 = 1  # discriminator triplet loss
aux_layer_gamma               = 1  # original task loss in the disc model
num_samples_per_epoch         = 1_000
learning_rate                 = 5e-5
lr_multiplier                 = 20
lambda_delta                  = 0.01
warmup_steps                  = 0
train_batch_size              = 1
per_gpu_train_batch_size      = 1
gradient_accumulation_steps   = 32
weight_decay                  = 0.0
adam_epsilon                  = 1e-8
initializer_range             = 0.02
max_grad_norm                 = 1.0
max_steps                     = -1
overwrite_output_dir          = True
overwrite_output_model_dir    = True
server_ip                     = ''
server_port                   = ''
threads                       = 512
lang_id                       = 0
version_2_with_negative       = False
fp16                          = False
fp16_opt_level                = 'O1'
eval_all_checkpoints          = False
evaluate_during_training      = False
logging_steps                 = 50_000_000
save_steps                    = 50_000_000