# Introduction
This is a Currency Conversion CLI Application, written in Python, that uses FastForex's API.

# Prerequisites
### Creating Virtual Environment
1. In the terminal, run `pip install virtualenv`.
   
2. After you make sure you are in the project directory create a virtual environment by running `python<version> -m venv <virtual-environment-name>`.
   - For example `python3 -m venv venv`.
     
### Running the Virtual Environment
1. After you have created the virtual environment, you can activate it by running
- MacOS / Linux Users :
   - `source <virtual-environment-name>/bin/activate`.
- The Windows Users:
   - `<virtual-environment-name>/Scripts/activate.bat` **In CMD**
   - `<virtual-environment-name>/Scripts/Activate.ps1`  **In Powershel**
   
4. In order to install all the dependencies, required for the project, once your virtual environment has been activated, run `pip install -r requirements.txt`.

5. In order to deactivate the virtual environment, simply type `deactivate`. 

### Adding your FastForex API key to the `config.json` file

1. Create a new file called `config.json`

2. In the newly created file, enter the following code **Instead of KEY, enter your *FastForex* API key**:
`{
    "api_key": "KEY"
}`

# Running the app
Once all the prerequisites are completed, you can run the app.

1. Activate the virtual environment using `source <virtual-environment-name>/bin/activate`.

2. Run `python<version> CurrencyConversion.py YYYY-MM-DD`. 
   - For example `python3 CurrencyConversion.py 2024-06-01`.
    
# App functionality

1. Run the application using the date as an argument.

2. Choose the amount you wish to convert.
  - The amount can be a positive number, different from 0 and rounded up to 2 decimal points.
  - Valid examples are **10.2** ; **7** ; **42.42**. 

3. Choose the base currency.
   - The currency must be in 3 letter ISO4217 format (case insensitive).
   - The API is called and the results for each base currencies are cached under the *cache/* dir.

4. Choose the target currency.
   - The currency must be in 3 letter ISO4217 format (case insensitive).

5. The conversion result will be printed.

6. The conversion result will be saved in a *json* file under the *successful_conversions/* dir.

7. Steps 2-6 are performed until the user ends it by typing **end** (case insensitive)

## On application end

1. All cached results are deleted.

2. All saved results are deleted. 
