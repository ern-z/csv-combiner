import pandas as pd
import sys


class CSVCombiner:

    def __init__(self):
        self.files = []
        

    def parseArgs(self, args):
        if len(args) < 3:
            print("Provide at least 2 input files.")
            return False


        for i in range(1, len(args)):
            file = args[i].split('/')[-1]
            self.files.append(file)
        return True


    def combine(self):

        if not self.files:
            return False

        newDF = []
        for file in self.files:
            df = pd.read_csv(f"fixtures/{file}")
            df["filename"] = file
            newDF.append(df)
        newDF = pd.concat(newDF, axis=0, ignore_index= True)

        newfile = "-".join([i.split(".")[0] for i in self.files])

        newDF.to_csv(f"combined/{newfile}")

        print(f"\nDone!\nCombined file -> {newfile}.csv\n")
        return True





def main():
    combiner = CSVCombiner()
    combiner.parseArgs(sys.argv)
    combiner.combine()


if __name__ == '__main__':
    main()