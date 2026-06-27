from transformers import AutoTokenizer 
from transformers import AutoModelForCausalLM
from config import MODEL_NAME
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
from peft import LoraConfig
from peft import get_peft_model
from peft import TaskType 

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type= TaskType.CAUSAL_LM
)

model = get_peft_model(
    model,
    lora_config
)

model.print_trainable_parameters()