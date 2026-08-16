





# Using LangchainLLMWrapper

from dotenv import load_dotenv
load_dotenv()

from ragas import EvaluationDataset
from langchain_anthropic import ChatAnthropic
from load_test_data import test_data_list
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import ResponseRelevancy, Faithfulness, LLMContextPrecisionWithReference, LLMContextRecall


evaluation_dataset = EvaluationDataset.from_list(test_data_list)


llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
evaluator_llm = LangchainLLMWrapper(llm)

results = evaluate(
    dataset=evaluation_dataset,
    metrics=[Faithfulness(),LLMContextRecall(),ResponseRelevancy(),LLMContextPrecisionWithReference()],
    llm= evaluator_llm
)

print(results)

df = results.to_pandas()
df.to_csv("ragas_results.csv", index=False)
print("\nSaved detailed results to ragas_results.csv")

