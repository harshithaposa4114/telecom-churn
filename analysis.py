from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).parent
OUT=HERE/"outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(HERE/"telecom_customers.csv").drop_duplicates().dropna()
rate=df["Churn"].eq("Yes").mean()*100
contract=df.groupby("ContractType")["Churn"].apply(lambda s:s.eq("Yes").mean()*100).sort_values(ascending=False)
tenure=df.groupby("Churn")["TenureMonths"].mean()
print(f"Overall churn rate: {rate:.1f}%")
print("\\nChurn rate by contract (%):\\n",contract.round(1))
print("\\nAverage tenure by churn status:\\n",tenure.round(1))
contract.rename("ChurnRatePercent").to_csv(OUT/"churn_by_contract.csv")
plt.figure(figsize=(7,4)); contract.plot(kind="bar"); plt.ylabel("Churn rate (%)"); plt.title("Churn by Contract Type"); plt.tight_layout(); plt.savefig(OUT/"churn_by_contract.png"); plt.close()
