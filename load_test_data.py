
from expected_answers import reference
import html
import pandas as pd

df = pd.read_csv("ragas_test_data.csv", encoding="utf-8-sig")
test_data_list = df.to_dict(orient="records")


for entry in test_data_list:
   
    entry["user_input"] = html.unescape(entry["question"])
    entry["retrieved_contexts"] = [entry["context"]]
    entry["response"] = entry["answer"]
    entry["reference"] = reference[entry["user_input"]]
    
