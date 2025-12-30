This project predicts the heating requirements of buildings based on their design parameters using machine learning algorithms. The dataset is sourced from the UCI Machine Learning Repository's Energy Efficiency dataset.

## Project Structure

- `app.py`: Streamlit web application to input building features and generate heating demand predictions.
- `best_energy_efficiency_model.pkl`: Pretrained machine learning model saved using joblib.
- `requirements/requirements.txt`: Python dependency file required for both the notebook and Streamlit app.
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
- VS Code (or similar IDE)  
- Git (for repository setup)  
- PowerShell or any supported terminal in VS Code  
- Reliable internet connection to download the dataset during notebook execution  

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

3. Install necessary packages:
    ```
    pip install -r requirements/requirements.txt
    ```

4. Run the Streamlit application locally:
    ```
    streamlit run app.py
    ```

5. Open the URL displayed in the terminal (commonly `http://localhost:8501`) in your web browser to access the interface.

## Usage

- Use the webpage to enter building feature values.  
- Click "Predict Heating Load" to display the estimated heating requirement using the stored model.

## How It Works

- `app.py` loads the trained CatBoost regression model saved as a pickle file.  
- User inputs are gathered and structured into the necessary input format.  
- The model performs prediction, and the results are shown through the Streamlit interface.

## Exploratory Data Analysis

- Handled missing and duplicate entries.  
- Identified and capped outliers using the Interquartile Range (IQR) technique.  
- Conducted univariate analysis with distribution plots.  
- Created scatterplots for bivariate feature-target exploration.  
- Displayed multivariate correlations via heatmaps.  
- Standardized numerical variables using StandardScaler before modeling.

## Models Trained

- Linear Regression  
- Gradient Boosting Regressor  
- Random Forest Regressor  
- CatBoost Regressor (best-performing and deployed)  

## License

This project is open-sourced under the MIT License.

## Acknowledgements

- Dataset provided by the UCI Machine Learning Repository: [Energy Efficiency Data Set](https://archive.ics.uci.edu/ml/datasets/Energy+efficiency)  
- Streamlit for interactive interface development  
- CatBoost for robust gradient boosting implementation
