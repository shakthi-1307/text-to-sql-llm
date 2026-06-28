# training/model.py

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)

from peft import (
    LoraConfig,
    TaskType,
    get_peft_model
)

from config import MODEL_NAME

def load_tokenizer():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    tokenizer.pad_token = tokenizer.eos_token

    return tokenizer

def load_base_model():

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME
    )

    return model

def get_lora_config():

    config = LoraConfig(

        r=16,

        lora_alpha=32,

        lora_dropout=0.05,

        bias="none",

        task_type=TaskType.CAUSAL_LM,

        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj"
        ]
    )

    return config

def load_model():

    tokenizer = load_tokenizer()

    model = load_base_model()

    lora_config = get_lora_config()

    model = get_peft_model(
        model,
        lora_config
    )

    return model, tokenizer