"""
Title: Data statistics
Author: Mitchell Verhaar

Description:
Implements the statistics for the data set.
"""

import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Stats:

    def __init__(self, files: list[str]) -> None:
        self.files = files
        self.data = {}

    def load_files(self) -> None:
        for name in self.files:
            with open(name, newline='') as F:
                rows = {}
                csv_f = csv.reader(F, delimiter=";")
                keys = next(csv_f)[1:]
                print(keys)
                for line in csv_f:
                    if len(line) > 0:
                        rows[line[0]] = {k:v for k, v in zip(keys, line[1:])}

                self.data[name.removesuffix(".csv")] = rows
        self.train_df = pd.read_csv(self.files[1],delimiter=";")
        self.val_df = pd.read_csv(self.files[2], delimiter=";")
        self.test_df = pd.read_csv(self.files[3], delimiter=";")
    
    def compute_product_stats(self) -> None:
        print(list(self.data["product_data"].values())[1])
        row_count = 0
        high_count_word = []
        high_count_char = []
        high_count_sent = []
        empty = 0
        for row in self.data["product_data"].values():
            if len(row["highlights"]) == 0:
                empty += 1
                continue
            high_count_sent.append(len(row["highlights"].split(".")))
            high_count_word.append(len(row["highlights"].split(" ")))
            high_count_char.append(len(row["highlights"].replace(" ", "")))
            row_count += 1

        #plot distributions
        #kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
        #kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)
        #plt.figure(figsize=(10,7), dpi= 80)
        fig, axes = plt.subplots(1, 3, figsize=(10, 3), sharey=False, dpi=100)
        fig.tight_layout(pad=3.0)
        #plt.hist(high_count_sent, **kwargs, color='g', label="Amount of sentences")
        #plt.hist(high_count_word, **kwargs, color='r', label="Amount of words")
        #plt.hist(high_count_char, **kwargs, color='b', label="Amount of characters")
        #plt.gca().set(title='Distribution of product description statistics.', ylabel='Relative amounts')
        sns.histplot(x=high_count_sent, color="dodgerblue", ax=axes[0], label="Amount of Sentences", kde=True)
        axes[0].set_xlabel("Sentence count")
        axes[0].set_ylabel("Frequency")
        sns.histplot(x=high_count_word, color="orange", ax=axes[1], label="Amount of words", kde=True)
        axes[1].set_xlabel("Word count")
        axes[1].set_ylabel("Frequency")
        sns.histplot(x=high_count_char, color="deeppink", ax=axes[2], label="Amount of characters", kde=True)
        axes[2].set_xlabel("Character count")
        axes[2].set_ylabel("Frequency")
        fig.legend()
        fig.suptitle("Statistics of product descriptions")
        plt.show()

        print(row_count)
        print("Average sentence count of product descriptions: ", round(sum(high_count_sent) / row_count))
        print("Minimum sentences length in product descriptions: ",  min(high_count_sent))
        print("Maximum sentences length in product descriptions: ",  max(high_count_sent))
        print("Average word count of product descriptions: ", round(sum(high_count_word) / row_count))
        print("Minimum words length in product descriptions: ",  min(high_count_word))
        print("Maximum words length in product descriptions: ",  max(high_count_word))
        print("Average character count of product descriptions: ", round(sum(high_count_char) / row_count))
        print("Minimum characters length in product descriptions: ",  min(high_count_char))
        print("Maximum characters length in product descriptions: ",  max(high_count_char))
        print("Number of products without a description: ", empty)

    def compute_search_stats(self) -> None:
        high_count_sent_train = []
        high_count_word_train = []
        high_count_char_train = []

        high_count_sent_val = []
        high_count_word_val = []
        high_count_char_val = []

        high_count_sent_test = []
        high_count_word_test = []
        high_count_char_test = []
        empty_train = 0
        empty_val = 0
        empty_test = 0
        row_count = 0
        for row_train, row_val, row_test in zip(self.data["train_data"].values(), self.data["validation_data"].values(), self.data["test_data"].values()):
            if len(row_train["search_query"]) == 0:
                empty_train += 1
                continue

            if len(row_val["search_query"]) == 0:
                empty_val += 1
                continue

            if len(row_test["search_query"]) == 0:
                empty_test += 1
                continue

            high_count_sent_train.append(len(row_train["search_query"].split(".")))
            high_count_word_train.append(len(row_train["search_query"].split(" ")))
            high_count_char_train.append(len(row_train["search_query"].replace(" ", "")))

            high_count_sent_val.append(len(row_val["search_query"].split(".")))
            high_count_word_val.append(len(row_val["search_query"].split(" ")))
            high_count_char_val.append(len(row_val["search_query"].replace(" ", "")))

            high_count_sent_test.append(len(row_test["search_query"].split(".")))
            high_count_word_test.append(len(row_test["search_query"].split(" ")))
            high_count_char_test.append(len(row_test["search_query"].replace(" ", "")))
            row_count += 1

        print(row_count)
        print("Average sentence count of search query across splits: ", round(sum(high_count_sent_train) / row_count), round(sum(high_count_sent_val) / row_count), round(sum(high_count_sent_test) / row_count))
        print("Maximal sentence count of search query across splits: ", max(high_count_sent_train), max(high_count_sent_val), max(high_count_sent_test))
        print("Average word count of search queries across splits: ", round(sum(high_count_word_train) / row_count), round(sum(high_count_word_val) / row_count), round(sum(high_count_word_test) / row_count))
        print("Maximal word count of search queries across splits: ", max(high_count_word_train), max(high_count_word_val), max(high_count_word_test))
        print("Average character count of search queries across splits: ", round(sum(high_count_char_train) / row_count), round(sum(high_count_char_val) / row_count), round(sum(high_count_char_test) / row_count))
        print("Maximal character count of search queries across splits: ", max(high_count_char_train), max(high_count_char_val), max(high_count_char_test))
        print("Number of products without a description: ", empty_train, empty_val, empty_test)
        #    clean_prop = self.clean_text(row["properties"])

    #def clean_text(self, txt: str) -> str:
    def determine_threshold(self) -> None:
        low_count = 0
        mid_count = 0
        high_count = 0
        for row_train, row_val, row_test in zip(self.data["train_data"].values(), self.data["validation_data"].values(), self.data["test_data"].values()):
            if not row_val["score"]:
                print(row_val["search_query"], row_val["score"])
            train_score = float(row_train["score"]) if row_train["score"] else 0.0
            val_score = float(row_val["score"]) if row_val["score"] else 0.0
            test_score = float(row_test["score"]) if row_test["score"] else 0.0
            if train_score <= 0.25 or val_score <= 0.25 or test_score <= 0.25:
                low_count += 1
            
            if 0.25 <= train_score <= 0.75 or 0.25 <= val_score <= 0.75 or 0.25 <= test_score <= 0.75:
                mid_count += 1
            
            if train_score > 0.75 or val_score > 0.75 or test_score > 0.75:
                high_count += 1

        print(f"The data contains the following division:\n\nProducts up to 0.25: {low_count}\nProducts ranging from 0.25 to 0.75: {mid_count}\n Products exceeding 0.75: {high_count}")

    def visualize_data(self) -> None:
        score_df_train = self.train_df[["search_query", "score"]].groupby(["search_query"], dropna=True).mean().rename(columns={"score": "train_score"})
        print(score_df_train["train_score"].mean())
        score_df_val = self.val_df[["search_query", "score"]].groupby(["search_query"], dropna=True).mean().rename(columns={"score": "val_score"})
        score_df_test = self.test_df[["search_query", "score"]].groupby(["search_query"], dropna=True).mean().rename(columns={"score": "test_score"})
        dfs = [score_df_train, score_df_val, score_df_test]
        df_merged = pd.DataFrame().join(dfs, how="outer")
        print(df_merged.head(10))
        sns.histplot(df_merged, bins=100)
        plt.axvline(score_df_train["train_score"].mean(), 0.33, 0.66, color="cyan", lw=2)
        plt.axvline(score_df_val["val_score"].mean(), 0.66, 1, color="orange", lw=2)
        plt.axvline(score_df_test["test_score"].mean(), 0, 0.33, color="green", lw=2)
        plt.xlabel("Average score")
        plt.ylabel("Frequency")
        plt.title("Aggregrated query scores")
        plt.show()

stats = Stats(["product_data.csv", "train_data.csv", "validation_data.csv", "test_data.csv"])
stats.load_files()
#stats.compute_product_stats()
#stats.compute_search_stats()
#stats.determine_threshold()
stats.visualize_data()
