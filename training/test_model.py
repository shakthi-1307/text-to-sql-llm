from model import load_model

model, tokenizer = load_model()

model.print_trainable_parameters()