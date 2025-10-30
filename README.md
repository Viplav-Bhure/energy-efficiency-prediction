# Energy Efficiency Heating Load Prediction

This project predicts the heating load of buildings based on architectural features using machine learning models. The dataset is from the UCI Machine Learning Repository's Energy Efficiency dataset.

## Project Structure

- `app.py`: Streamlit web application to input building features and get heating load predictions.
- `best_energy_efficiency_model.pkl`: Pretrained machine learning model saved using joblib.
- `requirements/requirements.txt`: Python dependencies required for both the Jupyter notebook and Streamlit app.
- `Copy_of_main_but_better.ipynb`: Jupyter notebook containing exploratory data analysis, model training, evaluation, and visualization.

## Features Used

- Relative Compactness
- Surface Area
- Wall Area
- Roof Area
- Overall Height
- Orientation
- Glazing Area
- Glazing Area Distribution

## Getting Started

### Prerequisites

- Python 3.8 or higher
- VS Code (or any preferred IDE)
- Git (for version control)
- PowerShell terminal (default in VS Code on Windows)
- Internet connection to fetch datasets when running notebook

### Setup Instructions

1. Clone this repository:
    ```
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements/requirements.txt
    ```

4. Run the Streamlit app locally:
    ```
    streamlit run app.py
    ```
5. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser to interact with the app.

## Usage

- Use the web interface to input features of a building.
- Click "Predict Heating Load" to see the predicted heating load from the saved model.

## How It Works

- `app.py` loads the pretrained CatBoost model saved as a pickle file.
- Inputs from the user are collected and arranged into the appropriate format.
- Prediction is made using the model and displayed on the Streamlit frontend.

## Exploratory Data Analysis

- Handled missing values and duplicates.
- Outliers were detected and capped using Interquartile Range (IQR) method.
- Performed univariate analysis through histograms.
- Bivariate analysis with scatterplots to visualize feature-target relations.
- Multivariate correlations visualized via heatmaps.
- Features were standardized using StandardScaler for model training.

## Models Trained

- Linear Regression
- Gradient Boosting Regressor
- Random Forest Regressor
- CatBoost Regressor (best performing and used for final predictions)

## License

This project is licensed under the MIT License.

## Acknowledgements

- Dataset from UCI Machine Learning Repository: [Energy Efficiency Data Set](https://archive.ics.uci.edu/ml/datasets/Energy+efficiency)
- Streamlit for easy GUI deployment
- CatBoost for powerful gradient boosting models
