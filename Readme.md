# Loan Eligibility Prediction
This machine learning project predicts whether an applicant is eligible for loan approval or not. This app is build using pythona nd depolyed with the help of streamlit.

# Project Description 
The model takes input such as gender, income, credit history, education and education status and predicts whether a loan will be approved or not. The prediction is made using a random forest classifier.

# Features
1. User- friendly web interface.
2. Modular design of the project which makes it easy to use.
3. End-to-End Pipeline script ties everything together.
4. Loan Eligibilty prediction. The final model predicts whether a loan should be approved (Y or N)of a new applicant.
5. Input validation and logging.

# Folder Structure 
loan_eligibility_project/
├── app/
│   └── app.py                  # Streamlit application
├── modules/
│   ├── data_loader.py          # Data loading logic
│   ├── preprocessing.py        # Data cleaning and preprocessing
│   ├── model.py                # Model training and saving
│   ├── predict.py              # Model loading and predictions
│   └── utils.py                # Logging setup
├── data/
│   └── credit.csv              # Source dataset
├── models/
│   └── loan_model.pkl          # Trained model file
├── logs/
│   └── app.log                 # Application logs
├── train.py                    # Script to train and save the model
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files to exclude from version control


# Steps to run the Project.
1. Clone the repository
git clone https://github.com/sing2288/loan-eligibility-project.git
cd loan-eligibility-project

2. Install Dependencies
pip install -r requirements.txt

3. Train the model 
python train.py

4. Run the Streamlit App
streamlit run app/app.py

# Depnedencies
The Project requires the folowing python libraries 
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
logging

# License
The project is made for eductaional purposes.
