import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global variable to store the dataframe
dataframe = None

def menu():
    while True:
        print("\n1. Upload Dataset\n2. View Dataset\n3. Perform Analysis\n4. Visualize Data\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            upload()
        elif choice == '2':
            view()
        elif choice == '3':
            analysis()
        elif choice == '4':
            visualize()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def upload():
    global dataframe
    file_path = input("Enter the path to your dataset (CSV file) without quotes: ")
    try:
        dataframe = pd.read_csv(file_path)
        print("Dataset uploaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view():
    if dataframe is not None:
        print(dataframe.head())
    else:
        print("No dataset uploaded.")

def analysis():
    if dataframe is not None:
        column = input("Enter the column name for analysis: ")
        if column in dataframe.columns:
            print(f"Mean: {dataframe[column].mean()}")
            print(f"Median: {dataframe[column].median()}")
            print(f"Std Dev: {dataframe[column].std()}")
            print(f"Min: {dataframe[column].min()}")
            print(f"Max: {dataframe[column].max()}")
        else:
            print("Column not found.")
    else:
        print("No dataset uploaded.")

def visualize():
    global dataframe
    if dataframe is not None:
        print("\nChoose a type of plot:")
        print("1. Line Plot")
        print("2. Bar Plot")
        print("3. Histogram")
        
        plot_choice = input("Enter your choice: ")
        
        if plot_choice == '1':
            sns.lineplot(data=dataframe)
            plt.title("Line Plot")
            plt.show()
        elif plot_choice == '2':
            sns.barplot(data=dataframe)
            plt.title("Bar Plot")
            plt.show()
        elif plot_choice == '3':
            dataframe.hist()
            plt.title("Histogram")
            plt.show()
        else:
            print("Invalid choice.")
    else:
        print("No dataset uploaded.")


menu()
