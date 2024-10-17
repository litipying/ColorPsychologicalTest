## Installation and Setup

1. Install Python 3.7 or higher if you haven't already.

2. Install virtualenv:
   ```
   pip install virtualenv
   ```

3. Create and activate a virtual environment:
   - On Windows:
     ```
     virtualenv venv
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     virtualenv venv
     source venv/bin/activate
     ```

4. Upgrade pip and install the required packages:
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application:

1. Ensure your virtual environment is activated.

2. Navigate to the project directory containing main.py.

3. Run the following command:
   ```
   streamlit run main.py
   ```

4. Streamlit will start the application and open it in your default web browser. If it doesn't open automatically, you'll see a local URL in the terminal that you can copy and paste into your browser.

