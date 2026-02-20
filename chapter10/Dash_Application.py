import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Load Dataset

# Using seaborn built-in tips dataset
import seaborn as sns
df = sns.load_dataset("tips")

# Features and Target
X = df[['total_bill', 'size']]
y = df['tip']

# Step 2: Train Linear Regression Model


model = LinearRegression()
model.fit(X, y)

# Step 3: Create Dash App

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.H1("Tip Prediction Dashboard", style={'textAlign': 'center'}),

    html.Label("Enter Total Bill Amount:"),
    dcc.Input(
        id='total_bill_input',
        type='number',
        placeholder='Enter total bill',
        style={'marginBottom': '10px'}
    ),

    html.Br(),

    html.Label("Enter Number of People:"),
    dcc.Input(
        id='size_input',
        type='number',
        placeholder='Enter number of people',
        style={'marginBottom': '10px'}
    ),

    html.Br(),
    html.Button("Predict Tip", id='predict_button', n_clicks=0),

    html.Br(), html.Br(),

    html.H3(id='prediction_output')

])

# Step 4: Callback Function

@app.callback(
    Output('prediction_output', 'children'),
    Input('predict_button', 'n_clicks'),
    State('total_bill_input', 'value'),
    State('size_input', 'value')
)
def predict_tip(n_clicks, total_bill, size):
    if n_clicks > 0 and total_bill is not None and size is not None:
        
        input_data = np.array([[total_bill, size]])
        predicted_tip = model.predict(input_data)[0]
        
        return f"Predicted Tip Amount: ${predicted_tip:.2f}"
    
    return ""
# Run App

if __name__ == '__main__':
    app.run(debug=True)