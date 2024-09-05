import pandas as pd 
from sklearn.linear_model import LogisticRegression

def main():
    # Load the dataset
    try:
        bank_full = pd.read_csv('.\\data\\bank_full_w_dummy_vars.csv')
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return

    x = bank_full.iloc[:, 18:37]
    y = bank_full.iloc[:,17]

    LogReg= LogisticRegression( )
    LogReg.fit(x , y)
    print(LogReg)

# Print the model coefficients and intercept
    print("Model Coefficients:", LogReg.coef_)
    print("Model Intercept:", LogReg.intercept_)

# Optionally, calculate and print the accuracy of the model
    accuracy = LogReg.score(x, y)
    print("Model Accuracy:", accuracy)

if __name__ == "__main__":
    main()