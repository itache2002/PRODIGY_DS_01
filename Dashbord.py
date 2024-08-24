import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv", skiprows=4)

# Filter out unnecessary columns
data = data.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 68'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("World Population Dashboard"),
    
    # Dropdown to select the country
    html.Label("Select a Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in data['Country Name'].unique()],
        value='India'
    ),
    
    # Graph to display the population trend
    dcc.Graph(id='population-graph')
])

# Define the callback to update the graph based on selected country
@app.callback(
    Output('population-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    country_data = data[data['Country Name'] == selected_country]
    country_data = country_data.melt(id_vars=['Country Name'], var_name='Year', value_name='Population')
    country_data['Year'] = pd.to_numeric(country_data['Year'])
    
    # Create the line chart
    fig = px.line(country_data, x='Year', y='Population', title=f'Population Trend for {selected_country}')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
