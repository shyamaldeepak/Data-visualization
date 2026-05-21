import json

filename = "video_game_sales_analysis (1) (1).ipynb"

with open(filename, 'r') as f:
    nb = json.load(f)

# Define cell for Question 4 Pie Chart
q4_md = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Question 4: Which Region Contributes the Most?"
    ]
}

q4_code = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import plotly.express as px\n",
        "import pandas as pd\n",
        "\n",
        "# 1. Calculate the total sales for each region\n",
        "regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']\n",
        "regional_sales = [df[region].sum() for region in regions]\n",
        "labels = ['North America', 'Europe', 'Japan', 'Other']\n",
        "\n",
        "# 2. Create a temporary dataframe for Plotly\n",
        "pie_df = pd.DataFrame({'Region': labels, 'Total Sales (Millions)': regional_sales})\n",
        "\n",
        "# 3. Plot the interactive pie chart\n",
        "fig = px.pie(pie_df, values='Total Sales (Millions)', names='Region', \n",
        "             title='Q4: Which Region Contributes the Most to Global Sales?',\n",
        "             color_discrete_sequence=px.colors.qualitative.Pastel)\n",
        "\n",
        "# Make the labels appear inside the pie slices\n",
        "fig.update_traces(textposition='inside', textinfo='percent+label',\n",
        "                  marker=dict(line=dict(color='#000000', width=1)))\n",
        "fig.show()"
    ]
}

# Define cell for Question 6 World Map
q6_md = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Question 6: How are video game sales geographically concentrated across the globe?"
    ]
}

q6_code = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import plotly.express as px\n",
        "import pandas as pd\n",
        "\n",
        "# 1. Calculate the total sales for each region from the dataset\n",
        "na_sales = df['NA_Sales'].sum()\n",
        "eu_sales = df['EU_Sales'].sum()\n",
        "jp_sales = df['JP_Sales'].sum()\n",
        "other_sales = df['Other_Sales'].sum()\n",
        "\n",
        "# 2. Create geographic coordinates (Latitude and Longitude) for the center of each region\n",
        "map_data = {\n",
        "    'Region': ['North America', 'Europe', 'Japan', 'Rest of World'],\n",
        "    'Latitude': [45.0, 50.0, 36.2, -15.0],\n",
        "    'Longitude': [-100.0, 10.0, 138.2, -60.0],\n",
        "    'Total Sales (Millions)': [na_sales, eu_sales, jp_sales, other_sales]\n",
        "}\n",
        "\n",
        "# Convert to a DataFrame\n",
        "map_df = pd.DataFrame(map_data)\n",
        "\n",
        "# 3. Create an interactive World Bubble Map\n",
        "fig = px.scatter_geo(map_df,\n",
        "                     lat='Latitude',\n",
        "                     lon='Longitude',\n",
        "                     size='Total Sales (Millions)',\n",
        "                     color='Region',\n",
        "                     hover_name='Region',\n",
        "                     title='Q6: Geographic Concentration of Global Video Game Sales',\n",
        "                     size_max=60,\n",
        "                     projection='natural earth')\n",
        "\n",
        "# Tweak the layout to make it look professional\n",
        "fig.update_geos(showcountries=True, countrycolor=\"lightgrey\",\n",
        "                showcoastlines=True, coastlinecolor=\"darkgrey\",\n",
        "                showland=True, landcolor=\"whitesmoke\",\n",
        "                showocean=True, oceancolor=\"aliceblue\")\n",
        "\n",
        "fig.update_layout(height=600, margin={\"r\":0,\"t\":50,\"l\":0,\"b\":0})\n",
        "fig.show()"
    ]
}

# Find if Q4 already exists and replace it, or append if not found
q4_index = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and len(cell['source']) > 0 and 'Question 4: Which Region Contributes the Most?' in cell['source'][0]:
        q4_index = i
        break

if q4_index != -1:
    # Insert code after q4 markdown, we'll assume the next cell is code and replace it or insert
    if q4_index + 1 < len(nb['cells']) and nb['cells'][q4_index+1]['cell_type'] == 'code':
        nb['cells'][q4_index+1] = q4_code
    else:
        nb['cells'].insert(q4_index+1, q4_code)
else:
    nb['cells'].extend([q4_md, q4_code])

# Append Q6 at the end
nb['cells'].extend([q6_md, q6_code])

with open(filename, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
