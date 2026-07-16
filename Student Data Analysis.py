import pandas as pd
import matplotlib.pyplot as plt
import os


class StudentAnalyzer:

    def __init__(self, file):

        try:
            self.data = pd.read_excel(file)

        except:
            print("Cannot open file")
            exit()


        self.find_columns()


    # پیدا کردن ستون ها به صورت خودکار
    def find_columns(self):

        columns = self.data.columns

        mapping = {

            "age": [
                "age",
                "Age",
                "سن"
            ],

            "gender": [
                "gender",
                "Gender",
                "جنسیت",
                "sex"
            ],

            "score": [
                "score",
                "Score",
                "grade",
                "Grade",
                "نمره"
            ]

        }


        self.cols = {}


        for key, names in mapping.items():

            found = False

            for name in names:

                if name in columns:
                    self.cols[key] = name
                    found = True
                    break


            if not found:
                print(
                    f"{key} column not found"
                )
                exit()



    def show_info(self):

        print("\nDataset information")

        print(
            self.data.info()
        )


        print("\nFirst rows:")

        print(
            self.data.head()
        )



    def analyze_gender(self, gender):

        gender_col = self.cols["gender"]

        data = self.data[
            self.data[gender_col]
            .astype(str)
            .str.lower()
            ==
            gender.lower()
        ]


        if len(data)==0:

            print(
                "No data found"
            )

            return



        age = self.cols["age"]
        score = self.cols["score"]


        print("\nGender:", gender)

        print(
            "Students:",
            len(data)
        )

        print(
            "Average age:",
            data[age].mean()
        )


        print(
            "Maximum age:",
            data[age].max()
        )


        print(
            "Minimum age:",
            data[age].min()
        )


        print("\nScore:")

        print(
            data[score].describe()
        )



    def score_by_gender(self):

        gender = self.cols["gender"]
        score = self.cols["score"]


        result = (
            self.data
            .groupby(gender)[score]
            .mean()
        )


        print(
            result
        )


        os.makedirs(
            "charts",
            exist_ok=True
        )


        plt.figure(figsize=(6,4))


        result.plot(
            kind="bar"
        )


        plt.title(
            "Average Score By Gender"
        )


        plt.xlabel(
            "Gender"
        )


        plt.ylabel(
            "Score"
        )


        plt.tight_layout()


        plt.savefig(
            "charts/gender_score.png"
        )


        plt.show()



    def score_by_age(self):

        age = self.cols["age"]
        score = self.cols["score"]


        result = (
            self.data
            .groupby(age)[score]
            .mean()
        )


        print(result)


        plt.figure(figsize=(7,4))


        result.plot(
            kind="bar"
        )


        plt.title(
            "Average Score By Age"
        )


        plt.xlabel(
            "Age"
        )


        plt.ylabel(
            "Score"
        )


        plt.tight_layout()


        plt.savefig(
            "charts/age_score.png"
        )


        plt.show()



    def save_report(self):

        age = self.cols["age"]
        gender = self.cols["gender"]
        score = self.cols["score"]


        report = (

            self.data
            .groupby(gender)
            .agg(

                Students=(
                    score,
                    "count"
                ),

                Average_Score=(
                    score,
                    "mean"
                ),

                Average_Age=(
                    age,
                    "mean"
                ),

                Max_Score=(
                    score,
                    "max"
                ),

                Min_Score=(
                    score,
                    "min"
                )

            )

        )


        report.to_excel(
            "report.xlsx"
        )


        print(
            "Report saved"
        )




def main():


    file = input(
        "Enter excel file name: "
    )


    analyzer = StudentAnalyzer(
        file
    )


    while True:


        print("""

========================

Student Data Analyzer

1. Show information
2. Analyze gender
3. Average score by gender
4. Average score by age
5. Save report
6. Exit

========================

""")


        choice=input(
            "Choose: "
        )



        if choice=="1":

            analyzer.show_info()



        elif choice=="2":

            g=input(
                "Enter gender: "
            )

            analyzer.analyze_gender(g)



        elif choice=="3":

            analyzer.score_by_gender()



        elif choice=="4":

            analyzer.score_by_age()



        elif choice=="5":

            analyzer.save_report()



        elif choice=="6":

            print(
                "Goodbye"
            )

            break


        else:

            print(
                "Invalid choice"
            )



main()