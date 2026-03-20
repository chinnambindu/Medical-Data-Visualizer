import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")          # non-interactive backend for file output
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data 
df = pd.read_csv("medical_examination.csv", sep=";")

# 2. Overweight column 
df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2 > 25).astype(int)

#  3. Normalize cholesterol & glucose
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"]        = (df["gluc"]        > 1).astype(int)


# Categorical Plot

def draw_cat_plot():
    # 4. Melt into long format 
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # 5. Group, count, rename 
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 6. Draw catplot
    g = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    )
    g.set_axis_labels("variable", "total")
    g.set_titles("cardio = {col_name}")

    # 7. Store figure 
    fig = g.figure

    # 8. Save & return 
    fig.savefig("catplot.png")
    return fig


# Heat Map

def draw_heat_map():
    # 9. Clean data 
    df_heat = df[
        (df["ap_lo"]  <= df["ap_hi"])                              &
        (df["height"] >= df["height"].quantile(0.025))             &
        (df["height"] <= df["height"].quantile(0.975))             &
        (df["weight"] >= df["weight"].quantile(0.025))             &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 10. Correlation matrix 
    corr = df_heat.corr()

    # 11. Upper-triangle mask 
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Figure 
    fig, ax = plt.subplots(figsize=(12, 10))

    # 13. Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    # 14. Save & return 
    fig.savefig("heatmap.png")
    return fig
