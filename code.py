from flask import Flask, request
import pandas as pd

app = Flask(__name__)


# Define API endpoint for energy data analysis
@app.route('/energy-data-analysis', methods=['POST'])
def energy_data_analysis():
    # Read input data from request
    input_data = request.json

    # Load energy dataset
    energy_data = pd.read_csv('energy_data.csv')

    # Filter energy data by date range and energy type
    start_date = input_data['start_date']
    end_date = input_data['end_date']
    energy_type = input_data['energy_type']
    filtered_data = energy_data[
        (energy_data['date'] >= start_date) & (energy_data['date'] <= end_date) & (energy_data['type'] == energy_type)]

    # Perform data analysis
    analysis_result = {}
    analysis_result['total_energy'] = filtered_data['value'].sum()
    analysis_result['average_energy'] = filtered_data['value'].mean()
    analysis_result['max_energy'] = filtered_data['value'].max()
    analysis_result['min_energy'] = filtered_data['value'].min()

    # Return analysis result as JSON response
    return analysis_result


if __name__ == '__main__':
    app.run(debug=True)
