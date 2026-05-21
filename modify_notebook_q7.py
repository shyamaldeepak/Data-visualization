import json

filename = "video_game_sales_analysis (1) (1).ipynb"

with open(filename, 'r') as f:
    nb = json.load(f)

# Define cell for Question 7
q7_md = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Question 7: Which Publisher has the most commercial success?"
    ]
}

q7_code = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import plotly.express as px\n",
        "\n",
        "# 1. Group the data by Publisher and sum their global sales\n",
        "publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().reset_index()\n",
        "\n",
        "# 2. Sort the values in descending order and select the top 10\n",
        "top_publishers = publisher_sales.sort_values(by='Global_Sales', ascending=False).head(10)\n",
        "\n",
        "# 3. Create an interactive Bar Chart using Plotly\n",
        "fig = px.bar(top_publishers, x='Publisher', y='Global_Sales',\n",
        "             title='Q7: Top 10 Video Game Publishers by Global Sales',\n",
        "             labels={'Global_Sales': 'Total Global Sales (Millions)', 'Publisher': 'Publisher'},\n",
        "             color='Global_Sales',\n",
        "             color_continuous_scale=px.colors.sequential.Viridis)\n",
        "\n",
        "# Tweak layout for better readability\n",
        "fig.update_layout(xaxis_tickangle=-45)\n",
        "fig.show()"
    ]
}

nb['cells'].extend([q7_md, q7_code])

with open(filename, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
