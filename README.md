# Energy Efficiency Heating Load Prediction

This project estimates the heating demand of buildings based on their architectural parameters using machine learning models. The dataset is obtained from the UCI Machine Learning Repository's Energy Efficiency dataset.

## Project Structure

- `app.py`: Streamlit application to enter building attributes and generate heating load predictions.
- `best_energy_efficiency_model.pkl`: Pretrained ML model stored using joblib.
- `requirements/requirements.txt`: Python dependency file needed for both the Jupyter notebook and the Streamlit application.
- `Copy_of_main_but_better.ipynb`: Jupyter notebook including exploratory data analysis, model development, assessment, and visualization.

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

- Python 3.8 or later  
- VS Code (or any suitable IDE)  
- Git (for repository management)  
- PowerShell or compatible terminal in VS Code  
- Stable internet connection to fetch the dataset when executing the notebook  

### Setup Instructions

1. Clone the repository:
    ```
    git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3. Install packages:
    ```
    pip install -r requirements/requirements.txt
    ```

4. Launch the Streamlit app locally:
    ```
    streamlit run app.py
    ```
5. Open the link displayed in the terminal (usually `http://localhost:8501`) in your web browser to use the app.

## Usage

- Use the web page to fill in building feature values.  
- Select "Predict Heating Load" to view the predicted heating requirement using the saved model.

## How It Works

- `app.py` loads the trained CatBoost regression model stored as a pickle file.  
- User inputs are captured and arranged into the required format.  
- The model performs prediction, and the result is shown through the Streamlit interface.

## Exploratory Data Analysis

- Managed missing and duplicate records.  
- Detected and capped outliers using the Interquartile Range (IQR) technique.  
- Conducted univariate analysis with histograms.  
- Created scatterplots for bivariate feature-target visualization.  
- Displayed multivariate correlations using heatmaps.  
- Standardized numeric data employing StandardScaler before training.

## Models Trained

- Linear Regression  
- Gradient Boosting Regressor  
- Random Forest Regressor  
- CatBoost Regressor (top-performing and selected for deployment)  

## License

This project is released under the MIT License.

## Acknowledgements

- Dataset courtesy of UCI Machine Learning Repository: [Energy Efficiency Data Set](https://archive.ics.uci.edu/ml/datasets/Energy+efficiency)  
- Streamlit for easy interface creation  
- CatBoost for efficient gradient boosting performance
