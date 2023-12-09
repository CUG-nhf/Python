import xgboost as xgb
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 加载数据集
file_path = 'training_set.csv'
df = pd.read_csv(file_path)

# 选择属性和标签
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建 XGBoost 分类器
model = xgb.XGBClassifier(objective="binary:logistic", eval_metric="logloss", use_label_encoder=False)

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")

# 打印分类报告
print("分类报告：")
print(classification_report(y_test, y_pred))
