from datasets import load_dataset

print("Dowloading WikiSQL...")
wikisql = load_dataset("wikisql",trust_remote_code=True)

print("Download Spider...")
spider = load_dataset("spider",trust_remote_code=True)

print("Done")